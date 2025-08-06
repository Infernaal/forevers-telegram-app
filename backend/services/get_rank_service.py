from sqlalchemy import select, func, literal_column
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Users  # Модель таблицы users

async def get_user_rank(user_id: int, db: AsyncSession) -> str:
    try:
        stmt = select(
            func.ifnull(
                func.json_unquote(
                    func.json_extract(Users.qualification_data, "$.current_rank")
                ),
                "None"
            ).label("user_rank")
        ).where(Users.id == user_id).limit(1)

        result = await db.execute(stmt)
        row = result.scalar_one_or_none()

        return row if row is not None else "None"

    except Exception as e:
        print(f"Error while fetching user rank: {e}")
        return "None"
