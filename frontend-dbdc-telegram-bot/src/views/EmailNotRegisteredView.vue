<template>
  <div class="w-full min-h-screen bg-white font-montserrat overflow-x-hidden flex flex-col">
    <!-- Main Content -->
    <div class="flex-1 flex items-center justify-center p-3 sm:p-4 md:p-5 lg:p-6">
      <!-- Card Container -->
      <div class="w-full max-w-[347px] sm:max-w-md md:max-w-lg lg:max-w-xl mx-auto relative rounded-3xl sm:rounded-[2rem] md:rounded-[2.5rem] p-4 sm:p-6 md:p-8 lg:p-10 text-white flex flex-col min-h-[320px] sm:min-h-[360px] md:min-h-[400px] lg:min-h-[440px] xl:min-h-[480px] shadow-2xl"
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
        <div class="mt-auto pt-4">
          <button
            class="w-full h-[52px] sm:h-14 md:h-15 lg:h-16 px-6 sm:px-8 flex items-center justify-center gap-3 rounded-full border border-white bg-transparent text-white font-bold text-sm sm:text-base md:text-lg transition-all duration-200 active:scale-98 outline-none touch-manipulation"
            @click="continueWithTelegram">
            <span>Continue with Telegram</span>

            <!-- Telegram Icon -->
            <div class="w-8 h-8 flex-shrink-0">
              <img src="/telegram-icon.svg" alt="Telegram" class="w-full h-full" />
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
