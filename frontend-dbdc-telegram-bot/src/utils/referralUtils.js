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
 * Expected format: "ref_4344_code_MJ4KSD" where ref can be 1-3+ digits and code is always 6 characters
 * @param {string} startParam - The start parameter from Telegram
 * @returns {Object|null} Parsed referral info or null
 */
export function parseReferralCode(startParam) {
  if (!startParam || typeof startParam !== 'string') {
    return null
  }

  const param = startParam.trim()

  // New format: ref_USERID_code_CODE (e.g., ref_4344_code_MJ4KSD)
  const newFormatMatch = param.match(/^ref_(\d+)_code_([A-Z0-9]{6})$/)
  if (newFormatMatch) {
    const userId = newFormatMatch[1]
    const code = newFormatMatch[2]
    return {
      type: 'ref_code',
      userId: userId,
      code: code,
      isReferral: true,
      firstName: null,
      lastName: null
    }
  }

  // Legacy format: Check if it starts with "ref_" or "code_"
  if (param.startsWith('ref_')) {
    const userId = param.substring(4) // Remove "ref_" prefix
    if (userId && !isNaN(parseInt(userId))) {
      return {
        type: 'ref',
        userId: userId,
        isReferral: true,
        username: null, // Will be populated if available
        firstName: null,
        lastName: null
      }
    }
  }

  if (param.startsWith('code_')) {
    const userId = param.substring(5) // Remove "code_" prefix
    if (userId && !isNaN(parseInt(userId))) {
      return {
        type: 'code',
        userId: userId,
        isReferral: true,
        username: null, // Will be populated if available
        firstName: null,
        lastName: null
      }
    }
  }

  // Fallback: check if it's just a numeric user ID
  if (!isNaN(parseInt(param))) {
    return {
      type: 'direct',
      userId: param,
      isReferral: true,
      username: null, // Will be populated if available
      firstName: null,
      lastName: null
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
 * Enrich referral info with additional user data if available
 * @param {Object} referralInfo - Basic referral info
 * @returns {Promise<Object>} Enhanced referral info
 */
export async function enrichReferralInfo(referralInfo) {
  if (!referralInfo) return null

  try {
    // Fetch referrer information from backend
    if (referralInfo.userId) {
      const referrerData = await getReferrerInfo(referralInfo.userId)
      if (referrerData) {
        // Update referral info with fetched data
        referralInfo.firstName = referrerData.first_name
        referralInfo.lastName = referrerData.last_name
        referralInfo.email = referrerData.email
      }
    }
  } catch (error) {
    console.warn('Could not enrich referral info:', error)
  }

  return referralInfo
}

// Import referrer info service
import { getReferrerInfo } from '@/services/referralInfoService.js'

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
