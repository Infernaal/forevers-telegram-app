from sqlalchemy import String, Integer, Boolean, Date, DateTime, Enum, Text, ForeignKey, DECIMAL, TIMESTAMP, text
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column(String(255), nullable=True)
    password_recovery: Mapped[str] = mapped_column(String(255), nullable=True)
    document_verified: Mapped[int] = mapped_column(nullable=True)
    last_verification_failed_email_sent: Mapped[int] = mapped_column(nullable=True)
    verification_email_sent: Mapped[bool] = mapped_column(nullable=True)
    email_verified: Mapped[int] = mapped_column(nullable=True)
    email_hash: Mapped[str] = mapped_column(String(255), nullable=True)
    email: Mapped[str] = mapped_column(String(255), nullable=True)
    status: Mapped[int] = mapped_column(nullable=True)
    account_type: Mapped[int] = mapped_column(nullable=True)
    account_level: Mapped[int] = mapped_column(nullable=True)
    account_user: Mapped[str] = mapped_column(String(255), nullable=True)
    ip: Mapped[str] = mapped_column(String(255), nullable=True)
    last_login: Mapped[int] = mapped_column(nullable=True)
    signup_time: Mapped[int] = mapped_column(nullable=True)
    twofa_auth: Mapped[int] = mapped_column("2fa_auth", nullable=True)
    twofa_auth_login: Mapped[int] = mapped_column("2fa_auth_login", nullable=True)
    twofa_auth_send: Mapped[int] = mapped_column("2fa_auth_send", nullable=True)
    twofa_auth_withdrawal: Mapped[int] = mapped_column("2fa_auth_withdrawal", nullable=True)
    googlecode: Mapped[str] = mapped_column(String(255), nullable=True)
    wallet_passphrase: Mapped[str] = mapped_column(String(255), nullable=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str] = mapped_column(String(255), nullable=True)
    business_name: Mapped[str] = mapped_column(String(255), nullable=True)
    business_website: Mapped[str] = mapped_column(String(255), nullable=True)
    business_description: Mapped[str] = mapped_column(Text, nullable=True)
    business_category: Mapped[str] = mapped_column(String(255), nullable=True)
    business_who_pay_fee: Mapped[int] = mapped_column(nullable=True)
    merchant_api_key: Mapped[str] = mapped_column(String(255), nullable=True)
    business_reject: Mapped[int] = mapped_column(nullable=True)
    business_status: Mapped[int] = mapped_column(nullable=True)
    country: Mapped[str] = mapped_column(String(255), nullable=True)
    city: Mapped[str] = mapped_column(String(255), nullable=True)
    province: Mapped[str] = mapped_column(String(255), nullable=True)
    zip_code: Mapped[str] = mapped_column(String(255), nullable=True)
    address: Mapped[str] = mapped_column(String(255), nullable=True)
    birthday_date: Mapped[Date] = mapped_column(nullable=True)
    membership: Mapped[int] = mapped_column(nullable=True)
    parent_id: Mapped[int] = mapped_column(nullable=True)
    phone_number: Mapped[str] = mapped_column(String(100), nullable=True)
    avatar: Mapped[str] = mapped_column(String(255), nullable=True)
    language: Mapped[str] = mapped_column(Text, nullable=True)
    gender: Mapped[str] = mapped_column(String(10), nullable=True)
    s_messanger: Mapped[str] = mapped_column(String(50), nullable=True)
    s_instagram: Mapped[str] = mapped_column(String(50), nullable=True)
    s_telegram: Mapped[str] = mapped_column(String(50), nullable=True)
    s_skype: Mapped[str] = mapped_column(String(50), nullable=True)
    s_viber: Mapped[str] = mapped_column(String(50), nullable=True)
    s_tiktok: Mapped[str] = mapped_column(String(50), nullable=True)
    s_whatsapp: Mapped[str] = mapped_column(String(50), nullable=True)
    s_snapchat: Mapped[str] = mapped_column(String(50), nullable=True)
    show_modal: Mapped[bool] = mapped_column(nullable=True)
    default_gateway: Mapped[int] = mapped_column(nullable=True)
    qualification_data: Mapped[str] = mapped_column(Text, nullable=True)
    qualification_data_updated: Mapped[DateTime] = mapped_column(nullable=True)
    structural_data: Mapped[str] = mapped_column(Text, nullable=True)
    structural_data_updated: Mapped[DateTime] = mapped_column(nullable=True)
    user_token_id: Mapped[str] = mapped_column(String(36), nullable=True)
    rank_modal_shown: Mapped[int] = mapped_column(nullable=True)
    partner_deal_ref_link: Mapped[bool] = mapped_column(nullable=True)
    partner_deal_ref_link_date: Mapped[DateTime] = mapped_column(nullable=True)

