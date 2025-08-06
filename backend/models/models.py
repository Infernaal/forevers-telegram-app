from typing import List, Optional
from sqlalchemy import CheckConstraint, DECIMAL, Date, DateTime, Enum, ForeignKeyConstraint, Index, Integer, SmallInteger, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import LONGTEXT, TINYINT
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime
import decimal
from db.database import Base


class Activity(Base):
    __tablename__ = 'activity'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    txid: Mapped[Optional[str]] = mapped_column(String(255))
    type: Mapped[Optional[int]] = mapped_column(Integer)
    uid: Mapped[Optional[int]] = mapped_column(Integer)
    u_field_1: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_2: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_3: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_4: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_5: Mapped[Optional[str]] = mapped_column(String(255))
    amount: Mapped[Optional[str]] = mapped_column(String(255))
    currency: Mapped[Optional[str]] = mapped_column(String(255))
    deposit_via: Mapped[Optional[int]] = mapped_column(Integer)
    withdrawal_via: Mapped[Optional[int]] = mapped_column(Integer)
    status: Mapped[Optional[int]] = mapped_column(Integer)
    created: Mapped[Optional[int]] = mapped_column(Integer)
    updated: Mapped[Optional[int]] = mapped_column(Integer)


class AdminBonusLogs(Base):
    __tablename__ = 'admin_bonus_logs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    admin_id: Mapped[int] = mapped_column(Integer)
    admin_username: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(Integer)
    wallet_type: Mapped[str] = mapped_column(Enum('bonus', 'rent'))
    amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(16, 2))
    action: Mapped[str] = mapped_column(String(50))
    date_added: Mapped[datetime.datetime] = mapped_column(DateTime)
    txid: Mapped[str] = mapped_column(String(255))


class AdminDeleteUsersLog(Base):
    __tablename__ = 'admin_delete_users_log'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    user_email: Mapped[str] = mapped_column(String(255))
    admin_id: Mapped[int] = mapped_column(Integer)
    admin_username: Mapped[str] = mapped_column(String(255))
    deleted_at: Mapped[datetime.datetime] = mapped_column(DateTime)


class AdminEarnings(Base):
    __tablename__ = 'admin_earnings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    amount: Mapped[Optional[str]] = mapped_column(String(255))
    currency: Mapped[Optional[str]] = mapped_column(String(255))
    created: Mapped[Optional[int]] = mapped_column(Integer)
    updated: Mapped[Optional[int]] = mapped_column(Integer)


class AdminForeversLogs(Base):
    __tablename__ = 'admin_forevers_logs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    admin_id: Mapped[int] = mapped_column(Integer)
    admin_username: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(Integer)
    forevers_amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(16, 8))
    usd_amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(16, 8))
    action: Mapped[str] = mapped_column(Enum('add_forevers', 'create_deposit'))
    date_added: Mapped[datetime.datetime] = mapped_column(DateTime)
    forever_type: Mapped[str] = mapped_column(Enum('UAE', 'KZ', 'DE', 'PL', 'UA'), server_default=text("'UAE'"))
    txid: Mapped[Optional[str]] = mapped_column(String(255))


class AdminLogs(Base):
    __tablename__ = 'admin_logs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[Optional[int]] = mapped_column(Integer)
    time: Mapped[Optional[int]] = mapped_column(Integer)
    u_field_1: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_2: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_3: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_4: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_5: Mapped[Optional[str]] = mapped_column(String(255))


class ApiTokens(Base):
    __tablename__ = 'api_tokens'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    token: Mapped[str] = mapped_column(String(255))


class Country(Base):
    __tablename__ = 'country'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    name_uk: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    name_ru: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    code: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    status: Mapped[Optional[int]] = mapped_column(Integer)
    vat: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"))


class Currency(Base):
    __tablename__ = 'currency'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    currency: Mapped[Optional[str]] = mapped_column(String(255))
    code: Mapped[Optional[str]] = mapped_column(String(255))
    status: Mapped[Optional[int]] = mapped_column(Integer)
    default_curr: Mapped[Optional[int]] = mapped_column(Integer)


