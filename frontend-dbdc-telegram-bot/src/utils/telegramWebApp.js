/**
 * Utility functions for handling Telegram WebApp initialization and start parameters
 */

/**
 * Extracts start parameter from Telegram WebApp
 * @returns {string|null} Start parameter or null if not found
 */
export function getStartParameter() {
  try {
    if (!window.Telegram || !window.Telegram.WebApp) {
      return null
    }

    const initDataUnsafe = window.Telegram.WebApp.initDataUnsafe
    
    // Check for start_param in initDataUnsafe
    if (initDataUnsafe?.start_param) {
      return initDataUnsafe.start_param
    }

    // Fallback: parse from initData string
    const initData = window.Telegram.WebApp.initData
    if (!initData) {
      return null
    }

    const params = new URLSearchParams(initData)
    const startParam = params.get('start_param')
    
    return startParam || null
  } catch (error) {
    console.error('Error extracting start parameter:', error)
    return null
  }
}

/**
 * Parses referral information from start parameter
 * @param {string} startParam - The start parameter from Telegram
 * @returns {Object|null} Referral info object or null
 */
export function parseReferralInfo(startParam) {
  if (!startParam) {
    return null
  }

  try {
    // Expected format: ref_4344_code_ZKOXJK
    const referralMatch = startParam.match(/^ref_(\d+)_code_([A-Z0-9]+)$/i)
    
    if (referralMatch) {
      return {
        isReferral: true,
        userId: referralMatch[1],
        code: referralMatch[2],
        fullParam: startParam
      }
    }

    // Check for other possible formats
    if (startParam.startsWith('ref_')) {
      return {
        isReferral: true,
        userId: null,
        code: null,
        fullParam: startParam,
        rawParam: startParam
      }
    }

    return null
  } catch (error) {
    console.error('Error parsing referral info:', error)
    return null
  }
}

/**
 * Gets complete referral context from Telegram WebApp
 * @returns {Object} Complete referral context
 */
export function getReferralContext() {
  const startParam = getStartParameter()
  const referralInfo = parseReferralInfo(startParam)
  
  return {
    hasStartParam: !!startParam,
    startParam,
    isReferral: referralInfo?.isReferral || false,
    referralInfo,
    telegramInitData: window.Telegram?.WebApp?.initData || null,
    telegramUser: window.Telegram?.WebApp?.initDataUnsafe?.user || null
  }
}

/**
 * Checks if the current session came from a referral link
 * @returns {boolean} True if this is a referral session
 */
export function isReferralSession() {
  const context = getReferralContext()
  return context.isReferral
}

/**
 * Stores referral context in sessionStorage for use across navigation
 * @param {Object} context - Referral context to store
 */
export function storeReferralContext(context) {
  try {
    sessionStorage.setItem('referralContext', JSON.stringify(context))
  } catch (error) {
    console.error('Error storing referral context:', error)
  }
}

/**
 * Retrieves stored referral context from sessionStorage
 * @returns {Object|null} Stored referral context or null
 */
export function getStoredReferralContext() {
  try {
    const stored = sessionStorage.getItem('referralContext')
    return stored ? JSON.parse(stored) : null
  } catch (error) {
    console.error('Error retrieving referral context:', error)
    return null
  }
}

/**
 * Clears stored referral context
 */
export function clearReferralContext() {
  try {
    sessionStorage.removeItem('referralContext')
  } catch (error) {
    console.error('Error clearing referral context:', error)
  }
}
