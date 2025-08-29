// Deposits Service for fetching all user deposits
const BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api/v1/dbdc'

export class DepositsService {
  /**
   * Get all deposits for current user
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
   * Get full deposits history for current user (raw)
   * @returns {Promise<Object>} Raw response from deposits-history endpoint
   */
  static async getUserDepositsHistory() {
    try {
      const response = await fetch(`${BASE_URL}/forevers/deposits-history`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include'
      })
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`)
      const data = await response.json()
      return data
    } catch (_) {
      return { status: 'failed', message: 'Failed to fetch deposits history' }
    }
  }

  /**
   * Normalize a deposits-history item to ListOfContracts shape
   */
  static normalizeHistoryItem(it) {
    const amountNum = parseFloat(it?.amount || 0)
    const rate = parseFloat(it?.rate_at_deposit || 0)
    const forevers = rate > 0 ? amountNum / rate : 0
    const ms = it?.requested_on ? Number(it.requested_on) * 1000 : null
    return {
      txid: it?.txid || '',
      processed_on: ms ? new Date(ms).toISOString() : null,
      forevers,
      price: rate || 0,
      type: it?.type || '',
      paid: amountNum || 0,
      access: (it?.activated_forevers || 0) === 1,
      participation: (it?.activated_loyalty || 0) === 1,
      _raw: it
    }
  }

  /**
   * Get contracts list normalized for ListOfContracts view
   */
  static async getUserContractsForList() {
    const res = await this.getUserDepositsHistory()
    if (res.status === 'success') {
      const deposits = (res.data?.deposits || []).map(this.normalizeHistoryItem)
      return {
        status: 'success',
        data: { user_id: res.data?.user_id, deposits, total_count: deposits.length },
        message: res.message || 'Deposits history normalized'
      }
    }
    return res
  }

  /**
   * Get deposits filtered by type
   * @param {string} type - Deposit type ('UAE', 'KZ', 'DE', 'PL', 'UA')
   * @returns {Promise<Object>} Response with filtered deposits
   */
  static async getDepositsByType(type) {
    const response = await this.getUserDeposits()
    
    if (response.status === 'success' && response.data && response.data.deposits) {
      const filteredDeposits = response.data.deposits.filter(deposit => deposit.type === type)
      
      return {
        status: 'success',
        data: {
          ...response.data,
          deposits: filteredDeposits,
          total_count: filteredDeposits.length
        },
        message: `${type} deposits retrieved successfully`
      }
    }
    
    return response
  }

  /**
   * Calculate total amount for specific deposit type
   * @param {string} type - Deposit type ('UAE', 'KZ', 'DE', 'PL', 'UA')
   * @returns {Promise<number>} Total amount for the type
   */
  static async getTotalByType(type) {
    const response = await this.getDepositsByType(type)
    
    if (response.status === 'success' && response.data && response.data.deposits) {
      return response.data.deposits.reduce((total, deposit) => {
        return total + parseFloat(deposit.paid || 0)
      }, 0)
    }
    
    return 0
  }

  /**
   * Calculate total UAE deposits (for Plan calculation)
   * @returns {Promise<number>} Total UAE deposits amount
   */
  static async getUaeTotalForPlan() {
    return await this.getTotalByType('UAE')
  }
}

export default DepositsService
