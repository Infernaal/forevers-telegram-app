const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

export const CryptoService = {
  async initCryptoTransaction(payload) {
    const res = await fetch(`${API_BASE_URL}/forevers/crypto/init`, {
      method: 'POST',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    const data = await res.json()
    if (!res.ok || data.status === 'failed') {
      throw new Error(data.message || data.error || `HTTP ${res.status}`)
    }
    return data
  },

  async verifyCryptoTransaction(payload) {
    const res = await fetch(`${API_BASE_URL}/forevers/crypto/verify`, {
      method: 'POST',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    const data = await res.json()
    if (!res.ok || data.status === 'failed') {
      throw new Error(data.message || data.error || `HTTP ${res.status}`)
    }
    return data
  }
}
