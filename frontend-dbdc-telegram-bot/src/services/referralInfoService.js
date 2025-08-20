/**
 * Service for fetching referral information from the backend API
 */
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

/**
 * Fetch referrer information by user ID
 * @param {string|number} refId - The referrer user ID
 * @returns {Promise<Object|null>} Referrer info or null
 */
export async function getReferrerInfo(refId) {
  if (!refId || isNaN(parseInt(refId))) {
    return null
  }

  try {
    const response = await fetch(`${API_BASE_URL}/referral/referrer/${refId}`)
    
    if (!response.ok) {
      if (response.status === 404) {
        console.warn(`Referrer with ID ${refId} not found`)
        return null
      }
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Error fetching referrer info:', error)
    return null
  }
}
