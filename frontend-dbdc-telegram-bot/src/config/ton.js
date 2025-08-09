// Centralized TON config
export const TON_NETWORK = import.meta.env.VITE_TON_NETWORK || 'testnet'
export const TON_RECEIVER = import.meta.env.VITE_TON_RECEIVER || ''
export const TON_COMMENT_PREFIX = import.meta.env.VITE_TON_COMMENT_PREFIX || 'Order'

export function validateTonAddress(address) {
  return !!address && /[A-Za-z0-9_-]{48,}/.test(address)
}

export async function normalizeTonAddress(address) {
  if (!address) return ''
  try {
    const mod = await import('@ton/core')
    // parse either raw or user-friendly
    const parsed = mod.Address.parse(address)
    // Return bounceable user-friendly testnet/mainnet depending on workchain (testnet remains same format)
    return parsed.toString({ bounceable: true, urlSafe: true })
  } catch (e) {
    return address // fallback (let TonConnect validate)
  }
}
