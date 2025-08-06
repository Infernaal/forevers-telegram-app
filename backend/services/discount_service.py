from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.models import Discounts
from schemas.forevers_prices import DiscountItem, PriceItem
from decimal import Decimal
from datetime import date

async def apply_discounts(db: AsyncSession, base_prices: list[PriceItem]) -> tuple[list[PriceItem], list[DiscountItem]]:
    today = date.today()

    # Получаем ORM-объекты Discounts
    result = await db.execute(select(Discounts))
    discounts_orm = result.scalars().all()

    # Конвертируем в DiscountItem
    discounts = [
        DiscountItem(
            type=discount.type,
            start_date=discount.start_date,
            end_date=discount.end_date,
            discount=discount.discount
        )
        for discount in discounts_orm
    ]

    discounted_prices = []
    for price in base_prices:
        discount = next(
            (d.discount for d in discounts if d.type == price.type and d.start_date <= today <= d.end_date),
            Decimal(0)
        )
        discounted_value = price.value * (1 - discount / Decimal(100))
        discounted_prices.append(
            PriceItem(type=price.type, value=discounted_value.quantize(Decimal("0.01")))
        )

    return discounted_prices, discounts
