<template>
  <div class="w-full bg-gray-100 px-4 pt-3 pb-4 sm:pb-5 md:pb-6 lg:pb-7">
    <!-- Total Section -->
    <div class="flex items-center justify-center gap-2 mb-3 lg:mb-4">
      <span class="text-dbd-dark font-semibold text-lg sm:text-xl md:text-xl lg:text-2xl">Total to pay:</span>
      <span class="text-dbd-primary font-semibold text-lg sm:text-xl md:text-xl lg:text-2xl">${{ totalAmount.toLocaleString() }}</span>
    </div>

    <!-- Action Buttons -->
    <div class="flex items-center justify-center gap-3 sm:gap-4 md:gap-5 lg:gap-6">
      <!-- Back Button -->
      <button
        @click="$emit('back')"
        class="flex items-center justify-center gap-2 h-11 sm:h-12 md:h-13 lg:h-14 px-5 sm:px-6 md:px-7 lg:px-8 bg-dbd-off-white border border-dbd-gray rounded-full flex-shrink-0 transition-all duration-200 hover:bg-gray-100 hover:transform hover:-translate-y-0.5 min-w-[110px] sm:min-w-[120px] md:min-w-[130px] lg:min-w-[140px]"
      >
        <svg width="18" height="18" viewBox="0 0 20 20" fill="none" class="text-dbd-gray w-4 h-4 sm:w-5 sm:h-5 md:w-5 md:h-5 lg:w-6 lg:h-6">
          <path d="M18.2208 9.22071L3.66019 9.22071L7.13456 5.74611C7.43894 5.44192 7.43894 4.94845 7.13456 4.6443C6.83019 4.33992 6.33672 4.33992 6.03279 4.6443L1.22828 9.4489C0.923906 9.7531 0.923906 10.2466 1.22828 10.5507L6.03279 15.3555C6.18494 15.5078 6.38433 15.5838 6.58368 15.5838C6.78303 15.5838 6.98242 15.5078 7.13456 15.3555C7.43894 15.0513 7.43894 14.5579 7.13456 14.2538L3.66019 10.779L18.2208 10.779C18.6511 10.779 19 10.4301 19 9.99983C19 9.56955 18.6511 9.22071 18.2208 9.22071Z" fill="currentColor"/>
        </svg>
        <span class="text-dbd-gray font-medium text-sm sm:text-base md:text-base lg:text-lg">Back</span>
      </button>

      <!-- Primary Action Button -->
      <button
        @click="!disabled ? $emit('purchase') : null"
        :disabled="disabled"
        class="flex items-center justify-center h-11 sm:h-12 md:h-13 lg:h-14 px-6 sm:px-8 md:px-10 lg:px-12 rounded-full text-white font-semibold text-base sm:text-lg md:text-lg lg:text-xl transition-all duration-200 min-w-[160px] sm:min-w-[180px] md:min-w-[200px] lg:min-w-[220px]"
        :class="{
          'opacity-50 cursor-not-allowed': disabled,
          'hover:transform hover:-translate-y-0.5 hover:shadow-lg': !disabled
        }"
        :style="disabled ? 'background: #9CA3AF' : 'background: linear-gradient(90deg, #2019CE 0%, #473FFF 100%)'"
      >
        {{ buttonText }}
      </button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  totalAmount: {
    type: Number,
    required: true
  },
  disabled: {
    type: Boolean,
    default: false
  },
  buttonText: {
    type: String,
    default: 'Buy Forevers'
  }
})

const emit = defineEmits(['back', 'purchase'])
</script>

<style scoped>
/* Base styles */
.w-full {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Button hover effects */
button {
  touch-action: manipulation;
  user-select: none;
  -webkit-user-select: none;
}

button:active {
  transform: scale(0.98) translateY(1px);
}

/* Performance optimizations */
button {
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Custom height class */
.h-13 {
  height: 3.25rem; /* 52px */
}

/* Telegram WebApp specific optimizations */
* {
  -webkit-tap-highlight-color: transparent;
}
</style>
