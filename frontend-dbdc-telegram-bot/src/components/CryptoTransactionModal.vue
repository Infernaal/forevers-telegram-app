<template>
  <Transition
    name="modal"
    enter-active-class="transition-all duration-300 ease-out"
    leave-active-class="transition-all duration-200 ease-in"
    enter-from-class="opacity-0"
    enter-to-class="opacity-100"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
  >
    <div
      v-if="isVisible"
      class="fixed inset-0 flex items-center justify-center z-[99999] bg-black bg-opacity-20 backdrop-blur-md px-4"
      @click.self="handleClose"
    >
      <!-- Modal Content -->
      <div
        @click.stop
        class="relative bg-white rounded-[20px] shadow-xl font-montserrat w-full max-w-[347px] mx-auto flex flex-col items-center p-6 min-h-[396px]"
      >
        <!-- Status Icon -->
        <div class="flex justify-center mt-2 mb-6">
          <div
            v-if="status === 'processing'"
            class="w-16 h-16 rounded-full border-2 border-[#2019CE] bg-[#EFEEFF] flex items-center justify-center"
          >
            <svg class="animate-spin w-8 h-8 text-[#2019CE]" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
          </div>

          <div
            v-else-if="status === 'success'"
            class="w-16 h-16 rounded-full border-2 border-[#88EF8C] bg-[#B3FFB6] flex items-center justify-center"
          >
            <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
              <g clip-path="url(#clip0_success_tick)">
                <path d="M26.4264 2.07621C25.183 1.40975 23.7961 2.69507 22.9831 3.45674C21.118 5.26571 19.5397 7.36031 17.7701 9.26449C15.8093 11.3591 13.992 13.4537 11.9833 15.5007C10.8355 16.6433 9.5921 17.881 8.8269 19.3091C7.10521 17.6429 5.62264 15.8339 3.70964 14.3582C2.32272 13.3109 0.0271294 12.5493 0.0749543 15.0723C0.170604 18.3571 3.08792 21.8798 5.24004 24.1172C6.14871 25.0692 7.34433 26.0689 8.73125 26.1165C10.4051 26.2118 12.1268 24.2124 13.1311 23.1175C14.9007 21.2133 16.3355 19.071 17.9614 17.1193C20.0657 14.5487 22.2179 12.0255 24.2743 9.4073C25.5656 7.78875 29.6307 3.78989 26.4264 2.07621ZM2.17917 14.8819C2.13134 14.8819 2.08352 14.8819 1.98787 14.9294C1.79657 14.8819 1.6531 14.8342 1.4618 14.739C1.60527 14.6438 1.8444 14.6914 2.17917 14.8819Z" fill="#07B80E"/>
              </g>
              <defs>
                <clipPath id="clip0_success_tick">
                  <rect width="27.5556" height="27.4286" fill="white" transform="translate(0.0742188 0.289062)"/>
                </clipPath>
              </defs>
            </svg>
          </div>

          <div
            v-else-if="status === 'failed'"
            class="w-16 h-16 rounded-full border-2 border-[#FF6B6B] bg-[#FFE5E5] flex items-center justify-center"
          >
            <svg class="w-8 h-8 text-[#FF6B6B]" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </div>

          <div
            v-else
            class="w-16 h-16 rounded-full border-2 border-[#4B4D50] bg-[#FAFAFA] flex items-center justify-center"
          >
            <svg class="w-8 h-8 text-[#4B4D50]" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1" />
            </svg>
          </div>
        </div>

        <!-- Content -->
        <div class="flex flex-col items-center gap-5 flex-1 w-full max-w-[300px]">
          <!-- Title -->
          <h2 class="text-[30px] font-bold text-[#292727] text-center leading-9">
            {{ modalTitle }}
          </h2>

          <!-- Transaction Details (if available) -->
          <div
            v-if="transactionData && (transactionData.amount_usd || transactionData.amount_ton)"
            class="w-full flex justify-center"
          >
            <div class="w-full max-w-[280px] rounded-xl border border-[#FF6800] bg-[#FFE8D8] flex flex-col justify-center items-center gap-2 px-4 py-3">
              <div v-if="transactionData.amount_usd" class="flex items-center gap-1">
                <span class="text-base font-medium text-[#4B4D50]">Amount:</span>
                <span class="text-xl font-bold text-[#FF6800]">${{ transactionData.amount_usd }}</span>
              </div>
              <div v-if="transactionData.amount_ton" class="flex items-center gap-1">
                <span class="text-base font-medium text-[#4B4D50]">TON Amount:</span>
                <span class="text-lg font-bold text-[#FF6800]">{{ transactionData.amount_ton }} TON</span>
              </div>
            </div>
          </div>

          <!-- Transaction ID (if available) -->
          <div
            v-if="transactionData && transactionData.txid && status !== 'processing'"
            class="w-full bg-[#FAFAFA] rounded-lg p-3"
          >
            <div class="text-sm">
              <div class="text-[#4B4D50] font-medium mb-1">Transaction ID:</div>
              <div class="font-mono text-xs text-[#7E7E7E] break-all">{{ transactionData.txid }}</div>
            </div>
          </div>

          <!-- Progress indicator for processing -->
          <div v-if="status === 'processing' && pollingAttempts > 0" class="w-full">
            <div class="flex justify-between text-sm text-[#4B4D50] mb-2">
              <span>Verifying transaction...</span>
              <span>{{ pollingAttempts }}/60</span>
            </div>
            <div class="w-full bg-[#FAFAFA] rounded-full h-2">
              <div
                class="bg-gradient-to-r from-[#2019CE] to-[#473FFF] h-2 rounded-full transition-all duration-300"
                :style="{ width: `${(pollingAttempts / 60) * 100}%` }"
              ></div>
            </div>
          </div>

          <!-- Message -->
          <div class="text-base font-medium text-[#4B4D50] text-center">
            {{ modalMessage }}
          </div>
        </div>

        <!-- Action Button -->
        <button
          @click="$emit('close')"
          class="w-full max-w-[300px] h-11 px-12 flex justify-center items-center rounded-full bg-gradient-to-r from-[#2019CE] to-[#473FFF] hover:opacity-90 transition-all mt-6"
        >
          <span class="text-white text-sm font-bold">
            {{ buttonText }}
          </span>
        </button>

        <!-- Additional Information -->
        <div v-if="status === 'processing'" class="mt-3 text-xs text-[#7E7E7E] text-center max-w-[280px]">
          We're checking the blockchain for your transaction. This usually takes 1-2 minutes.
        </div>
      </div>
    </div>
  </Transition>
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

