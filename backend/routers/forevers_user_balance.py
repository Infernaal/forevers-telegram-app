from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from db.database import get_db
from models.models import Forevers, UsersWallets
from schemas.forevers_user_balance import ForeversBalance, ForeversBalanceData, WalletItem
from schemas.deposits import UserDepositsResponse, UserDepositsData, DepositItem, UserDepositsSummaryResponse, UserDepositsSummaryData, DepositByType
from utils.calculate_available_forevers import calculate_available_forevers
from utils.get_user_deposits import get_user_deposits_list, get_user_deposits_by_type, get_user_deposits_total_usd
from dependencies.current_user import get_current_user_id

router = APIRouter(prefix="/forevers", tags=["Forevers User Stats"])

@router.get("/me", response_model=ForeversBalance)
async def get_my_forevers_balance(current_user_id: int = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    user_id = current_user_id
    try:
        stmt = select(Forevers).where(Forevers.user_id == user_id)
        result = await db.execute(stmt)
        row = result.scalar_one_or_none()

        if not row:
            return ForeversBalance(
                status="failed",
                message="No balance data available for the specified user"
            )

        bonus_stmt = (select(UsersWallets.currency, func.sum(UsersWallets.amount))
            .where(UsersWallets.uid == user_id, UsersWallets.wallet_type == 'bonus')
            .group_by(UsersWallets.currency))
        bonus_result = await db.execute(bonus_stmt)
        bonus_items = [
            WalletItem(type="bonus", currency=currency, amount=amount)
            for currency, amount in bonus_result.all()
        ]

        rent_stmt = (select(UsersWallets.currency, func.sum(UsersWallets.amount))
            .where(UsersWallets.uid == user_id, UsersWallets.wallet_type == 'rent')
            .group_by(UsersWallets.currency))
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

        available_forevers = await calculate_available_forevers(
            user_id=user_id,
            db=db
        )

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



@router.get("/deposits", response_model=UserDepositsResponse)
async def get_user_deposits_endpoint(current_user_id: int = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    """
    Get all user deposits grouped by type.
    Returns deposits by type with both original amounts and USD values.
    Can be filtered on frontend for specific types (UAE, KZ, DE, PL, UA).
    """
    try:
        deposits_by_type = await get_user_deposits_by_type(current_user_id, db)
        total_usd_value = await get_user_deposits_total_usd(current_user_id, db)

        # Convert to response format
        deposit_items = [
            DepositByType(
                type=deposit['type'],
                total_amount=deposit['total_amount'],
                total_usd_value=deposit['total_usd_value']
            )
            for deposit in deposits_by_type
        ]

        return UserDepositsResponse(
            status="success",
            data=UserDepositsData(
                user_id=current_user_id,
                deposits_by_type=deposit_items,
                total_usd_value=total_usd_value
            ),
            message="User deposits retrieved successfully"
        )
    except Exception as e:
        return UserDepositsResponse(
            status="failed",
            message="An error occurred while loading deposits data. Please try again later"
        )
