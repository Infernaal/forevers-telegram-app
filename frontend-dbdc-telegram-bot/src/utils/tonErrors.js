export function mapTonConnectError(err) {
  const raw = (err?.message || '').toString()
  const name = (err?.name || '').toString()
  const lower = raw.toLowerCase()

  // Common wallet errors
  if (name.includes('UserRejects') || lower.includes('user reject') || lower.includes('rejected by user')) {
    return 'Transaction was cancelled in the wallet.'
  }
  if (lower.includes('no enough funds') || lower.includes('insufficient') || lower.includes('not enough')) {
    return 'Insufficient TON balance to cover amount and network fee.'
  }
  if (lower.includes('network') && lower.includes('timeout')) {
    return 'Network timeout. Please try again.'
  }
  if (lower.includes('manifest') || lower.includes('bad request')) {
    return 'Wallet request is invalid. Please reopen the wallet and try again.'
  }
  if (lower.includes('connection') || lower.includes('connect')) {
    return 'Failed to connect to wallet. Please try again.'
  }

  return 'Unable to process transaction. Please try again.'
}
