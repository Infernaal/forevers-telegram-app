const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

export const TonCryptoService = {
  async initTonPurchase(payload) {
    const res = await fetch(`${API_BASE_URL}/crypto/ton/init`, {
      method: 'POST',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    const data = await res.json()
    if (!res.ok || data.status !== 'success') {
      throw new Error(data.message || 'Failed to init TON purchase')
    }
    return data
  },
  async verifyTonPurchase(payload) {
    const res = await fetch(`${API_BASE_URL}/crypto/ton/verify`, {
      method: 'POST',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    const data = await res.json()
    if (!res.ok) {
      throw new Error(data.message || 'Verification request failed')
    }
    return data
  }
}
