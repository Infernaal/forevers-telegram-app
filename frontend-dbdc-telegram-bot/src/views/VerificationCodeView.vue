<template>
  <div class="w-full min-h-screen bg-dbd-off-white font-montserrat overflow-hidden flex flex-col">
    <!-- Main Content -->
    <div class="flex-1 flex items-center justify-center p-4 xs:p-6 sm:p-8">
      <div class="w-full max-w-sm xs:max-w-md sm:max-w-lg md:max-w-xl">
        <!-- Verification Card -->
        <div
          class="w-full h-[320px] xs:h-[340px] sm:h-[360px] md:h-[380px] rounded-3xl p-6 xs:p-7 sm:p-8 md:p-10 flex flex-col text-white"
          :style="cardStyle"
        >
          <!-- Title -->
          <div class="text-center mb-6 xs:mb-7 sm:mb-8">
            <h1 class="text-lg xs:text-xl sm:text-2xl md:text-3xl font-semibold leading-tight max-w-[300px] mx-auto">
              Please, enter your verification code in the box below
            </h1>
          </div>

          <!-- Verification Code Input -->
          <div class="flex flex-col items-center gap-3 xs:gap-4">
            <!-- Code Input Boxes -->
            <div class="flex justify-center gap-3 xs:gap-4 sm:gap-5">
              <div
                v-for="(digit, index) in verificationCode"
                :key="index"
                class="w-12 xs:w-14 sm:w-16 md:w-18 h-12 xs:h-14 sm:h-16 md:h-18 rounded-lg border-2 flex items-center justify-center cursor-pointer transition-all"
                :class="{
                  'border-dbd-orange bg-black': digit === '' && focusedIndex === index,
                  'border-green-500 bg-green-900': digit !== '',
                  'border-white bg-black': digit === '' && focusedIndex !== index
                }"
                :style="{
                  backgroundColor: digit !== '' ? '#020F03' : '#000000',
                  borderColor: digit !== '' ? '#07B80E' : (focusedIndex === index ? '#FF6800' : '#FFFFFF')
                }"
                @click="focusInput(index)"
              >
                <input
                  :ref="el => inputRefs[index] = el"
                  v-model="verificationCode[index]"
                  @input="handleInput(index, $event)"
                  @keydown="handleKeydown(index, $event)"
                  @focus="focusedIndex = index"
                  @blur="focusedIndex = -1"
                  type="text"
                  maxlength="1"
                  class="w-full h-full bg-transparent text-center text-white text-2xl xs:text-3xl sm:text-4xl font-bold border-none outline-none"
                  inputmode="numeric"
                  pattern="[0-9]*"
                  :style="{
                    fontSize: digit !== '' ? '26px' : '20px'
                  }"
                />
              </div>
            </div>

            <!-- Resend Section -->
            <div class="flex justify-between items-center w-full max-w-[300px] xs:max-w-[320px] sm:max-w-[340px] whitespace-nowrap">
              <button
                @click="resendCode"
                :disabled="timeLeft > 0"
                class="text-sm font-semibold underline transition-all duration-200 flex-shrink-0"
                :class="{
                  'text-dbd-orange hover:text-orange-400 cursor-pointer': timeLeft === 0,
                  'text-gray-300 cursor-not-allowed': timeLeft > 0
                }"
              >
                Resend verification code
              </button>

              <span
                v-if="timeLeft > 0"
                class="text-sm text-white font-medium flex-shrink-0 ml-2"
              >
                in {{ formatTime(timeLeft) }} sec
              </span>
            </div>
          </div>

          <!-- Continue Button -->
          <div class="mt-auto pt-6 xs:pt-7 sm:pt-8">
            <button
              @click="handleContinue"
              :disabled="!isCodeComplete"
              class="w-full h-12 xs:h-14 sm:h-16 rounded-full font-bold text-sm xs:text-base sm:text-lg
                     bg-dbd-orange border border-dbd-orange text-white
                     transition-all duration-300 ease-in-out
                     flex items-center justify-center gap-2 xs:gap-3
                     hover:bg-orange-600 hover:border-orange-600 hover:shadow-lg hover:scale-[1.02]
                     active:scale-[0.98] disabled:cursor-not-allowed
                     disabled:hover:scale-100 disabled:hover:bg-dbd-orange"
              :class="{
                'opacity-50': !isCodeComplete
              }"
            >
              <span>Continue</span>
              <svg class="w-5 h-5 xs:w-6 xs:h-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M1.03895 13.0391L20.4531 13.0391L15.8206 17.6718C15.4147 18.0774 15.4147 18.7354 15.8206 19.1409C16.2264 19.5468 16.8844 19.5468 17.2896 19.1409L23.6956 12.7348C24.1015 12.3292 24.1015 11.6712 23.6956 11.2657L17.2896 4.85927C17.0867 4.6563 16.8209 4.55496 16.5551 4.55496C16.2893 4.55496 16.0234 4.6563 15.8206 4.85927C15.4147 5.26487 15.4147 5.92282 15.8206 6.3283L20.4531 10.9613L1.03895 10.9613C0.465234 10.9613 -1.20632e-06 11.4265 -1.25648e-06 12.0002C-1.30663e-06 12.5739 0.465174 13.0391 1.03895 13.0391Z" fill="currentColor"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// State
