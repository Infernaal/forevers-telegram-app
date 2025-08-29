from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, case, and_, or_, literal, update
from sqlalchemy.dialects.mysql import insert as mysql_insert
from db.database import get_db
from models.models import Forevers, UsersWallets, Deposits, Stats, LoyaltyActivationHistory, Settings
from schemas.forevers_user_balance import ForeversBalance, ForeversBalanceData, WalletItem
from schemas.deposits import DepositsResponse, DepositsData
from schemas.deposits_history import DepositsHistoryResponse, DepositsHistoryData, DepositsHistoryItem
from schemas.activate_forevers import ActivateForeversRequest, ActivateForeversResponse
from schemas.activate_loyalty import ActivateLoyaltyRequest, ActivateLoyaltyResponse
from utils.calculate_available_forevers import calculate_available_forevers
from utils.get_user_deposits import get_user_deposits
from dependencies.current_user import get_current_user_id
import logging

logger = logging.getLogger(__name__)

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


@router.get("/deposits-history", response_model=DepositsHistoryResponse)
async def get_user_deposits_history(current_user_id: int = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    try:
        import time
        current_time = int(time.time())

        lah_subq = (
            select(
                LoyaltyActivationHistory.deposit_id.label("deposit_id"),
                func.max(LoyaltyActivationHistory.loyalty_activation_date).label("loyalty_activation_date")
            )
            .group_by(LoyaltyActivationHistory.deposit_id)
            .subquery()
        )

        is_expired_expr = case(
            (
                and_(
                    Deposits.activated_loyalty == 1,
                    lah_subq.c.loyalty_activation_date.isnot(None),
                    (literal(current_time) - lah_subq.c.loyalty_activation_date) >= (365 * 24 * 60 * 60)
                ),
                1
            ),
            else_=0
        ).label("is_expired")

        is_not_fully_activated_expr = case(
            (
                or_(
                    Deposits.activated_forevers == 0,
                    and_(Deposits.activated_forevers == 1, Deposits.activated_loyalty == 0)
                ),
                1
            ),
            else_=0
        ).label("is_not_fully_activated")

        # Settings join to compute loyalty availability per type
        loyalty_available_expr = case(
            (Deposits.type == 'UAE', Settings.loyalty_available_type_uae_date),
            (Deposits.type == 'KZ', Settings.loyalty_available_type_kz_date),
            (Deposits.type == 'DE', Settings.loyalty_available_type_de_date),
            (Deposits.type == 'PL', Settings.loyalty_available_type_pl_date),
            (Deposits.type == 'UA', Settings.loyalty_available_type_ua_date),
            else_=literal(None)
        ).label("loyalty_available_date")

        stmt = (
            select(
                Deposits.id,
                Deposits.txid,
                Deposits.amount,
                Deposits.rate_at_deposit,
                Deposits.requested_on,
                Deposits.deal_status,
                Deposits.status,
                Deposits.activated_forevers,
                Deposits.activated_loyalty,
                Deposits.type,
                Stats.forevers_activation_date,
                Stats.forevers_reactivate_date,
                lah_subq.c.loyalty_activation_date,
                loyalty_available_expr,
                is_expired_expr,
                is_not_fully_activated_expr
            )
            .select_from(Deposits)
            .outerjoin(Stats, Stats.deposit_id == Deposits.id)
            .outerjoin(lah_subq, lah_subq.c.deposit_id == Deposits.id)
            .outerjoin(Settings, Settings.id == literal(1))
            .where(
                Deposits.uid == current_user_id,
                Deposits.status.in_([1, 4, 5])
            )
            .order_by(
                is_expired_expr.desc(),
                is_not_fully_activated_expr.desc(),
                Deposits.requested_on.desc()
            )
        )

        result = await db.execute(stmt)
        rows = result.all()

        deposits = [
            DepositsHistoryItem(
                id=row.id,
                txid=row.txid,
                amount=row.amount,
                rate_at_deposit=row.rate_at_deposit,
                requested_on=row.requested_on,
                deal_status=row.deal_status,
                status=row.status,
                activated_forevers=row.activated_forevers,
                activated_loyalty=row.activated_loyalty,
                type=row.type,
                forevers_activation_date=row.forevers_activation_date,
                forevers_reactivate_date=row.forevers_reactivate_date,
                loyalty_activation_date=row.loyalty_activation_date,
                loyalty_available_date=row.loyalty_available_date,
                is_expired=row.is_expired,
                is_not_fully_activated=row.is_not_fully_activated
            ) for row in rows
        ]

        return DepositsHistoryResponse(
            status="success",
            data=DepositsHistoryData(
                user_id=current_user_id,
                deposits=deposits,
                total_count=len(deposits)
            ),
            message="User deposits history retrieved successfully"
        )
    except Exception:
        return DepositsHistoryResponse(
            status="failed",
            message="An error occurred while loading deposits history data. Please try again later"
        )


@router.post("/activate-forevers", response_model=ActivateForeversResponse)
async def activate_forevers(payload: ActivateForeversRequest, current_user_id: int = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    try:
        import time
        now = int(time.time())
        affected = 0
        upd = (
            update(Deposits)
            .where(
                Deposits.id == payload.deposit_id,
                Deposits.txid == payload.txid,
                Deposits.uid == current_user_id,
                Deposits.activated_forevers == 0
            )
            .values(activated_forevers=1)
        )
        result = await db.execute(upd)
        affected = result.rowcount or 0

        if affected > 0:
            ins = mysql_insert(Stats).values(
                uid=current_user_id,
                deposit_id=payload.deposit_id,
                forevers_activation_date=now,
                created_at=now
            )
            ondup = ins.on_duplicate_key_update(
                forevers_activation_date=ins.inserted.forevers_activation_date
            )
            await db.execute(ondup)
        await db.commit()
        if affected > 0:
            return ActivateForeversResponse(status="success", message="Forevers access activated")
        return ActivateForeversResponse(status="failed", message="Not found or already activated")
    except Exception as e:
        try:
            await db.rollback()
        except Exception:
            pass
        logger.exception("activate_forevers failed")
        return ActivateForeversResponse(status="failed", message=f"Activation failed. Please try again later. Reason: {e}")


@router.post("/activate-loyalty", response_model=ActivateLoyaltyResponse)
async def activate_loyalty(payload: ActivateLoyaltyRequest, current_user_id: int = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    try:
        import time
        now = int(time.time())

        # 1) Check deposit existence and active status
        dep_stmt = (
            select(Deposits.id, Deposits.type, Deposits.activated_forevers, Deposits.activated_loyalty)
            .where(
                Deposits.id == payload.deposit_id,
                Deposits.txid == payload.txid,
                Deposits.uid == current_user_id,
                Deposits.status == 1
            )
        )
        dep_row = (await db.execute(dep_stmt)).first()
        if not dep_row:
            return ActivateLoyaltyResponse(status="failed", message="Deposit not found or not active")

        dep_id, dep_type, activated_forevers, activated_loyalty = dep_row

        # 2) Check isExpired (loyalty 1 year passed)
        lah_stmt = (
            select(func.max(LoyaltyActivationHistory.loyalty_activation_date))
            .where(LoyaltyActivationHistory.deposit_id == dep_id)
        )
        last_loyalty_ts = (await db.execute(lah_stmt)).scalar()
        is_expired = False
        if last_loyalty_ts is not None:
            is_expired = (now - int(last_loyalty_ts)) >= (365 * 24 * 60 * 60)

        # 3) If not UAE and not expired — check settings availability date
        if dep_type != 'UAE' and not is_expired:
            type_map = {
                'KZ': Settings.loyalty_available_type_kz_date,
                'DE': Settings.loyalty_available_type_de_date,
                'PL': Settings.loyalty_available_type_pl_date,
                'UA': Settings.loyalty_available_type_ua_date,
                'UAE': Settings.loyalty_available_type_uae_date,
            }
            field_col = type_map.get(dep_type)
            if field_col is not None:
                avail_stmt = select(field_col).where(Settings.id == 1)
                avail_ts = (await db.execute(avail_stmt)).scalar()
                if avail_ts is not None and int(avail_ts) > now:
                    return ActivateLoyaltyResponse(status="failed", message="Loyalty program not available yet")

        # 4) Pre checks
        if not is_expired and (activated_forevers or 0) != 1:
            return ActivateLoyaltyResponse(status="failed", message="Forevers must be activated first")
        if not is_expired and (activated_loyalty or 0) == 1:
            return ActivateLoyaltyResponse(status="failed", message="Loyalty program already activated")

        # 5) Transaction: update deposits, upsert stats, insert history
        upd = (
            update(Deposits)
            .where(Deposits.id == dep_id, Deposits.uid == current_user_id)
            .values(activated_loyalty=1)
        )
        result = await db.execute(upd)
        if (result.rowcount or 0) == 0:
            await db.rollback()
            return ActivateLoyaltyResponse(status="failed", message="Failed to update deposits")

        ins = mysql_insert(Stats).values(
            uid=current_user_id,
            deposit_id=dep_id,
            forevers_reactivate_date=now,
            created_at=now
        )
        ondup = ins.on_duplicate_key_update(
            forevers_reactivate_date=ins.inserted.forevers_reactivate_date
        )
        await db.execute(ondup)

        lah_ins = mysql_insert(LoyaltyActivationHistory).values(
            uid=current_user_id,
            deposit_id=dep_id,
            loyalty_activation_date=now,
            created_at=now
        )
        await db.execute(lah_ins)

        await db.commit()

        return ActivateLoyaltyResponse(status="success", message="Loyalty program activated")
    except Exception as e:
        try:
            await db.rollback()
        except Exception:
            pass
        logger.exception("activate_loyalty failed")
        return ActivateLoyaltyResponse(status="failed", message=f"Activation failed. Please try again later. Reason: {e}")
