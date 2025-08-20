const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc';

/**
 * Сервис для работы с реферальной системой
 */
class ReferralService {
  /**
   * Получает данные приглашения (ссылку и QR-код) одним запросом
   * Backend возвращает invite_link в формате Telegram WebApp: https://t.me/dbdc_test_bot/app?startapp=ref_4344_code_52J01Z
   * @returns {Promise<Object>} Объект с invite_link, qr_code, user_id, code
   */
  async getInviteData() {
    try {
      const response = await fetch(`${BASE_URL}/referral/invite`, {
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
   * Получает полную реферальную ссылку для пользователя (оставлено для совместимости)
   * @returns {Promise<Object>} Объект с данными реферальной ссылки
   * @deprecated Используйте getInviteData() вместо этого метода
   */
  async getFullReferralLink() {
    // Используем новый единый endpoint для обратной совместимости
    const inviteData = await this.getInviteData();
    return {
      display_link: inviteData.invite_link,
      full_link: inviteData.invite_link, // Теперь display_link это и есть полная ссылка
      qr_params: `?ref=${inviteData.user_id}&code=${inviteData.code}`,
      user_id: inviteData.user_id,
      code: inviteData.code
    };
  }

  /**
   * Получает информацию о реферере по ID пользователя
   * @param {string|number} refId - ID пользователя-реферера
   * @returns {Promise<Object|null>} Информация о реферере или null
   */
  async getReferrerInfo(refId) {
    if (!refId || isNaN(parseInt(refId))) {
      return null;
    }

    try {
      const response = await fetch(`${BASE_URL}/referral/referrer/${refId}`);
      
      if (!response.ok) {
        if (response.status === 404) {
          console.warn(`Referrer with ID ${refId} not found`);
          return null;
        }
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching referrer info:', error);
      return null;
    }
  }
}

const referralService = new ReferralService();

// Экспорт для обратной совместимости
export const getReferrerInfo = (refId) => referralService.getReferrerInfo(refId);

export default referralService;
