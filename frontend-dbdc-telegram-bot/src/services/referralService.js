const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

/**
 * Сервис для работы с реферальными ссылками
 */
class ReferralService {
  /**
   * Получает полную реферральную ссылку для пользователя
   * @returns {Promise<Object>} Объект с данными реферальной ссылки
   */
  async getFullReferralLink() {
    try {
      const response = await fetch(`${BASE_URL}/api/v1/dbdc/full-referral-link`, {
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
      console.error('Error fetching referral link:', error);
      throw error;
    }
  }

  /**
   * Получает реферальную ссылку в формате ?ref=user_id&code={6 digits}
   * @returns {Promise<Object>} Объект с параметрами реферальной ссылки
   */
  async getReferralLink() {
    try {
      const response = await fetch(`${BASE_URL}/api/v1/dbdc/referral-link`, {
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
      console.error('Error fetching referral link:', error);
      throw error;
    }
  }

  /**
   * Генерирует QR-код для реферальной ссылки
   * @param {string} referralLink - Реферальная ссылка в формате ?ref=user_id&code=XXXXXX
   * @returns {Promise<Blob>} Blob объект с изображением QR-кода
   */
  async generateQRCode(referralLink) {
    try {
      const response = await fetch(`${BASE_URL}/api/v1/dbdc/generate-qr-code`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({
          referral_link: referralLink
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const blob = await response.blob();
      return blob;
    } catch (error) {
      console.error('Error generating QR code:', error);
      throw error;
    }
  }

  /**
   * Создает URL для отображения QR-кода из Blob
   * @param {Blob} qrBlob - Blob объект с QR-кодом
   * @returns {string} URL для отображения изображения
   */
  createQRImageURL(qrBlob) {
    return URL.createObjectURL(qrBlob);
  }

  /**
   * Освобождает URL объект
   * @param {string} url - URL для освобождения
   */
  revokeQRImageURL(url) {
    URL.revokeObjectURL(url);
  }
}

export default new ReferralService();
