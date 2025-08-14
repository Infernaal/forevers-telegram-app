// Service to establish and use Telegram-backed session
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

class TelegramUserService {
  // Call ONCE at app bootstrap to exchange Telegram initData for a server session cookie.
  async authWithInitData(initData) {
    // Skip if we already marked session established in this tab
    if (sessionStorage.getItem('sessionEstablished')) {
      return { status: 'success', cached: true }
    }
    try {
      const response = await fetch(`${API_BASE_URL}/user/auth/by-telegram/0`, {
        headers: { 'X-Telegram-Init-Data': initData },
        credentials: 'include'
      })
      const data = await response.json()
      if (data.status === 'success') {
        sessionStorage.setItem('sessionEstablished', '1')
      }
      return data
    } catch (e) {
      return { status: 'failed', message: e.message }
    }
  }

  // Get current authorized user info (after session established)
  async getUserInfo() {
    try {
      const response = await fetch(`${API_BASE_URL}/user/me`, { credentials: 'include' })
      if (!response.ok) throw new Error('Network error')
      return await response.json()
    } catch (e) {
      return { status: 'failed', message: e.message }
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
    sessionStorage.removeItem('sessionEstablished')
  }
}

export default new TelegramUserService()
