const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

class CryptoService {
  async initTonPurchase(usdAmount, walletAddress, options = {}) {
    const body = {
      usd_amount: Number(usdAmount),
      wallet_address: walletAddress,
      ...(options.foreversPrice != null ? { forevers_price: Number(options.foreversPrice) } : {}),
      ...(options.foreversType ? { forevers_type: String(options.foreversType) } : {})
    }
    const res = await fetch(`${API_BASE_URL}/forevers/crypto/init`, {
      method: 'POST',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    })
    const data = await res.json().catch(() => ({}))
    if (!res.ok) {
      throw new Error(data?.message || data?.error || `HTTP ${res.status}`)
    }
    return data
  }

  async verifyTonPurchase(verifyId) {
    const url = new URL(`${API_BASE_URL}/forevers/crypto/verify`)
    if (verifyId) url.searchParams.set('id', verifyId)
    const res = await fetch(url.toString(), { method: 'GET', credentials: 'include' })
    const data = await res.json().catch(() => ({}))
    if (!res.ok) {
      throw new Error(data?.message || data?.error || `HTTP ${res.status}`)
    }
    return data
  }
}

export default new CryptoService()
