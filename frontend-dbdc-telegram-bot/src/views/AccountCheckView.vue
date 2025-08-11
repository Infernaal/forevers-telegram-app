<template>
  <div class="w-full min-h-screen bg-white font-montserrat overflow-hidden flex items-center justify-center">
    <!-- Main Content Container -->
    <div class="w-full flex-1 flex items-center justify-center p-3 sm:p-4 md:p-6 lg:p-8 pb-20 xs:pb-24">
      <div class="w-full min-h-[348px] xs:min-h-[380px] sm:min-h-[420px] md:min-h-[460px] lg:min-h-[500px]
                  relative rounded-2xl sm:rounded-3xl md:rounded-[2rem] lg:rounded-[2.5rem]
                  p-4 xs:p-6 sm:p-8 md:p-10 lg:p-12 mx-auto
                  text-white flex flex-col justify-between" :style="cardStyle">
        
        <!-- Question Section -->
        <div class="flex flex-col items-center text-center mb-6 xs:mb-8 sm:mb-10 md:mb-12">
          <h1 class="text-xl xs:text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold text-white leading-tight max-w-[298px]">
            Do you have an account on DBD Capital?
          </h1>
        </div>

        <!-- Form Section -->
        <div class="flex flex-col gap-4 xs:gap-6 sm:gap-8">
          <!-- Email Input -->
          <div class="relative w-full">
            <div
              class="w-full h-12 xs:h-14 sm:h-16 bg-white rounded-lg border flex items-center px-4 gap-3 transition-colors"
              :class="{
                'border-red-500': emailError,
                'border-dbd-light-gray': !emailError,
                'border-dbd-primary': isFocused && !emailError
              }"
            >
              <!-- Email Icon -->
              <svg class="w-6 h-6 xs:w-7 xs:h-7 text-dbd-gray flex-shrink-0" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M24.9709 15.5249C25.4844 15.5249 25.9006 15.1402 25.9006 14.6656V9.03695C25.9006 7.1416 24.2324 5.59961 22.1818 5.59961H5.81934C3.76882 5.59961 2.10059 7.1416 2.10059 9.03695V18.9623C2.10059 20.8576 3.76882 22.3996 5.81934 22.3996H22.1818C24.2324 22.3996 25.9006 20.8576 25.9006 18.9623C25.9006 18.4877 25.4844 18.1029 24.9709 18.1029C24.4574 18.1029 24.0412 18.4877 24.0412 18.9623C24.0412 19.9099 23.2071 20.6809 22.1818 20.6809H5.81934C4.79408 20.6809 3.95996 19.9099 3.95996 18.9623V9.21904L12.0369 13.8614C12.6425 14.2095 13.3215 14.3835 14.0006 14.3835C14.6796 14.3835 15.3587 14.2095 15.9643 13.8614L24.0412 9.21904V14.6656C24.0412 15.1402 24.4574 15.5249 24.9709 15.5249ZM14.9824 12.4018C14.3768 12.7499 13.6243 12.75 13.0187 12.4018L4.73574 7.64105C5.04105 7.43798 5.41534 7.31828 5.81934 7.31828H22.1818C22.5858 7.31828 22.9601 7.43803 23.2654 7.64109L14.9824 12.4018Z" fill="currentColor"/>
              </svg>

              <!-- Input Field -->
              <input
                v-model="email"
                type="email"
                placeholder="Email"
                @focus="handleFocus"
                @blur="handleBlur"
                @input="validateEmail"
                class="flex-1 text-sm xs:text-base text-dbd-dark placeholder-dbd-light-gray outline-none bg-transparent"
              />

              <!-- Required asterisk -->
              <span class="text-red-500 text-sm xs:text-base font-medium">*</span>
            </div>

            <!-- Error message -->
            <div v-if="emailError" class="mt-1 px-2">
              <p class="text-red-400 font-medium text-xs xs:text-sm px-2 py-1 rounded">{{ emailErrorMessage }}</p>
            </div>
          </div>

          <!-- Terms Checkbox -->
          <div class="flex justify-center">
            <TermsCheckbox
              v-model="termsAgreed"
              @open-terms="openTerms"
            />
          </div>

          <!-- Continue Button -->
          <button
            @click="handleContinue"
            :disabled="!canContinue"
            class="continue-button w-full h-12 xs:h-14 sm:h-16 rounded-full font-bold text-sm xs:text-base sm:text-lg
                   border-2 bg-transparent relative overflow-hidden
                   transition-all duration-300 ease-in-out"
            :class="{
              'continue-button--active': canContinue,
              'continue-button--disabled': !canContinue
            }"
          >
            <span class="relative z-10">Continue</span>
            <div class="absolute inset-0 bg-white/5 opacity-0 transition-opacity duration-300 ease-in-out continue-button__overlay"></div>
          </button>
        </div>
      </div>
    </div>

    <!-- Bottom Telegram Button -->
    <div
      class="fixed bottom-0 left-0 right-0 bg-white/75 backdrop-blur-sm p-4 transition-transform duration-300"
      :class="{ 'translate-y-full': keyboardVisible }"
      style="padding-bottom: calc(1rem + var(--tg-safe-area-bottom, 0px))"
    >
      <button
        @click="handleTelegramContinue"
        class="w-full mx-auto h-12 xs:h-14 sm:h-16 bg-gradient-to-r from-dbd-primary to-[#473FFF]
               text-white font-bold text-sm xs:text-base rounded-full flex items-center justify-center gap-3
               transition-all duration-200 hover:shadow-lg border-2 border-white/20 hover:border-white/40 hover:scale-[1.02]"
      >
        <span>Continue with Telegram</span>
        <img src="/telegram-icon.svg" alt="Telegram" class="w-6 h-6" />
      </button>
    </div>

    <!-- Terms and Conditions Modal -->
    <TermsAndConditionsModal
      :isVisible="showTermsModal"
      @close="closeTermsModal"
      @agree="agreeToTerms"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import TermsCheckbox from '../components/TermsCheckbox.vue'
