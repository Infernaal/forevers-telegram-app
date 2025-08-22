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
      @click.self="handleBackdropClick"
    >
      <!-- Modal Content -->
      <div
        @click.stop
        class="relative bg-white rounded-[20px] shadow-xl font-montserrat w-full max-w-[347px] mx-auto"
        style="min-height: 200px;"
      >
        <!-- Close Button -->
        <button
          @click="handleDecline"
          class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center rounded-full bg-gray-100 hover:bg-gray-200 transition-colors z-10"
        >
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13 1L1 13M1 1L13 13" stroke="#666" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>

        <!-- Content -->
        <div class="px-6 py-8">
          <!-- Title -->
          <h2 class="text-xl font-bold text-[#292727] text-center mb-6">
            Confirm Exchange
          </h2>

          <!-- Confirmation Message -->
          <div class="text-base font-medium text-[#4B4D50] text-center mb-8 leading-relaxed">
            Are you sure you want to buy <span class="font-bold text-dbd-primary">{{ amount }} Forevers {{ foreversType }}</span> for <span class="font-bold text-dbd-primary">${{ price }} USD</span> from your wallet: <span class="font-bold text-dbd-primary">{{ walletDisplayName }}</span> ?
          </div>

          <!-- Action Buttons -->
          <div class="flex gap-3">
            <!-- Decline Button -->
            <button
              @click="handleDecline"
              class="flex-1 h-11 px-4 flex justify-center items-center rounded-full bg-dbd-orange hover:opacity-90 transition-all"
              :disabled="isProcessing"
            >
              <span class="text-white text-sm font-bold">DECLINE</span>
            </button>

            <!-- Agree Button -->
            <button
              @click="handleAgree"
              class="flex-1 h-11 px-4 flex justify-center items-center rounded-full bg-gradient-to-r from-[#2019CE] to-[#473FFF] hover:opacity-90 transition-all"
              :disabled="isProcessing"
            >
              <span v-if="!isProcessing" class="text-white text-sm font-bold">I AGREE</span>
              <div v-else class="flex items-center gap-2">
                <!-- Loading spinner -->
                <div class="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                <span class="text-white text-sm font-bold">Processing...</span>
              </div>
            </button>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, watch, onUnmounted, computed } from 'vue'

// Props
const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  },
  amount: {
    type: [String, Number],
    required: true
  },
  price: {
    type: [String, Number],
    required: true
  },
  walletType: {
    type: String,
    required: true,
    validator: (value) => ['bonus', 'loyalty'].includes(value)
  },
  foreversType: {
    type: String,
    default: 'UAE'
  },
  isProcessing: {
    type: Boolean,
    default: false
  }
})

// Emits
const emit = defineEmits(['close', 'decline', 'agree'])

// Computed properties
const walletDisplayName = computed(() => {
  return props.walletType === 'loyalty' ? 'Loyalty' : 'Bonus'
})

// Methods
const handleBackdropClick = () => {
  if (props.isProcessing) return // Prevent closing while processing
  
  // Haptic feedback for modal close
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'light')
  }
  emit('close')
}

const handleDecline = () => {
  if (props.isProcessing) return // Prevent action while processing
  
  // Haptic feedback for decline
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'light')
  }
  emit('decline')
}

const handleAgree = () => {
  if (props.isProcessing) return // Prevent action while processing
  
  // Haptic feedback for agreement
  if (window.triggerHaptic) {
    window.triggerHaptic('notification', 'success')
  }
  emit('agree')
}

const handleKeyDown = (event) => {
  if (props.isProcessing) return // Prevent keyboard actions while processing
  
  if (event.key === 'Escape') {
    handleDecline()
  } else if (event.key === 'Enter') {
    handleAgree()
  }
}

// Watch for visibility changes
watch(() => props.isVisible, (newVal, oldVal) => {
  console.log('🔄 ConfirmExchangeModal visibility changed:', { from: oldVal, to: newVal, props: props })

  if (newVal) {
    console.log('📱 Modal opened with data:', {
      amount: props.amount,
      price: props.price,
      walletType: props.walletType,
      foreversType: props.foreversType,
      isProcessing: props.isProcessing
    })
    document.addEventListener('keydown', handleKeyDown)
    document.body.style.overflow = 'hidden'
  } else {
    console.log('❌ Modal closed')
    document.removeEventListener('keydown', handleKeyDown)
    document.body.style.overflow = ''
  }
})

// Cleanup on unmount
onUnmounted(() => {
  document.removeEventListener('keydown', handleKeyDown)
  document.body.style.overflow = ''
})
</script>

<style scoped>
/* Modal responsive sizing for Telegram WebApp */
@media (max-width: 375px) {
  .fixed.inset-0 {
    padding-left: 16px;
    padding-right: 16px;
  }

  .max-w-\[347px\] {
    max-width: calc(100vw - 32px) !important;
    min-width: 280px;
  }
}

@media (max-width: 320px) {
  .fixed.inset-0 {
    padding-left: 12px;
    padding-right: 12px;
  }

  .max-w-\[347px\] {
    max-width: calc(100vw - 24px) !important;
    min-width: 260px;
  }
}

@media (min-width: 376px) and (max-width: 768px) {
  .fixed.inset-0 {
    padding-left: 20px;
    padding-right: 20px;
  }

  .max-w-\[347px\] {
    max-width: 347px !important;
  }
}

@media (min-width: 769px) {
  .fixed.inset-0 {
    padding-left: 24px;
    padding-right: 24px;
  }

  .max-w-\[347px\] {
    max-width: 347px !important;
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

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

button:disabled:active {
  transform: none;
}

/* Telegram WebApp optimizations */
* {
  -webkit-tap-highlight-color: transparent;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  user-select: none;
}

/* Button touch feedback */
button {
  touch-action: manipulation;
  -webkit-user-select: none;
  user-select: none;
}

/* Responsive text sizes for small screens */
@media (max-width: 375px) {
  .text-xl {
    font-size: 18px;
  }
  
  .text-base {
    font-size: 15px;
  }
  
  .text-sm {
    font-size: 13px;
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

/* Loading spinner animation */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>
