// Universal Deposits Service for all deposit types
const BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api/v1/dbdc'

export class DepositsService {
  /**
   * Get detailed list of all user deposits
   * @returns {Promise<Object>} Response with array of deposits
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
   * Get deposits summary grouped by type (legacy format)
   * @returns {Promise<Object>} Response with deposits grouped by type
   */
  static async getUserDepositsSummary() {
    try {
      const response = await fetch(`${BASE_URL}/forevers/deposits/summary`, {
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
        message: 'Failed to fetch deposits summary data'
      }
    }
  }

  /**
   * Filter deposits array by specific type(s)
   * @param {Array} deposits - Array of deposit objects
   * @param {string|string[]} types - Deposit type(s) to filter (e.g., 'UAE' or ['UAE', 'KZ'])
   * @returns {Array} Filtered deposits array
   */
  static filterDepositsByType(deposits, types) {
    if (!deposits || !Array.isArray(deposits)) return []
    
    const filterTypes = Array.isArray(types) ? types : [types]
    return deposits.filter(deposit => filterTypes.includes(deposit.type))
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

      const filteredDeposits = this.filterDepositsByType(response.data.deposits, types)
      
      return {
        status: 'success',
        data: {
          user_id: response.data.user_id,
          deposits: filteredDeposits,
          total_count: filteredDeposits.length,
          filtered_types: Array.isArray(types) ? types : [types]
        },
        message: `Deposits for ${Array.isArray(types) ? types.join(', ') : types} retrieved successfully`
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

      // Calculate total USD value from UAE deposits
      const totalUaeDeposits = response.data.deposits.reduce(
        (sum, deposit) => sum + parseFloat(deposit.paid || 0), 
        0
      )

      // Transform to match old uaeDepositsService format
      return {
        status: 'success',
        data: {
          user_id: response.data.user_id,
          total_uae_deposits: totalUaeDeposits
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
   * Calculate total USD value from deposits array
   * @param {Array} deposits - Array of deposit objects
   * @returns {number} Total USD value
   */
  static calculateTotalUsdValue(deposits) {
    if (!deposits || !Array.isArray(deposits)) return 0
    
    return deposits.reduce((sum, deposit) => sum + parseFloat(deposit.paid || 0), 0)
  }

  /**
   * Calculate total forevers from deposits array
   * @param {Array} deposits - Array of deposit objects
   * @returns {number} Total forevers
   */
  static calculateTotalForevers(deposits) {
    if (!deposits || !Array.isArray(deposits)) return 0
    
    return deposits.reduce((sum, deposit) => sum + parseFloat(deposit.forevers || 0), 0)
  }

  /**
   * Get total USD value for all deposits
   * @returns {Promise<number>} Total USD value
   */
  static async getTotalUsdValue() {
    try {
      const response = await this.getUserDeposits()
      
      if (response.status === 'success' && response.data) {
        return this.calculateTotalUsdValue(response.data.deposits)
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
        return this.calculateTotalUsdValue(response.data.deposits)
      }
      
      return 0
    } catch (error) {
      return 0
    }
  }

  /**
   * Group deposits by type for summary
   * @param {Array} deposits - Array of deposit objects
   * @returns {Object} Deposits grouped by type with totals
   */
  static groupDepositsByType(deposits) {
    if (!deposits || !Array.isArray(deposits)) return {}
    
    const grouped = {}
    
    deposits.forEach(deposit => {
      const type = deposit.type
      if (!grouped[type]) {
        grouped[type] = {
          type,
          deposits: [],
          total_usd_value: 0,
          total_forevers: 0,
          count: 0
        }
      }
      
      grouped[type].deposits.push(deposit)
      grouped[type].total_usd_value += parseFloat(deposit.paid || 0)
      grouped[type].total_forevers += parseFloat(deposit.forevers || 0)
      grouped[type].count += 1
    })
    
    return grouped
  }
}

export default DepositsService
