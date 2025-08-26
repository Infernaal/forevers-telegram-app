import { TonConnect } from '@tonconnect/sdk'

let connector

export function useTonConnect() {
  if (!connector) {
    const manifestUrl = `${window.location.origin}/tonconnect-manifest.json`
    connector = new TonConnect({ manifestUrl })
  }

  const isConnected = () => !!connector.account

  const ensureConnected = async () => {
    if (!connector.account) {
      await connector.restoreConnection()
    }
    if (!connector.account) {
      await connector.connect() // will open wallet selection
    }
    return connector.account
  }

  const getAddress = () => connector?.account?.address || null

  const sendTransaction = async (to, amountNano, validUntil) => {
    const tx = {
      validUntil,
      messages: [{ address: to, amount: amountNano.toString() }]
    }
    const boc = await connector.sendTransaction(tx)
    return { boc }
  }

  return { connector, isConnected, ensureConnected, getAddress, sendTransaction }
}
