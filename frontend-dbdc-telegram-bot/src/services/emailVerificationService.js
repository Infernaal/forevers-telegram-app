// API service for email verification
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1/dbdc'

class EmailVerificationService {
  async sendVerificationCode(email) {
    try {
      const response = await fetch(`${API_BASE_URL}/email/send-verification-code`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email })
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.detail || 'Failed to send verification code')
      }

      return {
        success: true,
        data: data,
        message: data.message
      }
    } catch (error) {
      return {
        success: false,
        error: error.message
      }
    }
  }

  async verifyCode(email, code) {
    try {
      const response = await fetch(`${API_BASE_URL}/email/verify-code`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, code })
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.detail || 'Failed to verify code')
      }

      return {
        success: data.valid,
        data: data,
        message: data.message
      }
    } catch (error) {
      return {
        success: false,
        error: error.message
      }
    }
  }

  async resendVerificationCode(email) {
    try {
      const response = await fetch(`${API_BASE_URL}/email/resend-verification-code`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email })
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.detail || 'Failed to resend verification code')
      }

      return {
        success: true,
        data: data,
        message: data.message
      }
    } catch (error) {
      return {
        success: false,
        error: error.message
      }
    }
  }
}

export default new EmailVerificationService()
