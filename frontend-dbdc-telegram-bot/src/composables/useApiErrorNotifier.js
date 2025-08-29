import { reactive, toRefs } from 'vue'

const state = reactive({
  visible: false,
  routeKey: null,
  message: '',
  status: null,
  detail: null,
  timestamp: 0
})

let hideTimer = null

const ROUTE_MAP = {
  forevers_prices: 'Failed to load prices',
  forevers_user_balance: 'Failed to load balances',
  user_me: 'Failed to load profile',
  forevers_purchase: 'Purchase failed. Please check your balance and try again.',
  wallet_connection: 'Failed to connect to wallet. Please try again.',
  crypto_purchase: 'Payment could not be processed via wallet.'
}

function buildMessage(routeKey, opts) {
  const fallback = ROUTE_MAP[routeKey] || 'Unexpected error.'
  if (opts && typeof opts.message === 'string' && opts.message.trim()) return opts.message.trim()
  if (opts && typeof opts.detail === 'string' && opts.detail.trim()) return opts.detail.trim()
  if (opts?.error && opts.error.name === 'TypeError') return 'Network issue. Check connection.'
  return fallback
}

export function useApiErrorNotifier() {
  function showError(routeKey, opts = {}) {
    const msg = buildMessage(routeKey, opts)
    state.routeKey = routeKey
    state.message = msg
    state.status = opts.status || null
    state.detail = opts.detail || null
    state.timestamp = Date.now()
    state.visible = true
    if (hideTimer) clearTimeout(hideTimer)
    hideTimer = setTimeout(() => { state.visible = false }, opts.ttl || 5000)
  }

  function hide() {
    state.visible = false
    if (hideTimer) { clearTimeout(hideTimer); hideTimer = null }
  }

  return { ...toRefs(state), showError, hide }
}

export function scheduleRetry(fn, delay = 3000) {
  return setTimeout(fn, delay)
}
