const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

export class TonConnectService {

  /**
   * Initiate crypto transaction (includes USD to TON conversion)
   * @param {Object} transactionData - Transaction data
   * @param {number} transactionData.usd_amount - Amount in USD
   * @param {string} transactionData.wallet_address - User's wallet address
   * @param {Array} transactionData.forevers_details - Forevers purchase details
   * @returns {Promise<Object>} Transaction initialization response with TON amount and rate
   */
  static async initiateCryptoTransaction(transactionData) {
    try {
      const response = await fetch(`${API_BASE_URL}/forevers/crypto/init`, {
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
      console.log('Crypto transaction initiated:', data)
      return data
    } catch (error) {
      console.error('Error initiating crypto transaction:', error)
      throw error
    }
  }

  /**
   * Verify crypto transaction on blockchain
   * @param {string} txHash - Transaction hash
   * @param {string} depositId - Deposit ID from backend
   * @returns {Promise<Object>} Verification response
   */
  static async verifyCryptoTransaction(txHash, depositId) {
    try {
      const response = await fetch(`${API_BASE_URL}/forevers/crypto/verify`, {
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
      console.log('Crypto transaction verified:', data)
      return data
    } catch (error) {
      console.error('Error verifying crypto transaction:', error)
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
   * Process complete crypto payment flow
   * @param {Object} paymentData - Payment data
   * @param {Object} tonConnectInstance - TonConnect instance
   * @returns {Promise<Object>} Payment result
   */
  static async processCryptoPayment(paymentData, tonConnectInstance) {
    try {
      // Step 1: Initiate transaction on backend (includes USD to TON conversion)
      const initResponse = await this.initiateCryptoTransaction(paymentData)

      // Step 2: Create TON transaction
      const tonTransaction = this.createTonTransaction(
        initResponse.recipient_address,
        this.tonToNanotons(initResponse.ton_amount),
        `Forevers Purchase - ${initResponse.deposit_id}`
      )

      // Step 3: Send transaction via TonConnect
      const txResult = await tonConnectInstance.sendTransaction(tonTransaction)

      // Step 4: Verify transaction on backend
      const verificationResult = await this.verifyCryptoTransaction(
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
      console.error('Crypto payment failed:', error)
      throw error
    }
  }
}
