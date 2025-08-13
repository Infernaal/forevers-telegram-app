<template>
  <div class="w-full min-h-screen bg-white font-montserrat overflow-x-hidden flex flex-col">
    <!-- Main Content -->
    <div class="flex-1 flex items-center justify-center p-3 sm:p-4 md:p-5 lg:p-6">
      <!-- Card Container -->
      <div class="w-full max-w-[347px] sm:max-w-md md:max-w-lg lg:max-w-xl mx-auto relative rounded-3xl sm:rounded-[2rem] md:rounded-[2.5rem] p-4 sm:p-6 md:p-8 lg:p-10 text-white flex flex-col min-h-[292px] sm:min-h-[340px] md:min-h-[380px] lg:min-h-[420px] shadow-2xl"
           style="background: linear-gradient(0deg, rgba(0, 0, 0, 0.25) 0%, rgba(0, 0, 0, 0.25) 100%), linear-gradient(90deg, #2019CE 20.91%, #473FFF 68.93%);">
        
        <!-- Main Message -->
        <div class="text-center mb-6 sm:mb-8 md:mb-10 lg:mb-12">
          <h1 class="text-lg sm:text-xl md:text-2xl lg:text-3xl font-bold leading-tight mb-4 sm:mb-5 md:mb-6 lg:mb-8 text-white">
            Unfortunately, your email<br class="hidden xs:block">
            is not registered on<br class="hidden xs:block">
            the DBD Capital platform
          </h1>
          
          <p class="text-sm sm:text-base md:text-lg lg:text-xl font-medium leading-relaxed text-white opacity-95 px-2 sm:px-4">
            We recommend you to pass the<br class="hidden sm:block">
            authorisation with an alternative option from the following
          </p>
        </div>

        <!-- Action Button -->
        <div class="mt-auto">
          <button 
            class="w-full h-12 sm:h-13 md:h-14 lg:h-16 px-6 sm:px-8 flex items-center justify-center gap-3 rounded-full border border-white bg-transparent text-white font-bold text-sm sm:text-base md:text-lg transition-all duration-200 hover:bg-white/10 active:scale-98 outline-none touch-manipulation"
            @click="continueWithTelegram">
            <span>Continue with Telegram</span>
            
            <!-- Telegram Icon -->
            <div class="w-8 h-8 flex-shrink-0 bg-gray-100 rounded-full flex items-center justify-center">
              <svg class="w-5 h-5" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M8.27827 12.5451L8.0136 17.0123C8.39227 17.0123 8.55628 16.8171 8.75295 16.5827L10.5283 14.5467L14.2071 17.7795C14.8818 18.2307 15.3571 17.9931 15.5391 17.0347L17.9538 3.45712L17.9545 3.45632C18.1685 2.25952 17.5938 1.79152 16.9365 2.08512L2.7428 8.60592C1.77411 9.05713 1.78878 9.70512 2.57813 9.99872L6.20689 11.3531L14.6358 5.02432C15.0324 4.70912 15.3931 4.88352 15.0964 5.19872L8.27827 12.5451Z" fill="#039BE5"/>
              </svg>
            </div>
          </button>
        </div>
      </div>
    </div>

    <!-- Bottom Safe Area -->
    <div class="bg-white px-4 sm:px-5 md:px-6 lg:px-8 pb-[max(var(--tg-content-safe-area-inset-bottom),1rem)] h-16 sm:h-20 md:h-24">
      <!-- Space for bottom safe area -->
    </div>
  </div>
</template>

<script setup>
const continueWithTelegram = () => {
  // Handle Telegram authentication flow
  console.log('Continue with Telegram clicked')
  // Add navigation or authentication logic here
}
</script>

<style scoped>
/* Custom responsive utilities */
@media (min-width: 375px) {
  .xs\:block {
    display: block;
  }
}

/* Touch optimization */
button {
  -webkit-tap-highlight-color: transparent;
  user-select: none;
}

/* Enhanced button states */
button:active {
  transform: scale(0.98);
}

/* Ensure proper text rendering */
h1, p {
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Responsive height utilities */
.h-13 {
  height: 3.25rem; /* 52px */
}

.h-15 {
  height: 3.75rem; /* 60px */
}
</style>
