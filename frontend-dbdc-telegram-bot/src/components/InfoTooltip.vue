<template>
  <Transition
    name="tooltip"
    enter-active-class="transition-all duration-200 ease-out"
    leave-active-class="transition-all duration-150 ease-in"
    enter-from-class="opacity-0 scale-90 translate-y-4"
    enter-to-class="opacity-100 scale-100 translate-y-0"
    leave-from-class="opacity-100 scale-100 translate-y-0"
    leave-to-class="opacity-0 scale-95 translate-y-2"
  >
    <div
      v-if="isVisible"
      class="fixed inset-0 z-50 flex items-center justify-center px-9"
      @click="closeTooltip"
    >
      <!-- Blur backdrop -->
      <div class="absolute inset-0 bg-black bg-opacity-20 backdrop-blur-sm"></div>
      
      <!-- Tooltip content -->
      <div
        @click.stop
        class="relative bg-white rounded-3xl p-4 shadow-xl border border-gray-100"
        style="width: 300px; min-height: 154px;"
      >
        <!-- Close button -->
        <button
          @click="closeTooltip"
          class="absolute top-1 right-1 w-11 h-11 flex items-center justify-center"
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

/* Tooltip animations - Optimized for smooth mobile experience */
.tooltip-enter-active {
  transition: all 0.2s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.tooltip-leave-active {
  transition: all 0.15s cubic-bezier(0.4, 0, 0.6, 1);
}

.tooltip-enter-from {
  opacity: 0;
  transform: scale(0.9) translateY(16px);
}

.tooltip-leave-to {
  opacity: 0;
  transform: scale(0.95) translateY(8px);
}

/* Ensure text is readable on gradient background */
h3, p {
  position: relative;
  z-index: 1;
}

/* Mobile optimizations */
@media (max-width: 375px) {
  div[style*="width: 300px"] {
    width: calc(100vw - 72px) !important;
    max-width: 300px;
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
  div[style*="width: 300px"] {
    width: calc(100vw - 40px) !important;
    max-width: 280px;
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
</style>
