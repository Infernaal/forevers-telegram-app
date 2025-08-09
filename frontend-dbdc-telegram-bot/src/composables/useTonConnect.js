import { ref, onMounted } from 'vue'
import { TonConnectUI } from '@tonconnect/ui'

export function useTonConnect() {
  const tonConnectUI = ref(null)
  const isConnected = ref(false)
  const wallet = ref(null)
  const isLoading = ref(false)

  const initTonConnect = () => {
    tonConnectUI.value = new TonConnectUI({
      manifestUrl: `${window.location.origin}/tonconnect-manifest.json`,
      buttonRootId: null,
      network: 'testnet' // Use testnet instead of mainnet
    })

    // Subscribe to connection status changes
    tonConnectUI.value.onStatusChange((walletInfo) => {
      if (walletInfo) {
        isConnected.value = true
        wallet.value = walletInfo
        console.log('Wallet connected:', walletInfo)
      } else {
        isConnected.value = false
        wallet.value = null
        console.log('Wallet disconnected')
      }
    })
  }

  const connectWallet = async () => {
    if (!tonConnectUI.value) return

    try {
      isLoading.value = true
      await tonConnectUI.value.openModal()
    } catch (error) {
      console.error('Failed to connect wallet:', error)
    } finally {
      isLoading.value = false
    }
  }

  const disconnectWallet = async () => {
    if (!tonConnectUI.value) return

    try {
      await tonConnectUI.value.disconnect()
    } catch (error) {
      console.error('Failed to disconnect wallet:', error)
    }
  }

  const sendTransaction = async (transaction) => {
    if (!tonConnectUI.value || !isConnected.value) {
      throw new Error('Wallet not connected')
    }

    try {
      const result = await tonConnectUI.value.sendTransaction(transaction)
      console.log('Transaction sent:', result)
      return result
    } catch (error) {
      console.error('Failed to send transaction:', error)
      throw error
    }
  }

  onMounted(() => {
    initTonConnect()
  })

  return {
    tonConnectUI,
    isConnected,
    wallet,
    isLoading,
    connectWallet,
    disconnectWallet,
    sendTransaction
  }
}
