import { TonConnect } from '@tonconnect/sdk'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

// Fixed receiver wallet address for TON testnet
const FIXED_RECEIVER_WALLET = '0QBgEwEKpmG4yPvn7-_VqljYE2s88oI6v7R2Vu_E8TvHjMGG'

/**
 * TonConnect service for handling TON cryptocurrency transactions
 */
import { TonConnectUI } from '@tonconnect/ui'

export class TonConnectService {
  constructor() {
    this.tonConnect = null
    this.isInitialized = false
  }

  /**
   * Initialize TonConnect UI (works in Telegram WebApp and browser)
   */
  async init() {
    if (this.isInitialized) {
      return this.tonConnect
    }

    try {
      // Use absolute path to public manifest; UI auto-detects Telegram environment
      const manifestUrl = `${window.location.origin}/tonconnect-manifest.json`
      this.tonConnect = new TonConnectUI({
        manifestUrl,
        restoreConnection: true
      })

      this.isInitialized = true
      console.log('TonConnect UI initialized')
      return this.tonConnect
    } catch (error) {
      console.error('Failed to initialize TonConnect:', error)
      throw new Error('Failed to initialize TON wallet connection')
    }
  }

  /**
   * Check if wallet is connected
   */
  isWalletConnected() {
    const addr = this.tonConnect?.wallet?.account?.address
    return typeof addr === 'string' && addr.length > 0
  }

  /**
   * Get connected wallet info
   */
  getWallet() {
    if (!this.isWalletConnected()) {
      return null
    }
    return this.tonConnect.wallet
  }

  /**
   * Get wallet address
   */
  getWalletAddress() {
    const wallet = this.getWallet()
    return wallet?.account?.address || null
  }

  /**
   * Connect to TON wallet
   */
  async connectWallet() {
    try {
      if (!this.tonConnect) {
        await this.init()
      }

      // Optionally show picker modal and connect
      const wallet = await this.tonConnect.connectWallet()
      console.log('Wallet connected successfully')

      const chain = this.getChain()
      if (!this.isTestnet()) {
        throw new Error('Please switch your TON wallet to Testnet and try again.')
      }

      return wallet
    } catch (error) {
      console.error('Failed to connect wallet:', error)
      throw new Error(error?.message || 'Failed to connect to TON wallet. Please try again.')
    }
  }

  /**
   * Disconnect wallet
   */
  async disconnectWallet() {
    try {
      if (this.tonConnect) {
        await this.tonConnect.disconnect()
        console.log('Wallet disconnected')
      }
    } catch (error) {
      console.error('Error disconnecting wallet:', error)
      throw new Error('Failed to disconnect wallet')
    }
  }

