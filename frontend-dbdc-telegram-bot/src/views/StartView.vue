<template>
  <div class="w-full min-h-screen bg-white font-montserrat overflow-x-hidden flex flex-col">
    <!-- Main Content -->
    <div class="flex-1 flex items-center justify-center p-4 sm:p-5 md:p-6 lg:p-8">
      <div class="w-full relative rounded-3xl sm:rounded-[2.5rem] md:rounded-[3rem] p-5 sm:p-6 md:p-7 lg:p-8 text-white flex flex-col min-h-[360px] sm:min-h-[380px] md:min-h-[420px] lg:min-h-[460px] shadow-2xl" :style="cardStyle">
        <!-- Brand Section -->
        <div class="flex items-start gap-3 sm:gap-4 md:gap-5 lg:gap-6 mb-6 sm:mb-7 md:mb-9 lg:mb-10">
          <div class="flex-shrink-0">
            <div class="w-10 h-10 sm:w-11 sm:h-11 md:w-12 md:h-12 lg:w-14 lg:h-14 bg-white rounded-full flex items-center justify-center shadow-lg">
              <svg
                class="w-6 h-6 sm:w-7 sm:h-7 md:w-8 md:h-8 lg:w-10 lg:h-10"
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
            <h2 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold leading-tight mb-1.5 sm:mb-2 text-white">Forevers</h2>
            <p class="text-sm sm:text-base md:text-lg lg:text-xl font-medium leading-snug text-white opacity-95">
              With us — you're always ahead
            </p>
          </div>
        </div>

        <!-- Features Section -->
        <div class="mt-8 sm:mt-10 md:mt-12">
          <h3 class="text-base sm:text-lg md:text-xl lg:text-2xl font-medium mb-3 sm:mb-4 md:mb-5 lg:mb-6 text-center text-white">
            What can this bot do?
          </h3>
          <ul class="list-none p-0 m-0 flex flex-col gap-2.5 sm:gap-3 md:gap-3.5 lg:gap-4">
            <li
              v-for="feature in features"
              :key="feature.id"
              class="flex items-start gap-2 leading-relaxed"
            >
              <span class="w-1.5 h-1.5 sm:w-2 sm:h-2 md:w-2.5 md:h-2.5 bg-white/70 rounded-full flex-shrink-0 mt-1.5 sm:mt-2"></span>
              <span class="text-xs sm:text-sm md:text-base lg:text-lg font-medium text-white opacity-95">
                {{ feature.text }}
              </span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Bottom Section -->
    <div class="bg-white p-4 border-t border-black/5 safe-bottom">
      <button @click="handleStart" class="w-full h-12 sm:h-13 md:h-14 lg:h-15 bg-gradient-to-r from-dbd-primary to-[#473FFF] border-0 rounded-full text-white font-bold text-sm sm:text-base md:text-lg lg:text-xl font-montserrat cursor-pointer transition-all duration-200 ease-out shadow-lg hover:shadow-xl active:scale-98 outline-none touch-manipulation">
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
/* Global scrollbar hiding and Telegram optimizations */
::-webkit-scrollbar {
  width: 0;
}

* {
  -webkit-tap-highlight-color: transparent;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

/* Performance optimizations */
* {
  will-change: auto;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Safe area handling for iOS and other devices with home indicator */
.safe-bottom {
  padding-bottom: calc(8px + env(safe-area-inset-bottom, 0px));
}
</style>