class Deposits(Base):
    __tablename__ = 'deposits'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    processed: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'0'"))
    ip_address: Mapped[str] = mapped_column(String(45), server_default=text("''"))
    is_exchange: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'0'"), comment='0 = real deposit, 1 = bonus exchange')
    consider_pct_nct: Mapped[str] = mapped_column(Enum('YES', 'NO'), server_default=text("'YES'"))
    uid: Mapped[Optional[int]] = mapped_column(Integer)
    txid: Mapped[Optional[str]] = mapped_column(String(255))
    method: Mapped[Optional[int]] = mapped_column(Integer)
    amount: Mapped[Optional[str]] = mapped_column(String(255))
    currency: Mapped[Optional[str]] = mapped_column(String(255))
    requested_on: Mapped[Optional[int]] = mapped_column(Integer)
    processed_on: Mapped[Optional[int]] = mapped_column(Integer)
    gateway_txid: Mapped[Optional[str]] = mapped_column(String(255))
    reference_number: Mapped[Optional[str]] = mapped_column(String(255))
    status: Mapped[Optional[int]] = mapped_column(Integer)
    user_consent: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    deal_status: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    deal_signed: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    rate_at_deposit: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(16, 8))
    invoice_path: Mapped[Optional[str]] = mapped_column(String(255))
    vat_rate: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"))
    vat_amount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), server_default=text("'0.00'"))
    bonus_eligible: Mapped[Optional[str]] = mapped_column(Enum('YES', 'NO'), server_default=text("'YES'"))
    type: Mapped[Optional[str]] = mapped_column(Enum('UAE', 'KZ', 'DE', 'PL', 'UA'), server_default=text("'UAE'"))
    paypal_order_id: Mapped[Optional[str]] = mapped_column(String(255))
    stripe_payment_intent_id: Mapped[Optional[str]] = mapped_column(String(255))


class Discounts(Base):
    __tablename__ = 'discounts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(Enum('KZ', 'DE', 'PL', 'UA'))
    start_date: Mapped[datetime.date] = mapped_column(Date)
    end_date: Mapped[datetime.date] = mapped_column(Date)
    discount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(5, 2))


class Disputes(Base):
    __tablename__ = 'disputes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    recipient: Mapped[str] = mapped_column(String(255))
    currency: Mapped[str] = mapped_column(String(10))
    status: Mapped[int] = mapped_column(TINYINT)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


class ForeversRent(Base):
    __tablename__ = 'forevers_rent'
    __table_args__ = (
        Index('unique_entry', 'uid', 'deposit_id', 'date', unique=True),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uid: Mapped[int] = mapped_column(Integer)
    deposit_id: Mapped[int] = mapped_column(Integer)
    date: Mapped[datetime.date] = mapped_column(Date)
    amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 6))


class Gateways(Base):
    __tablename__ = 'gateways'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_gateway: Mapped[int] = mapped_column(Integer, server_default=text("'0'"))
    limit_visa_md: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'0'"))
    type: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    friendly_name: Mapped[Optional[str]] = mapped_column(String(255))
    currency: Mapped[Optional[str]] = mapped_column(String(255))
    reserve: Mapped[Optional[str]] = mapped_column(String(255))
    min_amount: Mapped[Optional[str]] = mapped_column(String(255))
    max_amount: Mapped[Optional[str]] = mapped_column(String(255))
    exchange_type: Mapped[Optional[int]] = mapped_column(Integer)
    include_fee: Mapped[Optional[int]] = mapped_column(Integer)
    extra_fee: Mapped[Optional[str]] = mapped_column(String(255))
    fee: Mapped[Optional[str]] = mapped_column(String(255))
    allow_send: Mapped[Optional[int]] = mapped_column(Integer)
    allow_receive: Mapped[Optional[int]] = mapped_column(Integer)
    default_send: Mapped[Optional[int]] = mapped_column(Integer)
    default_receive: Mapped[Optional[int]] = mapped_column(Integer)
    allow_payouts: Mapped[Optional[int]] = mapped_column(Integer)
    a_field_1: Mapped[Optional[str]] = mapped_column(String(255))
    a_field_2: Mapped[Optional[str]] = mapped_column(String(255))
    a_field_3: Mapped[Optional[str]] = mapped_column(String(255))
    a_field_4: Mapped[Optional[str]] = mapped_column(String(255))
    a_field_5: Mapped[Optional[str]] = mapped_column(String(255))
    a_field_6: Mapped[Optional[str]] = mapped_column(String(255))
    a_field_7: Mapped[Optional[str]] = mapped_column(String(255))
    a_field_8: Mapped[Optional[str]] = mapped_column(String(255))
    a_field_9: Mapped[Optional[str]] = mapped_column(String(255))
    a_field_10: Mapped[Optional[str]] = mapped_column(String(255))
    status: Mapped[Optional[int]] = mapped_column(Integer)
    generate_invoice: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    external_icon: Mapped[Optional[str]] = mapped_column(Text)
    process_type: Mapped[Optional[int]] = mapped_column(Integer)
    process_time: Mapped[Optional[int]] = mapped_column(Integer)

    gateway_mappings: Mapped[List["GatewayMappings"]] = relationship('GatewayMappings', foreign_keys='[GatewayMappings.deposit_gateway_id]', back_populates='deposit_gateway')
    gateway_mappings_: Mapped[List["GatewayMappings"]] = relationship('GatewayMappings', foreign_keys='[GatewayMappings.withdrawal_gateway_id]', back_populates='withdrawal_gateway')


