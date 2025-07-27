<template>
  <Transition
    name="modal"
    enter-active-class="transition-all duration-300 ease-out"
    leave-active-class="transition-all duration-200 ease-in"
    enter-from-class="opacity-0 backdrop-blur-0 scale-95"
    enter-to-class="opacity-100 backdrop-blur-md scale-100"
    leave-from-class="opacity-100 backdrop-blur-md scale-100"
    leave-to-class="opacity-0 backdrop-blur-0 scale-95"
  >
    <div
      v-if="isVisible"
      class="fixed inset-0 flex items-center justify-center z-50 px-4"
      style="background: rgba(2, 7, 14, 0.20); backdrop-filter: blur(9px);"
      @click="onCancel"
    >
      
      <!-- Modal Content -->
      <div
        @click.stop
        class="relative bg-dbd-off-white rounded-[20px] shadow-xl font-montserrat w-full max-w-[320px] mx-auto transition-all duration-300 p-6 flex flex-col items-center gap-6"
      >
        <!-- Icon Container -->
        <div class="flex items-center justify-center">
          <div class="w-14 h-14 bg-red-50 border-2 border-red-200 rounded-full flex items-center justify-center">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path d="M12 9V13M12 17H12.01M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="#ef4444" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
        </div>

        <!-- Content -->
        <div class="text-center flex flex-col gap-3">
          <!-- Title -->
          <h3 class="text-lg font-semibold text-dbd-dark">Delete Position?</h3>

          <!-- Description -->
          <p class="text-sm text-dbd-gray leading-6">
            Are you sure you want to delete this item?
          </p>
        </div>

        <!-- Actions -->
        <div class="flex gap-3 w-full">
          <!-- Cancel Button -->
          <button
            @click="onCancel"
            class="flex-1 h-11 px-6 rounded-full border border-dbd-gray bg-dbd-off-white hover:bg-gray-50 transition-colors"
          >
            <span class="text-dbd-gray text-base font-medium">No</span>
          </button>

          <!-- Confirm Button -->
          <button
            @click="onConfirm"
            class="flex-1 h-11 rounded-full bg-red-500 hover:bg-red-600 transition-colors"
          >
            <span class="text-white text-base font-medium">Yes</span>
          </button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { watch } from 'vue'

const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['cancel', 'confirm'])

const onCancel = () => {
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'light')
  }
  emit('cancel')
}

const onConfirm = () => {
  if (window.triggerHaptic) {
    window.triggerHaptic('notification', 'warning')
  }
  emit('confirm')
}

const handleKeyDown = (event) => {
  if (event.key === 'Escape' && props.isVisible) {
    onCancel()
  } else if (event.key === 'Enter' && props.isVisible) {
    onConfirm()
  }
}

// Watch for visibility changes to add/remove event listeners
watch(() => props.isVisible, (isVisible) => {
  if (isVisible) {
    document.addEventListener('keydown', handleKeyDown)
    document.body.style.overflow = 'hidden'
  } else {
    document.removeEventListener('keydown', handleKeyDown)
    document.body.style.overflow = ''
  }
})
</script>

<style scoped>
/* Enhanced modal styling */
.shadow-xl {
  box-shadow: 0 10px 25px -3px rgba(2, 7, 14, 0.12), 0 4px 6px -2px rgba(2, 7, 14, 0.05);
}

/* Modal animations */
.modal-enter-active,
.modal-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
  transform: scale(0.95) translateY(10px);
}

/* Enhanced button interactions */
button {
  touch-action: manipulation;
  -webkit-user-select: none;
  user-select: none;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

button:active {
  transform: scale(0.97);
}

/* Telegram specific improvements */
@media (hover: none) {
  button:hover {
    opacity: 1 !important;
    background: inherit !important;
  }

  button:active {
    transform: scale(0.95);
    opacity: 0.85;
  }
}

/* Clean typography */
* {
  -webkit-tap-highlight-color: transparent;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  user-select: none;
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-feature-settings: 'kern' 1;
  text-rendering: optimizeLegibility;
}

/* Telegram WebApp specific optimizations */
@media (max-width: 375px) {
  .max-w-\[320px\] {
    max-width: calc(100vw - 24px);
  }

  /* Smaller font sizes for mobile */
  .text-lg { font-size: 16px; }
  .text-base { font-size: 14px; }
  .text-sm { font-size: 12px; }

  /* Compact spacing for mobile */
  .px-4 { padding-left: 12px; padding-right: 12px; }
  .p-6 { padding: 16px; }
}

/* Telegram WebApp viewport handling */
@media (max-height: 600px) {
  .p-6 {
    padding: 16px;
  }

  .gap-6 {
    gap: 16px;
  }
}


</style>
