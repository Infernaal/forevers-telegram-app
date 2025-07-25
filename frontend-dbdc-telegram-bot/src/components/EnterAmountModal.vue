<template>
  <Transition
    name="modal"
    enter-active-class="transition-all duration-300 ease-out"
    leave-active-class="transition-all duration-200 ease-in"
    enter-from-class="opacity-0 backdrop-blur-0 scale-95"
    enter-to-class="opacity-100 backdrop-blur-md scale-100"
    leave-from-class="opacity-100 backdrop-blur-md scale-100"
    leave-to-class="opacity-0 backdrop-blur-0 scale-95"
  >
    <div
      v-if="isVisible"
      class="fixed inset-0 flex items-center justify-center z-50 px-4"
      style="background: rgba(2, 7, 14, 0.20); backdrop-filter: blur(9px);"
      @click.self="closeModal"
    >
      <!-- Modal Content -->
      <div
        @click.stop
        class="relative bg-dbd-off-white rounded-[20px] shadow-xl font-montserrat w-full max-w-[340px] mx-auto transition-all duration-300"

      >
        <!-- Title -->
        <div class="flex justify-center items-center pt-4 pb-2">
          <h2 class="text-[18px] font-semibold text-dbd-dark">
            Enter Amount
          </h2>
        </div>

        <!-- Exchange Rate Section -->
        <div class="flex justify-center mb-4">
          <div class="bg-white rounded-full border border-gray-100 px-4 py-2 flex items-center shadow-sm">
            <CountryFlag :country="selectedBalance?.code" class="w-6 h-6 flex-shrink-0 mr-2" />
            <div class="flex items-center text-sm font-medium">
              <span class="text-dbd-dark">1 Forevers {{ selectedBalance?.code }}</span>
              <span class="text-dbd-gray mx-1">/</span>
              <span class="text-dbd-primary">{{ selectedBalance?.usdRate }} USD</span>
            </div>
          </div>
        </div>

        <!-- Input Field -->
        <div class="px-4 relative" :class="{ 'mb-6': !inputError, 'mb-2': inputError }">
          <div
            class="w-full rounded-full border-2 bg-dbd-off-white flex items-center px-4 py-3 transition-all duration-200"
            :class="[
              isInputFocused || inputError
                ? inputError
                  ? 'border-red-500 bg-red-50'
                  : 'border-dbd-primary bg-dbd-light-blue'
                : 'border-dbd-gray'
            ]"
          >
            <!-- Forevers Section -->
            <div class="flex items-center" style="flex: 1 1 46%; min-width: 0;">
              <div
                class="w-9 h-9 rounded-full flex items-center justify-center flex-shrink-0 transition-all duration-200"
                :class="[
                  isInputFocused && !inputError
                    ? 'bg-dbd-primary'
                    : inputError
                      ? 'bg-red-400'
                      : 'bg-dbd-light-blue'
                ]"
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M22.0457 2.40039H7.50852C6.86852 2.40039 6.41138 2.85753 6.41138 3.49753V7.97753H2.29709C1.65709 8.06896 1.19995 8.52611 1.19995 9.16611C1.19995 9.80611 1.65709 10.2632 2.29709 10.2632H6.41138V20.5033C6.41138 21.1432 6.86852 21.6004 7.50852 21.6004C8.14852 21.6004 8.60567 21.1432 8.60567 20.5033V15.749H13.2685C13.9085 15.749 14.3657 15.2918 14.3657 14.6518C14.3657 14.0118 13.9085 13.5547 13.2685 13.5547H8.60567V10.1718H17.4742C18.1142 10.1718 18.5714 9.71468 18.5714 9.07468C18.5714 8.43468 18.1142 7.97753 17.4742 7.97753H8.60567V4.59468H21.9542C22.5942 4.59468 23.0514 4.13753 23.0514 3.49753C23.0514 2.85753 22.6857 2.40039 22.0457 2.40039Z"
                    :fill="isInputFocused && !inputError ? '#FFFFFF' : inputError ? '#FFFFFF' : '#02070E'"
                  />
                </svg>
              </div>
              <div class="flex flex-col ml-2 flex-1">
                <span class="text-dbd-gray text-xs font-medium whitespace-nowrap">Forevers {{ selectedBalance?.code }}</span>
                <input
                  ref="inputField"
                  v-model="inputValue"
                  type="text"
                  inputmode="numeric"
                  class="text-base font-semibold bg-transparent border-none outline-none p-0 m-0 w-full telegram-input"
                  :class="inputError ? 'text-red-500' : 'text-dbd-dark'"
                  placeholder="250"
                  @input="handleInput"
                  @focus="isInputFocused = true"
                  @blur="isInputFocused = false"
                  @keydown.enter="handleAddToCart"
                  @keydown.escape="closeModal"
                />
              </div>
            </div>

            <!-- Exchange Icon -->
            <div class="flex-shrink-0 mx-3">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M8.00065 14.6667C4.31865 14.6667 1.33398 11.682 1.33398 8.00004C1.33398 4.31804 4.31865 1.33337 8.00065 1.33337C11.6827 1.33337 14.6673 4.31804 14.6673 8.00004C14.6673 11.682 11.6827 14.6667 8.00065 14.6667ZM8.00065 13.3334C9.41514 13.3334 10.7717 12.7715 11.7719 11.7713C12.7721 10.7711 13.334 9.41453 13.334 8.00004C13.334 6.58555 12.7721 5.229 11.7719 4.2288C10.7717 3.22861 9.41514 2.66671 8.00065 2.66671C6.58616 2.66671 5.22961 3.22861 4.22942 4.2288C3.22922 5.229 2.66732 6.58555 2.66732 8.00004C2.66732 9.41453 3.22922 10.7711 4.22942 11.7713C5.22961 12.7715 6.58616 13.3334 8.00065 13.3334ZM4.66732 8.66671L10.6673 8.66671V10H8.00065V12L4.66732 8.66671ZM8.00065 6.00004V4.00004L11.334 7.33337L5.33398 7.33337V6.00004H8.00065Z" fill="#7E7E7E"/>
              </svg>
            </div>

            <!-- Dollar Section -->
            <div class="flex items-center" style="flex: 1 1 44%; min-width: 0;">
              <div class="w-9 h-9 rounded-full bg-gray-100 flex items-center justify-center flex-shrink-0">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M11.8515 24C11.5488 24 11.2984 23.9056 11.1004 23.7167C10.9025 23.5278 10.8035 23.2889 10.8035 23V21.2C9.68559 21.0222 8.73071 20.6444 7.93886 20.0667C7.14702 19.4889 6.52984 18.7556 6.08734 17.8667C5.97089 17.6222 5.97089 17.3667 6.08734 17.1C6.20378 16.8333 6.40175 16.6444 6.68122 16.5333C6.93741 16.4222 7.19942 16.4222 7.46725 16.5333C7.73508 16.6444 7.93886 16.8222 8.0786 17.0667C8.49782 17.8222 9.04512 18.3889 9.72052 18.7667C10.3959 19.1444 11.1761 19.3333 12.0611 19.3333C13.179 19.3333 14.099 19.0667 14.821 18.5333C15.5429 18 15.9039 17.2667 15.9039 16.3333C15.9039 15.3556 15.5837 14.6 14.9432 14.0667C14.3028 13.5333 13.0975 12.9889 11.3275 12.4333C9.65065 11.9222 8.39883 11.2444 7.57205 10.4C6.74527 9.55556 6.33188 8.5 6.33188 7.23333C6.33188 6.01111 6.74527 4.98889 7.57205 4.16667C8.39883 3.34444 9.47598 2.87778 10.8035 2.76667V1C10.8035 0.711111 10.9025 0.472222 11.1004 0.283333C11.2984 0.0944446 11.5488 0 11.8515 0C12.1543 0 12.4047 0.0944446 12.6026 0.283333C12.8006 0.472222 12.8996 0.711111 12.8996 1V2.76667C13.738 2.87778 14.4891 3.12222 15.1528 3.5C15.8166 3.87778 16.3697 4.36667 16.8122 4.96667C16.9753 5.18889 17.0102 5.42778 16.917 5.68333C16.8239 5.93889 16.6376 6.12222 16.3581 6.23333C16.1019 6.34444 15.8341 6.35556 15.5546 6.26667C15.2751 6.17778 15.0422 6.01111 14.8559 5.76667C14.5298 5.36667 14.1281 5.07222 13.6507 4.88333C13.1732 4.69444 12.5968 4.6 11.9214 4.6C10.8501 4.6 10 4.83333 9.37118 5.3C8.74236 5.76667 8.42795 6.4 8.42795 7.2C8.42795 8.04444 8.77729 8.72778 9.47598 9.25C10.1747 9.77222 11.4672 10.3111 13.3537 10.8667C14.9374 11.3333 16.1077 12.0056 16.8646 12.8833C17.6215 13.7611 18 14.8667 18 16.2C18 17.6 17.5691 18.7278 16.7074 19.5833C15.8457 20.4389 14.5764 20.9889 12.8996 21.2333V23C12.8996 23.2889 12.8006 23.5278 12.6026 23.7167C12.4047 23.9056 12.1543 24 11.8515 24Z" fill="#4B4D50"/>
                </svg>
              </div>
              <div class="flex flex-col ml-2 flex-1 min-w-0">
                <span class="text-dbd-gray text-xs font-medium whitespace-nowrap">Dollars</span>
                <div class="text-sm font-semibold text-dbd-gray whitespace-nowrap overflow-hidden text-ellipsis" :title="'$' + calculatedDollars">
                  ${{ calculatedDollars }}
                </div>
              </div>
            </div>
          </div>


        </div>

        <!-- Error Notification positioned between input and buttons -->
        <div v-if="inputError && errorMessage" class="px-4 mb-6 mt-2">
          <ErrorNotification
            :is-visible="inputError && !!errorMessage"
            :message="errorMessage"
            position="modal"
          />
        </div>

        <!-- Buttons -->
        <div class="px-4 pb-6 flex items-center gap-3">
          <!-- Back Button -->
          <button
            @click="closeModal"
            class="flex-shrink-0 h-11 px-6 rounded-full border border-dbd-gray bg-dbd-off-white hover:bg-gray-50 transition-colors"
          >
            <span class="text-dbd-gray text-base font-medium">Back</span>
          </button>

          <!-- Add to Cart Button -->
          <button
            @click="handleAddToCart"
            :disabled="!inputValue || inputError"
            class="flex-1 h-11 rounded-full bg-gradient-to-r from-dbd-primary to-[#473FFF] hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
          >
            <span class="text-white text-lg font-bold">Add to Cart</span>
          </button>
        </div>
      </div>
    </div>
  </Transition>

  <!-- Error Notification -->
  <ErrorNotification
    :is-visible="showError"
    :message="errorMessage"
    @close="hideError"
  />
