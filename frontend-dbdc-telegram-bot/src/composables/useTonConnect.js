import { ref, onMounted, onUnmounted } from 'vue'
import { TonConnectUI } from '@tonconnect/ui'

const tonConnectUI = ref(null)
const isConnected = ref(false)
const wallet = ref(null)
const isLoading = ref(false)

export function useTonConnect() {
  const initTonConnect = async () => {
    try {
      console.log('🔗 Initializing TON Connect...')
      tonConnectUI.value = new TonConnectUI({
        manifestUrl: 'https://dbdc-mini.dubadu.com/tonconnect-manifest.json'
      })
      console.log('✅ TON Connect UI created')

      // Listen for wallet connection status changes
      tonConnectUI.value.onStatusChange((walletInfo) => {
        console.log('🔄 TON Connect status change:', walletInfo)
        if (walletInfo) {
          isConnected.value = true
          wallet.value = walletInfo
          console.log('✅ Wallet connected:', walletInfo.device?.appName)
        } else {
          isConnected.value = false
          wallet.value = null
          console.log('❌ Wallet disconnected')
        }
      })

      // Restore connection if exists
      if (tonConnectUI.value.wallet) {
        isConnected.value = true
        wallet.value = tonConnectUI.value.wallet
        console.log('🔄 Restored existing wallet connection')
      }

      console.log('✅ TON Connect initialized successfully')
    } catch (error) {
      console.error('❌ Failed to initialize TON Connect:', error)
    }
  }

  const connectWallet = async () => {
    if (!tonConnectUI.value) {
      console.error('❌ TON Connect UI not initialized')
      return false
    }

    try {
      console.log('🔗 Attempting to connect wallet...')
      isLoading.value = true
      await tonConnectUI.value.connectWallet()
      console.log('✅ Wallet connection initiated')
      return true
    } catch (error) {
      console.error('❌ Failed to connect wallet:', error)
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
