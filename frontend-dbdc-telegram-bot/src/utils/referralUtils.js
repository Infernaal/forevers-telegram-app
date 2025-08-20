/**
 * Utilities for handling Telegram Web App referral parameters
 */

/**
 * Get start parameter from Telegram Web App
 * @returns {string|null} The start parameter or null if not found
 */
export function getTelegramStartParam() {
  try {
    // Try to get from Telegram Web App initDataUnsafe
    const startParam = window?.Telegram?.WebApp?.initDataUnsafe?.start_param
    if (startParam) {
      return startParam
    }

    // Fallback: try to get from URL query parameters
    const urlParams = new URLSearchParams(window.location.search)
    const tgWebAppStartParam = urlParams.get('tgWebAppStartParam')
    if (tgWebAppStartParam) {
      return tgWebAppStartParam
    }

    return null
  } catch (error) {
    console.error('Error getting Telegram start param:', error)
    return null
  }
}

/**
 * Parse referral code from start parameter
 * Expected format: "ref_USERID" or "code_USERID" or just "USERID"
 * @param {string} startParam - The start parameter from Telegram
 * @returns {Object|null} Parsed referral info or null
 */
export function parseReferralCode(startParam) {
  if (!startParam || typeof startParam !== 'string') {
    return null
  }

  const param = startParam.trim()
  
  // Check if it starts with "ref_" or "code_"
  if (param.startsWith('ref_')) {
    const userId = param.substring(4) // Remove "ref_" prefix
    if (userId && !isNaN(parseInt(userId))) {
      return {
        type: 'ref',
        userId: userId,
        isReferral: true
      }
    }
  }
  
  if (param.startsWith('code_')) {
    const userId = param.substring(5) // Remove "code_" prefix
    if (userId && !isNaN(parseInt(userId))) {
      return {
        type: 'code',
        userId: userId,
        isReferral: true
      }
    }
  }

  // Fallback: check if it's just a numeric user ID
  if (!isNaN(parseInt(param))) {
    return {
      type: 'direct',
      userId: param,
      isReferral: true
    }
  }

  return null
}

/**
 * Check if user came through referral link
 * @returns {Object|null} Referral info or null if not a referral
 */
export function getReferralInfo() {
  const startParam = getTelegramStartParam()
  if (!startParam) {
    return null
  }

  return parseReferralCode(startParam)
}

/**
 * Store referral info in session storage for later use
 * @param {Object} referralInfo - The referral information
 */
export function storeReferralInfo(referralInfo) {
  if (!referralInfo) return
  
  try {
    sessionStorage.setItem('referralInfo', JSON.stringify(referralInfo))
  } catch (error) {
    console.error('Error storing referral info:', error)
  }
}

/**
 * Get stored referral info from session storage
 * @returns {Object|null} Stored referral info or null
 */
export function getStoredReferralInfo() {
  try {
    const stored = sessionStorage.getItem('referralInfo')
    return stored ? JSON.parse(stored) : null
  } catch (error) {
    console.error('Error getting stored referral info:', error)
    return null
  }
}

/**
 * Clear stored referral info
 */
export function clearReferralInfo() {
  try {
    sessionStorage.removeItem('referralInfo')
  } catch (error) {
    console.error('Error clearing referral info:', error)
  }
}

/**
 * Generate referral link (helper function)
 * @param {string} userId - The user ID to create referral for
 * @param {string} botUsername - Telegram bot username
 * @returns {string} Generated referral link
 */
export function generateReferralLink(userId, botUsername = 'your_bot_name') {
  const startParam = `ref_${userId}`
  return `https://t.me/${botUsername}?start=${startParam}`
}
