// API service for email verification
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

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

      if (!response.ok) {
        let errorMessage = 'Failed to send verification code'
        try {
          const errorData = await response.json()
          errorMessage = errorData.detail || errorMessage
        } catch (jsonError) {
          // If JSON parsing fails, use default error message
          console.warn('Failed to parse error response:', jsonError)
        }
        throw new Error(errorMessage)
      }

      const data = await response.json()

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

      if (!response.ok) {
        let errorMessage = 'Failed to verify code'
        try {
          const errorData = await response.json()
          errorMessage = errorData.detail || errorMessage
        } catch (jsonError) {
          console.warn('Failed to parse error response:', jsonError)
        }
        throw new Error(errorMessage)
      }

      const data = await response.json()

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

      if (!response.ok) {
        let errorMessage = 'Failed to resend verification code'
        try {
          const errorData = await response.json()
          errorMessage = errorData.detail || errorMessage
        } catch (jsonError) {
          console.warn('Failed to parse error response:', jsonError)
        }
        throw new Error(errorMessage)
      }

      const data = await response.json()

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
