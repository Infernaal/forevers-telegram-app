import { ref, computed, onMounted } from 'vue'
import { TonConnectUI } from '@tonconnect/ui'

// Simple Ton Connect composable for global-ish usage
const isInitialized = ref(false)
const isConnected = ref(false)
const wallet = ref(null)
const accountAddress = ref('')
let tcui = null

export function useTonConnect() {
  const init = () => {
    if (isInitialized.value) return
    try {
      tcui = new TonConnectUI({
        manifestUrl: `${window.location.origin}/tonconnect-manifest.json`
      })
      // sync initial state
      if (tcui.connected) {
        isConnected.value = true
        wallet.value = tcui.wallet
        try { accountAddress.value = tcui?.account?.address || '' } catch (_) { accountAddress.value = '' }
      }

      tcui.onStatusChange((w) => {
        if (w) {
          isConnected.value = true
          wallet.value = w
          try { accountAddress.value = tcui?.account?.address || '' } catch (_) { accountAddress.value = '' }
        } else {
          isConnected.value = false
          wallet.value = null
          accountAddress.value = ''
        }
      })

      isInitialized.value = true
    } catch (e) {
      // ignore init errors, will retry on demand
    }
  }

  onMounted(() => {
    init()
  })

  const connect = async () => {
    if (!tcui) init()
    await tcui?.connectWallet()
  }

  const disconnect = async () => {
    await tcui?.disconnect()
  }

  const sendTransaction = async (tx) => {
    if (!tcui) throw new Error('TonConnect not initialized')
    // tx must be TonConnect compatible: { validUntil, messages: [{address, amount, payload?}] }
    return tcui.sendTransaction(tx)
  }

  return {
    isInitialized: computed(() => isInitialized.value),
    isConnected: computed(() => isConnected.value),
    wallet,
    accountAddress: computed(() => accountAddress.value),
    connect,
    disconnect,
    sendTransaction,
    init
  }
}
