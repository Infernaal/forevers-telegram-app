from services.get_rank_service import get_user_rank
from services.forevers_prices_service import extract_base_prices
from services.discount_service import apply_discounts
from decimal import Decimal, ROUND_FLOOR
from typing import Dict, Optional, Union
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date
from utils.get_total_deposit_amount_by_type import get_total_deposit_amount_by_type
from utils.get_user_deposits import get_available_deposit_types

async def calculate_available_forevers(
    user_id: int,
    db: AsyncSession
) -> Dict[str, Optional[int]]:
    # �������� ����
    rank = await get_user_rank(user_id, db)

    # �������� ������� ����
    base_price_items = await extract_base_prices(db)
    if base_price_items is None:
        return {region: 0 for region in ["UAE", "KZ", "DE", "PL", "UA"]}

    # ��������� ������
    discounted_prices, _ = await apply_discounts(db, base_price_items)

    # ����������� � ������� {type: rate}
    final_rates: Dict[str, Decimal] = {
        item.type: item.value for item in discounted_prices
    }

    # �������� total_amounts �� ����
    region_types = ["UAE", "KZ", "DE", "PL", "UA"]
    total_amounts: Dict[str, Decimal] = {
        region: await get_total_deposit_amount_by_type(user_id, region, db)
        for region in region_types
    }

    # ������ max_volumes
    multiplier = Decimal("1.0") if rank != "None" else Decimal("0.5")
    total_all = total_amounts["UAE"] + total_amounts["KZ"] + total_amounts["DE"]
    max_allowed_pl_ua = total_all * multiplier

    max_volumes = {
        "UAE": None,
        "KZ": None,
        "DE": None,
        "PL": max(Decimal(0), max_allowed_pl_ua - total_amounts["PL"]),
        "UA": max(Decimal(0), max_allowed_pl_ua - total_amounts["UA"]),
    }

    # ������ ��������� �����
    available_forever_coins: Dict[str, Optional[int]] = {}

    for region in region_types:
        max_volume = max_volumes[region]
        rate = final_rates.get(region, Decimal(0))

        if max_volume is None:
            available_forever_coins[region] = None  # ��������
        elif rate > 0:
            available_forever_coins[region] = int((max_volume / rate).to_integral_value(ROUND_FLOOR))
        else:
            available_forever_coins[region] = 0

    return available_forever_coins
