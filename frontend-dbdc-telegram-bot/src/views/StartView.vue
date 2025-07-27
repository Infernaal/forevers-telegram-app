<template>
  <div class="min-h-screen bg-white flex flex-col font-montserrat overflow-x-hidden">
    <!-- Main Content -->
    <div class="flex-1 flex items-center justify-center px-3 py-5 xs:px-4 xs:py-4 sm:px-4 sm:py-[18px] ml:px-5 ml:py-6 md:px-6 md:py-8 lg:px-6 lg:py-8">
      <div class="w-full max-w-[100%] xs:max-w-[340px] sm:max-w-[340px] ml:max-w-[400px] md:max-w-[420px] lg:max-w-[420px] relative rounded-[32px] xs:rounded-[32px] sm:rounded-[36px] ml:rounded-[44px] md:rounded-[48px] lg:rounded-[48px] p-5 xs:p-5 sm:p-[22px] ml:p-7 md:p-8 lg:p-8 text-white flex flex-col min-h-[360px] xs:min-h-[360px] sm:min-h-[380px] ml:min-h-[420px] md:min-h-[460px] lg:min-h-[460px] shadow-2xl" :style="cardStyle">
        <!-- Brand Section -->
        <div class="flex items-start gap-3 xs:gap-3 sm:gap-[14px] ml:gap-[18px] md:gap-5 lg:gap-5 mb-6 xs:mb-6 sm:mb-7 ml:mb-9 md:mb-10 lg:mb-10">
          <div class="flex-shrink-0">
            <div class="w-10 h-10 xs:w-10 xs:h-10 sm:w-11 sm:h-11 ml:w-[52px] ml:h-[52px] md:w-14 md:h-14 lg:w-14 lg:h-14 bg-white rounded-full flex items-center justify-center shadow-lg">
              <svg
                class="w-6 h-6 xs:w-6 xs:h-6 sm:w-7 sm:h-7 ml:w-9 ml:h-9 md:w-10 md:h-10 lg:w-10 lg:h-10"
                viewBox="0 0 32 32"
                fill="none"
              >
                <path
                  d="M29.037 8.33839V2.96289H8.11476V9.78787H2.96289V15.1634H8.11476V28.54H14.128V21.9801H19.2136V16.6046H14.128V15.1634H24.117V9.78787H14.128V8.33839H29.037Z"
                  fill="#2019CE"
                />
              </svg>
            </div>
          </div>
          <div class="flex-1 min-w-0">
            <h2 class="text-[26px] xs:text-[26px] sm:text-[30px] ml:text-4xl md:text-[40px] lg:text-[40px] font-bold leading-tight mb-1.5 xs:mb-1.5 sm:mb-[7px] ml:mb-[9px] md:mb-[10px] lg:mb-[10px] text-white">Forevers</h2>
            <p class="text-sm xs:text-sm sm:text-[15px] ml:text-[17px] md:text-lg lg:text-lg font-medium leading-relaxed text-white opacity-95">
              With us — you're always ahead
            </p>
          </div>
        </div>

        <!-- Features Section -->
        <div class="mt-4">
          <h3 class="text-base xs:text-base sm:text-[17px] ml:text-[19px] md:text-xl lg:text-xl font-medium mb-3 xs:mb-3 sm:mb-[14px] ml:mb-[18px] md:mb-5 lg:mb-5 text-center text-white">
            What can this bot do?
          </h3>
          <ul class="list-none p-0 m-0 flex flex-col gap-2.5 xs:gap-2.5 sm:gap-[11px] ml:gap-[14px] md:gap-4 lg:gap-4">
            <li
              v-for="feature in features"
              :key="feature.id"
              class="flex items-start gap-2 leading-relaxed"
            >
              <span class="w-1.5 h-1.5 xs:w-1.5 xs:h-1.5 sm:w-[7px] sm:h-[7px] ml:w-[9px] ml:h-[9px] md:w-2.5 md:h-2.5 lg:w-2.5 lg:h-2.5 bg-white bg-opacity-70 rounded-full flex-shrink-0 mt-1 xs:mt-[5px] sm:mt-[5.5px] ml:mt-1.5 md:mt-1.5 lg:mt-1.5"></span>
              <span class="text-[13px] xs:text-[13px] sm:text-[13.5px] ml:text-[15px] md:text-base lg:text-base font-medium text-white opacity-95">
                {{ feature.text }}
              </span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Bottom Section -->
    <div class="bg-white px-3 py-3 xs:px-3 xs:py-3 sm:px-[14px] sm:py-[14px] ml:px-5 ml:py-[18px] md:px-6 md:py-5 lg:px-6 lg:py-5 flex items-center justify-center border-t border-black border-opacity-5 pb-[calc(0.75rem+env(safe-area-inset-bottom,0px))] xs:pb-[calc(0.75rem+env(safe-area-inset-bottom,0px))] sm:pb-[calc(0.875rem+env(safe-area-inset-bottom,0px))] ml:pb-[calc(1.125rem+env(safe-area-inset-bottom,0px))] md:pb-[calc(1.25rem+env(safe-area-inset-bottom,0px))] lg:pb-[calc(1.25rem+env(safe-area-inset-bottom,0px))]">
      <button @click="handleStart" class="w-full max-w-[100%] xs:max-w-[360px] sm:max-w-[360px] ml:max-w-[400px] md:max-w-[420px] lg:max-w-[420px] h-12 xs:h-12 sm:h-[50px] ml:h-14 md:h-[60px] lg:h-[60px] bg-gradient-to-r from-dbd-primary to-[#473FFF] border-none rounded-[24px] xs:rounded-[24px] sm:rounded-[25px] ml:rounded-[28px] md:rounded-[30px] lg:rounded-[30px] text-white font-bold text-[15px] xs:text-[15px] sm:text-[15.5px] ml:text-[17px] md:text-lg lg:text-lg cursor-pointer transition-all duration-200 shadow-[0_4px_12px_rgba(32,25,206,0.25)] outline-none transform will-change-transform hover:shadow-[0_6px_16px_rgba(32,25,206,0.35)] hover:-translate-y-px active:translate-y-0 active:scale-[0.98] active:shadow-[0_2px_8px_rgba(32,25,206,0.4)]">
        Start
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'

