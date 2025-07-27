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
      class="fixed inset-0 z-50 flex items-center justify-center px-4"
      style="background: rgba(2, 7, 14, 0.20); backdrop-filter: blur(9px);"
      @click="closeTooltip"
    >

      <!-- Tooltip content -->
      <div
        @click.stop
        class="relative bg-white rounded-3xl p-4 shadow-xl border border-gray-100 w-full max-w-[300px] mx-auto transition-all duration-300"
        style="min-height: 154px;"
      >
        <!-- Close button -->
        <button
          @click="closeTooltip"
          class="absolute top-1 right-1 w-11 h-11 flex items-center justify-center tooltip-close-btn"
        >
          <!-- White circle with gray border -->
          <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" class="absolute">
            <circle cx="16" cy="16" r="15.5" fill="#FAFAFA" stroke="#C7C7C7"/>
          </svg>
          <!-- Close cross -->
          <div class="relative w-5 h-5 z-10">
            <div class="absolute w-4 h-0.5 bg-black rounded-full transform rotate-45 top-2 left-0.5"></div>
            <div class="absolute w-4 h-0.5 bg-black rounded-full transform -rotate-45 top-2 left-0.5"></div>
          </div>
        </button>

        <!-- Title -->
        <h3 class="text-lg font-semibold text-white mb-4 pt-1 pr-10">
          {{ title }}
        </h3>

        <!-- Description -->
        <p class="text-sm text-white leading-6 pr-4">
          {{ description }}
        </p>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, watch, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  },
  title: {
    type: String,
    default: 'Forevers Balance'
  },
  description: {
    type: String,
    default: 'Dubadu Forevers ads you own. You invest and own your own advertising billboard on dubadu.com, and we rent it out.'
  }
})

const emit = defineEmits(['close'])

const closeTooltip = () => {
  emit('close')
}

const handleKeyDown = (event) => {
  if (event.key === 'Escape' && props.isVisible) {
    closeTooltip()
  }
}

// Watch for visibility changes to add/remove event listeners
watch(() => props.isVisible, (isVisible) => {
  if (isVisible) {
    document.addEventListener('keydown', handleKeyDown)
    // Prevent body scroll when tooltip is open
    document.body.style.overflow = 'hidden'
  } else {
    document.removeEventListener('keydown', handleKeyDown)
    // Restore body scroll
    document.body.style.overflow = ''
  }
})

// Cleanup on unmount
onBeforeUnmount(() => {
  document.removeEventListener('keydown', handleKeyDown)
  document.body.style.overflow = ''
})
</script>

<style scoped>
/* Custom styling to match Figma design */
.bg-white {
  background: linear-gradient(94deg, #120B81 33.64%, #09074E 76.52%);
  backdrop-filter: blur(32px);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

/* Backdrop blur effect */
.backdrop-blur-sm {
  backdrop-filter: blur(9px);
}

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

/* Text elements with proper z-index */
h3, p {
  position: relative;
  z-index: 1;
}

/* Mobile optimizations */
@media (max-width: 375px) {
  .fixed.inset-0 {
    padding-left: 16px;
    padding-right: 16px;
  }

  .max-w-\[300px\] {
    max-width: calc(100vw - 32px) !important;
    min-height: 140px !important;
  }

  .text-lg {
    font-size: 16px;
    line-height: 20px;
  }

  .text-sm {
    font-size: 13px;
    line-height: 18px;
  }
}

@media (max-width: 320px) {
  .fixed.inset-0 {
    padding-left: 12px;
    padding-right: 12px;
  }

  .max-w-\[300px\] {
    max-width: calc(100vw - 24px) !important;
    min-height: 130px !important;
  }

  .text-lg {
    font-size: 15px;
    line-height: 18px;
  }

  .text-sm {
    font-size: 12px;
    line-height: 16px;
  }
}

/* Tablet optimizations */
@media (min-width: 376px) and (max-width: 768px) {
  .fixed.inset-0 {
    padding-left: 20px;
    padding-right: 20px;
  }

  .max-w-\[300px\] {
    max-width: 300px !important;
  }
}

@media (min-width: 769px) {
  .fixed.inset-0 {
    padding-left: 24px;
    padding-right: 24px;
  }

  .max-w-\[300px\] {
    max-width: 300px !important;
  }
}
</style>
