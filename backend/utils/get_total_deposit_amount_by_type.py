from sqlalchemy import select, func
from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Deposits

async def get_total_deposit_amount_by_type(user_id: int, type_: str, db: AsyncSession) -> Decimal:
    stmt = (
        select(func.coalesce(func.sum(Deposits.amount), 0))
        .where(
            Deposits.uid == user_id,
            Deposits.type == type_,
            Deposits.status == 1,
            Deposits.consider_pct_nct == 'YES'
        )
    )
    result = await db.execute(stmt)
    total = result.scalar_one()
    return Decimal(total)
