import { ref, onMounted } from 'vue'

/**
 * useCryptoRates composable
 * Responsibilities:
 *  - Fetch TON & USDT (USD) rates from CoinGecko
 *  - Cache last successful response in localStorage (reduces flashes / API hits)
 *  - Provide conversion + formatting helpers
 *  - Optional auto-refresh with stop() control
 *  - Abort in‑flight request when a new fetch starts (avoids race conditions)
 *
 * Backward compatibility: original returned keys preserved.
 *
 * @param {Object} options
 * @param {number} [options.refreshIntervalMs=120000] Auto refresh interval (ms); set 0 / null to disable
 * @param {number} [options.cacheTtlMs=300000] Cache TTL (ms)
 */
export function useCryptoRates (options = {}) {
  const {
    refreshIntervalMs = 120000,
    cacheTtlMs = 300000
  } = options

  const tonRate = ref(0) // TON price in USD
  const usdtRate = ref(1) // USDT ~ $1
  const isLoading = ref(false)
  const error = ref(null)
  const lastUpdated = ref(null)
  const isStale = ref(false)
  const nextRefreshAt = ref(null)

  // internals
  let intervalId = null
  let abortController = null
  const STORAGE_KEY = 'cryptoRatesCacheV1'

  const readCache = () => {
    try {
      const raw = localStorage.getItem(STORAGE_KEY)
      if (!raw) return
      const cached = JSON.parse(raw)
      if (!cached || !cached.timestamp) return
      const age = Date.now() - cached.timestamp
      if (age > cacheTtlMs) {
        isStale.value = true
        return
      }
      tonRate.value = cached.tonRate
      usdtRate.value = cached.usdtRate
      lastUpdated.value = new Date(cached.timestamp)
      isStale.value = false
    } catch (_) {
      /* ignore */
    }
  }

  const writeCache = () => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        tonRate: tonRate.value,
        usdtRate: usdtRate.value,
        timestamp: Date.now()
      }))
    } catch (_) {
      /* ignore quota */
    }
  }

  const fetchRates = async () => {
    if (isLoading.value) {
      // allow re-entry only if previous finished / aborted
      if (abortController) abortController.abort()
    }
    isLoading.value = true
    error.value = null
    abortController = new AbortController()

    try {
      const url = 'https://api.coingecko.com/api/v3/simple/price?ids=the-open-network,tether&vs_currencies=usd'
      const response = await fetch(url, { signal: abortController.signal, headers: { 'Accept': 'application/json' } })
      if (!response.ok) throw new Error(`HTTP ${response.status}`)
      const data = await response.json()
      const newTon = Number(data['the-open-network']?.usd) || 0
      const newUsdt = Number(data['tether']?.usd) || 1
      if (newTon > 0) tonRate.value = newTon
      if (newUsdt > 0) usdtRate.value = newUsdt
      lastUpdated.value = new Date()
      isStale.value = false
      writeCache()
    } catch (err) {
      if (err?.name === 'AbortError') return
      error.value = err.message || 'Failed to load rates'
      // Keep previous cached values; if none, apply fallback
      if (!tonRate.value) tonRate.value = 6.0
      if (!usdtRate.value) usdtRate.value = 1.0
    } finally {
      isLoading.value = false
      abortController = null
      if (refreshIntervalMs && refreshIntervalMs > 0) {
        nextRefreshAt.value = new Date(Date.now() + refreshIntervalMs)
      }
    }
  }

  const start = () => {
    if (intervalId || !refreshIntervalMs) return
    intervalId = setInterval(() => {
      fetchRates()
    }, refreshIntervalMs)
  }

  const stop = () => {
    if (intervalId) {
      clearInterval(intervalId)
      intervalId = null
    }
  }

  // Convert USD amount to TON
  const convertUsdToTon = (usdAmount) => {
    const v = Number(usdAmount)
    if (!Number.isFinite(v) || v <= 0 || !tonRate.value) return 0
    return v / tonRate.value
  }

  // Convert USD amount to USDT
  const convertUsdToUsdt = (usdAmount) => {
    const v = Number(usdAmount)
    if (!Number.isFinite(v) || v <= 0 || !usdtRate.value) return 0
    return v / usdtRate.value
  }

  // Convert TON amount to nanotons (for transactions) – using BigInt for safety
  const tonToNanotons = (tonAmount) => {
    const v = Number(tonAmount)
    if (!Number.isFinite(v) || v <= 0) return '0'
    // Avoid floating precision issues: multiply as string when needed
    const nano = BigInt(Math.floor(v * 1e9))
    return nano.toString()
  }

  const intlTon = new Intl.NumberFormat(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 4 })
  const intlUsdt = new Intl.NumberFormat(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })

  // Format crypto amounts for display
  const formatTonAmount = (tonAmount) => `${intlTon.format(Number(tonAmount) || 0)} TON`
  const formatUsdtAmount = (usdtAmount) => `${intlUsdt.format(Number(usdtAmount) || 0)} USDT`

  onMounted(() => {
    readCache()
    // If no fresh cache, fetch immediately
    if (!lastUpdated.value || isStale.value) fetchRates()
    if (refreshIntervalMs) start()
  })

  return {
    // reactive state
    tonRate,
    usdtRate,
    isLoading,
    error,
    lastUpdated,
    isStale,
    nextRefreshAt,
    // actions
    fetchRates,
    start,
    stop,
    // helpers (backward compatible names preserved)
    convertUsdToTon,
    convertUsdToUsdt,
    tonToNanotons,
    formatTonAmount,
    formatUsdtAmount
  }
}