class GatewaysFields(Base):
    __tablename__ = 'gateways_fields'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    gateway_id: Mapped[Optional[int]] = mapped_column(Integer)
    field_name: Mapped[Optional[str]] = mapped_column(String(255))
    field_label: Mapped[Optional[str]] = mapped_column(String(255))
    field_type: Mapped[Optional[str]] = mapped_column(Enum('text', 'email', 'number', 'textarea', 'select'), server_default=text("'text'"))
    field_options: Mapped[Optional[str]] = mapped_column(Text)
    field_tooltip: Mapped[Optional[str]] = mapped_column(Text)
    is_required: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'1'"))
    field_number: Mapped[Optional[int]] = mapped_column(Integer)
    field_value: Mapped[Optional[str]] = mapped_column(String(255))


class LeaderPoolBonusLog(Base):
    __tablename__ = 'leader_pool_bonus_log'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    execution_date: Mapped[datetime.date] = mapped_column(Date)
    turnover: Mapped[decimal.Decimal] = mapped_column(DECIMAL(16, 2))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))


class Levels(Base):
    __tablename__ = 'levels'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mem_id: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb3_unicode_ci'))
    fix_com: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb3_unicode_ci'))
    per_com: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb3_unicode_ci'))
    status: Mapped[Optional[int]] = mapped_column(Integer)


class MembershipLog(Base):
    __tablename__ = 'membership_log'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    txid: Mapped[Optional[str]] = mapped_column(String(255))
    plan: Mapped[Optional[int]] = mapped_column(Integer)
    uid: Mapped[Optional[int]] = mapped_column(Integer)
    amount: Mapped[Optional[str]] = mapped_column(String(255))
    currency: Mapped[Optional[str]] = mapped_column(String(255))
    status: Mapped[Optional[int]] = mapped_column(Integer)
    created: Mapped[Optional[str]] = mapped_column(String(255))
    date: Mapped[Optional[str]] = mapped_column(String(255))
    end_date: Mapped[Optional[str]] = mapped_column(String(255))
    activated_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class Pages(Base):
    __tablename__ = 'pages'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[Optional[str]] = mapped_column(String(255))
    prefix: Mapped[Optional[str]] = mapped_column(String(255))
    content: Mapped[Optional[str]] = mapped_column(Text)
    created: Mapped[Optional[int]] = mapped_column(Integer)
    updated: Mapped[Optional[int]] = mapped_column(Integer)


class ReferralMembership(Base):
    __tablename__ = 'referral_membership'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    limits: Mapped[Optional[int]] = mapped_column(Integer)
    ref_com_fix: Mapped[Optional[str]] = mapped_column(String(255))
    ref_com_per: Mapped[Optional[int]] = mapped_column(Integer)
    price: Mapped[Optional[str]] = mapped_column(String(255))
    status: Mapped[Optional[int]] = mapped_column(Integer)
    duration: Mapped[Optional[int]] = mapped_column(Integer)
    levels_allow: Mapped[Optional[int]] = mapped_column(Integer)


class Requests(Base):
    __tablename__ = 'requests'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uid: Mapped[str] = mapped_column(String(255))
    status: Mapped[int] = mapped_column(TINYINT)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


class Reward(Base):
    __tablename__ = 'reward'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb3_unicode_ci'))
    reward: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb3_unicode_ci'))
    reward_limit: Mapped[Optional[int]] = mapped_column(Integer)
    status: Mapped[Optional[int]] = mapped_column(Integer)


class RewardLog(Base):
    __tablename__ = 'reward_log'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uid: Mapped[Optional[int]] = mapped_column(Integer)
    reward_id: Mapped[Optional[int]] = mapped_column(Integer)
    txid: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb3_unicode_ci'))
    amount: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb3_unicode_ci'))
    date: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb3_unicode_ci'))


