<template>
  <div class="w-full min-h-screen bg-white font-montserrat overflow-hidden flex flex-col">
    <!-- Main Content -->
    <div class="flex-1 flex items-center justify-center p-4 sm:p-6 md:p-8">
      <div class="w-fullmx-auto flex flex-col items-center">
        <!-- Email Icon -->
        <div class="mb-6 sm:mb-8 md:mb-10">
          <div class="w-16 h-16 xs:w-18 xs:h-18 sm:w-20 sm:h-20 md:w-24 md:h-24 flex items-center justify-center">
            <svg 
              viewBox="0 0 74 74" 
              fill="none" 
              xmlns="http://www.w3.org/2000/svg"
              class="w-full h-full"
            >
              <!-- Email envelope -->
              <rect x="10" y="20" width="44" height="32" rx="4" stroke="#22C55E" stroke-width="3" fill="none"/>
              <path d="M10 24L32 36L54 24" stroke="#22C55E" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
              
              <!-- Checkmark circle -->
              <circle cx="50" cy="50" r="12" fill="#22C55E"/>
              <path d="M44 50L48 54L56 46" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
        </div>

        <!-- Title -->
        <h1 class="text-2xl xs:text-3xl sm:text-4xl md:text-5xl font-semibold text-dbd-dark text-center capitalize mb-4 sm:mb-6 md:mb-8 leading-tight">
          Check Your Email
        </h1>

        <!-- Description Text -->
        <div class="w-full max-w-[343px] text-center mb-8 sm:mb-10 md:mb-12">
          <p class="text-sm sm:text-base text-dbd-light-gray font-medium leading-relaxed mb-4 sm:mb-6">
            We have sent you an email with the verification code to continue your authorization.
          </p>
          <p class="text-sm sm:text-base text-dbd-light-gray font-medium leading-relaxed">
            If you did not see the email right away please check your spam / junk folder.
          </p>
        </div>

        <!-- Resend Section -->
        <div class="w-full max-w-[347px] bg-white border border-dbd-light-gray rounded-xl p-4 sm:p-6 backdrop-blur-md">
          <p class="text-base sm:text-lg text-dbd-gray font-medium mb-3 sm:mb-4">
            Haven't received the verification code?
          </p>
          
          <div class="flex items-center justify-between">
            <button 
              @click="resendCode"
              :disabled="timeLeft > 0"
              class="text-sm sm:text-base font-semibold underline transition-all duration-200"
              :class="{
                'text-dbd-orange hover:text-orange-600 cursor-pointer': timeLeft === 0,
                'text-dbd-light-gray cursor-not-allowed': timeLeft > 0
              }"
            >
              Resend verification code
            </button>
            
            <span 
              v-if="timeLeft > 0"
              class="text-sm sm:text-base text-dbd-gray font-medium"
            >
              in {{ formatTime(timeLeft) }} secs
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// Timer state
const timeLeft = ref(59) // 59 seconds countdown
let intervalId = null

// Methods
const formatTime = (seconds) => {
  const mins = Math.floor(seconds / 60)
  const secs = seconds % 60
  return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`
}

const startTimer = () => {
  intervalId = setInterval(() => {
    if (timeLeft.value > 0) {
      timeLeft.value--
    } else {
      clearInterval(intervalId)
    }
  }, 1000)
}

const resendCode = () => {
  if (timeLeft.value === 0) {
    // Reset timer
    timeLeft.value = 59
    startTimer()
    
    // Here you would typically call your resend verification API
    console.log('Resending verification code...')
    
    // Add haptic feedback if available
    if (window.triggerHaptic) {
      window.triggerHaptic('impact', 'light')
    }
  }
}

// Lifecycle
onMounted(() => {
  startTimer()
  
  // Auto-redirect to next step after some time (optional)
  // setTimeout(() => {
  //   router.push('/favorites')
  // }, 10000) // 10 seconds
})

onUnmounted(() => {
  if (intervalId) {
    clearInterval(intervalId)
  }
})
</script>

<style scoped>
/* Ensure text is properly spaced and readable */
h1 {
  max-width: 300px;
  margin-left: auto;
  margin-right: auto;
}

/* Button hover states for touch devices */
@media (hover: none) and (pointer: coarse) {
  button:hover {
    transform: none;
  }
  
  button:active {
    opacity: 0.8;
  }
}

/* Performance optimizations */
* {
  will-change: auto;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Prevent zoom on mobile */
@media (max-width: 768px) {
  input, button, select, textarea {
    font-size: 16px;
  }
}
</style>
