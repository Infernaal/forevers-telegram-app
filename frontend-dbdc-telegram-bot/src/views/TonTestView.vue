<template>
  <div class="w-full min-h-screen bg-white font-montserrat p-4">
    <h1 class="text-2xl font-bold mb-6">TON Connect Test</h1>
    
    <!-- Status -->
    <div class="mb-6 p-4 border rounded-lg">
      <h2 class="text-lg font-semibold mb-2">Connection Status</h2>
      <p><strong>Connected:</strong> {{ isTonConnected ? 'Yes' : 'No' }}</p>
      <p><strong>Loading:</strong> {{ isTonLoading ? 'Yes' : 'No' }}</p>
      <p><strong>Wallet:</strong> {{ getWalletName() || 'None' }}</p>
      <p><strong>Address:</strong> {{ getWalletAddress() || 'None' }}</p>
    </div>

    <!-- Actions -->
    <div class="space-y-4">
      <button
        @click="connectWallet"
        :disabled="isTonLoading || isTonConnected"
        class="w-full px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-400"
      >
        {{ isTonLoading ? 'Connecting...' : isTonConnected ? 'Already Connected' : 'Connect Wallet' }}
      </button>

      <button
        @click="disconnectWallet"
        :disabled="!isTonConnected"
        class="w-full px-4 py-2 bg-red-500 text-white rounded disabled:bg-gray-400"
      >
        Disconnect Wallet
      </button>

      <button
        @click="testTransaction"
        :disabled="!isTonConnected || isTonLoading"
        class="w-full px-4 py-2 bg-green-500 text-white rounded disabled:bg-gray-400"
      >
        Test Transaction (0.001 TON)
      </button>
    </div>

    <!-- Debug Info -->
    <div class="mt-8 p-4 bg-gray-100 rounded-lg">
      <h3 class="font-semibold mb-2">Debug Info</h3>
      <pre class="text-xs">{{ debugInfo }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useTonConnect } from '../composables/useTonConnect.js'
import { TonConnectService } from '../services/tonConnectService.js'

// TON Connect setup
const { 
  isConnected: isTonConnected, 
  wallet: tonWallet, 
  isLoading: isTonLoading,
  initTonConnect,
  connectWallet: connectTonWallet,
  disconnectWallet: disconnectTonWallet,
  sendTransaction: sendTonTransaction,
  getWalletAddress,
  getWalletName,
  cleanup: cleanupTonConnect
} = useTonConnect()

const debugInfo = computed(() => {
  return {
    connected: isTonConnected.value,
    loading: isTonLoading.value,
    wallet: tonWallet.value ? {
      name: tonWallet.value.device?.appName,
      address: tonWallet.value.account?.address
    } : null
  }
})

const connectWallet = async () => {
  console.log('🔗 Test page: Attempting to connect wallet')
  const result = await connectTonWallet()
  console.log('📱 Test page: Connect result:', result)
}

const disconnectWallet = async () => {
  console.log('❌ Test page: Disconnecting wallet')
  await disconnectTonWallet()
}

const testTransaction = async () => {
  try {
    console.log('💸 Test page: Sending test transaction')
    
    const transaction = TonConnectService.createTonTransaction(
      "0QBgEwEKpmG4yPvn7-_VqljYE2s88oI6v7R2Vu_E8TvHjMGG", // Test address
      TonConnectService.tonToNanotons(0.001), // 0.001 TON
      "Test transaction from DBD Bot"
    )
    
    const result = await sendTonTransaction(transaction)
    console.log('✅ Test page: Transaction sent:', result)
    alert('Transaction sent successfully!')
    
  } catch (error) {
    console.error('❌ Test page: Transaction failed:', error)
    alert('Transaction failed: ' + error.message)
  }
}

onMounted(async () => {
  console.log('🚀 Test page: Mounting, initializing TON Connect')
  await initTonConnect()
})

onUnmounted(() => {
  console.log('👋 Test page: Unmounting, cleaning up TON Connect')
  cleanupTonConnect()
})
</script>

<style scoped>
.font-montserrat {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
</style>
