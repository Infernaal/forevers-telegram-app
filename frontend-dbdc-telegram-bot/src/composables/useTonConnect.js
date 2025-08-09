import { ref, onMounted, computed } from 'vue'
import { TonConnectUI } from '@tonconnect/ui'
let beginCellFn = null
import { TON_NETWORK } from '../config/ton.js'

// Simple singleton to avoid multiple TonConnectUI instances if composable used in many components
let _singletonInstance = null

export function useTonConnect() {
  const tonConnectUI = ref(null)
  const isConnected = ref(false)
  const wallet = ref(null)
  const isLoading = ref(false)

  const initTonConnect = () => {
    if (_singletonInstance) {
      tonConnectUI.value = _singletonInstance
      return
    }

    const manifestUrl = `${window.location.origin}/tonconnect-manifest.json`
    tonConnectUI.value = new TonConnectUI({
      manifestUrl,
      buttonRootId: null,
      network: TON_NETWORK
    })

    _singletonInstance = tonConnectUI.value

    // Subscribe to connection status changes
    tonConnectUI.value.onStatusChange((walletInfo) => {
      if (walletInfo) {
        isConnected.value = true
        wallet.value = walletInfo
        console.log('[TonConnect] Connected:', {
          address: walletInfo.account?.address,
          chain: walletInfo.account?.chain,
          device: walletInfo.device?.appName
        })
      } else {
        isConnected.value = false
        wallet.value = null
        console.log('[TonConnect] Disconnected')
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

    // Basic validation
    if (!transaction?.messages?.length) {
      throw new Error('Transaction must contain at least one message')
    }
    for (const m of transaction.messages) {
      if (!m.address) throw new Error('Message missing address')
      if (!m.amount) throw new Error('Message missing amount')
    }

    try {
      const result = await tonConnectUI.value.sendTransaction(transaction)
      console.log('[TonConnect] Transaction sent:', result)
      return result
    } catch (error) {
      console.error('[TonConnect] Failed to send transaction:', error)
      throw error
    }
  }

  // Placeholder for future comment payload builder (requires ton-core to serialize a cell)
  const buildCommentPayload = async (text) => {
    if (!text) return undefined
    try {
  if (!beginCellFn) {
        const mod = await import('@ton/core')
        beginCellFn = mod.beginCell
      }
      const cell = beginCellFn().storeUint(0, 32).storeStringTail(text).endCell()
      return cell.toBoc({ idx: false }).toString('base64')
    } catch (e) {
      console.warn('Failed to build comment payload', e)
      return undefined
    }
  }

  onMounted(() => {
    initTonConnect()
    // Attempt immediate restoration: TonConnectUI internally restores if existing session; we just reflect state
    setTimeout(() => {
      const restored = _singletonInstance?.wallet
      if (restored) {
        isConnected.value = true
        wallet.value = restored
      }
    }, 0)
  })

  return {
    tonConnectUI,
    isConnected,
    wallet,
    isLoading,
    connectWallet,
    disconnectWallet,
  sendTransaction,
  buildCommentPayload,
  chain: computed(() => wallet.value?.account?.chain || null),
  network: TON_NETWORK
  }
}
