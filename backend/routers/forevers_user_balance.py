from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from db.database import get_db
from models.models import Forevers, UsersWallets
from schemas.forevers_user_balance import ForeversBalance, ForeversBalanceData, WalletItem
from utils.calculate_available_forevers import calculate_available_forevers

router = APIRouter(prefix="/forevers", tags=["Forevers User Stats"])

@router.get("/{user_id}", response_model=ForeversBalance)
async def get_forevers_balance(user_id: int, db: AsyncSession = Depends(get_db)):
    try:
        stmt = select(Forevers).where(Forevers.user_id == user_id)
        result = await db.execute(stmt)
        row = result.scalar_one_or_none()

        if not row:
            return ForeversBalance(
                status="failed",
                message="No balance data available for the specified user"
            )

        # Bonus
        bonus_stmt = select(UsersWallets.currency, func.sum(UsersWallets.amount))\
            .where(UsersWallets.uid == user_id, UsersWallets.wallet_type == 'bonus')\
            .group_by(UsersWallets.currency)
        bonus_result = await db.execute(bonus_stmt)
        bonus_items = [
            WalletItem(type="bonus", currency=currency, amount=amount)
            for currency, amount in bonus_result.all()
        ]

        # Rent (loyalty_program)
        rent_stmt = select(UsersWallets.currency, func.sum(UsersWallets.amount))\
            .where(UsersWallets.uid == user_id, UsersWallets.wallet_type == 'rent')\
            .group_by(UsersWallets.currency)
        rent_result = await db.execute(rent_stmt)
        rent_items = [
            WalletItem(type="loyalty_program", currency=currency, amount=amount)
            for currency, amount in rent_result.all()
        ]

        all_wallets = bonus_items + rent_items

        total_balance = (
            row.balance_uae +
            row.balance_kz +
            row.balance_de +
            row.balance_pl +
            row.balance_ua
        )

        # Расчёт доступных монет с учётом скидок и ранга
        available_forevers = await calculate_available_forevers(
            user_id=user_id,
            db=db
        )

        # Возвращаем полный ответ
        return ForeversBalance(
            status="success",
            forevers_balance=ForeversBalanceData(
                user_id=row.user_id,
                balance_uae=row.balance_uae,
                balance_kz=row.balance_kz,
                balance_de=row.balance_de,
                balance_pl=row.balance_pl,
                balance_ua=row.balance_ua,
                balance=total_balance
            ),
            wallets=all_wallets,
            available_forevers=available_forevers,
            message="User balance retrieved successfully"
        )

    except Exception:
        return ForeversBalance(
            status="failed",
            message="An error occurred while loading the data. Please try again later"
        )

