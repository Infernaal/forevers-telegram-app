const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

export const CryptoPaymentService = {
  async initiate(order) {
    const url = new URL(`${API_BASE_URL}/forevers/crypto/initiate`)
    if (order?.chain) url.searchParams.set('chain', order.chain)
    const res = await fetch(url.toString(), {
      method: 'POST',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(order)
    })
    const data = await res.json()
    if (!res.ok || data.status !== 'success') throw new Error(data.message || 'Failed to initiate crypto order')
    return data
  },
  async confirm(payload) {
    const res = await fetch(`${API_BASE_URL}/forevers/crypto/confirm`, {
      method: 'POST',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    const data = await res.json()
    if (!res.ok || data.status !== 'success') throw new Error(data.message || 'Failed to confirm crypto payment')
    return data
  }
}
