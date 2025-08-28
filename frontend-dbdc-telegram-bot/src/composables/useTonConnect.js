import { ref, computed } from 'vue'
import { TonConnectUI } from '@tonconnect/ui'

const tonConnectUIRef = {
  instance: null
}

const connected = ref(false)
const account = ref(null)
const walletInfo = ref(null)

const MANIFEST_URL = `${window.location.origin}/tonconnect-manifest.json`

function ensureInstance() {
  if (!tonConnectUIRef.instance) {
    tonConnectUIRef.instance = new TonConnectUI({
      manifestUrl: MANIFEST_URL,
      buttonRootId: undefined
    })

    tonConnectUIRef.instance.connectionRestored.then(() => {
      const acc = tonConnectUIRef.instance.account
      if (acc) {
        connected.value = true
        account.value = acc
        walletInfo.value = tonConnectUIRef.instance.wallet
      }
    })
  }
  return tonConnectUIRef.instance
}

export function useTonConnect() {
  function getUI() {
    return ensureInstance()
  }

  async function connect() {
    const ui = getUI()

    // If already connected, return immediately
    if (ui.account) {
      connected.value = true
      account.value = ui.account
      walletInfo.value = ui.wallet
      return ui.account
    }

    // Wait for actual connection after opening the modal
    return await new Promise((resolve) => {
      const unsubscribe = ui.onStatusChange(() => {
        const acc = ui.account
        if (acc) {
          connected.value = true
          account.value = acc
          walletInfo.value = ui.wallet
          unsubscribe()
          resolve(acc)
        }
      })

      ui.openModal().catch(() => {
        try { unsubscribe() } catch {}
        resolve(null)
      })

      // Safety timeout in case modal was closed without connecting
      setTimeout(() => {
        try { unsubscribe() } catch {}
        resolve(null)
      }, 120000)
    })
  }

  async function disconnect() {
    const ui = getUI()
    await ui.disconnect()
    connected.value = false
    account.value = null
    walletInfo.value = null
  }

  async function sendTransaction(tx) {
    const ui = getUI()
    return await ui.sendTransaction(tx)
  }

  const isConnected = computed(() => connected.value)
  const userAddress = computed(() => (account.value ? account.value.address : null))

  return {
    connect,
    disconnect,
    sendTransaction,
    isConnected,
    userAddress,
    walletInfo: computed(() => walletInfo.value)
  }
}