class Settings(Base):
    __tablename__ = 'settings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    maintenance_mode: Mapped[int] = mapped_column(Integer, server_default=text("'0'"), comment='0 - т√ъы■ўхэ, 1 - тъы■ўхэ')
    deposits_show_fee: Mapped[int] = mapped_column(Integer, server_default=text("'0'"), comment='0 - ёъЁ√Є№ ъюыюэъш Fee ш Net Amount, 1 - яюърчрЄ№')
    title: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    keywords: Mapped[Optional[str]] = mapped_column(String(255))
    name: Mapped[Optional[str]] = mapped_column(String(255))
    infoemail: Mapped[Optional[str]] = mapped_column(String(255))
    supportemail: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))
    default_language: Mapped[Optional[str]] = mapped_column(String(255))
    default_template: Mapped[Optional[str]] = mapped_column(String(255))
    default_currency: Mapped[Optional[str]] = mapped_column(String(255))
    logo: Mapped[Optional[str]] = mapped_column(Text)
    favicon: Mapped[Optional[str]] = mapped_column(Text)
    white_logo: Mapped[Optional[str]] = mapped_column(Text)
    require_email_verify: Mapped[Optional[int]] = mapped_column(Integer)
    require_document_verify: Mapped[Optional[int]] = mapped_column(Integer)
    limit_maxamount_sent: Mapped[Optional[int]] = mapped_column(Integer)
    limit_maxtxs_sent: Mapped[Optional[int]] = mapped_column(Integer)
    payfee_type: Mapped[Optional[int]] = mapped_column(Integer)
    payfee_fixed: Mapped[Optional[str]] = mapped_column(String(255))
    payfee_percentage: Mapped[Optional[int]] = mapped_column(Integer)
    enable_recaptcha: Mapped[Optional[int]] = mapped_column(Integer)
    recaptcha_publickey: Mapped[Optional[str]] = mapped_column(String(255))
    recaptcha_privatekey: Mapped[Optional[str]] = mapped_column(String(255))
    enable_curcnv: Mapped[Optional[int]] = mapped_column(Integer)
    curcnv_fee_percentage: Mapped[Optional[int]] = mapped_column(Integer)
    ref_com: Mapped[Optional[int]] = mapped_column(Integer)
    live_chat_code: Mapped[Optional[str]] = mapped_column(Text)
    google_analytics_code: Mapped[Optional[str]] = mapped_column(Text)
    merchant_fixed: Mapped[Optional[str]] = mapped_column(String(255))
    merchant_percentage: Mapped[Optional[int]] = mapped_column(Integer)
    forevers_value: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), server_default=text("'4.00'"), comment='Value of one Forever in USD')
    rent_account_holder: Mapped[Optional[str]] = mapped_column(String(255))
    rent_iban: Mapped[Optional[str]] = mapped_column(String(255))
    rent_swift_bic: Mapped[Optional[str]] = mapped_column(String(255))
    rent_bank_name: Mapped[Optional[str]] = mapped_column(String(255))
    rent_business_address: Mapped[Optional[str]] = mapped_column(Text)
    bonus_account_holder: Mapped[Optional[str]] = mapped_column(String(255))
    bonus_iban: Mapped[Optional[str]] = mapped_column(String(255))
    bonus_swift_bic: Mapped[Optional[str]] = mapped_column(String(255))
    bonus_bank_name: Mapped[Optional[str]] = mapped_column(String(255))
    bonus_business_address: Mapped[Optional[str]] = mapped_column(Text)
    forevers_kz_value: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), server_default=text("'10.00'"))
    forevers_de_value: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), server_default=text("'10.00'"))
    forevers_pl_value: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), server_default=text("'1.25'"))
    forevers_ua_value: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), server_default=text("'0.75'"))


class Support(Base):
    __tablename__ = 'support'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    hash: Mapped[Optional[str]] = mapped_column(String(255))
    sender: Mapped[Optional[int]] = mapped_column(Integer)
    recipient: Mapped[Optional[int]] = mapped_column(Integer)
    txid: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'0'"))
    amount: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'0'"))
    currency: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'0'"))
    escalate_review: Mapped[Optional[int]] = mapped_column(Integer)
    escalate_message: Mapped[Optional[str]] = mapped_column(Text)
    escalate_issued_by: Mapped[Optional[int]] = mapped_column(Integer)
    created_by: Mapped[Optional[int]] = mapped_column(Integer)
    created: Mapped[Optional[int]] = mapped_column(Integer)
    updated: Mapped[Optional[int]] = mapped_column(Integer)
    status: Mapped[Optional[int]] = mapped_column(Integer)
    closed_time: Mapped[Optional[int]] = mapped_column(Integer)
    is_read: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))


