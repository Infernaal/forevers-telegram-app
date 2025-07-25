<template>
  <Transition
    name="success-notification"
    enter-active-class="transition-all duration-500 ease-out"
    leave-active-class="transition-all duration-300 ease-in"
    enter-from-class="opacity-0 transform translate-y-4 scale-95"
    enter-to-class="opacity-100 transform translate-y-0 scale-100"
    leave-from-class="opacity-100 transform translate-y-0 scale-100"
    leave-to-class="opacity-0 transform translate-y-2 scale-98"
  >
    <div
      v-if="isVisible"
      @click="$emit('close')"
      class="fixed bottom-24 left-1/2 transform -translate-x-1/2 z-50 success-notification px-4 sm:px-0 cursor-pointer"
    >
      <div class="bg-green-500 text-white px-4 sm:px-6 py-3 rounded-full shadow-lg flex items-center gap-2 sm:gap-3 border border-green-600 min-w-[257px] justify-center max-w-sm mx-auto hover:bg-green-600 transition-colors"
           style="filter: drop-shadow(4px 8px 12px rgba(7, 184, 14, 0.13));">
        <!-- Check Icon -->
        <div class="w-5 h-5 sm:w-6 sm:h-6 bg-white bg-opacity-20 rounded-full flex items-center justify-center flex-shrink-0">
          <svg class="w-3 h-3 sm:w-4 sm:h-4 text-white" viewBox="0 0 16 16">
            <path d="M13.5 4.5L6 12L2.5 8.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
          </svg>
        </div>

        <!-- Success Message -->
        <span class="font-semibold text-sm sm:text-base">{{ message }}</span>
      </div>
    </div>
  </Transition>
</template>

<script setup>
defineProps({
  isVisible: {
    type: Boolean,
    default: false
  },
  message: {
    type: String,
    default: 'Success!'
  }
})

defineEmits(['close'])
</script>

<style scoped>
/* Success notification responsive positioning */
@media (max-width: 375px) {
  .success-notification {
    bottom: 100px !important;
    left: 16px !important;
    right: 16px !important;
    transform: none !important;
    min-width: auto !important;
  }

  .success-notification > div {
    min-width: auto !important;
    width: 100%;
  }
}

@media (min-width: 376px) and (max-width: 768px) {
  .success-notification {
    bottom: 110px !important;
  }
}

/* Telegram mini app optimizations */
@media (max-width: 480px) {
  .success-notification {
    position: fixed;
    z-index: 1000;
  }

  .success-notification-mobile {
    bottom: calc(89px + env(safe-area-inset-bottom, 8px)) !important;
  }
}

/* Safe area support for notifications */
@supports (padding: max(0px)) {
  .success-notification {
    bottom: max(96px, calc(96px + env(safe-area-inset-bottom)));
  }
}

/* Success notification animations */
.success-notification-enter-active,
.success-notification-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.success-notification-enter-from {
  opacity: 0;
  transform: translateY(20px) scale(0.9);
}

.success-notification-leave-to {
  opacity: 0;
  transform: translateY(-10px) scale(0.95);
}
</style>
