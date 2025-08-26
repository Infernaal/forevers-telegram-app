import { ref, onMounted, onUnmounted } from 'vue'
import { TonConnectUI } from '@tonconnect/ui'

const tonConnectUI = ref(null)
const isConnected = ref(false)
const wallet = ref(null)
const isLoading = ref(false)

export function useTonConnect() {
  const initTonConnect = async () => {
    try {
      tonConnectUI.value = new TonConnectUI({
        manifestUrl: 'https://dbdc-mini.dubadu.com/tonconnect-manifest.json'
      })

      // Listen for wallet connection status changes
      tonConnectUI.value.onStatusChange((walletInfo) => {
        if (walletInfo) {
          isConnected.value = true
          wallet.value = walletInfo
        } else {
          isConnected.value = false
          wallet.value = null
        }
      })

      // Restore connection if exists
      if (tonConnectUI.value.wallet) {
        isConnected.value = true
        wallet.value = tonConnectUI.value.wallet
      }

    } catch (error) {
      console.error('Failed to initialize TON Connect:', error)
    }
  }

  const connectWallet = async () => {
    if (!tonConnectUI.value) return false
    
    try {
      isLoading.value = true
      await tonConnectUI.value.connectWallet()
      return true
    } catch (error) {
      console.error('Failed to connect wallet:', error)
      return false
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
      isLoading.value = true
      const result = await tonConnectUI.value.sendTransaction(transaction)
      return result
    } catch (error) {
      console.error('Transaction failed:', error)
      throw error
    } finally {
      isLoading.value = false
    }
  }

  const getWalletAddress = () => {
    if (!wallet.value || !wallet.value.account) return null
    return wallet.value.account.address
  }

  const getWalletName = () => {
    if (!wallet.value) return null
    return wallet.value.device.appName
  }

  const cleanup = () => {
    if (tonConnectUI.value) {
      tonConnectUI.value.disconnect()
      tonConnectUI.value = null
    }
  }

  return {
    tonConnectUI,
    isConnected,
    wallet,
    isLoading,
    initTonConnect,
    connectWallet,
    disconnectWallet,
    sendTransaction,
    getWalletAddress,
    getWalletName,
    cleanup
  }
}
