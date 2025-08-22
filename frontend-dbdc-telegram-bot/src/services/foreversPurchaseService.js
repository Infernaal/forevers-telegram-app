const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

export class ForeversPurchaseService {

  /**
   * Get current forevers prices from API
   * @returns {Promise<Object>} Prices response from API
   */
  static async getForeversPrices() {
    try {
      const response = await fetch(`${API_BASE_URL}/prices/forevers`, {
        method: 'GET',
        credentials: 'include',
        headers: {
          'Cache-Control': 'no-cache'
        }
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      console.log('Prices API response:', data)
      return data
    } catch (error) {
      console.error('Error fetching forevers prices:', error)
      throw error
    }
  }

  /**
   * Purchase Forevers using bonus or loyalty wallet
   * @param {Object} purchaseData - Purchase details
   * @param {string} purchaseData.wallet_type - "bonus" or "rent" 
   * @param {string} purchaseData.forever_type - "UAE", "KZ", "DE", "PL", "UA"
   * @param {number} purchaseData.forevers_amount - Amount of forevers to purchase
   * @param {number} purchaseData.final_rate - Exchange rate per forever
   * @param {number} purchaseData.usd_amount - Total USD amount
   * @returns {Promise<Object>} Purchase response
   */
  static async purchaseForevers(purchaseData) {
    try {
      const response = await fetch(`${API_BASE_URL}/forevers/purchase`, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(purchaseData)
      })

      const data = await response.json()

      // Log the response for debugging
      console.log('Purchase API response:', {
        status: response.status,
        ok: response.ok,
        data: data
      })

      if (!response.ok) {
        // Handle specific error messages from backend
        let errorMessage = data.message || data.detail || `HTTP error! status: ${response.status}`

        // Handle common error cases
        if (response.status === 400) {
          if (data.message?.includes('insufficient') || data.message?.includes('balance')) {
            errorMessage = 'Insufficient balance. Please check your wallet balance.'
          } else if (data.message?.includes('invalid')) {
            errorMessage = 'Invalid purchase parameters. Please try again.'
          }
        } else if (response.status === 401) {
          errorMessage = 'Authentication failed. Please log in again.'
        } else if (response.status === 403) {
          errorMessage = 'Access denied. You do not have permission to make this purchase.'
        } else if (response.status >= 500) {
          errorMessage = 'Server error. Please try again later.'
        }

        throw new Error(errorMessage)
      }

      // Check if API returned success but with error status in response body
      if (data.status === 'failed' || data.success === false) {
        throw new Error(data.message || data.error || 'Purchase failed')
      }

      return data
    } catch (error) {
      console.error('Error purchasing forevers:', error)
      throw error
    }
  }

  /**
   * Validate purchase data before sending to API
   * @param {Object} purchaseDetails - Purchase details from cart
   * @param {string} selectedPayment - Selected payment method ("bonus" or "loyalty")
   * @returns {Object} Validation result
   */
  static validatePurchaseData(purchaseDetails, selectedPayment) {
    if (!purchaseDetails || !purchaseDetails.foreversDetails) {
      return { valid: false, error: 'Missing purchase details' }
    }

    if (!selectedPayment || !['bonus', 'loyalty'].includes(selectedPayment)) {
      return { valid: false, error: 'Invalid payment method selected' }
    }

    if (!purchaseDetails.foreversDetails.length) {
      return { valid: false, error: 'No forevers selected for purchase' }
    }

    // Validate each forevers item
    for (const detail of purchaseDetails.foreversDetails) {
      if (!detail.code || typeof detail.code !== 'string' || detail.code.trim().length === 0) {
        return { valid: false, error: `Invalid forever type: ${detail.code}` }
      }
      
      if (!detail.amount || detail.amount <= 0) {
        return { valid: false, error: `Invalid amount for ${detail.code}` }
      }
      
      if (!detail.usdRate || detail.usdRate <= 0) {
        return { valid: false, error: `Invalid rate for ${detail.code}` }
      }
    }

    return { valid: true }
  }

  /**
   * Convert frontend purchase details to API format
   * @param {Object} purchaseDetails - Purchase details from cart
   * @param {string} selectedPayment - Selected payment method
   * @returns {Array} Array of purchase requests for API
   */
  static convertToApiFormat(purchaseDetails, selectedPayment) {
    if (!purchaseDetails?.foreversDetails) {
      return []
    }

    // Convert payment method
    const walletType = selectedPayment === 'loyalty' ? 'rent' : 'bonus'

    return purchaseDetails.foreversDetails.map(detail => ({
      wallet_type: walletType,
      forever_type: detail.code,
      forevers_amount: parseInt(detail.amount),
      final_rate: parseFloat(detail.usdRate),
      usd_amount: parseFloat(detail.totalCost)
    }))
  }

  /**
   * Process multiple forevers purchases (for cart with multiple items)
   * @param {Object} purchaseDetails - Purchase details from cart
   * @param {string} selectedPayment - Selected payment method
   * @returns {Promise<Object>} Combined purchase results
   */
  static async processMultiplePurchases(purchaseDetails, selectedPayment) {
    try {
      const validation = this.validatePurchaseData(purchaseDetails, selectedPayment)
      if (!validation.valid) {
        throw new Error(validation.error)
      }

      const apiRequests = this.convertToApiFormat(purchaseDetails, selectedPayment)
      const results = []
      const errors = []

      // Process each purchase sequentially to avoid concurrency issues
      for (const request of apiRequests) {
        try {
          const result = await this.purchaseForevers(request)
          console.log('Purchase result for', request.forever_type, ':', result)
          results.push(result)
        } catch (error) {
          console.error('Purchase error for', request.forever_type, ':', error.message)
          errors.push({
            forever_type: request.forever_type,
            error: error.message
          })
        }
      }

      const isSuccess = errors.length === 0 && results.length > 0
      console.log('Final purchase result:', {
        success: isSuccess,
        totalResults: results.length,
        totalErrors: errors.length,
        errors: errors
      })

      return {
        success: isSuccess,
        results,
        errors,
        totalProcessed: results.length,
        totalFailed: errors.length
      }
    } catch (error) {
      return {
        success: false,
        results: [],
        errors: [{ error: error.message }],
        totalProcessed: 0,
        totalFailed: 1
      }
    }
  }
}