class SupportMessages(Base):
    __tablename__ = 'support_messages'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uid: Mapped[Optional[int]] = mapped_column(Integer)
    dispute_id: Mapped[Optional[int]] = mapped_column(Integer)
    comment: Mapped[Optional[str]] = mapped_column(Text)
    attachment: Mapped[Optional[str]] = mapped_column(Text)
    time: Mapped[Optional[int]] = mapped_column(Integer)
    is_admin: Mapped[Optional[int]] = mapped_column(Integer)
    status: Mapped[Optional[int]] = mapped_column(Integer)


class Transactions(Base):
    __tablename__ = 'transactions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    txid: Mapped[Optional[str]] = mapped_column(String(255))
    type: Mapped[Optional[int]] = mapped_column(Integer)
    sender: Mapped[Optional[int]] = mapped_column(Integer)
    recipient: Mapped[Optional[int]] = mapped_column(Integer)
    description: Mapped[Optional[str]] = mapped_column(String(255))
    amount: Mapped[Optional[str]] = mapped_column(String(255))
    currency: Mapped[Optional[str]] = mapped_column(String(255))
    fee: Mapped[Optional[str]] = mapped_column(String(255))
    deposit_via: Mapped[Optional[int]] = mapped_column(Integer)
    withdrawal_via: Mapped[Optional[int]] = mapped_column(Integer)
    status: Mapped[Optional[int]] = mapped_column(Integer)
    created: Mapped[Optional[int]] = mapped_column(Integer)
    updated: Mapped[Optional[int]] = mapped_column(Integer)
    item_id: Mapped[Optional[str]] = mapped_column(String(255))
    item_name: Mapped[Optional[str]] = mapped_column(String(255))


class UserNotifications(Base):
    __tablename__ = 'user_notifications'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    type: Mapped[str] = mapped_column(Enum('membership', 'rank'))
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))


