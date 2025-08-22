from sqlalchemy import select, func, distinct
from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Deposits
from typing import List, Dict

async def get_user_deposits_list(user_id: int, db: AsyncSession) -> List[Dict]:
    """
    Get detailed list of user deposits with all fields
    
    Args:
        user_id: User ID to get deposits for
        db: Database session
        
    Returns:
        List[Dict]: List of deposit items with detailed information
    """
    stmt = (
        select(
            Deposits.txid,
            Deposits.processed_on,
            Deposits.amount,
            Deposits.rate_at_deposit,
            Deposits.type
        )
        .where(
            Deposits.uid == user_id,
            Deposits.status == 1,
            Deposits.consider_pct_nct == 'YES'
        )
        .order_by(Deposits.processed_on.desc())  # Most recent first
    )
    
    result = await db.execute(stmt)
    deposits = []
    
    for row in result.all():
        txid, processed_on, amount, rate_at_deposit, deposit_type = row
        
        # Convert string amount to Decimal
        amount_decimal = Decimal(amount) if amount else Decimal('0')
        rate_decimal = rate_at_deposit if rate_at_deposit else Decimal('0')
        
        # Calculate forevers: amount / rate_at_deposit
        forevers = amount_decimal / rate_decimal if rate_decimal > 0 else Decimal('0')
        
        # TODO: These fields will be added to DB later
        # For now, set as 0 (activated_forevers, activated_loyalty)
        access = Decimal('0')  # Will be populated from activated_forevers field
        participation = Decimal('0')  # Will be populated from activated_loyalty field
        
        deposits.append({
            'txid': txid,
            'processed_on': processed_on,
            'forevers': forevers,
            'price': rate_decimal,
            'type': deposit_type,
            'paid': amount_decimal,
            'access': access,
            'participation': participation
        })
    
    return deposits

async def get_user_deposits_by_type(user_id: int, db: AsyncSession) -> List[Dict]:
    """
    Get user deposits grouped by type with both total amount and USD value
    
    Args:
        user_id: User ID to get deposits for
        db: Database session
        
    Returns:
        List[Dict]: List of deposits by type with amounts and USD values
    """
    # Get all available deposit types
    available_types = ['UAE', 'KZ', 'DE', 'PL', 'UA']
    
    deposits_by_type = []
    
    for deposit_type in available_types:
        # Get total amount for this type
        amount_stmt = (
            select(func.coalesce(func.sum(Deposits.amount), 0))
            .where(
                Deposits.uid == user_id,
                Deposits.type == deposit_type,
                Deposits.status == 1,
                Deposits.consider_pct_nct == 'YES'
            )
        )
        
        # Get total USD value (rate_at_deposit * amount) for this type
        usd_value_stmt = (
            select(func.coalesce(func.sum(Deposits.rate_at_deposit * Deposits.amount), 0))
            .where(
                Deposits.uid == user_id,
                Deposits.type == deposit_type,
                Deposits.status == 1,
                Deposits.consider_pct_nct == 'YES'
            )
        )
        
        # Execute both queries
        amount_result = await db.execute(amount_stmt)
        usd_value_result = await db.execute(usd_value_stmt)
        
        total_amount = amount_result.scalar_one()
        total_usd_value = usd_value_result.scalar_one()
        
        # Only include types that have deposits
        if total_amount > 0:
            deposits_by_type.append({
                'type': deposit_type,
                'total_amount': Decimal(total_amount),
                'total_usd_value': Decimal(total_usd_value)
            })
    
    return deposits_by_type

async def get_user_deposits_total_usd(user_id: int, db: AsyncSession, deposit_types: List[str] = None) -> Decimal:
    """
    Get total USD value for specific deposit types or all types
    
    Args:
        user_id: User ID to calculate deposits for
        db: Database session
        deposit_types: List of deposit types to include (None for all)
        
    Returns:
        Decimal: Total USD value of deposits
    """
    query_filters = [
        Deposits.uid == user_id,
        Deposits.status == 1,
        Deposits.consider_pct_nct == 'YES'
    ]
    
    if deposit_types:
        query_filters.append(Deposits.type.in_(deposit_types))
    
    stmt = (
        select(func.coalesce(func.sum(Deposits.rate_at_deposit * Deposits.amount), 0))
        .where(*query_filters)
    )
    
    result = await db.execute(stmt)
    total = result.scalar_one()
    return Decimal(total)
