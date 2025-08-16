const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

class RegistrationService {
  async register(payload) {
  // payload: { first_name, last_name, country, email, phone, ref }
  // phone: combined string country_dial_code + local_number (digits only, no +), e.g. 380997126420
    let telegramInitData = null
    try { telegramInitData = window?.Telegram?.WebApp?.initData || null } catch (_) {}
    const body = { ...payload }
    if (telegramInitData) body.telegram_init_data = telegramInitData
    try {
      const res = await fetch(`${API_BASE_URL}/user/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      })
      const data = await res.json().catch(() => ({ status: 'failed', message: 'Invalid JSON' }))
  if (!res.ok) return { status: 'failed', message: data.message || 'Registration failed', target: data.target }
      return data
    } catch (e) {
      return { status: 'failed', message: e.message }
    }
  }
}

export default new RegistrationService()
