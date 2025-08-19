const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

class ReferrerService {
  /**
   * Get referrer information by user ID
   * @param {string} userId - The referrer user ID
   * @returns {Promise<Object>} Referrer information
   */
  async getReferrerInfo(userId) {
    try {
      const response = await fetch(`${API_BASE_URL}/user/referrer/${userId}`, {
        method: 'GET',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json'
        }
      })

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`)
      }

      const data = await response.json()
      return {
        success: true,
        data: data
      }
    } catch (error) {
      console.error('Error fetching referrer info:', error)
      return {
        success: false,
        error: error.message,
        data: null
      }
    }
  }
}

export default new ReferrerService()
