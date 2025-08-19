<template>
  <div class="p-4">
    <h1 class="text-xl font-bold mb-4">Debug Information</h1>
    
    <div class="space-y-4">
      <div class="bg-gray-100 p-3 rounded">
        <h2 class="font-semibold mb-2">URL Information</h2>
        <p><strong>Current URL:</strong> {{ currentUrl }}</p>
        <p><strong>URL Params:</strong> {{ urlParams }}</p>
        <p><strong>Hash:</strong> {{ urlHash }}</p>
      </div>

      <div class="bg-gray-100 p-3 rounded">
        <h2 class="font-semibold mb-2">Telegram WebApp</h2>
        <p><strong>Available:</strong> {{ telegramAvailable }}</p>
        <p><strong>initData:</strong> {{ telegramInitData }}</p>
        <p><strong>initDataUnsafe:</strong> {{ JSON.stringify(telegramInitDataUnsafe, null, 2) }}</p>
      </div>

      <div class="bg-gray-100 p-3 rounded">
        <h2 class="font-semibold mb-2">Referral Context</h2>
        <p><strong>Start Parameter:</strong> {{ referralContext.startParam }}</p>
        <p><strong>Is Referral:</strong> {{ referralContext.isReferral }}</p>
        <p><strong>Referral Info:</strong> {{ JSON.stringify(referralContext.referralInfo, null, 2) }}</p>
      </div>

      <div class="bg-gray-100 p-3 rounded">
        <h2 class="font-semibold mb-2">Stored Context</h2>
        <p><strong>SessionStorage:</strong> {{ storedContext }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { getReferralContext, getStoredReferralContext } from '@/utils/telegramWebApp.js'

export default {
  name: 'DebugView',
  setup() {
    const currentUrl = ref('')
    const urlParams = ref('')
    const urlHash = ref('')
    const telegramAvailable = ref(false)
    const telegramInitData = ref('')
    const telegramInitDataUnsafe = ref({})
    const referralContext = ref({})
    const storedContext = ref('')

    onMounted(() => {
      // URL info
      currentUrl.value = window.location.href
      urlParams.value = window.location.search
      urlHash.value = window.location.hash

      // Telegram info
      telegramAvailable.value = !!(window.Telegram && window.Telegram.WebApp)
      if (telegramAvailable.value) {
        telegramInitData.value = window.Telegram.WebApp.initData || 'Not available'
        telegramInitDataUnsafe.value = window.Telegram.WebApp.initDataUnsafe || {}
      }

      // Referral context
      referralContext.value = getReferralContext()

      // Stored context
      const stored = getStoredReferralContext()
      storedContext.value = stored ? JSON.stringify(stored, null, 2) : 'No stored context'
    })

    return {
      currentUrl,
      urlParams,
      urlHash,
      telegramAvailable,
      telegramInitData,
      telegramInitDataUnsafe,
      referralContext,
      storedContext,
      JSON
    }
  }
}
</script>