  /**
   * Initialize crypto purchase on backend
   */
  async initCryptoPurchase(amountUsd, rateAsDeposit = null) {
    try {
      const userWallet = this.getWalletAddress()
      if (!userWallet) {
        throw new Error('Wallet not connected')
      }

      const response = await fetch(`${API_BASE_URL}/forevers/crypto/init`, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          amount_usd: amountUsd,
          user_wallet: userWallet,
          receiver_wallet: FIXED_RECEIVER_WALLET,
          rate_as_deposit: rateAsDeposit
        })
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.message || `HTTP error! status: ${response.status}`)
      }

      if (data.status !== 'success') {
        throw new Error(data.message || 'Failed to initialize crypto purchase')
      }

      console.log('Crypto purchase initialized:', data.data)
      return data.data
    } catch (error) {
      console.error('Error initializing crypto purchase:', error)
      throw error
    }
  }

  /**
   * Send TON transaction
   */
  async sendTransaction(transactionData) {
    try {
      if (!this.isWalletConnected()) {
        throw new Error('Wallet not connected')
      }
      if (!this.isTestnet()) {
        throw new Error('Please switch your TON wallet to Testnet and try again.')
      }

      // Prepare transaction for TonConnect
      // Only pass payload if it's a valid base64 BOC; otherwise omit (plain text is invalid)
      const maybePayload = (typeof transactionData.payload === 'string' && /^[A-Za-z0-9+/]+={0,2}$/.test(transactionData.payload))
        ? transactionData.payload
        : undefined

      const transaction = {
        validUntil: Math.floor(Date.now() / 1000) + 300, // 5 minutes
        messages: [
          {
            address: transactionData.to,
            amount: this.tonToNanoton(transactionData.amount_ton),
            payload: maybePayload
          }
        ]
      }

      console.log('Sending transaction:', transaction)

      // Send transaction through TonConnect
      const result = await this.tonConnect.sendTransaction(transaction)

      console.log('Transaction sent successfully:', result)
      return result
    } catch (error) {
      console.error('Error sending transaction:', error)

      const msg = String(error?.message || '').toLowerCase()
      if (msg.includes('rejected') || msg.includes('cancel')) {
        throw new Error('Transaction was rejected by user')
      }
      if (msg.includes('insufficient') || msg.includes('not enough')) {
        throw new Error('Insufficient balance in wallet')
      }
      if (msg.includes('address') || msg.includes('network') || msg.includes('testnet') || msg.includes('mainnet')) {
        throw new Error('Invalid network or address. Make sure your wallet is on Testnet.')
      }
      throw new Error(error?.message || 'Failed to send transaction. Please try again.')
    }
  }

  /**
   * Verify transaction on backend
   */
  async verifyTransaction(requestId) {
    try {
      const response = await fetch(`${API_BASE_URL}/forevers/crypto/verify`, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          txid: requestId
        })
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.message || `HTTP error! status: ${response.status}`)
      }

      console.log('Transaction verification result:', data)
      return data
    } catch (error) {
      console.error('Error verifying transaction:', error)
      throw error
    }
  }


  /**
   * Start polling for transaction verification
   */
  async startTransactionPolling(requestId, onStatusUpdate, maxAttempts = 60) {
    let attempts = 0
    
    const poll = async () => {
      try {
        attempts++
        console.log(`Polling attempt ${attempts}/${maxAttempts} for request ${requestId}`)
        
        const result = await this.verifyTransaction(requestId)
        
        if (onStatusUpdate) {
          onStatusUpdate(result, attempts)
        }

        // Check if transaction is complete
        if (result.transaction_status === 'success') {
          console.log('Transaction verified successfully')
          return { success: true, result }
        } else if (result.transaction_status === 'failed' || result.transaction_status === 'invalid') {
          console.log('Transaction failed')
          return { success: false, result }
        }

        // Continue polling if still pending and haven't exceeded max attempts
        if (attempts < maxAttempts && result.transaction_status === 'pending') {
          setTimeout(poll, 60000) // Poll every 60 seconds
        } else if (attempts >= maxAttempts) {
          console.log('Transaction polling timeout')
          return { success: false, result: { transaction_status: 'timeout', message: 'Transaction verification timeout' } }
        }
      } catch (error) {
        console.error(`Polling error (attempt ${attempts}):`, error)
        
        // Retry on error unless max attempts reached
        if (attempts < maxAttempts) {
          setTimeout(poll, 60000)
        } else {
          return { success: false, result: { transaction_status: 'error', message: error.message } }
        }
      }
    }

    // Start polling
    poll()
  }

  /**
   * Complete crypto purchase flow
   */
  async completeCryptoPurchase(amountUsd, rateAsDeposit = null) {
    try {
      // Step 1: Initialize purchase
      console.log('Step 1: Initializing crypto purchase...')
      const initData = await this.initCryptoPurchase(amountUsd, rateAsDeposit)

      // Step 2: Send transaction
      console.log('Step 2: Sending transaction...')
      const txResult = await this.sendTransaction(initData)

      // Step 3: Return data for polling
      return {
        success: true,
        requestId: initData.txid,
        transactionResult: txResult,
        initData: initData
      }
    } catch (error) {
      console.error('Complete crypto purchase failed:', error)
      throw error
    }
  }

  /**
   * Convert TON to nanoton (smallest unit)
   */
  tonToNanoton(tonAmount) {
    return Math.floor(parseFloat(tonAmount) * 1000000000).toString()
  }

  /**
   * Convert nanoton to TON
   */
  nanotonToTon(nanotonAmount) {
    return (parseInt(nanotonAmount) / 1000000000).toString()
  }

  /**
   * Subscribe to wallet connection changes
   */
  onStatusChange(callback) {
    if (this.tonConnect) {
      this.tonConnect.onStatusChange(callback)
    }
  }

  getChain() {
    return this.tonConnect?.wallet?.account?.chain || this.tonConnect?.wallet?.account?.network || null
  }

  isTestnet() {
    const chain = (this.getChain() || '').toString().toLowerCase()
    return chain.includes('test') || chain.includes('testnet') || chain === '-3' || chain === '-239'
  }

  /**
   * Unsubscribe from wallet connection changes
   */
  off(callback) {
    if (this.tonConnect && callback) {
      this.tonConnect.offStatusChange(callback)
    }
  }
}

// Singleton instance
export const tonConnectService = new TonConnectService()
