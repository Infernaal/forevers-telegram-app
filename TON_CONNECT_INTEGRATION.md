# TON Connect Integration for DBD Capital Forevers Bot

## Обзор
Интегрирован TON Connect для crypto блока в SelectTypePayment, позволяя пользователям покупать Forevers через TON кошелек.

## Реализованные компоненты

### Frontend
1. **TON Connect Composable** (`src/composables/useTonConnect.js`)
   - Управление подключением кошелька
   - Отправка транзакций
   - Статус подключения

2. **TON Connect Service** (`src/services/tonConnectService.js`)
   - Инициализация криптовалютных транзакций
   - Верификация платежей
   - Полный флоу платежей

3. **Обновленный SelectTypePayment.vue**
   - Интеграция с TON Connect
   - Динамический текст кнопки (Connect Wallet / Buy Forevers)
   - Обработка TON платежей

### Backend
1. **Crypto Transaction Router** (`routers/crypto_transactions.py`)
   - `/forevers/crypto/init` - инициализация транзакции с конвертацией USD в TON
   - `/forevers/crypto/verify` - верификация платежа

2. **TON Transaction Service** (`services/ton_transactions_service.py`)
   - Интеграция с TonCenter API
   - Верификация на блокчейне
   - Зачисление Forevers
   - Запись в таблицы Deposits/Transactions

3. **Схемы данных** (`schemas/crypto_transactions.py`)
   - Валидация запросов и ответов
   - Типизация данных

## Конфигурация
- **Gateway ID**: 8 (для crypto платежей)
- **TonCenter API Key**: e708de5ba87a75a37477cb89d6eef609dfe4ac47618c7707e3ce27beed3ae434
- **TON Address**: 0QBgEwEKpmG4yPvn7-_VqljYE2s88oI6v7R2Vu_E8TvHjMGG
- **Network**: testnet
- **Manifest URL**: https://dbdc-mini.dubadu.com/tonconnect-manifest.json

## API Endpoints
### `/forevers/crypto/init`
**POST** - Инициализация криптовалютной транзакции
- Принимает USD сумму и детали Forevers
- Автоматически конвертирует USD в TON
- Создает записи в Deposits, Transactions, Activity
- Возвращает данные для TON транзакции

**Request:**
```json
{
  "usd_amount": 100.00,
  "wallet_address": "UQBgEwEKpmG4yPvn7-_VqljYE2s88oI6v7R2Vu_E8TvHjMGG",
  "forevers_details": [
    {
      "code": "UAE",
      "country": "United Arab Emirates",
      "amount": 25,
      "usd_rate": 4.00,
      "total_cost": 100.00
    }
  ],
  "ip_address": "192.168.1.1"
}
```

**Response:**
```json
{
  "status": "success",
  "deposit_id": 12345,
  "txid": "TON1234567890",
  "recipient_address": "0QBgEwEKpmG4yPvn7-_VqljYE2s88oI6v7R2Vu_E8TvHjMGG",
  "ton_amount": 15.384615384,
  "ton_rate": 6.50,
  "rate_source": "mock_testnet",
  "expires_at": 1704120000
}
```

### `/forevers/crypto/verify`
**POST** - Верификация криптовалютной транзакции
- Проверяет транзакцию на блокчейне
- Обновляет статусы записе��
- Зачисляет Forevers на баланс

**Request:**
```json
{
  "tx_hash": "abc123...",
  "deposit_id": 12345
}
```

**Response:**
```json
{
  "status": "success",
  "verified": true,
  "deposit_id": 12345,
  "forevers_credited": {
    "UAE": 25.0
  },
  "tx_hash": "abc123...",
  "verification_details": {}
}
```

## Флоу платежей
1. Пользователь выбирает crypto блок в SelectTypePayment
2. Если кошелек не подключен - показывается "Connect Wallet"
3. После подключения кнопка меняется на "Buy Forevers"
4. При клике инициируется криптовалютная транзакция:
   - Вызов `/forevers/crypto/init` с автоматической конвертацией USD→TON
   - Создание записи в Deposits с gateway_id=8
   - Отправка TON транзакции через кошелек
   - Вызов `/forevers/crypto/verify` для верификации
   - Зачисление Forevers на баланс

## Интеграция с существующими системами
- Использует те же таблицы: Deposits, Transactions, Activity, Forevers, ForeversLogs
- Gateway ID 8 для crypto платежей
- Совместимо с существующей логикой зачисления Forevers
- Поддерживает все типы Forevers (UAE, KZ, DE, PL, UA)

## Безопасность
- Верификация транзакций на блокчейне
- Валидация сумм и адресов
- Логирование всех операций
- Обработка ошибок и откатов

## Для тестирования
1. Откройте приложение в Telegram WebApp
2. Перейдите к покупке Forevers
3. Выберите crypto блок (USDT)
4. Подключите TON кошелек
5. Совершите тестовую транзакцию

## Технические детали
- **Frontend**: Vue 3 + TON Connect UI
- **Backend**: FastAPI + SQLAlchemy + TonCenter API
- **База данных**: Существующие таблицы с gateway_id=8
- **Блокчейн**: TON testnet
- **Конвертация**: USD↔TON через TonCenter/CoinGecko API
