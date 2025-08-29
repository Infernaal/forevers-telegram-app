<template>
  <div
    v-if="isVisible"
    class="fixed inset-0 z-[10000] flex items-center justify-center px-[2.5%] py-4 bg-black bg-opacity-50"
    @click.self="$emit('close')"
  >
    <div class="bg-white rounded-2xl p-6 w-full max-w-md mx-auto relative">
      <!-- Close button -->
      <button
        @click="$emit('close')"
        class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 transition-colors"
        :disabled="isProcessing"
      >
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>

      <!-- Modal Content -->
      <div class="text-center">
        <!-- Status Icon -->
        <div class="mb-4 flex justify-center">
          <div
            v-if="status === 'processing'"
            class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center"
          >
            <svg class="animate-spin w-8 h-8 text-blue-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
          </div>
          
          <div
            v-else-if="status === 'success'"
            class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center"
          >
            <svg class="w-8 h-8 text-green-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          
          <div
            v-else-if="status === 'failed'"
            class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center"
          >
            <svg class="w-8 h-8 text-red-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </div>
          
          <div
            v-else
            class="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center"
          >
            <svg class="w-8 h-8 text-gray-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1" />
            </svg>
          </div>
        </div>

        <!-- Title -->
        <h2 class="text-xl font-semibold text-gray-900 mb-2">
          {{ modalTitle }}
        </h2>

        <!-- Message -->
        <p class="text-gray-600 mb-6 leading-relaxed">
          {{ modalMessage }}
        </p>

        <!-- Transaction Details (if available) -->
        <div
          v-if="transactionData && status !== 'processing'"
          class="bg-gray-50 rounded-lg p-4 mb-6 text-left"
        >
          <div class="space-y-2 text-sm">
            <div v-if="transactionData.amount_usd" class="flex justify-between">
              <span class="text-gray-500">Amount:</span>
              <span class="font-medium">${{ transactionData.amount_usd }}</span>
            </div>
            <div v-if="transactionData.amount_ton" class="flex justify-between">
              <span class="text-gray-500">TON Amount:</span>
              <span class="font-medium">{{ transactionData.amount_ton }} TON</span>
            </div>
            <div v-if="transactionData.txid" class="flex justify-between">
              <span class="text-gray-500">Transaction ID:</span>
              <span class="font-mono text-xs break-all">{{ transactionData.txid }}</span>
            </div>
            <div v-if="pollingAttempts > 0" class="flex justify-between">
              <span class="text-gray-500">Verification Attempts:</span>
              <span class="font-medium">{{ pollingAttempts }}</span>
            </div>
          </div>
        </div>

        <!-- Progress indicator for processing -->
        <div v-if="status === 'processing' && pollingAttempts > 0" class="mb-6">
          <div class="flex justify-between text-sm text-gray-500 mb-2">
            <span>Verifying transaction...</span>
            <span>{{ pollingAttempts }}/60</span>
          </div>
          <div class="w-full bg-gray-200 rounded-full h-2">
            <div
              class="bg-blue-600 h-2 rounded-full transition-all duration-300"
              :style="{ width: `${(pollingAttempts / 60) * 100}%` }"
            ></div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex gap-3">
          <button
            v-if="status === 'success' || status === 'failed'"
            @click="$emit('close')"
            class="flex-1 bg-dbd-primary text-white px-6 py-3 rounded-xl font-medium hover:bg-blue-700 transition-colors"
          >
            {{ status === 'success' ? 'Continue' : 'Try Again' }}
          </button>
          
          <button
            v-if="status === 'processing'"
            @click="$emit('close')"
            class="flex-1 bg-gray-200 text-gray-700 px-6 py-3 rounded-xl font-medium hover:bg-gray-300 transition-colors"
          >
            Continue in Background
          </button>
        </div>

        <!-- Additional Information -->
        <div v-if="status === 'processing'" class="mt-4 text-xs text-gray-500">
          We're checking the blockchain for your transaction. This usually takes 5-10 minutes.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  },
  status: {
    type: String,
    default: 'processing', // 'processing', 'success', 'failed'
    validator: (value) => ['processing', 'success', 'failed'].includes(value)
  },
  transactionData: {
    type: Object,
    default: () => ({})
  },
  pollingAttempts: {
    type: Number,
    default: 0
  },
  customMessage: {
    type: String,
    default: ''
  },
  isProcessing: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['close'])

const modalTitle = computed(() => {
  switch (props.status) {
    case 'processing':
      return 'Transaction Processing'
    case 'success':
      return 'Payment Successful!'
    case 'failed':
      return 'Payment Failed'
    default:
      return 'Transaction Status'
  }
})

const modalMessage = computed(() => {
  if (props.customMessage) {
    return props.customMessage
  }

  switch (props.status) {
    case 'processing':
      return 'We are checking your transaction. Please wait while we verify the payment on the blockchain. This process typically takes 5-10 minutes.'
    case 'success':
      return 'Your crypto payment has been verified and processed successfully. Your Forevers will be credited to your account.'
    case 'failed':
      return 'Your transaction could not be verified or has failed. Please check your wallet and try again.'
    default:
      return 'Processing your transaction...'
  }
})
</script>

<style scoped>
/* Additional styles for smooth animations */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

/* Ensure modal is above everything else */
.z-\[10000\] {
  z-index: 10000;
}

/* Telegram WebApp safe area adjustments */
@supports (padding: max(0px)) {
  .fixed.inset-0 {
    padding-top: env(safe-area-inset-top);
    padding-bottom: env(safe-area-inset-bottom);
    padding-left: env(safe-area-inset-left);
    padding-right: env(safe-area-inset-right);
  }
}

/* Touch optimizations for mobile */
button {
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

/* Prevent text selection on status elements */
.text-center > * {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* Smooth progress bar animation */
.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 300ms;
}
</style>
