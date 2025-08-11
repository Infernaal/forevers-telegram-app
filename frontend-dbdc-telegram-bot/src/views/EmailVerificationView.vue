<template>
  <div class="w-full min-h-screen bg-white font-montserrat overflow-hidden flex flex-col">
    <!-- Main Content -->
    <div class="flex-1 flex items-center justify-center p-4 sm:p-6 md:p-8">
      <div class="w-full mx-auto flex flex-col items-center">
        <!-- Email Icon -->
        <div class="mb-6 sm:mb-8 md:mb-10">
          <img
            src="/email-icon.svg"
            alt="Email verification"
            class="w-16 h-16 xs:w-18 xs:h-18 sm:w-20 sm:h-20 md:w-24 md:h-24"
          />
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

        <!-- Continue Button -->
        <div class="w-full max-w-[347px]">
          <button
            @click="handleContinue"
            class="w-full h-12 xs:h-14 sm:h-16 rounded-full font-bold text-sm xs:text-base sm:text-lg
                   bg-dbd-primary text-white border-2 border-dbd-primary
                   active:scale-[0.98] focus:outline-none"
          >
            Continue
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// Timer state (keeping for potential future use)
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

const handleContinue = () => {
  // Add haptic feedback if available
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'medium')
  }

  // Navigate to verification code entry
  console.log('Continuing to verification code entry...')
  router.push('/verification-code')
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