import TermsAndConditionsModal from '../components/TermsAndConditionsModal.vue'

const router = useRouter()

// Form state
const email = ref('')
const termsAgreed = ref(false)
const emailError = ref(false)
const emailErrorMessage = ref('')
const isFocused = ref(false)
const hasBlurred = ref(false)
const keyboardVisible = ref(false)
const initialViewportHeight = ref(0)
const showTermsModal = ref(false)

// Computed
const canContinue = computed(() => {
  return email.value.trim() && termsAgreed.value && isValidEmail(email.value) && !emailError.value
})

// Methods
const isValidEmail = (emailString) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(emailString.trim())
}

const validateEmail = () => {
  const emailValue = email.value.trim()

  // Clear previous errors
  emailError.value = false
  emailErrorMessage.value = ''

  // Only validate if user has started typing and field has been blurred at least once
  if (!emailValue && hasBlurred.value) {
    emailError.value = true
    emailErrorMessage.value = 'Email is required'
    return
  }

  // Validate email format if there's content
  if (emailValue && !isValidEmail(emailValue)) {
    emailError.value = true
    emailErrorMessage.value = 'Please enter a valid email address'
    return
  }
}

const handleFocus = () => {
  isFocused.value = true
  // Detect keyboard appearance with a delay for mobile
  setTimeout(() => {
    keyboardVisible.value = true
  }, 300)
}

const handleBlur = () => {
  isFocused.value = false
  hasBlurred.value = true
  keyboardVisible.value = false
  validateEmail()
}


const openTerms = () => {
  showTermsModal.value = true
}

const closeTermsModal = () => {
  showTermsModal.value = false
}

const agreeToTerms = () => {
  termsAgreed.value = true
  showTermsModal.value = false
}

const handleContinue = () => {
  // Force validation on submit
  hasBlurred.value = true
  validateEmail()

  if (!canContinue.value) return

  // Handle email form continuation
  console.log('Continue with email:', email.value.trim())
  router.push('/favorites')
}

const handleTelegramContinue = () => {
  // Handle Telegram authentication
  console.log('Continue with Telegram')
  router.push('/favorites')
}

// Keyboard detection through viewport changes
const handleResize = () => {
  const currentHeight = window.innerHeight
  const heightDifference = initialViewportHeight.value - currentHeight

  // If viewport shrunk by more than 150px, assume keyboard is visible
  if (heightDifference > 150) {
    keyboardVisible.value = true
  } else {
    keyboardVisible.value = false
  }
}

// Lifecycle hooks
onMounted(() => {
  initialViewportHeight.value = window.innerHeight
  window.addEventListener('resize', handleResize)

  // Also listen for visual viewport changes (better for mobile)
  if (window.visualViewport) {
    window.visualViewport.addEventListener('resize', handleResize)
  }
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  if (window.visualViewport) {
    window.visualViewport.removeEventListener('resize', handleResize)
  }
})

// Computed style for the gradient card background
const cardStyle = {
  background: `
    linear-gradient(0deg, rgba(0, 0, 0, 0.25) 0%, rgba(0, 0, 0, 0.25) 100%),
    linear-gradient(90deg, #2019CE 20.91%, #473FFF 68.93%)
  `
}
</script>

<style scoped>
/* Remove input autofill background and focus outline */
input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus,
input:-webkit-autofill:active {
  -webkit-box-shadow: 0 0 0 30px white inset !important;
  -webkit-text-fill-color: #02070E !important;
}

/* Remove blue focus outline from input */
input:focus,
input:focus-visible {
  outline: none !important;
  box-shadow: none !important;
  border: none !important;
}

/* Button States */
.continue-button {
  border: 2px solid #FFFFFF !important;
  transform: scale(1);
  will-change: transform, border-color, color, background-color;
}

.continue-button--active {
  color: #FFFFFF;
  border: 2px solid #FFFFFF !important;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.continue-button--active:hover {
  background-color: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.9) !important;
  transform: scale(1.02);
}

.continue-button--active:hover .continue-button__overlay {
  opacity: 1;
}

.continue-button--disabled {
  color: rgba(255, 255, 255, 0.5) !important;
  border: 2px solid #FFFFFF !important;
  cursor: not-allowed !important;
  transform: scale(1);
}

.continue-button--disabled:hover {
  transform: none;
  background-color: transparent;
  border: 2px solid #FFFFFF !important;
}

/* Performance optimizations */
* {
  will-change: auto;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Global scrollbar hiding and Telegram optimizations */
:::-webkit-scrollbar {
  width: 0;
}

* {
  -webkit-tap-highlight-color: transparent;
  scrollbar-width: none;
  -ms-overflow-style: none;
}
</style>
