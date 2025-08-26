import { ref } from 'vue'
import { ref } from 'vue'
import { TonConnectUI } from '@tonconnect/ui'

let ui
const connectedRef = ref(false)
const addressRef = ref(null)

export function useTonConnect() {
  if (!ui) {
    ui = new TonConnectUI({ manifestUrl: '/tonconnect-manifest.json' })

    // track status
    ui.onStatusChange(wallet => {
      connectedRef.value = !!wallet
      addressRef.value = wallet?.address || null
    })

    // try to restore session silently
    setTimeout(() => {
      try {
        if (ui.account) {
          connectedRef.value = true
          addressRef.value = ui.account.address || null
        }
      } catch (_) {}
    }, 0)
  }

  const isConnected = connectedRef

  const ensureConnected = async () => {
    if (!ui.account) {
      await ui.openModal()
      // wait for connection once modal is open
      await new Promise(resolve => {
        const unsub = ui.onStatusChange(wallet => {
          if (wallet) {
            unsub()
            resolve(wallet)
          }
        })
      })
    }
    return ui.account
  }

  const getAddress = () => addressRef.value || ui?.account?.address || null

  const sendTransaction = async (to, amountNano, validUntil) => {
    const tx = {
      validUntil,
      messages: [{ address: to, amount: amountNano.toString() }]
    }
    const boc = await ui.sendTransaction(tx)
    return { boc }
  }

  return { connector: ui, isConnected, ensureConnected, getAddress, sendTransaction }
}
