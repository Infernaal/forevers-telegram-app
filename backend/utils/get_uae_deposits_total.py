from sqlalchemy import select, func
from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Deposits

async def get_uae_deposits_total(user_id: int, db: AsyncSession) -> Decimal:
    """
    Calculate total UAE deposits amount using formula: rate_at_deposit * amount
    
    Args:
        user_id: User ID to calculate deposits for
        db: Database session
        
    Returns:
        Decimal: Total USD value of UAE deposits
    """
    stmt = (
        select(func.coalesce(func.sum(Deposits.rate_at_deposit * Deposits.amount), 0))
        .where(
            Deposits.uid == user_id,
            Deposits.type == 'UAE',
            Deposits.status == 1,
            Deposits.consider_pct_nct == 'YES'
        )
    )
    result = await db.execute(stmt)
    total = result.scalar_one()
    return Decimal(total)