class UserQualificationHistory(Base):
    __tablename__ = 'user_qualification_history'
    __table_args__ = (
        CheckConstraint('json_valid(`branches_data`)', name='user_qualification_history_chk_1'),
        Index('user_id', 'user_id', 'year', 'month', unique=True)
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    year: Mapped[int] = mapped_column(SmallInteger)
    month: Mapped[int] = mapped_column(TINYINT)
    rank: Mapped[str] = mapped_column(String(50))
    total_bonus: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2))
    branches_data: Mapped[str] = mapped_column(LONGTEXT)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        Index('fk_parent', 'parent_id'),
        Index('user_token_id', 'user_token_id', unique=True)
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    password: Mapped[Optional[str]] = mapped_column(String(255))
    password_recovery: Mapped[Optional[str]] = mapped_column(String(255))
    document_verified: Mapped[Optional[int]] = mapped_column(Integer)
    last_verification_failed_email_sent: Mapped[Optional[int]] = mapped_column(Integer, server_default=text("'0'"))
    verification_email_sent: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    email_verified: Mapped[Optional[int]] = mapped_column(Integer)
    email_hash: Mapped[Optional[str]] = mapped_column(String(255))
    email: Mapped[Optional[str]] = mapped_column(String(255))
    status: Mapped[Optional[int]] = mapped_column(Integer)
    account_type: Mapped[Optional[int]] = mapped_column(Integer)
    account_level: Mapped[Optional[int]] = mapped_column(Integer)
    account_user: Mapped[Optional[str]] = mapped_column(String(255))
    ip: Mapped[Optional[str]] = mapped_column(String(255))
    last_login: Mapped[Optional[int]] = mapped_column(Integer)
    signup_time: Mapped[Optional[int]] = mapped_column(Integer)
    _2fa_auth: Mapped[Optional[int]] = mapped_column('2fa_auth', Integer)
    _2fa_auth_login: Mapped[Optional[int]] = mapped_column('2fa_auth_login', Integer)
    _2fa_auth_send: Mapped[Optional[int]] = mapped_column('2fa_auth_send', Integer)
    _2fa_auth_withdrawal: Mapped[Optional[int]] = mapped_column('2fa_auth_withdrawal', Integer)
    googlecode: Mapped[Optional[str]] = mapped_column(String(255))
    wallet_passphrase: Mapped[Optional[str]] = mapped_column(String(255))
    first_name: Mapped[Optional[str]] = mapped_column(String(255))
    last_name: Mapped[Optional[str]] = mapped_column(String(255))
    business_name: Mapped[Optional[str]] = mapped_column(String(255))
    business_website: Mapped[Optional[str]] = mapped_column(String(255))
    business_country: Mapped[Optional[str]] = mapped_column(String(255))
    business_description: Mapped[Optional[str]] = mapped_column(Text)
    business_category: Mapped[Optional[str]] = mapped_column(String(255))
    business_who_pay_fee: Mapped[Optional[int]] = mapped_column(Integer)
    merchant_api_key: Mapped[Optional[str]] = mapped_column(String(255))
    business_reject: Mapped[Optional[str]] = mapped_column(Text)
    business_status: Mapped[Optional[int]] = mapped_column(Integer)
    country: Mapped[Optional[str]] = mapped_column(String(255))
    city: Mapped[Optional[str]] = mapped_column(String(255))
    province: Mapped[Optional[str]] = mapped_column(String(255))
    zip_code: Mapped[Optional[str]] = mapped_column(String(255))
    address: Mapped[Optional[str]] = mapped_column(String(255))
    birthday_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    membership: Mapped[Optional[int]] = mapped_column(Integer)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer)
    phone_number: Mapped[Optional[str]] = mapped_column(String(100))
    avatar: Mapped[Optional[str]] = mapped_column(String(255))
    language: Mapped[Optional[str]] = mapped_column(Text)
    gender: Mapped[Optional[str]] = mapped_column(Enum('Male', 'Female', 'Other'), server_default=text("'Other'"))
    s_messanger: Mapped[Optional[str]] = mapped_column(String(50))
    s_instagram: Mapped[Optional[str]] = mapped_column(String(50))
    s_telegram: Mapped[Optional[str]] = mapped_column(String(50))
    s_skype: Mapped[Optional[str]] = mapped_column(String(50))
    s_viber: Mapped[Optional[str]] = mapped_column(String(50))
    s_tiktok: Mapped[Optional[str]] = mapped_column(String(50))
    s_whatsapp: Mapped[Optional[str]] = mapped_column(String(50))
    s_snapchat: Mapped[Optional[str]] = mapped_column(String(50))
    show_modal: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    default_gateway: Mapped[Optional[int]] = mapped_column(Integer)
    qualification_data: Mapped[Optional[str]] = mapped_column(LONGTEXT)
    qualification_data_updated: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    structural_data: Mapped[Optional[str]] = mapped_column(LONGTEXT)
    structural_data_updated: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    user_token_id: Mapped[Optional[str]] = mapped_column(String(36))
    rank_modal_shown: Mapped[Optional[int]] = mapped_column(Integer)
    partner_deal_ref_link: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    partner_deal_ref_link_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    admin_activity: Mapped[List["AdminActivity"]] = relationship('AdminActivity', back_populates='admin')
    bonus_logs: Mapped[List["BonusLogs"]] = relationship('BonusLogs', back_populates='users')
    forevers: Mapped[List["Forevers"]] = relationship('Forevers', back_populates='user')
    forevers_exchange_stats: Mapped[List["ForeversExchangeStats"]] = relationship('ForeversExchangeStats', back_populates='user')
    forevers_logs: Mapped[List["ForeversLogs"]] = relationship('ForeversLogs', back_populates='user')
    users_profile_logs: Mapped[List["UsersProfileLogs"]] = relationship('UsersProfileLogs', foreign_keys='[UsersProfileLogs.admin_id]', back_populates='admin')
    users_profile_logs_: Mapped[List["UsersProfileLogs"]] = relationship('UsersProfileLogs', foreign_keys='[UsersProfileLogs.user_id]', back_populates='user')


class UsersDocuments(Base):
    __tablename__ = 'users_documents'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uid: Mapped[Optional[int]] = mapped_column(Integer)
    document_path: Mapped[Optional[str]] = mapped_column(Text)
    uploaded: Mapped[Optional[int]] = mapped_column(Integer)
    status: Mapped[Optional[int]] = mapped_column(Integer)
    u_field_1: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_2: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_3: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_4: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_5: Mapped[Optional[str]] = mapped_column(String(255))


class UsersLogs(Base):
    __tablename__ = 'users_logs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uid: Mapped[Optional[int]] = mapped_column(Integer)
    type: Mapped[Optional[int]] = mapped_column(Integer)
    time: Mapped[Optional[int]] = mapped_column(Integer)
    u_field_1: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_2: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_3: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_4: Mapped[Optional[str]] = mapped_column(String(255))
    u_field_5: Mapped[Optional[str]] = mapped_column(String(255))


