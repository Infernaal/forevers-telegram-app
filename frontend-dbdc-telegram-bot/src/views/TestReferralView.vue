<template>
  <div class="p-4">
    <h1 class="text-xl font-bold mb-4">Test Referral Functionality</h1>
    
    <div class="space-y-4">
      <div class="bg-blue-100 p-3 rounded">
        <h2 class="font-semibold mb-2">Test Links</h2>
        <div class="space-y-2">
          <button 
            @click="testReferralLink"
            class="block w-full text-left p-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Test: Navigate with referral parameter
          </button>
          <button 
            @click="clearReferralData"
            class="block w-full text-left p-2 bg-red-500 text-white rounded hover:bg-red-600"
          >
            Clear referral data
          </button>
        </div>
      </div>

      <div class="bg-gray-100 p-3 rounded">
        <h2 class="font-semibold mb-2">Current State</h2>
        <p><strong>Stored Referral:</strong> {{ storedReferral ? 'Yes' : 'No' }}</p>
        <p><strong>Is Referral:</strong> {{ currentReferral.isReferral ? 'Yes' : 'No' }}</p>
        <p><strong>User ID:</strong> {{ currentReferral.referralInfo?.userId || 'None' }}</p>
        <p><strong>Code:</strong> {{ currentReferral.referralInfo?.code || 'None' }}</p>
      </div>

      <div class="bg-gray-100 p-3 rounded">
        <h2 class="font-semibold mb-2">Debug Info</h2>
        <pre class="text-xs bg-white p-2 rounded overflow-auto">{{ JSON.stringify(currentReferral, null, 2) }}</pre>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { 
  getReferralContext, 
  getStoredReferralContext, 
  storeReferralContext,
  clearReferralContext 
} from '@/utils/telegramWebApp.js'

export default {
  name: 'TestReferralView',
  setup() {
    const router = useRouter()
    const currentReferral = ref({})
    const storedReferral = ref(null)

    const updateState = () => {
      currentReferral.value = getReferralContext()
      storedReferral.value = getStoredReferralContext()
    }

    const testReferralLink = () => {
      // Simulate a referral context
      const mockReferral = {
        hasStartParam: true,
        startParam: 'ref_4344_code_Y5GA6R',
        isReferral: true,
        referralInfo: {
          isReferral: true,
          userId: '4344',
          code: 'Y5GA6R',
          fullParam: 'ref_4344_code_Y5GA6R'
        },
        telegramInitData: null,
        telegramUser: null
      }
      
      storeReferralContext(mockReferral)
      updateState()
      
      // Navigate to registration to test
      router.push('/registration')
    }

    const clearReferralData = () => {
      clearReferralContext()
      updateState()
    }

    onMounted(() => {
      updateState()
    })

    return {
      currentReferral,
      storedReferral,
      testReferralLink,
      clearReferralData,
      JSON
    }
  }
}
</script>
