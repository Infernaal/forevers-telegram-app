import { ref, computed } from 'vue'

export function useCryptoRates() {
  const tonRate = ref(0) // TON price in USD
  const usdtRate = ref(1) // USDT is always ~$1
  const isLoading = ref(false)
  const error = ref(null)
  const lastUpdated = ref(null)

  const fetchRates = async () => {
    isLoading.value = true
    error.value = null
    
    try {
      // Using CoinGecko API for real-time rates
      const response = await fetch(
        'https://api.coingecko.com/api/v3/simple/price?ids=the-open-network,tether&vs_currencies=usd'
      )
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      
      tonRate.value = data['the-open-network']?.usd || 0
      usdtRate.value = data['tether']?.usd || 1
      lastUpdated.value = new Date()
      
      console.log('Crypto rates updated:', {
        TON: tonRate.value,
        USDT: usdtRate.value,
        updated: lastUpdated.value
      })
      
    } catch (err) {
      console.error('Failed to fetch crypto rates:', err)
      error.value = err.message
      // Fallback rates
      tonRate.value = 6.0 // fallback TON price
      usdtRate.value = 1.0 // USDT is stable
    } finally {
      isLoading.value = false
    }
  }

  // Convert USD amount to TON
  const convertUsdToTon = (usdAmount) => {
    if (!tonRate.value || tonRate.value === 0) return 0
    return usdAmount / tonRate.value
  }

  // Convert USD amount to USDT
  const convertUsdToUsdt = (usdAmount) => {
    return usdAmount / usdtRate.value
  }

  // Convert TON amount to nanotons (for transactions)
  const tonToNanotons = (tonAmount) => {
    return Math.floor(tonAmount * 1000000000).toString()
  }

  // Format crypto amounts for display
  const formatTonAmount = (tonAmount) => {
    return tonAmount.toFixed(4) + ' TON'
  }

  const formatUsdtAmount = (usdtAmount) => {
    return usdtAmount.toFixed(2) + ' USDT'
  }

  return {
    tonRate,
    usdtRate,
    isLoading,
    error,
    lastUpdated,
    fetchRates,
    convertUsdToTon,
    convertUsdToUsdt,
    tonToNanotons,
    formatTonAmount,
    formatUsdtAmount
  }
}