class UsersWallets(Base):
    __tablename__ = 'users_wallets'
    __table_args__ = (
        Index('uid', 'uid', 'wallet_type', unique=True),
        Index('unique_bonus_wallet', 'uid', 'wallet_type', unique=True)
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    wallet_type: Mapped[str] = mapped_column(Enum('deposit', 'bonus', 'deals', 'rent'), server_default=text("'bonus'"))
    amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(16, 2), server_default=text("'0.00'"))
    uid: Mapped[Optional[int]] = mapped_column(Integer)
    currency: Mapped[Optional[str]] = mapped_column(String(5))
    updated: Mapped[Optional[int]] = mapped_column(Integer)


class UsersWalletsLog(Base):
    __tablename__ = 'users_wallets_log'
    __table_args__ = (
        Index('deposit_id_unique', 'deposit_id', unique=True),
        Index('idx_deposit_id', 'deposit_id', unique=True)
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uid: Mapped[int] = mapped_column(Integer)
    deposit_id: Mapped[int] = mapped_column(Integer)
    amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(16, 2))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)


class WalletAdjustmentLogs(Base):
    __tablename__ = 'wallet_adjustment_logs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    email: Mapped[Optional[str]] = mapped_column(String(255))
    difference: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    amount_deducted: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    remaining_balance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    remaining_to_deduct: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    status: Mapped[Optional[str]] = mapped_column(String(50))
    log_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class Withdrawals(Base):
    __tablename__ = 'withdrawals'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uid: Mapped[Optional[int]] = mapped_column(Integer)
    wallet_id: Mapped[Optional[int]] = mapped_column(Integer)
    txid: Mapped[Optional[str]] = mapped_column(String(255))
    method: Mapped[Optional[int]] = mapped_column(Integer)
    amount: Mapped[Optional[str]] = mapped_column(String(255))
    fee: Mapped[Optional[str]] = mapped_column(String(255))
    currency: Mapped[Optional[str]] = mapped_column(String(255))
    requested_on: Mapped[Optional[int]] = mapped_column(Integer)
    processed_on: Mapped[Optional[int]] = mapped_column(Integer)
    status: Mapped[Optional[int]] = mapped_column(Integer)
    gateway_txid: Mapped[Optional[str]] = mapped_column(String(255))
    invoice_path: Mapped[Optional[str]] = mapped_column(String(255))
    wallet_type: Mapped[Optional[str]] = mapped_column(Enum('deposit', 'bonus', 'deals', 'rent'))


class WithdrawalsValues(Base):
    __tablename__ = 'withdrawals_values'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uid: Mapped[Optional[int]] = mapped_column(Integer)
    withdrawal_id: Mapped[Optional[int]] = mapped_column(Integer)
    gateway_id: Mapped[Optional[int]] = mapped_column(Integer)
    field_id: Mapped[Optional[int]] = mapped_column(Integer)
    value: Mapped[Optional[str]] = mapped_column(String(255))
    is_default: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))


class AdminActivity(Base):
    __tablename__ = 'admin_activity'
    __table_args__ = (
        ForeignKeyConstraint(['admin_id'], ['users.id'], ondelete='CASCADE', name='admin_activity_ibfk_1'),
        Index('admin_id_unique', 'admin_id', unique=True)
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    admin_id: Mapped[int] = mapped_column(Integer)
    last_activity: Mapped[datetime.datetime] = mapped_column(DateTime)
    ip_address: Mapped[str] = mapped_column(String(45))

    admin: Mapped["Users"] = relationship('Users', back_populates='admin_activity')


class BonusLogs(Base):
    __tablename__ = 'bonus_logs'
    __table_args__ = (
        ForeignKeyConstraint(['uid'], ['users.id'], ondelete='CASCADE', name='bonus_logs_ibfk_1'),
        Index('from_uid', 'from_uid'),
        Index('uid', 'uid')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uid: Mapped[int] = mapped_column(Integer)
    generation: Mapped[int] = mapped_column(Integer)
    bonus_type: Mapped[str] = mapped_column(Enum('qualification', 'structural', 'leader_pool', 'referral', 'rental'), server_default=text("'referral'"))
    bonus_amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2))
    is_read: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'0'"))
    from_uid: Mapped[Optional[int]] = mapped_column(Integer)
    txid: Mapped[Optional[str]] = mapped_column(String(255))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

    users: Mapped["Users"] = relationship('Users', back_populates='bonus_logs')


