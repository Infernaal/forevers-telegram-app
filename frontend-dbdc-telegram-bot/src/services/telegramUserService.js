// Service to verify Telegram user existence in backend
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

class TelegramUserService {
  async getUserByTelegramId(telegramId) {
    try {
  const response = await fetch(`${API_BASE_URL}/user/auth/by-telegram/${telegramId}`)
      if (!response.ok) {
        throw new Error('Network error')
      }
      const data = await response.json()
      return data
    } catch (e) {
      return { status: 'failed', message: e.message }
    }
  }
}

export default new TelegramUserService()
