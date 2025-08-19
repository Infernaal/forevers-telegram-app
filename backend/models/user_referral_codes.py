from sqlalchemy import Column, Integer, String, DateTime, ForeignKeyConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base
from datetime import datetime


class UserReferralCode(Base):
    __tablename__ = 'user_referral_codes'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE', name='user_referral_codes_user_fk'),
        Index('user_id_unique', 'user_id', unique=True),
        Index('code_unique', 'code', unique=True)
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, unique=True)
    code: Mapped[str] = mapped_column(String(6), unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