class Forevers(Base):
    __tablename__ = 'forevers'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE', name='forevers_ibfk_1'),
        Index('user_forevers_unique', 'user_id', unique=True)
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    exchange_rate: Mapped[decimal.Decimal] = mapped_column(DECIMAL(16, 8), server_default=text("'1.00000000'"))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    balance_uae: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(16, 8), server_default=text("'0.00000000'"))
    balance_kz: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(16, 8), server_default=text("'0.00000000'"))
    balance_de: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(16, 8), server_default=text("'0.00000000'"))
    balance_pl: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(16, 8), server_default=text("'0.00000000'"))
    balance_ua: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(16, 8), server_default=text("'0.00000000'"))

    user: Mapped["Users"] = relationship('Users', back_populates='forevers')


class ForeversExchangeStats(Base):
    __tablename__ = 'forevers_exchange_stats'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE', name='forevers_exchange_stats_ibfk_1'),
        Index('user_id', 'user_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    wallet_type: Mapped[str] = mapped_column(Enum('bonus', 'rent'))
    forevers_amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(16, 8))
    usd_amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(16, 2))
    exchange_rate: Mapped[decimal.Decimal] = mapped_column(DECIMAL(16, 8))
    txid: Mapped[str] = mapped_column(String(255))
    date_exchanged: Mapped[datetime.datetime] = mapped_column(DateTime)
    forever_type: Mapped[str] = mapped_column(Enum('UAE', 'KZ', 'DE', 'PL', 'UA'), server_default=text("'UAE'"))
    ip_address: Mapped[Optional[str]] = mapped_column(String(45))

    user: Mapped["Users"] = relationship('Users', back_populates='forevers_exchange_stats')


class ForeversLogs(Base):
    __tablename__ = 'forevers_logs'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE', name='forevers_logs_ibfk_1'),
        Index('user_id', 'user_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    txid: Mapped[str] = mapped_column(String(255))
    forever_value: Mapped[decimal.Decimal] = mapped_column(DECIMAL(16, 8))
    forever_balance: Mapped[decimal.Decimal] = mapped_column(DECIMAL(16, 8))
    action: Mapped[str] = mapped_column(Enum('credit', 'debit', 'terminated'))
    txid_sync: Mapped[Optional[str]] = mapped_column(String(255))
    date_credited: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    date_debited: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    description: Mapped[Optional[str]] = mapped_column(Text)
    type: Mapped[Optional[str]] = mapped_column(Enum('UAE', 'KZ', 'DE', 'PL', 'UA'), server_default=text("'UAE'"))

    user: Mapped["Users"] = relationship('Users', back_populates='forevers_logs')


class GatewayMappings(Base):
    __tablename__ = 'gateway_mappings'
    __table_args__ = (
        ForeignKeyConstraint(['deposit_gateway_id'], ['gateways.id'], ondelete='CASCADE', name='gateway_mappings_ibfk_1'),
        ForeignKeyConstraint(['withdrawal_gateway_id'], ['gateways.id'], ondelete='CASCADE', name='gateway_mappings_ibfk_2'),
        Index('deposit_gateway_id', 'deposit_gateway_id'),
        Index('withdrawal_gateway_id', 'withdrawal_gateway_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    deposit_gateway_id: Mapped[int] = mapped_column(Integer)
    withdrawal_gateway_id: Mapped[int] = mapped_column(Integer)
    status: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'1'"))

    deposit_gateway: Mapped["Gateways"] = relationship('Gateways', foreign_keys=[deposit_gateway_id], back_populates='gateway_mappings')
    withdrawal_gateway: Mapped["Gateways"] = relationship('Gateways', foreign_keys=[withdrawal_gateway_id], back_populates='gateway_mappings_')


class UsersProfileLogs(Base):
    __tablename__ = 'users_profile_logs'
    __table_args__ = (
        ForeignKeyConstraint(['admin_id'], ['users.id'], ondelete='SET NULL', name='users_profile_logs_ibfk_2'),
        ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE', name='users_profile_logs_ibfk_1'),
        Index('admin_id', 'admin_id'),
        Index('user_id', 'user_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    field_name: Mapped[str] = mapped_column(String(100))
    change_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    admin_id: Mapped[Optional[int]] = mapped_column(Integer)
    old_value: Mapped[Optional[str]] = mapped_column(Text)
    new_value: Mapped[Optional[str]] = mapped_column(Text)

    admin: Mapped[Optional["Users"]] = relationship('Users', foreign_keys=[admin_id], back_populates='users_profile_logs')
    user: Mapped["Users"] = relationship('Users', foreign_keys=[user_id], back_populates='users_profile_logs_')
