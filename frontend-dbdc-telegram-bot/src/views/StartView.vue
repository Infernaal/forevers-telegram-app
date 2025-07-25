<template>
  <div class="start-view touch-optimized">
    <!-- Main Content -->
    <div class="flex-1 p-4 sm:p-6 md:p-8 flex items-center justify-center">
      <div
        class="w-full max-w-sm sm:max-w-md md:max-w-lg relative rounded-[2.5rem] p-6 sm:p-8 text-white flex flex-col h-auto"
        :style="cardStyle"
      >
        <!-- Brand Section -->
        <div class="flex items-start gap-4 mb-8">
          <div class="flex-shrink-0">
            <div class="w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-lg">
              <svg
                width="32"
                height="32"
                viewBox="0 0 32 32"
                fill="none"
                class="w-8 h-8"
              >
                <path
                  d="M29.037 8.33839V2.96289H8.11476V9.78787H2.96289V15.1634H8.11476V28.54H14.128V21.9801H19.2136V16.6046H14.128V15.1634H24.117V9.78787H14.128V8.33839H29.037Z"
                  fill="#2019CE"
                />
              </svg>
            </div>
          </div>
          <div class="flex-1 min-w-0">
            <h2 class="text-3xl sm:text-4xl font-bold leading-tight mb-2">
              Forevers
            </h2>
            <p class="text-base sm:text-lg md:text-xl font-medium leading-relaxed">
              With us — you're always ahead
            </p>
          </div>
        </div>

        <!-- Features Section -->
        <div class="mt-6">
          <h3 class="text-lg font-medium mb-4 text-center sm:text-left">
            What can this bot do?
          </h3>
          <ul class="space-y-3">
            <li
              v-for="feature in features"
              :key="feature.id"
              class="flex items-start gap-2"
            >
              <span class="w-2 h-2 bg-gray-300 rounded-full flex-shrink-0 mt-2"></span>
              <span class="text-sm sm:text-base font-medium leading-5">
                {{ feature.text }}
              </span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Bottom Section -->
    <div class="bg-white p-4 sm:p-6 flex items-center justify-center border-t border-gray-100">
      <button
        @click="handleStart"
        class="w-full max-w-sm h-12 sm:h-14 bg-gradient-to-r from-blue-700 to-purple-600 hover:from-blue-800 hover:to-purple-700 active:scale-95 transition-all duration-200 rounded-full text-white font-bold text-sm sm:text-base focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
      >
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

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap');

body {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Telegram WebApp specific styles */
.tg-viewport {
  height: var(--tg-viewport-height, 100vh) !important;
}

/* Smooth transitions for better UX */
* {
  -webkit-tap-highlight-color: transparent;
}

/* Custom scrollbar for webkit browsers */
::-webkit-scrollbar {
  width: 0;
}

/* Ensure proper touch scrolling on iOS */
.telegram-bot-screen {
  -webkit-overflow-scrolling: touch;
}
</style>
