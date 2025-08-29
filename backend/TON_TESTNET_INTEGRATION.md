# TON Testnet Integration Documentation

## Overview

This system implements real TON cryptocurrency payments using TON testnet for testing purposes.

## Architecture

### Backend Components

1. **Crypto Purchase Service** (`crypto_purchase_service.py`)
   - Handles crypto payment initialization and verification
   - Integrates with TONCenter testnet API for blockchain verification
   - Manages rate conversion (USD ↔ TON)

2. **API Endpoints**
   - `POST /forevers/crypto/init` - Initialize crypto purchase
   - `POST /forevers/crypto/verify` - Verify transaction on blockchain

### Frontend Components

1. **TonConnect Service** (`tonConnectService.js`)
   - Manages wallet connection using TonConnect SDK
   - Configured for TON testnet
   - Handles transaction sending and status polling

2. **Crypto Transaction Modal** (`CryptoTransactionModal.vue`)
   - Shows transaction verification progress
   - Updates in real-time with polling

## Blockchain Verification Process

### 1. Transaction Initialization
- User selects crypto payment
- System converts USD amount to TON using CoinGecko rate
- Creates pending deposit record with transaction data

### 2. Transaction Sending
- User connects TON wallet via TonConnect
- Transaction sent to fixed receiver address: `0QBgEwEKpmG4yPvn7-_VqljYE2s88oI6v7R2Vu_E8TvHjMGG`
- Frontend starts polling for verification

### 3. Blockchain Verification
- System queries TONCenter testnet API for recent transactions
- Searches for transaction matching:
  - Source: user wallet
  - Destination: fixed receiver wallet
  - Amount: expected TON amount (±1% tolerance)
  - Time: within last 30 minutes

### 4. Transaction Confirmation
- If verified: creates transaction record, updates deposit status
- If failed: marks as failed with reason
- If pending: continues polling up to 60 attempts (60 minutes)

## API Configuration

### TONCenter Testnet API
- Base URL: `https://testnet.toncenter.com/api/v2`
- Endpoint: `/getTransactions`
- Parameters: address, limit, archival=true

### Rate Conversion
- Uses CoinGecko API for TON/USD rate
- Fallback rate: $2.50 per TON
- Testnet uses mainnet rates for calculation

## Security Features

### Amount Validation
- Server-side rate verification
- Tolerance for gas fees (±1% or 0.01 TON minimum)
- Maximum transaction limits ($50,000 USD)

### Address Validation
- Fixed receiver wallet enforcement
- User wallet format validation
- Recent transaction check (30 minutes max age)

### Anti-Fraud Measures
- Comprehensive logging
- Session-based authentication
- Amount consistency verification

## Testing

### Prerequisites
1. TON testnet wallet with test TON tokens
2. Telegram WebApp environment
3. Backend with httpx dependency: `pip install httpx>=0.24.0`

### Test Flow
1. Select crypto payment method
2. Connect testnet wallet
3. Send transaction to fixed address
4. Monitor verification progress
5. Confirm successful completion

## Configuration

### Environment Variables
- `VITE_API_BASE_URL` - API base URL
- Rate limits and timeouts in service classes

### Fixed Addresses
- Receiver: `0QBgEwEKpmG4yPvn7-_VqljYE2s88oI6v7R2Vu_E8TvHjMGG`
- Network: TON testnet

## Troubleshooting

### Common Issues
1. **Transaction not found**: Check wallet addresses and amounts
2. **Verification timeout**: Ensure transaction was sent to correct address
3. **Rate fetch failure**: Check CoinGecko API availability
4. **Wallet connection**: Verify TonConnect configuration

### Logs
- All operations logged with user_id and txid
- Blockchain verification details in application logs
- Transaction status updates tracked

## Production Notes

- Replace testnet with mainnet APIs
- Update wallet addresses for production
- Implement additional security measures
- Add monitoring and alerting
