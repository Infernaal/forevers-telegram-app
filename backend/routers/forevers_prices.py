from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from schemas.forevers_prices import ForeversPricesResponse, ForeversPricesData
from services.forevers_prices_service import extract_base_prices
from services.discount_service import apply_discounts

router = APIRouter(prefix="/prices", tags=["Prices"])

@router.get("/forevers", response_model=ForeversPricesResponse, summary="Get Forevers Price")
async def get_forevers_prices(db: AsyncSession = Depends(get_db)):
    try:
        base_prices = await extract_base_prices(db)
        if base_prices is None:
            return ForeversPricesResponse(
                status="failed",
                message="Pricing data unavailable. Please try again later."
            )

        discounted_prices, discounts = await apply_discounts(db, base_prices)

        return ForeversPricesResponse(
            status="success",
            data=ForeversPricesData(
                prices=base_prices,
                discounted_prices=discounted_prices,
                discounts=discounts
            )
        )
    except Exception:
        return ForeversPricesResponse(
            status="failed",
            message="A server error occurred while retrieving pricing information."
        )

