<template>
  <div class="w-full min-h-screen bg-dbd-off-white font-montserrat overflow-hidden flex flex-col">
    <!-- Main Content -->
    <div class="flex-1 flex items-center justify-center p-4 xs:p-6 sm:p-8">
      <div class="w-full max-w-[347px] xs:max-w-[380px] sm:max-w-[420px]">
        <!-- Verification Card -->
        <div
          class="w-full h-[300px] xs:h-[320px] sm:h-[340px] rounded-3xl p-5 xs:p-6 sm:p-7 flex flex-col justify-between text-white"
          :style="cardStyle"
        >
          <!-- Title -->
          <div class="text-center">
            <h1 class="text-base xs:text-lg sm:text-xl font-semibold leading-tight max-w-[280px] mx-auto">
              Please, enter your verification code in the box below
            </h1>
          </div>

          <!-- Verification Code Input -->
          <div class="flex flex-col items-center gap-3 flex-1 justify-center">
            <!-- Code Input Boxes -->
            <div class="flex justify-center gap-2 xs:gap-3 sm:gap-4">
              <div
                v-for="(digit, index) in verificationCode"
                :key="index"
                class="w-11 xs:w-12 sm:w-14 h-11 xs:h-12 sm:h-14 rounded-lg border-2 flex items-center justify-center cursor-pointer transition-all flex-shrink-0"
                :class="{
                  'border-dbd-orange bg-black': digit === '' && focusedIndex === index && !verificationError,
                  'border-green-500 bg-green-900': digit !== '' && !verificationError,
                  'border-white bg-black': digit === '' && focusedIndex !== index && !verificationError,
                  'border-red-500 bg-red-900': verificationError
                }"
                :style="{
                  backgroundColor: verificationError ? '#1F0F0F' : (digit !== '' ? '#020F03' : '#000000'),
                  borderColor: verificationError ? '#EF4444' : (digit !== '' ? '#07B80E' : (focusedIndex === index ? '#FF6800' : '#FFFFFF'))
                }"
                @click="focusInput(index)"
              >
                <input
                  :ref="el => inputRefs[index] = el"
                  v-model="verificationCode[index]"
                  @input="handleInput(index, $event)"
                  @keydown="handleKeydown(index, $event)"
                  @paste="handlePaste(index, $event)"
                  @beforeinput="handleBeforeInput(index, $event)"
                  @focus="focusedIndex = index; clearError()"
                  @blur="focusedIndex = -1"
                  type="text"
                  maxlength="1"
                  class="w-full h-full bg-transparent text-center text-white font-bold border-none outline-none"
                  inputmode="numeric"
                  pattern="[0-9]*"
                  autocomplete="one-time-code"
                  name="one-time-code"
                  autocapitalize="off"
                  autocorrect="off"
                  :style="{
                    fontSize: digit !== '' ? '22px' : '18px'
                  }"
                />
              </div>
            </div>

            <!-- Error Message -->
            <div v-if="verificationError" class="w-full max-w-[280px] xs:max-w-[300px] sm:max-w-[320px] text-center">
              <p class="text-red-400 font-medium text-xs xs:text-sm">{{ errorMessage }}</p>
            </div>

            <!-- Resend Section -->
            <div class="flex justify-between items-center w-full max-w-[280px] xs:max-w-[300px] sm:max-w-[320px] text-xs xs:text-sm">
              <button
                @click="resendCode"
                :disabled="timeLeft > 0"
                class="font-semibold underline transition-all duration-200 flex-shrink-0"
                :class="{
                  'text-dbd-orange hover:text-orange-400 cursor-pointer': timeLeft === 0,
                  'text-gray-300 cursor-not-allowed': timeLeft > 0
                }"
              >
                Resend verification code
              </button>

              <span
                v-if="timeLeft > 0"
                class="text-white font-medium flex-shrink-0 ml-2 whitespace-nowrap"
              >
                in {{ formatTime(timeLeft) }} sec
              </span>
            </div>
          </div>

          <!-- Continue Button -->
          <div class="w-full">
            <button
              @click="handleContinue"
              :disabled="!isCodeComplete || isVerifying"
              class="w-full h-11 xs:h-12 sm:h-14 rounded-full font-bold text-sm xs:text-base
                     bg-dbd-orange border border-dbd-orange text-white
                     transition-all duration-300 ease-in-out
                     flex items-center justify-center gap-2
                     hover:bg-orange-600 hover:border-orange-600 hover:shadow-lg hover:scale-[1.02]
                     active:scale-[0.98] disabled:cursor-not-allowed
                     disabled:hover:scale-100 disabled:hover:bg-dbd-orange"
              :class="{
                'opacity-50': !isCodeComplete || isVerifying
              }"
            >
              <svg v-if="isVerifying" class="animate-spin h-4 w-4 xs:h-5 xs:w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span>{{ isVerifying ? 'Verifying...' : 'Continue' }}</span>
              <svg v-if="!isVerifying" class="w-4 h-4 xs:w-5 xs:h-5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
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
import emailVerificationService from '../services/emailVerificationService.js'

const router = useRouter()

// State
const verificationCode = ref(['', '', '', '', ''])
const focusedIndex = ref(-1)
const inputRefs = ref([])
const timeLeft = ref(59)
const email = ref('')
const isLoading = ref(false)
const isVerifying = ref(false)
const verificationError = ref(false)
const errorMessage = ref('')
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

