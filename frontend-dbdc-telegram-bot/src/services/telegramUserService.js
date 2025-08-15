// Service to establish and use Telegram-backed session
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

class TelegramUserService {
  // Call ONCE at app bootstrap to exchange Telegram initData for a server session cookie.
  async authWithInitData(initData) {
    if (sessionStorage.getItem('sessionEstablished')) {
      return { status: 'success', cached: true }
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
