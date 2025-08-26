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
   - Конвертация USD в TON
   - Инициализация транзакций
   - Верификация платежей
   - Полный флоу платежей

3. **Обновленный SelectTypePayment.vue**
   - Интеграция с TON Connect
   - Динамический текст кнопки (Connect Wallet / Buy Forevers)
   - Обработка TON плате��ей

### Backend
1. **TON Transaction Router** (`routers/ton_transactions.py`)
   - `/ton/convert-usd` - конвертация USD в TON
   - `/ton/initiate` - инициализация транзакции
   - `/ton/verify` - верификация платежа

2. **TON Transaction Service** (`services/ton_transactions_service.py`)
   - Интеграция с TonCenter API
   - Верификация на блокчейне
   - Зачисление Forevers
   - Запись в таблицы Deposits/Transactions

3. **Схемы данных** (`schemas/ton_transactions.py`)
   - Валидация запросов и ответов
   - Типизация данных

## Конфигурация
- **TonCenter API Key**: e708de5ba87a75a37477cb89d6eef609dfe4ac47618c7707e3ce27beed3ae434
- **TON Address**: 0QBgEwEKpmG4yPvn7-_VqljYE2s88oI6v7R2Vu_E8TvHjMGG
- **Network**: testnet
- **Manifest URL**: https://dbdc-mini.dubadu.com/tonconnect-manifest.json

## Флоу платежей
1. Пользователь выбирает crypto блок в SelectTypePayment
2. Если кошелек не подключен - показывается "Connect Wallet"
3. После подключения кнопка меняется на "Buy Forevers"
4. При клике инициируетс�� TON транзакция:
   - Конвертация USD в TON
   - Создание записи в Deposits
   - Отправка TON транзакции через кошелек
   - Верификация на блокчейне
   - Зачисление Forevers на баланс

## Интеграция с существующими системами
- Использует те же таблицы: Deposits, Transactions, Activity, Forevers, ForeversLogs
- Gateway ID 999 для TON платежей
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

## Дальнейшие улучшения
- Добавить поддержку mainnet
- Расширить верификацию транзакций
- Добавить историю TON платежей
- Оптимизировать UX для мобильных устройств