// Helper: distribute a string of digits across inputs starting from given index
const distributeDigits = (startIndex, digitsStr) => {
  const digits = (digitsStr || '').replace(/\D/g, '')
  if (!digits) return 0

  let filled = 0
  for (let idx = startIndex; idx < 5 && filled < digits.length; idx++, filled++) {
    verificationCode.value[idx] = digits[filled]
  }

  // Focus next empty input or last filled
  const nextEmptyIndex = verificationCode.value.findIndex(d => d === '')
  nextTick(() => {
    if (nextEmptyIndex !== -1) {
      focusInput(nextEmptyIndex)
    } else {
      focusInput(Math.min(startIndex + filled - 1, 4))
    }
  })

  if (window.triggerHaptic) {
    window.triggerHaptic('selection')
  }

  return filled
}

const handleInput = (index, event) => {
  const value = event.target.value || ''
  const digitsOnly = value.replace(/[^0-9]/g, '')

  // If iOS autofill or manual paste injected multiple digits via input event
  if (digitsOnly.length > 1) {
    distributeDigits(index, digitsOnly)
    return
  }

  // Single digit typing behavior (unchanged)
  const digit = digitsOnly
  if (digit.length <= 1) {
    verificationCode.value[index] = digit
    if (digit && index < 4) {
      nextTick(() => {
        focusInput(index + 1)
      })
    }
  }

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

// Distribute pasted digits across inputs starting from current index
const handlePaste = (startIndex, event) => {
  event.preventDefault()

  const clipboardData = event.clipboardData || window.clipboardData
  if (!clipboardData) return

  const raw = clipboardData.getData('text') || ''
  distributeDigits(startIndex, raw)
}

// Handle iOS OTP QuickType autofill and any multi-character replacements
const handleBeforeInput = (index, event) => {
  // Possible types: insertReplacementText (iOS QuickType), insertFromPaste, insertText
  const it = event.inputType || ''
  let data = event.data || ''

  if (!data && it === 'insertFromPaste' && event.dataTransfer) {
    data = event.dataTransfer.getData('text') || ''
  }

  const digits = (data || '').replace(/\D/g, '')
  if (digits.length > 1 || it === 'insertReplacementText') {
    // Prevent default single-cell insert limited by maxlength
    event.preventDefault()
    // Reset and distribute from first cell for full-code autofill
    verificationCode.value = ['', '', '', '', '']
    distributeDigits(0, digits || (event.target && event.target.value) || '')
  }
}

const clearError = () => {
  verificationError.value = false
  errorMessage.value = ''
}

const resendCode = async () => {
  if (timeLeft.value === 0 && !isLoading.value) {
    isLoading.value = true
    clearError()

    try {
      const result = await emailVerificationService.resendVerificationCode(email.value)
      
      if (result.success) {
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
      } else {
        verificationError.value = true
        errorMessage.value = result.error || 'Failed to resend verification code'
      }
    } catch (error) {
      console.error('Error resending verification code:', error)
      verificationError.value = true
      errorMessage.value = 'Failed to resend verification code'
    } finally {
      isLoading.value = false
    }
  }
}

const handleContinue = async () => {
  if (!isCodeComplete.value || isVerifying.value) return
  
  isVerifying.value = true
  clearError()
  
  try {
    const code = verificationCode.value.join('')
    const result = await emailVerificationService.verifyCode(email.value, code)
    
    if (result.success) {
      // Add haptic feedback
      if (window.triggerHaptic) {
        window.triggerHaptic('impact', 'medium')
      }
      
      // Navigate to next step
      router.push('/favorites')
    } else {
      // Show error
      verificationError.value = true
      errorMessage.value = result.message || 'Verification code invalid'
      
      // Add error haptic feedback
      if (window.triggerHaptic) {
        window.triggerHaptic('impact', 'heavy')
      }
    }
  } catch (error) {
    console.error('Error verifying code:', error)
    verificationError.value = true
    errorMessage.value = 'Failed to verify code. Please try again.'
    
    // Add error haptic feedback
    if (window.triggerHaptic) {
      window.triggerHaptic('impact', 'heavy')
    }
  } finally {
    isVerifying.value = false
  }
}

// Removed header-related functions

// Lifecycle
onMounted(() => {
  // Get email from sessionStorage
  const storedEmail = sessionStorage.getItem('verificationEmail')
  if (storedEmail) {
    email.value = storedEmail
  } else {
    // If no email found, redirect back to account check
    router.push('/account-check')
    return
  }
  
  startTimer()
  
  // Auto-focus first input
  nextTick(() => {
    focusInput(0)
  })

  // Capture iOS QuickType OTP autofill reliably
  const beforeInputListener = (e) => {
    const target = e.target
    if (!target) return
    const idx = inputRefs.value.findIndex(el => el === target)
    if (idx !== -1) {
      handleBeforeInput(idx, e)
    }
  }
  // store on window for removal
  window.__otpBeforeInputListener = beforeInputListener
  window.addEventListener('beforeinput', beforeInputListener, { capture: true })
})

onUnmounted(() => {
  if (intervalId) {
    clearInterval(intervalId)
  }
  if (window.__otpBeforeInputListener) {
    window.removeEventListener('beforeinput', window.__otpBeforeInputListener, { capture: true })
    delete window.__otpBeforeInputListener
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
  appearance: textfield;
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

/* Remove blue focus outline from inputs */
input:focus,
input:focus-visible,
input:active {
  outline: none !important;
  box-shadow: none !important;
  -webkit-box-shadow: none !important;
  border: none !important;
  -webkit-appearance: none !important;
  -moz-appearance: none !important;
  appearance: none !important;
}
</style>
