// Universal Deposits Service for all deposit types
const BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api/v1/dbdc'

export class DepositsService {
  /**
   * Get all user deposits grouped by type
   * @returns {Promise<Object>} Response with deposits by type
   */
  static async getUserDeposits() {
    try {
      const response = await fetch(`${BASE_URL}/forevers/deposits`, {
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
      return {
        status: 'failed',
        message: 'Failed to fetch deposits data'
      }
    }
  }

  /**
   * Get deposits filtered by specific type(s)
   * @param {string|string[]} types - Deposit type(s) to filter (e.g., 'UAE' or ['UAE', 'KZ'])
   * @returns {Promise<Object>} Response with filtered deposits
   */
  static async getDepositsByType(types) {
    try {
      const response = await this.getUserDeposits()
      
      if (response.status !== 'success' || !response.data) {
        return response
      }

      const filterTypes = Array.isArray(types) ? types : [types]
      const filteredDeposits = response.data.deposits_by_type.filter(
        deposit => filterTypes.includes(deposit.type)
      )

      // Calculate total for filtered types
      const totalUsdValue = filteredDeposits.reduce(
        (sum, deposit) => sum + parseFloat(deposit.total_usd_value || 0), 
        0
      )

      return {
        status: 'success',
        data: {
          user_id: response.data.user_id,
          deposits_by_type: filteredDeposits,
          total_usd_value: totalUsdValue,
          filtered_types: filterTypes
        },
        message: `Deposits for ${filterTypes.join(', ')} retrieved successfully`
      }
    } catch (error) {
      return {
        status: 'failed',
        message: 'Failed to filter deposits data'
      }
    }
  }

  /**
   * Get UAE deposits only (for backward compatibility)
   * @returns {Promise<Object>} Response with UAE deposits total
   */
  static async getUaeDeposits() {
    try {
      const response = await this.getDepositsByType('UAE')
      
      if (response.status !== 'success' || !response.data) {
        return response
      }

      // Transform to match uaeDepositsService format
      return {
        status: 'success',
        data: {
          user_id: response.data.user_id,
          total_uae_deposits: response.data.total_usd_value
        },
        message: 'UAE deposits total retrieved successfully'
      }
    } catch (error) {
      return {
        status: 'failed',
        message: 'Failed to fetch UAE deposits data'
      }
    }
  }

  /**
   * Get total USD value for all deposits
   * @returns {Promise<number>} Total USD value
   */
  static async getTotalUsdValue() {
    try {
      const response = await this.getUserDeposits()
      
      if (response.status === 'success' && response.data) {
        return parseFloat(response.data.total_usd_value || 0)
      }
      
      return 0
    } catch (error) {
      return 0
    }
  }

  /**
   * Get total USD value for specific deposit type
   * @param {string} type - Deposit type (UAE, KZ, DE, PL, UA)
   * @returns {Promise<number>} Total USD value for type
   */
  static async getTotalUsdValueByType(type) {
    try {
      const response = await this.getDepositsByType(type)
      
      if (response.status === 'success' && response.data) {
        return response.data.total_usd_value
      }
      
      return 0
    } catch (error) {
      return 0
    }
  }
}

export default DepositsService