</template>

<script setup>
import { ref, computed, watch, nextTick } from 'vue'
import CountryFlag from './CountryFlag.vue'
import ErrorNotification from './ErrorNotification.vue'

const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  },
  selectedBalance: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['close', 'add-to-cart'])

const inputField = ref(null)
const inputValue = ref('')
const inputError = ref(false)
const showError = ref(false)
const errorMessage = ref('')
const isInputFocused = ref(false)
let errorTimeout = null

const calculatedDollars = computed(() => {
  if (!inputValue.value || !props.selectedBalance?.usdRate) {
    return '1,000.00'
  }
  const amount = parseFloat(inputValue.value) * props.selectedBalance.usdRate

  // Format large amounts with K suffix
  if (amount >= 100000) {
    return (amount / 1000).toLocaleString('en-US', { minimumFractionDigits: 0, maximumFractionDigits: 1 }) + 'K'
  } else if (amount >= 10000) {
    return (amount / 1000).toLocaleString('en-US', { minimumFractionDigits: 1, maximumFractionDigits: 1 }) + 'K'
  }

  return amount.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })
})

const handleInput = (event) => {
  // Haptic feedback for input
  if (window.triggerHaptic) {
    window.triggerHaptic('selection')
  }

  // Filter out non-numeric characters in real-time
  const value = event.target.value
  const numericValue = value.replace(/[^0-9]/g, '')

  if (value !== numericValue) {
    event.target.value = numericValue
    inputValue.value = numericValue
  }

  // Reset error state for real-time validation
  inputError.value = false
  errorMessage.value = ''

  // Validate input
  if (numericValue === '') {
    // Empty input is allowed
    return
  }

  const amount = parseFloat(numericValue)

  if (isNaN(amount) || amount <= 0) {
    inputError.value = true
    return
  }

  // Check if amount exceeds available balance
  const availableText = props.selectedBalance?.availableText
  const availableAmount = props.selectedBalance?.availableAmount
  let maxAllowed

  console.log('Validation check:', { availableText, availableAmount, amount })

  // Check if it's "without restrictions" or unlimited
  if (availableText && availableText.includes('without restrictions')) {
    maxAllowed = 50000 // 50k limit for unrestricted items
  } else if (availableAmount && !isNaN(Number(availableAmount))) {
    maxAllowed = Number(availableAmount) // Use actual available amount
  } else {
    maxAllowed = 50000 // Default to 50k if unclear
  }

  console.log('Max allowed:', maxAllowed)

  if (amount > maxAllowed) {
    inputError.value = true
    errorMessage.value = maxAllowed === 50000
      ? `Maximum amount allowed is ${maxAllowed.toLocaleString()}`
      : `Amount cannot exceed available balance (${maxAllowed.toLocaleString()})`
    return
  } else {
    errorMessage.value = ''
  }
}

