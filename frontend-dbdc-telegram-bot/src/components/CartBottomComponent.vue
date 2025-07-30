<template>
  <div class="w-full bg-gray-100 px-4 pt-4 pb-6 sm:pb-8 md:pb-10 lg:pb-12 xl:pb-16 max-w-6xl mx-auto">
    <!-- Total Section -->
    <div class="flex items-center justify-center gap-2 mb-4 lg:mb-6 xl:mb-8">
      <span class="text-dbd-dark font-semibold text-lg sm:text-xl md:text-2xl lg:text-3xl xl:text-4xl">Total to pay:</span>
      <span class="text-dbd-primary font-semibold text-lg sm:text-xl md:text-2xl lg:text-3xl xl:text-4xl">${{ totalAmount.toLocaleString() }}</span>
    </div>

    <!-- Action Buttons -->
    <div class="flex items-center justify-center gap-3 sm:gap-4 md:gap-6 lg:gap-8 xl:gap-10">
      <!-- Back Button -->
      <button
        @click="$emit('back')"
        class="flex items-center justify-center gap-2 h-12 sm:h-14 md:h-16 lg:h-20 xl:h-24 px-6 sm:px-8 md:px-10 lg:px-12 xl:px-16 bg-dbd-off-white border border-dbd-gray rounded-full flex-shrink-0 transition-all duration-200 hover:bg-gray-100 hover:transform hover:-translate-y-0.5 min-w-[120px] sm:min-w-[140px] md:min-w-[160px] lg:min-w-[180px] xl:min-w-[200px]"
      >
        <svg width="18" height="18" viewBox="0 0 20 20" fill="none" class="text-dbd-gray w-4 h-4 sm:w-5 sm:h-5 md:w-6 md:h-6 lg:w-8 lg:h-8 xl:w-10 xl:h-10">
          <path d="M18.2208 9.22071L3.66019 9.22071L7.13456 5.74611C7.43894 5.44192 7.43894 4.94845 7.13456 4.6443C6.83019 4.33992 6.33672 4.33992 6.03279 4.6443L1.22828 9.4489C0.923906 9.7531 0.923906 10.2466 1.22828 10.5507L6.03279 15.3555C6.18494 15.5078 6.38433 15.5838 6.58368 15.5838C6.78303 15.5838 6.98242 15.5078 7.13456 15.3555C7.43894 15.0513 7.43894 14.5579 7.13456 14.2538L3.66019 10.779L18.2208 10.779C18.6511 10.779 19 10.4301 19 9.99983C19 9.56955 18.6511 9.22071 18.2208 9.22071Z" fill="currentColor"/>
        </svg>
        <span class="text-dbd-gray font-medium text-sm sm:text-base md:text-lg lg:text-xl xl:text-2xl">Back</span>
      </button>

      <!-- Buy Forevers Button -->
      <button
        @click="$emit('purchase')"
        class="flex items-center justify-center h-12 sm:h-14 md:h-16 lg:h-20 xl:h-24 px-8 sm:px-10 md:px-12 lg:px-16 xl:px-20 rounded-full text-white font-semibold text-base sm:text-lg md:text-xl lg:text-2xl xl:text-3xl transition-all duration-200 hover:transform hover:-translate-y-0.5 hover:shadow-lg min-w-[180px] sm:min-w-[200px] md:min-w-[220px] lg:min-w-[240px] xl:min-w-[280px]"
        style="background: linear-gradient(90deg, #2019CE 0%, #473FFF 100%)"
      >
        Buy Forevers
      </button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  totalAmount: {
    type: Number,
    required: true
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

/* Telegram WebApp specific optimizations */
* {
  -webkit-tap-highlight-color: transparent;
}
</style>
