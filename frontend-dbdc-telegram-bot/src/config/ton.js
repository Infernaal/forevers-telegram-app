// Centralized TON config
export const TON_NETWORK = import.meta.env.VITE_TON_NETWORK || 'testnet'
export const TON_RECEIVER = import.meta.env.VITE_TON_RECEIVER || ''
export const TON_COMMENT_PREFIX = import.meta.env.VITE_TON_COMMENT_PREFIX || 'Order'

export function validateTonAddress(address) {
  // Accept common user-friendly (EQ/UQ/kQ/0Q etc) or base64url raw (>=48 chars)
  if (!address) return false
  if (address.length < 36) return false
  return /^[A-Za-z0-9_-]+=?$/.test(address)
}

export async function normalizeTonAddress(address) {
  // Keep original form; only verify parseable, but don't force bounceable transformation.
  if (!address) return ''
  try {
    const mod = await import('@ton/core')
    mod.Address.parse(address) // will throw if invalid
    return address
  } catch {
    return address // leave as-is; downstream TonConnect may still handle or error gracefully
  }
}

// Dev-time warning
if (!TON_RECEIVER) {
  // eslint-disable-next-line no-console
  console.warn('[TON CONFIG] VITE_TON_RECEIVER is empty. Create .env with VITE_TON_RECEIVER=... and rebuild (Vite inlines at build time).')
}
