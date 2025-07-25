<template>
  <Transition
    name="modal"
    enter-active-class="transition-all duration-300 ease-out"
    leave-active-class="transition-all duration-200 ease-in"
    enter-from-class="opacity-0 scale-95"
    enter-to-class="opacity-100 scale-100"
    leave-from-class="opacity-100 scale-100"
    leave-to-class="opacity-0 scale-95"
  >
    <div
      v-if="isVisible"
      class="fixed inset-0 z-50 flex items-center justify-center px-4"
      @click="onCancel"
    >
      <!-- Blur backdrop -->
      <div class="absolute inset-0 bg-black bg-opacity-20 backdrop-blur-sm"></div>
      
      <!-- Modal content -->
      <div
        @click.stop
        class="relative bg-dbd-off-white rounded-2xl shadow-xl"
        style="width: 229px; height: 198px;"
      >
        <!-- Title -->
        <div class="absolute left-9 top-6 w-38 h-6">
          <h3 class="text-lg font-semibold text-dbd-dark text-center">
            Delete Position?
          </h3>
        </div>

        <!-- Description -->
        <div class="absolute left-6 top-16 w-45 h-11">
          <p class="text-base text-dbd-gray text-center leading-5">
            Are you sure you want<br>to delete this item?
          </p>
        </div>

        <!-- Action Buttons Container -->
        <div class="absolute left-6 top-32 flex items-center gap-3" style="width: 181px; height: 44px;">
          <!-- No Button -->
          <button
            @click="onCancel"
            class="flex items-center justify-center rounded-full border border-dbd-gray bg-dbd-off-white hover:bg-gray-50 transition-colors"
            style="width: 84px; height: 44px; padding: 12px 24px;"
          >
            <span class="text-dbd-gray text-base font-medium">No</span>
          </button>

          <!-- Yes Button -->
          <button
            @click="onConfirm"
            class="flex items-center justify-center rounded-full border border-white text-white hover:bg-red-600 transition-colors"
            style="width: 85px; height: 44px; padding: 12px 24px; background: #FF1919;"
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
  emit('cancel')
}

const onConfirm = () => {
  emit('confirm')
}

const handleKeyDown = (event) => {
  if (event.key === 'Escape' && props.isVisible) {
    onCancel()
  }
}

// Watch for visibility changes to add/remove event listeners
watch(() => props.isVisible, (isVisible) => {
  if (isVisible) {
    document.addEventListener('keydown', handleKeyDown)
    // Prevent body scroll when modal is open
    document.body.style.overflow = 'hidden'
  } else {
    document.removeEventListener('keydown', handleKeyDown)
    // Restore body scroll
    document.body.style.overflow = ''
  }
})
</script>

<style scoped>
/* Use exact colors from Figma design */
.bg-red-500 {
  background-color: #FF1919 !important;
}

.hover\:bg-red-600:hover {
  background-color: #E60000 !important;
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
  transform: scale(0.95) translateY(-10px);
}

/* Backdrop blur effect */
.backdrop-blur-sm {
  backdrop-filter: blur(9px);
}

/* Mobile optimizations */
@media (max-width: 375px) {
  div[style*="width: 229px"] {
    width: calc(100vw - 32px) !important;
    max-width: 229px;
  }

  /* Maintain exact proportions for smaller screens */
  .absolute.left-6 {
    left: calc(6/229 * 100%) !important;
  }

  .absolute.left-9 {
    left: calc(9/229 * 100%) !important;
  }

  .absolute.top-6 {
    top: calc(6/198 * 100%) !important;
  }

  .absolute.top-16 {
    top: calc(16/198 * 100%) !important;
  }

  .absolute.top-32 {
    top: calc(32/198 * 100%) !important;
  }
}

@media (max-width: 320px) {
  div[style*="width: 229px"] {
    width: calc(100vw - 24px) !important;
    max-width: 220px;
  }

  button[style*="width: 84px"] {
    width: calc(84/229 * 100%) !important;
    min-width: 70px;
  }

  button[style*="width: 85px"] {
    width: calc(85/229 * 100%) !important;
    min-width: 70px;
  }

  div[style*="width: 181px"] {
    width: calc(181/229 * 100%) !important;
  }
}
</style>
