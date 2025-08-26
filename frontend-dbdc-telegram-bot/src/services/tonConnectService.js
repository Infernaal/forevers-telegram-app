const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

export class TonConnectService {
  
  /**
   * Get USD to TON conversion rate
   * @param {number} usdAmount - Amount in USD
   * @returns {Promise<Object>} Conversion data including TON amount
   */
  static async getUsdToTonRate(usdAmount) {
    try {
      const response = await fetch(`${API_BASE_URL}/ton/convert-usd`, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ usd_amount: usdAmount })
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      console.log('USD to TON conversion:', data)
      return data
    } catch (error) {
      console.error('Error getting USD to TON rate:', error)
      throw error
    }
  }

  /**
   * Initiate TON transaction on backend
   * @param {Object} transactionData - Transaction data
   * @param {number} transactionData.usd_amount - Amount in USD
   * @param {number} transactionData.ton_amount - Amount in TON
   * @param {string} transactionData.wallet_address - User's wallet address
   * @param {Array} transactionData.forevers_details - Forevers purchase details
   * @returns {Promise<Object>} Transaction initialization response
   */
  static async initiateTonTransaction(transactionData) {
    try {
      const response = await fetch(`${API_BASE_URL}/ton/initiate`, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(transactionData)
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      console.log('TON transaction initiated:', data)
      return data
    } catch (error) {
      console.error('Error initiating TON transaction:', error)
      throw error
    }
  }

  /**
   * Verify TON transaction on blockchain
   * @param {string} txHash - Transaction hash
   * @param {string} depositId - Deposit ID from backend
   * @returns {Promise<Object>} Verification response
   */
  static async verifyTonTransaction(txHash, depositId) {
    try {
      const response = await fetch(`${API_BASE_URL}/ton/verify`, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          tx_hash: txHash,
          deposit_id: depositId
        })
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      console.log('TON transaction verified:', data)
      return data
    } catch (error) {
      console.error('Error verifying TON transaction:', error)
      throw error
    }
  }

  /**
   * Create TON transaction object for TonConnect
   * @param {string} toAddress - Recipient address
   * @param {string} tonAmount - Amount in nanotons (string)
   * @param {string} comment - Transaction comment
   * @returns {Object} Transaction object for TonConnect
   */
  static createTonTransaction(toAddress, tonAmount, comment = '') {
    return {
      validUntil: Math.floor(Date.now() / 1000) + 600, // 10 minutes
      messages: [
        {
          address: toAddress,
          amount: tonAmount, // in nanotons
          payload: comment ? this.encodeComment(comment) : undefined
        }
      ]
    }
  }

  /**
   * Encode comment for TON transaction
   * @param {string} comment - Comment text
   * @returns {string} Encoded comment
   */
  static encodeComment(comment) {
    // Simple encoding for comment - in production should use proper BOC encoding
    return btoa(comment)
  }

  /**
   * Convert TON to nanotons
   * @param {number} tonAmount - Amount in TON
   * @returns {string} Amount in nanotons as string
   */
  static tonToNanotons(tonAmount) {
    return (Math.floor(tonAmount * 1e9)).toString()
  }

  /**
   * Convert nanotons to TON
   * @param {string|number} nanotons - Amount in nanotons
   * @returns {number} Amount in TON
   */
  static nanotonsToTon(nanotons) {
    return Number(nanotons) / 1e9
  }

  /**
   * Process complete TON payment flow
   * @param {Object} paymentData - Payment data
   * @param {Object} tonConnectInstance - TonConnect instance
   * @returns {Promise<Object>} Payment result
   */
  static async processTonPayment(paymentData, tonConnectInstance) {
    try {
      // Step 1: Get conversion rate
      const conversionData = await this.getUsdToTonRate(paymentData.usd_amount)
      
      // Step 2: Initiate transaction on backend
      const initData = {
        ...paymentData,
        ton_amount: conversionData.ton_amount,
        ton_rate: conversionData.ton_rate
      }
      
      const initResponse = await this.initiateTonTransaction(initData)
      
      // Step 3: Create TON transaction
      const tonTransaction = this.createTonTransaction(
        initResponse.recipient_address,
        this.tonToNanotons(conversionData.ton_amount),
        `Forevers Purchase - ${initResponse.deposit_id}`
      )
      
      // Step 4: Send transaction via TonConnect
      const txResult = await tonConnectInstance.sendTransaction(tonTransaction)
      
      // Step 5: Verify transaction on backend
      const verificationResult = await this.verifyTonTransaction(
        txResult.boc, // Transaction hash
        initResponse.deposit_id
      )
      
      return {
        success: true,
        transaction_hash: txResult.boc,
        deposit_id: initResponse.deposit_id,
        verification: verificationResult
      }
      
    } catch (error) {
      console.error('TON payment failed:', error)
      throw error
    }
  }
}