const handleAddToCart = () => {
  if (!inputValue.value) {
    inputError.value = true
    errorMessage.value = 'Please enter an amount'
    return
  }

  const amount = parseFloat(inputValue.value)

  if (isNaN(amount) || amount <= 0) {
    inputError.value = true
    errorMessage.value = 'Please enter a valid positive amount'
    return
  }

  // Check available balance
  const availableText = props.selectedBalance?.availableText
  const availableAmount = props.selectedBalance?.availableAmount
  let maxAllowed

  console.log('handleAddToCart validation:', { availableText, availableAmount, amount })

  // Check if it's "without restrictions" or unlimited
  if (availableText && availableText.includes('without restrictions')) {
    maxAllowed = 50000 // 50k limit for unrestricted items
  } else if (availableAmount && !isNaN(Number(availableAmount))) {
    maxAllowed = Number(availableAmount) // Use actual available amount
  } else {
    maxAllowed = 50000 // Default to 50k if unclear
  }

  console.log('handleAddToCart maxAllowed:', maxAllowed)

  if (amount > maxAllowed) {
    inputError.value = true
    errorMessage.value = maxAllowed === 50000
      ? `Maximum amount allowed is ${maxAllowed.toLocaleString()}`
      : `Amount cannot exceed available balance (${maxAllowed.toLocaleString()})`
    return
  }

  if (inputError.value) {
    return
  }

  // Haptic feedback for success
  if (window.triggerHaptic) {
    window.triggerHaptic('notification', 'success')
  }

  emit('add-to-cart', {
    amount: amount,
    balance: props.selectedBalance
  })
  closeModal()
}

