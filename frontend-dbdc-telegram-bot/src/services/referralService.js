const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

/**
 * Сервис для работы с реферальными ссылками
 */
class ReferralService {
  /**
   * Получает данные приглашения (ссылку и QR-код) одним запросом
   * @returns {Promise<Object>} Объект с invite_link, qr_code, user_id, code
   */
  async getInviteData() {
    try {
      const response = await fetch(`${BASE_URL}/api/v1/dbdc/invite`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include'
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching invite data:', error);
      throw error;
    }
  }

  /**
   * Получает полную реферральную ссылку для пользователя (оставлено для совместимости)
   * @returns {Promise<Object>} Объект с данными реферальной ссылки
   * @deprecated Используйте getInviteData() вместо этого метода
   */
  async getFullReferralLink() {
    // Используем новый единый endpoint для обратной совместимости
    const inviteData = await this.getInviteData();
    return {
      display_link: inviteData.invite_link,
      full_link: `https://t.me/your_bot_name?start=ref=${inviteData.user_id}&code=${inviteData.code}`,
      qr_params: `?ref=${inviteData.user_id}&code=${inviteData.code}`,
      user_id: inviteData.user_id,
      code: inviteData.code
    };
  }

}

export default new ReferralService();