class Deposit(Base):
    __tablename__ = "deposits"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    uid: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    txid: Mapped[str] = mapped_column(String(255), nullable=True)
    method: Mapped[int] = mapped_column(nullable=True)
    amount: Mapped[str] = mapped_column(String(255), nullable=True)
    currency: Mapped[str] = mapped_column(String(255), nullable=True)

    requested_on: Mapped[int] = mapped_column(nullable=True)
    processed_on: Mapped[int] = mapped_column(nullable=True)
    gateway_txid: Mapped[str] = mapped_column(String(255), nullable=True)
    reference_number: Mapped[str] = mapped_column(String(255), nullable=True)
    status: Mapped[int] = mapped_column(nullable=True)

    user_consent: Mapped[bool] = mapped_column(nullable=True, default=False)
    deal_status: Mapped[bool] = mapped_column(nullable=True, default=False)
    deal_signed: Mapped[bool] = mapped_column(nullable=True, default=False)

    rate_at_deposit: Mapped[float] = mapped_column(DECIMAL(16, 8), nullable=True)
    processed: Mapped[bool] = mapped_column(nullable=True, default=False)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=True)

    is_exchange: Mapped[bool] = mapped_column(nullable=True, default=False)
    invoice_path: Mapped[str] = mapped_column(String(255), nullable=True)

    consider_pct_nct: Mapped[str] = mapped_column(Enum("YES", "NO"), nullable=True, default="YES")
    vat_rate: Mapped[float] = mapped_column(DECIMAL(5, 2), nullable=True, default=0.0)
    vat_amount: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=True, default=0.0)

    bonus_eligible: Mapped[str] = mapped_column(Enum("YES", "NO"), nullable=True, default="YES")
    type: Mapped[str] = mapped_column(Enum("UAE", "KZ", "DE", "PL", "UA"), nullable=True, default="UAE")

    paypal_order_id: Mapped[str] = mapped_column(String(255), nullable=True)
    stripe_payment_intent_id: Mapped[str] = mapped_column(String(255), nullable=True)

class Forevers(Base):
    __tablename__ = "forevers"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    exchange_rate: Mapped[float] = mapped_column(DECIMAL(16, 8), nullable=False, default=1.0)

    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP"),
        server_onupdate=text("CURRENT_TIMESTAMP")
    )

    balance_uae: Mapped[float] = mapped_column(DECIMAL(16, 8), nullable=True, default=0.0)
    balance_kz: Mapped[float] = mapped_column(DECIMAL(16, 8), nullable=True, default=0.0)
    balance_de: Mapped[float] = mapped_column(DECIMAL(16, 8), nullable=True, default=0.0)
    balance_pl: Mapped[float] = mapped_column(DECIMAL(16, 8), nullable=True, default=0.0)
    balance_ua: Mapped[float] = mapped_column(DECIMAL(16, 8), nullable=True, default=0.0)

class ForeverExchangeStat(Base):
    __tablename__ = "forevers_exchange_stats"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    wallet_type: Mapped[str] = mapped_column(Enum("bonus", "rent"), nullable=False)
    forevers_amount: Mapped[float] = mapped_column(DECIMAL(16, 8), nullable=False)
    usd_amount: Mapped[float] = mapped_column(DECIMAL(16, 2), nullable=False)
    exchange_rate: Mapped[float] = mapped_column(DECIMAL(16, 8), nullable=False)
    
    txid: Mapped[str] = mapped_column(String(255), nullable=False)
    date_exchanged: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=True)

    forever_type: Mapped[str] = mapped_column(
        Enum("UAE", "KZ", "DE", "PL", "UA"), 
        nullable=False, 
        default="UAE"
    )

class ForeverLog(Base):
    __tablename__ = "forevers_logs"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    txid: Mapped[str] = mapped_column(String(255), nullable=False)
    txid_sync: Mapped[str] = mapped_column(String(255), nullable=True)

    forever_value: Mapped[float] = mapped_column(DECIMAL(16, 8), nullable=False)
    forever_balance: Mapped[float] = mapped_column(DECIMAL(16, 8), nullable=False)

    action: Mapped[str] = mapped_column(
        Enum("credit", "debit", "terminated"), 
        nullable=False
    )

    date_credited: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_debited: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    description: Mapped[str] = mapped_column(Text, nullable=True)

    type: Mapped[str] = mapped_column(
        Enum("UAE", "KZ", "DE", "PL", "UA"),
        nullable=False,
        default="UAE"
    )

class ForeverRent(Base):
    __tablename__ = "forevers_rent"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    uid: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    deposit_id: Mapped[int] = mapped_column(nullable=False)

    date: Mapped[Date] = mapped_column(nullable=False)
    amount: Mapped[float] = mapped_column(DECIMAL(10, 6), nullable=False)