const showErrorMessage = (message) => {
  if (window.triggerHaptic) {
    window.triggerHaptic('notification', 'error')
  }

  errorMessage.value = message
  showError.value = true

  if (errorTimeout) {
    clearTimeout(errorTimeout)
  }

  errorTimeout = setTimeout(() => {
    showError.value = false
  }, 3000)
}

const hideError = () => {
  showError.value = false
  if (errorTimeout) {
    clearTimeout(errorTimeout)
  }
}

const closeModal = () => {
  // Haptic feedback for modal close
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'light')
  }

  inputValue.value = ''
  inputError.value = false
  errorMessage.value = ''
  isInputFocused.value = false
  hideError()
  emit('close')
}

const handleKeyDown = (event) => {
  if (event.key === 'Escape') {
    closeModal()
  }
}

watch(() => props.isVisible, async (isVisible) => {
  if (isVisible) {
    document.addEventListener('keydown', handleKeyDown)
    document.body.style.overflow = 'hidden'
    
    // Set default value
    inputValue.value = '250'
    
    // Focus input field after modal is rendered
    await nextTick()
    setTimeout(() => {
      if (inputField.value) {
        inputField.value.focus()
        inputField.value.select()
      }
    }, 100)
  } else {
    document.removeEventListener('keydown', handleKeyDown)
    document.body.style.overflow = ''
  }
})
</script>