// Router instance
const router = useRouter()

// Features data
const features = ref([
  { id: 1, text: 'Discover the capabilities of this bot!' },
  { id: 2, text: 'Explore the features of this bot!' },
  { id: 3, text: 'Discover the amazing features this bot offers!' }
])

// Computed styles for better performance
const cardStyle = computed(() => ({
  background: `
    linear-gradient(0deg, rgba(0, 0, 0, 0.25) 0%, rgba(0, 0, 0, 0.25) 100%),
    linear-gradient(90deg, #2019CE 20.91%, #473FFF 68.93%)
  `
}))

// Handle start button click
const handleStart = () => {
  router.push('/favorites')
}

// Initialize app
onMounted(() => {
  // Prevent zoom on mobile
  const viewport = document.querySelector('meta[name="viewport"]')
  if (!viewport) {
    const meta = document.createElement('meta')
    meta.name = 'viewport'
    meta.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no'
    document.head.appendChild(meta)
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap');

/* Landscape orientation adjustments for phones */
@media (max-height: 500px) and (orientation: landscape) {
  .min-h-screen {
    min-height: 100vh;
  }
}

/* High DPI displays */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  svg {
    image-rendering: -webkit-optimize-contrast;
    image-rendering: crisp-edges;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .min-h-screen {
    background: #1a1a1a !important;
  }

  .bg-white {
    background: #1a1a1a !important;
    border-top-color: rgba(255, 255, 255, 0.1) !important;
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  button {
    transition: none !important;
  }

  button:hover {
    transform: none !important;
  }

  button:active {
    transform: scale(0.98) !important;
  }
}

/* Touch optimizations */
@media (hover: none) and (pointer: coarse) {
  button:hover {
    box-shadow: 0 4px 12px rgba(32, 25, 206, 0.25) !important;
    transform: none !important;
  }

  button:active {
    transform: scale(0.96) !important;
    box-shadow: 0 2px 8px rgba(32, 25, 206, 0.4) !important;
  }
}

/* Custom scrollbar for webkit browsers */
::-webkit-scrollbar {
  width: 0;
}

/* Telegram WebApp specific optimizations */
* {
  -webkit-tap-highlight-color: transparent;
}

/* Performance optimizations */
button {
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  touch-action: manipulation;
}
</style>
