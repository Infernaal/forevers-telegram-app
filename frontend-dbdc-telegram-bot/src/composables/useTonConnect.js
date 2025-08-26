import { ref } from 'vue'
import { TonConnectUI } from '@tonconnect/ui'

let ui
const connectedRef = ref(false)
const addressRef = ref(null)
const errorRef = ref(null)

export function useTonConnect() {
  if (!ui) {
    try {
      ui = new TonConnectUI({
        manifestUrl: '/tonconnect-manifest.json',
        // Explicitly support both mainnet and testnet
        walletsList: {
          includeWallets: [
            {
              name: 'Tonkeeper',
              universalLink: 'https://app.tonkeeper.com/ton-connect',
              bridgeUrl: 'https://bridge.tonapi.io/bridge'
            }
          ]
        }
      })

      // track status
      ui.onStatusChange(wallet => {
        connectedRef.value = !!wallet
        addressRef.value = wallet?.address || null
        if (wallet) {
          errorRef.value = null // clear errors on successful connection
        }
      })

      // try to restore session silently
      setTimeout(() => {
        try {
          if (ui.account) {
            connectedRef.value = true
            addressRef.value = ui.account.address || null
          }
        } catch (error) {
          console.warn('Failed to restore TON Connect session:', error)
          errorRef.value = error.message
        }
      }, 0)
    } catch (error) {
      console.error('Failed to initialize TON Connect UI:', error)
      errorRef.value = error.message
    }
  }

  const isConnected = connectedRef

  const ensureConnected = async () => {
    try {
      if (!ui) {
        throw new Error('TON Connect UI not initialized')
      }

      if (!ui.account) {
        errorRef.value = null
        await ui.openModal()

        // wait for connection with timeout
        const connection = await Promise.race([
          new Promise((resolve, reject) => {
            const unsub = ui.onStatusChange(wallet => {
              if (wallet) {
                unsub()
                resolve(wallet)
              }
            })
            // Also listen for connection errors
            setTimeout(() => {
              unsub()
              reject(new Error('Connection timeout - please try again'))
            }, 30000) // 30 second timeout
          }),
          new Promise((_, reject) => {
            setTimeout(() => reject(new Error('Connection timeout')), 30000)
          })
        ])

        return connection
      }
      return ui.account
    } catch (error) {
      console.error('TON Connect connection error:', error)
      errorRef.value = error.message

      // Handle specific error types
      if (error.message?.includes('network') || error.message?.includes('Network')) {
        throw new Error('Network connection error. Please check your internet connection and try again.')
      } else if (error.message?.includes('rejected') || error.message?.includes('cancelled')) {
        throw new Error('Connection was cancelled by user.')
      } else {
        throw new Error(error.message || 'Failed to connect wallet. Please try again.')
      }
    }
  }

  const getAddress = () => addressRef.value || ui?.account?.address || null

  const sendTransaction = async (to, amountNano, validUntil) => {
    try {
      if (!ui?.account) {
        throw new Error('Wallet not connected. Please connect your wallet first.')
      }

      const account = ui.account

      // Validate network support
      if (!account.chain) {
        throw new Error('Unable to determine wallet network. Please reconnect your wallet.')
      }

      // Support both mainnet and testnet, but prefer mainnet
      const supportedNetworks = ['-239', '-3'] // mainnet, testnet
      if (!supportedNetworks.includes(account.chain)) {
        throw new Error(`Network ${account.chain} is not supported. Please switch to TON Mainnet in your wallet.`)
      }

      const tx = {
        validUntil: validUntil || Math.floor(Date.now() / 1000) + 600,
        network: account.chain,
        messages: [{
          address: to,
          amount: amountNano.toString()
        }]
      }

      console.log('Sending transaction:', {
        network: account.chain,
        to,
        amount: amountNano.toString()
      })

      const result = await ui.sendTransaction(tx)
      return { boc: result }

    } catch (error) {
      console.error('Transaction error:', error)
      errorRef.value = error.message

      // Handle specific transaction errors
      if (error.message?.includes('Network is not supported')) {
        throw new Error('Your wallet network is not supported. Please switch to TON Mainnet.')
      } else if (error.message?.includes('insufficient funds')) {
        throw new Error('Insufficient funds in your wallet.')
      } else if (error.message?.includes('rejected') || error.message?.includes('cancelled')) {
        throw new Error('Transaction was cancelled.')
      } else {
        throw new Error(error.message || 'Transaction failed. Please try again.')
      }
    }
  }

  const getChain = () => ui?.account?.chain || null

  const disconnect = async () => {
    try {
      if (ui?.account) {
        await ui.disconnect()
        connectedRef.value = false
        addressRef.value = null
        errorRef.value = null
      }
    } catch (error) {
      console.error('Disconnect error:', error)
    }
  }

  return {
    connector: ui,
    isConnected,
    ensureConnected,
    getAddress,
    getChain,
    sendTransaction,
    disconnect,
    error: errorRef
  }
}
