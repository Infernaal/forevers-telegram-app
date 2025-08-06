from models.models import Settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from schemas.forevers_prices import PriceItem

async def extract_base_prices(db: AsyncSession) -> list[PriceItem] | None:
    settings = (await db.execute(select(Settings).limit(1))).scalar_one_or_none()
    if not settings:
        return None

    base_prices = {}

    for attr in dir(settings):
        if attr.startswith("forevers_") and attr.endswith("_value"):
            value = getattr(settings, attr)
            if value is not None:
                if attr == "forevers_value":
                    type_code = "UAE"
                else:
                    type_code = attr.replace("forevers_", "").replace("_value", "").upper()
                base_prices[type_code] = value

    return [PriceItem(type=key, value=value) for key, value in base_prices.items()]
