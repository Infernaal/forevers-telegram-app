<template>
  <Transition
    name="modal"
    enter-active-class="transition-all duration-300 ease-out"
    leave-active-class="transition-all duration-200 ease-in"
    enter-from-class="opacity-0 backdrop-blur-0"
    enter-to-class="opacity-100 backdrop-blur-md"
    leave-from-class="opacity-100 backdrop-blur-md"
    leave-to-class="opacity-0 backdrop-blur-0"
  >
    <div
      v-if="isVisible"
      class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-20 backdrop-blur-md"
      @click.self="handleBackdropClick"
    >
      <!-- Modal Content -->
      <div
        @click.stop
        class="relative bg-white rounded-[20px] shadow-xl font-montserrat"
        style="width: 347px; height: 396px;"
      >
        <!-- Success Icon -->
        <div class="absolute left-[142px] top-8 w-16 h-16">
          <div class="w-16 h-16 rounded-r-full border-2 border-[#88EF8C] bg-[#B3FFB6] flex items-center justify-center">
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
        </div>

        <!-- Content -->
        <div class="absolute left-6 top-[122px] w-[300px] h-[178px] flex flex-col items-center gap-5">
          <!-- Title -->
          <h2 class="text-[30px] font-bold text-[#292727] text-center leading-9">
            Congratulations!
          </h2>

          <!-- Reward Box -->
          <div class="w-[300px] h-20 relative">
            <div class="absolute left-[49px] top-0 w-[202px] h-20 rounded-xl border border-[#FF6800] bg-[#FFE8D8]"></div>
            <div class="absolute left-[81px] top-3 w-[138px] h-[54px] flex flex-col justify-center items-center gap-0.5">
              <div class="text-base font-medium text-[#4B4D50] text-center">
                You just received
              </div>
              <div class="flex items-center gap-1">
                <!-- Forevers Icon -->
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M19.1668 4.61296V0.833313H4.4559V5.63213H0.833496V9.41178H4.4559V18.8172H8.68398V14.2048H12.2598V10.4251H8.68398V9.41178H15.7075V5.63213H8.68398V4.61296H19.1668Z" fill="#FF6800"/>
                </svg>
                <span class="text-2xl font-bold text-[#FF6800] text-center leading-[30px]">
                  {{ amount || '4,164' }}
                </span>
              </div>
            </div>
          </div>

          <!-- Success Message -->
          <div class="text-base font-medium text-[#4B4D50] text-center mt-2">
            {{ message || 'Funds have been successfully' }}
          </div>
        </div>

        <!-- OK Button -->
        <button
          @click="handleConfirm"
          class="absolute left-6 top-80 w-[300px] h-11 px-12 flex justify-center items-center rounded-full bg-gradient-to-r from-[#2019CE] to-[#473FFF] hover:opacity-90 transition-all"
        >
          <span class="text-white text-sm font-bold">{{ confirmText || 'Ok' }}</span>
        </button>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, watch, onUnmounted } from 'vue'

// Props
const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  },
  amount: {
    type: [String, Number],
    default: '4,164'
  },
  message: {
    type: String,
    default: 'Funds have been successfully'
  },
  confirmText: {
    type: String,
    default: 'Ok'
  },
  autoClose: {
    type: Boolean,
    default: false
  },
  autoCloseDelay: {
    type: Number,
    default: 3000
  }
})

// Emits
const emit = defineEmits(['close', 'confirm'])

// Auto close functionality
let autoCloseTimer = null

const startAutoClose = () => {
  if (props.autoClose && props.isVisible) {
    autoCloseTimer = setTimeout(() => {
      handleConfirm()
    }, props.autoCloseDelay)
  }
}

const clearAutoClose = () => {
  if (autoCloseTimer) {
    clearTimeout(autoCloseTimer)
    autoCloseTimer = null
  }
}

// Methods
const handleBackdropClick = () => {
  // Haptic feedback for modal close
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'light')
  }
  emit('close')
}

const handleConfirm = () => {
  // Haptic feedback for success
  if (window.triggerHaptic) {
    window.triggerHaptic('notification', 'success')
  }
  
  clearAutoClose()
  emit('confirm')
}

const handleKeyDown = (event) => {
  if (event.key === 'Escape') {
    handleBackdropClick()
  } else if (event.key === 'Enter') {
    handleConfirm()
  }
}

// Watch for visibility changes
watch(() => props.isVisible, (newVal) => {
  if (newVal) {
    startAutoClose()
    document.addEventListener('keydown', handleKeyDown)
    document.body.style.overflow = 'hidden'
  } else {
    clearAutoClose()
    document.removeEventListener('keydown', handleKeyDown)
    document.body.style.overflow = ''
  }
})

// Cleanup on unmount
onUnmounted(() => {
  clearAutoClose()
  document.removeEventListener('keydown', handleKeyDown)
  document.body.style.overflow = ''
})
</script>

<style scoped>
/* Modal responsive sizing for Telegram WebApp */
@media (max-width: 375px) {
  .modal-content {
    width: calc(100vw - 32px) !important;
    max-width: 347px;
    margin: 0 16px;
  }
}

@media (min-width: 376px) and (max-width: 768px) {
  .modal-content {
    width: 347px !important;
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

/* Button touch feedback */
button {
  touch-action: manipulation;
  -webkit-user-select: none;
  user-select: none;
}

/* Responsive text sizes for small screens */
@media (max-width: 375px) {
  .text-[30px] {
    font-size: 26px;
  }
  
  .text-2xl {
    font-size: 20px;
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
</style>
