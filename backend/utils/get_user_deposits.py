from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Deposits
from schemas.deposits import DepositItem
from decimal import Decimal
from datetime import datetime
from typing import List

async def get_user_deposits(user_id: int, db: AsyncSession) -> List[DepositItem]:
    """
    Get all user deposits with detailed information
    
    Args:
        user_id: User ID to get deposits for
        db: Database session
        
    Returns:
        List[DepositItem]: List of deposits with detailed format
    """
    stmt = (
        select(Deposits)
        .where(
            Deposits.uid == user_id,
            Deposits.status == 1,
            Deposits.consider_pct_nct == 'YES'
        )
        .order_by(Deposits.processed_on.desc())
    )
    
    result = await db.execute(stmt)
    deposit_records = result.scalars().all()
    
    deposits = []
    for record in deposit_records:
        # Calculate forevers (amount / rate_as_deposit)
        amount = Decimal(record.amount) if record.amount else Decimal('0')
        rate = record.rate_at_deposit if record.rate_at_deposit else Decimal('1')
        forevers = amount / rate if rate > 0 else Decimal('0')
        
        # Convert processed_on timestamp to datetime
        processed_date = None
        if record.processed_on:
            processed_date = datetime.fromtimestamp(record.processed_on)
        
        deposit_item = DepositItem(
            txid=record.txid or "",
            processed_on=processed_date,
            forevers=forevers,
            price=rate,
            type=record.type or "UAE",
            paid=amount,
            access=bool(record.activated_forevers),
            participation=bool(record.activated_loyalty)
        )
        deposits.append(deposit_item)
    
    return deposits