const verificationCode = ref(['', '', '', '', ''])
const focusedIndex = ref(-1)
const inputRefs = ref([])
const timeLeft = ref(59)
let intervalId = null

// Computed
const isCodeComplete = computed(() => {
  return verificationCode.value.every(digit => digit !== '')
})

const cardStyle = {
  background: `linear-gradient(90deg, #2019CE 20.91%, #473FFF 68.93%)`
}

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

const focusInput = (index) => {
  if (inputRefs.value[index]) {
    inputRefs.value[index].focus()
  }
}

const handleInput = (index, event) => {
  const value = event.target.value
  
  // Only allow digits
  const digit = value.replace(/[^0-9]/g, '')
  
  if (digit.length <= 1) {
    verificationCode.value[index] = digit
    
    // Move to next input if digit entered and not last input
    if (digit && index < 4) {
      nextTick(() => {
        focusInput(index + 1)
      })
    }
  }
  
  // Trigger haptic feedback
  if (window.triggerHaptic && digit) {
    window.triggerHaptic('selection')
  }
}

const handleKeydown = (index, event) => {
  // Handle backspace
  if (event.key === 'Backspace') {
    if (verificationCode.value[index] === '' && index > 0) {
      // Move to previous input if current is empty
      nextTick(() => {
        focusInput(index - 1)
      })
    } else {
      // Clear current input
      verificationCode.value[index] = ''
    }
  }
  
  // Handle arrow keys
  if (event.key === 'ArrowLeft' && index > 0) {
    focusInput(index - 1)
  }
  if (event.key === 'ArrowRight' && index < 4) {
    focusInput(index + 1)
  }
  
  // Handle Enter key
  if (event.key === 'Enter' && isCodeComplete.value) {
    handleContinue()
  }
}

const resendCode = () => {
  if (timeLeft.value === 0) {
    // Reset timer
    timeLeft.value = 59
    startTimer()
    
    // Clear existing code
    verificationCode.value = ['', '', '', '', '']
    focusInput(0)
    
    // Add haptic feedback
    if (window.triggerHaptic) {
      window.triggerHaptic('impact', 'light')
    }
    
    console.log('Resending verification code...')
  }
}

const handleContinue = () => {
  if (!isCodeComplete.value) return
  
  // Add haptic feedback
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'medium')
  }
  
  const code = verificationCode.value.join('')
  console.log('Verification code entered:', code)
  
  // Navigate to next step
  router.push('/favorites')
}

// Removed header-related functions

// Lifecycle
onMounted(() => {
  startTimer()
  
  // Auto-focus first input
  nextTick(() => {
    focusInput(0)
  })
})

onUnmounted(() => {
  if (intervalId) {
    clearInterval(intervalId)
  }
})
</script>

<style scoped>
/* Prevent zoom on input focus in iOS */
input {
  font-size: 16px;
}

@media screen and (max-width: 767px) {
  input {
    font-size: 16px !important;
  }
}

/* Remove input appearance */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type=number] {
  -moz-appearance: textfield;
}

/* Performance optimizations */
* {
  will-change: auto;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Touch optimizations */
button {
  touch-action: manipulation;
}

/* Hide input autofill background */
input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus {
  -webkit-box-shadow: 0 0 0 30px transparent inset !important;
  -webkit-text-fill-color: white !important;
}
</style>
