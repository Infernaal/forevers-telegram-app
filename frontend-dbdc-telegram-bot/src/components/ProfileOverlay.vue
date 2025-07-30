<template>
  <div v-if="isVisible" class="fixed inset-0 z-[9998] font-montserrat bg-black/20 backdrop-blur-sm
                               flex items-center justify-center px-4 py-8 profile-overlay">
    
    <!-- ProfileOverlay Placeholder -->
    <div class="relative w-full max-w-xs sm:max-w-sm md:max-w-md lg:max-w-lg
                bg-gradient-to-br from-indigo-500 to-purple-600
                rounded-2xl sm:rounded-3xl shadow-2xl border border-white/20
                p-6 sm:p-8 text-white text-center
                transform transition-all duration-300 ease-out
                animate-pulse">
      
      <!-- Close Button -->
      <button @click="$emit('close')" 
              class="absolute top-4 right-4 w-8 h-8 sm:w-10 sm:h-10
                     bg-white/20 hover:bg-white/30 rounded-full
                     flex items-center justify-center
                     transition-all duration-200 ease-in-out
                     hover:scale-110 active:scale-95">
        <svg class="w-4 h-4 sm:w-5 sm:h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <!-- Profile Icon -->
      <div class="mx-auto mb-6 w-16 h-16 sm:w-20 sm:h-20 md:w-24 md:h-24
                  bg-white/20 rounded-full flex items-center justify-center">
        <svg class="w-8 h-8 sm:w-10 sm:h-10 md:w-12 md:h-12 text-white/80" 
             fill="currentColor" viewBox="0 0 24 24">
          <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
        </svg>
      </div>

      <!-- Title -->
      <h2 class="text-xl sm:text-2xl md:text-3xl font-bold mb-4">
        Profile Menu
      </h2>

      <!-- Description -->
      <p class="text-white/80 text-sm sm:text-base mb-8 leading-relaxed">
        This is a temporary placeholder for the ProfileOverlay component. 
        The interface will be redesigned soon.
      </p>

      <!-- Placeholder Cards -->
      <div class="space-y-3">
        <div class="h-12 sm:h-14 bg-white/10 rounded-xl animate-pulse"></div>
        <div class="h-12 sm:h-14 bg-white/10 rounded-xl animate-pulse"></div>
        <div class="h-12 sm:h-14 bg-white/10 rounded-xl animate-pulse"></div>
        <div class="h-12 sm:h-14 bg-white/10 rounded-xl animate-pulse"></div>
      </div>

      <!-- Footer Text -->
      <div class="mt-8 pt-6 border-t border-white/20">
        <p class="text-xs sm:text-sm text-white/60">
          Coming Soon...
        </p>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// Props
const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  }
})

// Emits
const emit = defineEmits(['close'])

console.log('ProfileOverlay Placeholder loaded')
</script>

<style scoped>
.profile-overlay {
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from { 
    opacity: 0; 
    transform: scale(0.95);
  }
  to { 
    opacity: 1; 
    transform: scale(1);
  }
}

/* Prevent touch highlighting */
* {
  -webkit-tap-highlight-color: transparent;
}
</style>