// Methods
const handleClose = () => {
  // Haptic feedback for modal close
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'light')
  }
  emit('close')
}

const modalTitle = computed(() => {
  switch (props.status) {
    case 'processing':
      return 'Processing...'
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
      return 'We are verifying your payment on the blockchain.'
    case 'success':
      return 'Your crypto payment has been verified and processed successfully.'
    case 'failed':
      return 'Transaction could not be verified. Please check your wallet and try again.'
    default:
      return 'Processing your transaction...'
  }
})

const buttonText = computed(() => {
  switch (props.status) {
    case 'processing':
      return 'Continue in Background'
    case 'success':
      return 'Continue'
    case 'failed':
      return 'Try Again'
    default:
      return 'Ok'
  }
})
</script>

<style scoped>
/* Modal responsive sizing for Telegram WebApp */
@media (max-width: 375px) {
  .max-w-\[347px\] {
    max-width: calc(100vw - 32px) !important;
    min-width: 280px;
  }
}

@media (max-width: 320px) {
  .max-w-\[347px\] {
    max-width: calc(100vw - 24px) !important;
    min-width: 260px;
  }
}

/* Modal animations */
.modal-enter-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.modal-leave-active {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.6, 1);
}

.modal-enter-from {
  opacity: 0;
  transform: scale(0.9) translateY(20px);
}

.modal-leave-to {
  opacity: 0;
  transform: scale(0.9) translateY(20px);
}

/* Touch-friendly button states */
button:active {
  transform: scale(0.98);
  transition: transform 0.1s ease;
}

/* Telegram WebApp optimizations */
* {
  -webkit-tap-highlight-color: transparent;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  user-select: none;
}

/* Typography optimization for Telegram */
.modal-content {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-feature-settings: 'kern' 1;
  text-rendering: optimizeLegibility;
}

/* Ensure proper content spacing */
.flex-1 {
  display: flex;
  flex: 1;
  flex-direction: column;
  justify-content: center;
}

/* Better gap spacing on smaller screens */
@media (max-width: 375px) {
  .gap-5 {
    gap: 1rem !important;
  }

  .gap-6 {
    gap: 1.25rem !important;
  }
}

/* Button touch feedback */
button {
  touch-action: manipulation;
  -webkit-user-select: none;
  user-select: none;
}

/* Responsive text sizes for small screens */
@media (max-width: 375px) {
  .text-\[30px\] {
    font-size: 26px !important;
    line-height: 1.2;
  }

  .text-xl {
    font-size: 18px !important;
  }

  .text-lg {
    font-size: 16px !important;
  }

  .text-base {
    font-size: 14px !important;
  }

  .text-sm {
    font-size: 13px !important;
  }

  /* Reduce padding on small screens */
  .p-6 {
    padding: 1rem !important;
  }

  /* Adjust transaction details box width on small screens */
  .max-w-\[280px\] {
    max-width: 240px !important;
  }
}

@media (max-width: 320px) {
  .text-\[30px\] {
    font-size: 24px !important;
    line-height: 1.2;
  }

  .text-xl {
    font-size: 16px !important;
  }

  .text-lg {
    font-size: 15px !important;
  }

  .text-base {
    font-size: 13px !important;
  }

  /* Further reduce on very small screens */
  .max-w-\[280px\] {
    max-width: 200px !important;
  }
}

/* Improved backdrop blur for better visibility */
.backdrop-blur-md {
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

/* Better modal shadows */
.shadow-xl {
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

/* Smooth progress bar animation */
.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 300ms;
}
</style>