class Withdrawal(Base):
    __tablename__ = "withdrawals"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    uid: Mapped[int] = mapped_column(nullable=True)
    wallet_id: Mapped[int] = mapped_column(nullable=True)

    txid: Mapped[str] = mapped_column(String(255), nullable=True)
    method: Mapped[int] = mapped_column(nullable=True)
    amount: Mapped[str] = mapped_column(String(255), nullable=True)
    fee: Mapped[str] = mapped_column(String(255), nullable=True)
    currency: Mapped[str] = mapped_column(String(255), nullable=True)

    requested_on: Mapped[int] = mapped_column(nullable=True)
    processed_on: Mapped[int] = mapped_column(nullable=True)
    status: Mapped[int] = mapped_column(nullable=True)

    gateway_txid: Mapped[str] = mapped_column(String(255), nullable=True)
    invoice_path: Mapped[str] = mapped_column(String(255), nullable=True)

    wallet_type: Mapped[str] = mapped_column(
        Enum("deposit", "bonus", "deals", "rent"),
        nullable=True
    )

class WithdrawalValue(Base):
    __tablename__ = "withdrawals_values"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    uid: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    withdrawal_id: Mapped[int] = mapped_column(ForeignKey("withdrawals.id", ondelete="CASCADE"), nullable=True)
    gateway_id: Mapped[int] = mapped_column(ForeignKey("gateways.id", ondelete="CASCADE"), nullable=True)
    field_id: Mapped[int] = mapped_column(nullable=True)

    value: Mapped[str] = mapped_column(String(255), nullable=True)
    is_default: Mapped[bool] = mapped_column(nullable=True, default=False)

class Transaction(Base):
    __tablename__ = "transactions"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    txid: Mapped[str] = mapped_column(String(255), nullable=True)
    type: Mapped[int] = mapped_column(nullable=True)
    sender: Mapped[int] = mapped_column(nullable=True)
    recipient: Mapped[int] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    amount: Mapped[str] = mapped_column(String(255), nullable=True)
    currency: Mapped[str] = mapped_column(String(255), nullable=True)
    fee: Mapped[str] = mapped_column(String(255), nullable=True)
    deposit_via: Mapped[int] = mapped_column(nullable=True)
    withdrawal_via: Mapped[int] = mapped_column(nullable=True)
    status: Mapped[int] = mapped_column(nullable=True)
    created: Mapped[int] = mapped_column(nullable=True)
    updated: Mapped[int] = mapped_column(nullable=True)
    item_id: Mapped[str] = mapped_column(String(255), nullable=True)
    item_name: Mapped[str] = mapped_column(String(255), nullable=True)

class Gateway(Base):
    __tablename__ = "gateways"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type: Mapped[int] = mapped_column(nullable=True)
    name: Mapped[str] = mapped_column(String(255), nullable=True)
    friendly_name: Mapped[str] = mapped_column(String(255), nullable=True)
    currency: Mapped[str] = mapped_column(String(255), nullable=True)
    reserve: Mapped[str] = mapped_column(String(255), nullable=True)
    min_amount: Mapped[str] = mapped_column(String(255), nullable=True)
    max_amount: Mapped[str] = mapped_column(String(255), nullable=True)
    exchange_type: Mapped[int] = mapped_column(nullable=True)
    include_fee: Mapped[int] = mapped_column(nullable=True)
    extra_fee: Mapped[str] = mapped_column(String(255), nullable=True)
    fee: Mapped[str] = mapped_column(String(255), nullable=True)
    allow_send: Mapped[int] = mapped_column(nullable=True)
    allow_receive: Mapped[int] = mapped_column(nullable=True)
    default_send: Mapped[int] = mapped_column(nullable=True)
    default_receive: Mapped[int] = mapped_column(nullable=True)
    allow_payouts: Mapped[int] = mapped_column(nullable=True)

    a_field_1: Mapped[str] = mapped_column(String(255), nullable=True)
    a_field_2: Mapped[str] = mapped_column(String(255), nullable=True)
    a_field_3: Mapped[str] = mapped_column(String(255), nullable=True)
    a_field_4: Mapped[str] = mapped_column(String(255), nullable=True)
    a_field_5: Mapped[str] = mapped_column(String(255), nullable=True)
    a_field_6: Mapped[str] = mapped_column(String(255), nullable=True)
    a_field_7: Mapped[str] = mapped_column(String(255), nullable=True)
    a_field_8: Mapped[str] = mapped_column(String(255), nullable=True)
    a_field_9: Mapped[str] = mapped_column(String(255), nullable=True)
    a_field_10: Mapped[str] = mapped_column(String(255), nullable=True)

    status: Mapped[int] = mapped_column(nullable=True)
    generate_invoice: Mapped[bool] = mapped_column(nullable=True)
    external_gateway: Mapped[int] = mapped_column(nullable=True)
    external_icon: Mapped[str] = mapped_column(Text, nullable=True)
    process_type: Mapped[int] = mapped_column(nullable=True)
    process_time: Mapped[int] = mapped_column(nullable=True)
    limit_visa_md: Mapped[bool] = mapped_column(nullable=True)