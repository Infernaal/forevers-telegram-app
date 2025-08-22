from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from db.database import get_db
from models.models import Forevers, UsersWallets
from schemas.forevers_user_balance import ForeversBalance, ForeversBalanceData, WalletItem
from schemas.uae_deposits import UAEDepositsResponse, UAEDepositsData
from schemas.deposits import DepositsResponse, DepositsData
from utils.calculate_available_forevers import calculate_available_forevers
from utils.get_uae_deposits_total import get_uae_deposits_total
from utils.get_user_deposits import get_user_deposits
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


@router.get("/uae-deposits", response_model=UAEDepositsResponse)
async def get_uae_deposits_total_endpoint(current_user_id: int = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    """
    Get total UAE deposits amount for plan calculation.
    Uses formula: rate_at_deposit * amount for UAE deposits only.
    """
    try:
        total_uae_deposits = await get_uae_deposits_total(current_user_id, db)

        return UAEDepositsResponse(
            status="success",
            data=UAEDepositsData(
                user_id=current_user_id,
                total_uae_deposits=total_uae_deposits
            ),
            message="UAE deposits total retrieved successfully"
        )
    except Exception as e:
        return UAEDepositsResponse(
            status="failed",
            message="An error occurred while loading UAE deposits data. Please try again later"
        )


@router.get("/deposits", response_model=DepositsResponse)
async def get_user_deposits_endpoint(current_user_id: int = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    """
    Get all user deposits with detailed information.
    Returns array with txid, processed_on, forevers, price, type, paid, access, participation.
    """
    try:
        deposits = await get_user_deposits(current_user_id, db)

        return DepositsResponse(
            status="success",
            data=DepositsData(
                user_id=current_user_id,
                deposits=deposits,
                total_count=len(deposits)
            ),
            message="User deposits retrieved successfully"
        )
    except Exception as e:
        return DepositsResponse(
            status="failed",
            message="An error occurred while loading deposits data. Please try again later"
        )