<style scoped>
/* Enhanced modal styling */
.shadow-xl {
  box-shadow: 0 10px 25px -3px rgba(2, 7, 14, 0.12), 0 4px 6px -2px rgba(2, 7, 14, 0.05);
}

/* Modal animations */
.modal-enter-active,
.modal-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
  transform: scale(0.95) translateY(10px);
}

/* Telegram WebApp optimized input */
.telegram-input {
  font-size: 16px !important; /* Prevents zoom on iOS */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-user-select: text;
  user-select: text;
}

.telegram-input::-webkit-outer-spin-button,
.telegram-input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.telegram-input:focus {
  outline: none;
  border: none;
  background: transparent;
}

/* Enhanced button interactions */
button {
  touch-action: manipulation;
  -webkit-user-select: none;
  user-select: none;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

button:active {
  transform: scale(0.97);
}

/* Telegram specific improvements */
@media (hover: none) {
  button:hover {
    opacity: 1 !important;
    background: inherit !important;
  }

  button:active {
    transform: scale(0.95);
    opacity: 0.85;
  }
}

/* Input container focus state animation */
.border-dbd-primary {
  animation: pulseBlue 2s infinite;
}

@keyframes pulseBlue {
  0%, 100% {
    border-color: #2019CE;
    box-shadow: 0 0 0 0 rgba(32, 25, 206, 0.4);
  }
  50% {
    border-color: #2019CE;
    box-shadow: 0 0 0 4px rgba(32, 25, 206, 0.1);
  }
}

/* Error state animation */
.border-red-400 {
  animation: shakeError 0.5s cubic-bezier(0.36, 0.07, 0.19, 0.97);
}

@keyframes shakeError {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-2px); }
  20%, 40%, 60%, 80% { transform: translateX(2px); }
}

/* Clean typography */
* {
  -webkit-tap-highlight-color: transparent;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  user-select: none;
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-feature-settings: 'kern' 1;
  text-rendering: optimizeLegibility;
}

/* Telegram WebApp specific optimizations */
@media (max-width: 375px) {
  .max-w-\[340px\] {
    max-width: calc(100vw - 24px);
  }

  /* Smaller font sizes for mobile */
  .text-lg { font-size: 16px; }
  .text-base { font-size: 14px; }
  .text-sm { font-size: 12px; }
  .text-xs { font-size: 10px; }

  /* Compact spacing for mobile */
  .px-4 { padding-left: 12px; padding-right: 12px; }
  .py-3 { padding-top: 8px; padding-bottom: 8px; }
}

/* Telegram WebApp viewport handling */
@media (max-height: 600px) {
  .min-h-\[300px\] {
    min-height: 280px;
  }

  .pb-6 {
    padding-bottom: 16px;
  }
}

/* Better number formatting display */
.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* Telegram theme compatibility */
@media (prefers-color-scheme: dark) {
  .bg-dbd-off-white {
    background-color: #1e1e1e;
  }

  .text-dbd-dark {
    color: #ffffff;
  }

  .border-gray-100 {
    border-color: #2a2a2a;
  }
}

/* Smooth backdrop */
.backdrop-blur-sm {
  backdrop-filter: blur(9px);
  -webkit-backdrop-filter: blur(9px);
}

.backdrop-blur-md {
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

/* Perfect circles for icons */
.w-9.h-9 {
  width: 36px;
  height: 36px;
  min-width: 36px;
  min-height: 36px;
}

/* Button gradient enhancement */
.bg-gradient-to-r {
  background: linear-gradient(90deg, #2019CE 0%, #473FFF 100%);
  box-shadow: 0 4px 12px rgba(32, 25, 206, 0.25);
}

.bg-gradient-to-r:hover:not(:disabled) {
  box-shadow: 0 6px 16px rgba(32, 25, 206, 0.35);
}

.bg-gradient-to-r:disabled {
  opacity: 0.5;
  box-shadow: none;
}
</style>
