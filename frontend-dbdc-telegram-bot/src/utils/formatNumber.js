// Utility to format large numbers into compact form (e.g., 1_000 -> 1K, 1_200 -> 1.2K, 1_000_000 -> 1M)
// Supports K, M, B, T. Falls back to locale string for smaller numbers.
export function formatCompactNumber(value, { decimals = 1 } = {}) {
  if (value === null || value === undefined || isNaN(value)) return '0'
  const abs = Math.abs(value)
  const units = [
    { v: 1e12, s: 'T' },
    { v: 1e9, s: 'B' },
    { v: 1e6, s: 'M' },
    { v: 1e3, s: 'K' }
  ]
  for (const u of units) {
    if (abs >= u.v) {
      const formatted = (value / u.v).toFixed(decimals)
      return `${trimTrailingZero(formatted)}${u.s}`
    }
  }
  return Number(value).toLocaleString()
}

function trimTrailingZero(str) {
  return str.replace(/\.0+$/, '').replace(/(\.[0-9]*?)0+$/, '$1').replace(/\.$/, '')
}

export function formatUSDPrefix(value, opts) {
  return 'USD ' + formatCompactNumber(value, opts)
}
