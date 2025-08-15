const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

class AuthByEmailService {
  async auth(email, options = {}) {
    // options: { initData?: string }
    let telegramId = null
    let telegramInitData = options.initData || null
    try { telegramId = window?.Telegram?.WebApp?.initDataUnsafe?.user?.id || null } catch(e) { telegramId = null }
    if (!telegramInitData) {
      try { telegramInitData = window?.Telegram?.WebApp?.initData || null } catch(e) { telegramInitData = null }
    }
    try {
      const response = await fetch(`${API_BASE_URL}/user/auth/by-email`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, telegram_id: telegramId, telegram_init_data: telegramInitData })
      })
      if (!response.ok) throw new Error('Network error')
      return await response.json()
    } catch (e) {
      return { status: 'failed', target: '/email-not-registered', message: e.message }
    }
  }
}

export default new AuthByEmailService()
