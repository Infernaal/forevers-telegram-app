import { TonConnect } from '@tonconnect/sdk'
import { TonConnectUI } from '@tonconnect/ui'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

class TonConnectService {
  constructor() {
    this.tonConnect = null
    this.tonConnectUI = null
    this.wallet = null
    this.isConnected = false
    this.isInitialized = false
  }

  /**
   * Initialize TON Connect with Telegram WebApp specific configuration
   */
  async initialize() {
    if (this.isInitialized) return

    try {
      // Initialize TON Connect UI for Telegram WebApp
      this.tonConnectUI = new TonConnectUI({
        manifestUrl: 'https://dbdc-mini.dubadu.com/tonconnect-manifest.json',
        restoreConnection: true,
        uiPreferences: {
          theme: 'SYSTEM',
          borderRadius: 'm',
          colorsSet: {
            [TonConnectUI.THEME.LIGHT]: {
              connectButton: {
                background: '#2019CE',
                foreground: '#FFFFFF'
              }
            },
            [TonConnectUI.THEME.DARK]: {
              connectButton: {
                background: '#2019CE', 
                foreground: '#FFFFFF'
              }
            }
          }
        },
        widgetRootId: 'ton-connect-root'
      })

      // Setup connection status listener
      this.tonConnectUI.onStatusChange(wallet => {
        this.wallet = wallet
        this.isConnected = !!wallet
        console.log('TON wallet connection status changed:', wallet)
      })

      // Initialize base TON Connect for transactions
      this.tonConnect = new TonConnect({
        manifestUrl: 'https://dbdc-mini.dubadu.com/tonconnect-manifest.json'
      })

      this.isInitialized = true
      console.log('TON Connect initialized successfully')
    } catch (error) {
      console.error('Failed to initialize TON Connect:', error)
      throw error
    }
  }

  /**
   * Connect wallet using TON Connect UI modal
   */
  async connectWallet() {
    if (!this.isInitialized) {
      await this.initialize()
    }

    try {
      // This will open TON Connect's native modal
      await this.tonConnectUI.connectWallet()
      return this.isConnected
    } catch (error) {
      console.error('Failed to connect TON wallet:', error)
      throw error
    }
  }

  /**
   * Disconnect current wallet
   */
  async disconnectWallet() {
    if (!this.tonConnectUI) return

    try {
      await this.tonConnectUI.disconnect()
      this.wallet = null
      this.isConnected = false
      console.log('TON wallet disconnected')
    } catch (error) {
      console.error('Failed to disconnect TON wallet:', error)
      throw error
    }
  }

  /**
   * Get current wallet info
   */
  getWallet() {
    return {
      wallet: this.wallet,
      isConnected: this.isConnected,
      address: this.wallet?.account?.address || null,
      publicKey: this.wallet?.account?.publicKey || null
    }
  }

  /**
   * Get wallet balance in TON
   */
  async getBalance() {
    if (!this.isConnected || !this.wallet?.account?.address) {
      throw new Error('Wallet not connected')
    }

    try {
      // Use TON API to get balance
      const response = await fetch(`https://toncenter.com/api/v2/getAddressBalance?address=${this.wallet.account.address}`)
      const data = await response.json()
      
      if (!data.ok) {
        throw new Error('Failed to fetch balance')
      }

      // Convert from nanotons to TON
      const balanceInTON = parseInt(data.result) / 1000000000
      return balanceInTON
    } catch (error) {
      console.error('Failed to get TON balance:', error)
      throw error
    }
  }

  /**
   * Send TON payment transaction
   */
  async sendPayment(recipientAddress, amountInTON, memo = '') {
    if (!this.isConnected || !this.tonConnectUI) {
      throw new Error('Wallet not connected')
    }

    try {
      const amountInNanotons = Math.floor(amountInTON * 1000000000).toString()

      const transaction = {
        validUntil: Math.floor(Date.now() / 1000) + 60, // Valid for 1 minute
        messages: [
          {
            address: recipientAddress,
            amount: amountInNanotons,
            payload: memo ? btoa(memo) : undefined // Base64 encode memo
          }
        ]
      }

      console.log('Sending TON transaction:', transaction)
      
      const result = await this.tonConnectUI.sendTransaction(transaction)
      console.log('TON transaction sent:', result)
      
      return result
    } catch (error) {
      console.error('Failed to send TON payment:', error)
      throw error
    }
  }

  /**
   * Create payment request for Forevers purchase
   */
  async createPaymentRequest(purchaseDetails, tonPrice) {
    if (!this.isConnected) {
      throw new Error('Wallet not connected')
    }

    try {
      const response = await fetch(`${API_BASE_URL}/ton/create-payment`, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          wallet_address: this.wallet.account.address,
          purchase_details: purchaseDetails,
          ton_price: tonPrice
        })
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      return data
    } catch (error) {
      console.error('Failed to create TON payment request:', error)
      throw error
    }
  }

  /**
   * Execute Forevers purchase with TON
   */
  async purchaseWithTON(purchaseDetails) {
    if (!this.isConnected) {
      throw new Error('Wallet not connected')
    }

    try {
      // Step 1: Get current TON price and create payment request
      const paymentRequest = await this.createPaymentRequest(purchaseDetails)
      
      // Step 2: Send TON transaction
      const txResult = await this.sendPayment(
        paymentRequest.recipient_address,
        paymentRequest.amount_ton,
        paymentRequest.memo
      )

      // Step 3: Confirm payment on backend
      const confirmResponse = await fetch(`${API_BASE_URL}/ton/confirm-payment`, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          payment_id: paymentRequest.payment_id,
          transaction_hash: txResult.boc,
          wallet_address: this.wallet.account.address
        })
      })

      if (!confirmResponse.ok) {
        throw new Error(`Failed to confirm payment: ${confirmResponse.status}`)
      }

      const confirmData = await confirmResponse.json()
      return {
        success: true,
        transaction_hash: txResult.boc,
        payment_id: paymentRequest.payment_id,
        data: confirmData
      }
    } catch (error) {
      console.error('Failed to purchase with TON:', error)
      throw error
    }
  }

  /**
   * Get TON price in USD
   */
  async getTONPrice() {
    try {
      // Use CoinGecko API to get current TON price
      const response = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd')
      const data = await response.json()
      
      return data['the-open-network']?.usd || 0
    } catch (error) {
      console.error('Failed to fetch TON price:', error)
      // Fallback price if API fails
      return 5.0
    }
  }

  /**
   * Calculate required TON amount for USD purchase
   */
  async calculateTONAmount(usdAmount) {
    const tonPrice = await this.getTONPrice()
    if (tonPrice === 0) {
      throw new Error('Unable to get TON price')
    }
    
    return usdAmount / tonPrice
  }

  /**
   * Restore previous connection on app load
   */
  async restoreConnection() {
    if (!this.isInitialized) {
      await this.initialize()
    }

    // TON Connect UI automatically restores connection
    // Just wait for status change
    return new Promise((resolve) => {
      const checkConnection = () => {
        if (this.tonConnectUI.connected) {
          this.isConnected = true
          this.wallet = this.tonConnectUI.wallet
          resolve(true)
        } else {
          resolve(false)
        }
      }

      // Check immediately
      setTimeout(checkConnection, 100)
    })
  }
}

// Export singleton instance
export const tonConnectService = new TonConnectService()
export { TonConnectService }
