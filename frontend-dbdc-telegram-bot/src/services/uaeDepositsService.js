// UAE Deposits Service for plan calculation
const BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'

export class UaeDepositsService {
  /**
   * Get total UAE deposits for current user
   * @returns {Promise<Object>} Response with total UAE deposits
   */
  static async getUserUaeDeposits() {
    try {
      const response = await fetch(`${BASE_URL}/forevers/uae-deposits`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include'
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      return data
    } catch (error) {
      console.error('UAE Deposits Service Error:', error)
      return {
        status: 'failed',
        message: 'Failed to fetch UAE deposits data'
      }
    }
  }
}

export default UaeDepositsService
