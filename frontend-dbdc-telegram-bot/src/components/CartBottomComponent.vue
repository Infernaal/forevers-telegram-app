<template>
  <div class="cart-bottom-component bg-gray-100 px-4 pt-4 pb-6 sm:pb-6 md:pb-7 lg:pb-8">
    <!-- Total Section -->
    <div class="total-section flex items-center justify-center gap-1 mb-3 text-base sm:text-[17px] md:text-[18px] lg:text-[19px] leading-6">
      <span class="text-dbd-dark font-semibold">Total to pay:</span>
      <span class="text-dbd-primary font-semibold">${{ totalAmount.toLocaleString() }}</span>
    </div>

    <!-- Action Buttons -->
    <div class="action-buttons flex items-center justify-center gap-2.5">
      <!-- Back Button -->
      <button
        @click="$emit('back')"
        class="back-button flex items-center justify-center gap-2 h-10 sm:h-[40px] md:h-[42px] lg:h-[44px]
               px-6 sm:px-5 md:px-5 lg:px-6 min-w-[120px] sm:min-w-[110px] md:min-w-[115px] lg:min-w-[120px]
               bg-dbd-off-white border border-dbd-gray rounded-full flex-shrink-0
               transition-all duration-200 hover:bg-gray-100"
      >
        <svg width="18" height="18" viewBox="0 0 20 20" fill="none" class="text-dbd-gray">
          <path d="M18.2208 9.22071L3.66019 9.22071L7.13456 5.74611C7.43894 5.44192 7.43894 4.94845 7.13456 4.6443C6.83019 4.33992 6.33672 4.33992 6.03279 4.6443L1.22828 9.4489C0.923906 9.7531 0.923906 10.2466 1.22828 10.5507L6.03279 15.3555C6.18494 15.5078 6.38433 15.5838 6.58368 15.5838C6.78303 15.5838 6.98242 15.5078 7.13456 15.3555C7.43894 15.0513 7.43894 14.5579 7.13456 14.2538L3.66019 10.779L18.2208 10.779C18.6511 10.779 19 10.4301 19 9.99983C19 9.56955 18.6511 9.22071 18.2208 9.22071Z" fill="currentColor"/>
        </svg>
        <span class="text-dbd-gray font-medium text-sm leading-5">Back</span>
      </button>

      <!-- Buy Forevers Button -->
      <button
        @click="$emit('purchase')"
        class="buy-button flex items-center justify-center
               h-10 sm:h-[40px] md:h-[42px] lg:h-[44px]
               px-8 sm:px-6 md:px-6 lg:px-8
               text-white font-semibold text-base sm:text-[14px] md:text-[15px] lg:text-[16px] leading-5
               min-w-[180px] sm:min-w-[160px] md:min-w-[170px] lg:min-w-[180px]
               rounded-full transition-all duration-200"
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
.cart-bottom-component {
  font-family: 'Montserrat', sans-serif;
}

.back-button:hover,
.buy-button:hover {
  transform: translateY(-1px);
}
</style>


