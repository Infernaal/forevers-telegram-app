// Service to establish and use Telegram-backed session
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

class TelegramUserService {
  // Call ONCE at app bootstrap to exchange Telegram initData for a server session cookie.
  async authWithInitData(initData) {
    // First check if we have cached session and validate it
    if (sessionStorage.getItem('sessionEstablished')) {
      const validationResult = await this.validateSession()
      if (validationResult.status === 'success') {
        return { status: 'success', cached: true, validated: true }
      } else {
        // Session is invalid, clear cache and proceed with fresh auth
        this.clearSession()
      }
    }

    try {
      // ✅ если забыли передать — возьмём каноничную строку сами
      const initDataString = typeof initData === 'string'
        ? initData
        : (window?.Telegram?.WebApp?.initData || '')

      // ⚠️ tgId только как хинт (на подпись не влияет)
      let tgId = 0
      try { tgId = window?.Telegram?.WebApp?.initDataUnsafe?.user?.id || 0 } catch (_) {}

      const res = await fetch(`${API_BASE_URL}/user/auth/by-telegram/${tgId}`, {
        method: 'GET',                   // лучше явно POST
        headers: {
          'X-Telegram-Init-Data': initDataString,
        },
        credentials: 'include'
      })

      const data = await res.json().catch(() => ({}))
      if (res.ok && data?.status === 'success') {
        sessionStorage.setItem('sessionEstablished', '1')
      }
      return data?.status ? data : { status: res.ok ? 'success' : 'failed', code: res.status }
    } catch (e) {
      return { status: 'failed', message: e?.message || 'Network error' }
    }
  }

  // Validate current session by checking /user/me endpoint
  async validateSession() {
    try {
      const response = await fetch(`${API_BASE_URL}/user/me`, {
        credentials: 'include',
        headers: {
          'Cache-Control': 'no-cache'
        }
      })
      if (response.ok) {
        const data = await response.json()
        return { status: 'success', data }
      } else {
        return { status: 'failed', code: response.status }
      }
    } catch (e) {
      return { status: 'failed', message: e?.message || 'Network error' }
    }
  }

  // Clear session cache
  clearSession() {
    sessionStorage.removeItem('sessionEstablished')
  }

  // Get current authorized user info (after session established)
  async getUserInfo() {
    try {
      const response = await fetch(`${API_BASE_URL}/user/me`, { credentials: 'include' })
      if (!response.ok) {
        // If unauthorized (401) or forbidden (403), clear session cache
        if (response.status === 401 || response.status === 403) {
          this.clearSession()
        }
        throw new Error('Network error')
      }
      return await response.json()
    } catch (e) {
      return { status: 'failed', message: e.message }
    }
  }

  // Get user's forevers balance and available limits
  async getUserBalance() {
    try {
      const response = await fetch(`${API_BASE_URL}/forevers/me`, { credentials: 'include' })
      if (!response.ok) {
        // If unauthorized (401) or forbidden (403), clear session cache
        if (response.status === 401 || response.status === 403) {
          this.clearSession()
        }
        throw new Error('Network error')
      }
      return await response.json()
    } catch (e) {
      return { status: 'failed', message: e.message }
    }
  }

  // Handle authorization errors globally - clear session cache for auth errors
  handleAuthError(response) {
    if (response && (response.status === 401 || response.status === 403)) {
      this.clearSession()
    }
  }

  // Logout user and clear session
  async logout() {
    try {
      await fetch(`${API_BASE_URL}/user/logout`, {
        method: 'POST',
        credentials: 'include'
      })
    } catch (_) { /* ignore */ }
    this.clearSession()
  }
}

export default new TelegramUserService()
