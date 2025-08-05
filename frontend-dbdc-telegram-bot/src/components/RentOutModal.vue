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
      class="fixed inset-0 flex items-center justify-center z-[10002] px-4"
      style="background: rgba(2, 7, 14, 0.20); backdrop-filter: blur(9px);"
      @click.self="closeModal"
    >
      <!-- Modal Content -->
      <div
        @click.stop
        class="relative bg-dbd-off-white rounded-[20px] shadow-xl font-montserrat w-full max-w-[311px] mx-auto transition-all duration-300"
      >
        <!-- Title -->
        <div class="flex justify-center items-center pt-3 pb-2">
          <h2 class="text-lg font-semibold text-dbd-dark">
            Rent Amount
          </h2>
        </div>

        <!-- Exchange Rate Section -->
        <div class="flex justify-center mb-4">
          <div class="bg-white rounded-full border border-gray-100 px-3 py-2.5 flex items-center shadow-sm w-[250px] sm:w-[270px] md:w-[290px] h-11">
            <!-- F Logo and Amount -->
            <div class="flex items-center gap-2">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M23 5.53558V1H5.34689V6.75858H1V11.2942H5.34689V22.5807H10.4206V17.0457H14.7116V12.5102H10.4206V11.2942H18.8488V6.75858H10.4206V5.53558H23Z" fill="#2019CE"/>
              </svg>
              <span class="text-dbd-primary font-bold text-xl">{{ rentAmount || '1,225' }}</span>
            </div>
            <!-- Country Flag and Name -->
            <div class="ml-auto flex items-center gap-2 md:gap-1.5">
              <CountryFlag :country="selectedBalance?.code || 'AE'" class="w-6 h-6 flex-shrink-0" />
              <span class="text-dbd-dark text-sm font-medium whitespace-nowrap">Forevers {{ selectedBalance?.code || 'UAE' }}</span>
            </div>
          </div>
        </div>

        <!-- Input Field -->
        <div class="px-4 mb-6">
          <div
            class="w-full rounded-full border-2 bg-dbd-off-white flex items-center px-4 py-3 transition-all duration-200"
            :class="[
              isInputFocused
                ? 'border-dbd-primary bg-dbd-light-blue'
                : 'border-dbd-gray'
            ]"
          >
            <!-- Forevers Icon -->
            <div
              class="w-9 h-9 rounded-full flex items-center justify-center flex-shrink-0 transition-all duration-200"
              :class="[
                isInputFocused
                  ? 'bg-dbd-primary'
                  : 'bg-dbd-light-blue'
              ]"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M22.0457 2.40039H7.50852C6.86852 2.40039 6.41138 2.85753 6.41138 3.49753V7.97753H2.29709C1.65709 8.06896 1.19995 8.52611 1.19995 9.16611C1.19995 9.80611 1.65709 10.2632 2.29709 10.2632H6.41138V20.5033C6.41138 21.1432 6.86852 21.6004 7.50852 21.6004C8.14852 21.6004 8.60567 21.1432 8.60567 20.5033V15.749H13.2685C13.9085 15.749 14.3657 15.2918 14.3657 14.6518C14.3657 14.0118 13.9085 13.5547 13.2685 13.5547H8.60567V10.1718H17.4742C18.1142 10.1718 18.5714 9.71468 18.5714 9.07468C18.5714 8.43468 18.1142 7.97753 17.4742 7.97753H8.60567V4.59468H21.9542C22.5942 4.59468 23.0514 4.13753 23.0514 3.49753C23.0514 2.85753 22.6857 2.40039 22.0457 2.40039Z"
                  :fill="isInputFocused ? '#FFFFFF' : '#02070E'"
                />
              </svg>
            </div>

            <!-- Input Content -->
            <div class="flex flex-col ml-2 flex-1">
              <span class="text-dbd-gray text-xs font-medium whitespace-nowrap">Forevers {{ selectedBalance?.code || 'UAE' }}</span>
              <input
                ref="inputField"
                v-model="inputValue"
                type="number"
                inputmode="numeric"
                class="text-base font-semibold bg-transparent border-none outline-none p-0 m-0 w-full telegram-input text-dbd-dark"
                placeholder="250"
                @input="handleInput"
                @focus="isInputFocused = true"
                @blur="isInputFocused = false"
                @keydown.enter="handleRentOut"
                @keydown.escape="closeModal"
              />
            </div>
          </div>
        </div>

        <!-- Terms Checkbox -->
        <div class="px-4 mb-6">
          <TermsCheckbox
            v-model="termsAccepted"
            @open-terms="$emit('open-terms')"
            class="terms-checkbox-dark"
          />
        </div>

        <!-- Buttons -->
        <div class="px-3 pb-6 flex items-center gap-3">
          <!-- Back Button -->
          <button
            @click="closeModal"
            class="inline-flex h-11 px-6 items-center justify-center rounded-full border border-dbd-gray bg-dbd-off-white hover:bg-gray-50 transition-colors"
          >
            <span class="text-dbd-gray text-base font-medium">Back</span>
          </button>

          <!-- Rent Out Button -->
          <button
            @click="handleRentOut"
            :disabled="!termsAccepted"
            class="flex-1 h-11 rounded-full bg-gradient-to-r from-dbd-primary to-[#473FFF] hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
          >
            <span class="text-white text-base font-bold">Rent Out</span>
          </button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, watch, nextTick } from 'vue'
import CountryFlag from './CountryFlag.vue'
import TermsCheckbox from './TermsCheckbox.vue'

const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  },
  selectedBalance: {
    type: Object,
    default: () => ({
      code: 'UAE',
      name: 'Forevers UAE Balance'
    })
  },
  rentAmount: {
    type: [String, Number],
    default: '1,225'
  },
  inputAmount: {
    type: [String, Number],
    default: '250'
  },
  termsAgreed: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['close', 'rent-out', 'open-terms'])

const inputField = ref(null)
const termsAccepted = ref(false)
const inputValue = ref(props.inputAmount || '250')
const isInputFocused = ref(false)

const handleInput = () => {
  // Convert to string first, then remove non-numeric characters
  const stringValue = String(inputValue.value || '')
  inputValue.value = stringValue.replace(/[^0-9]/g, '')
}

const handleRentOut = () => {
  if (!termsAccepted.value) {
    return
  }

  // Haptic feedback for success
  if (window.triggerHaptic) {
    window.triggerHaptic('notification', 'success')
  }

  emit('rent-out', {
    amount: inputValue.value,
    balance: props.selectedBalance,
    rentAmount: props.rentAmount
  })
  closeModal()
}

const closeModal = () => {
  // Haptic feedback for modal close
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'light')
  }

  termsAccepted.value = false
  inputValue.value = props.inputAmount || '250'
  emit('close')
}

const handleKeyDown = (event) => {
  if (event.key === 'Escape') {
    closeModal()
  } else if (event.key === 'Enter' && termsAccepted.value) {
    handleRentOut()
  }
}

watch(() => props.isVisible, async (isVisible) => {
  if (isVisible) {
    document.addEventListener('keydown', handleKeyDown)

    // Auto-focus input field for Telegram WebApp - immediate focus for keyboard
    await nextTick()
    setTimeout(() => {
      if (inputField.value) {
        inputField.value.focus()
        inputField.value.select() // Select all text for easy replacement

        // Trigger virtual keyboard on mobile
        if (window.Telegram?.WebApp?.HapticFeedback) {
          window.Telegram.WebApp.HapticFeedback.selectionChanged()
        }
      }
    }, 100) // Reduced delay for faster keyboard appearance
  } else {
    document.removeEventListener('keydown', handleKeyDown)
  }
})

// Watch for termsAgreed changes to auto-check the checkbox
watch(() => props.termsAgreed, (agreed) => {
  if (agreed) {
    termsAccepted.value = true
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
  .max-w-\[311px\] {
    max-width: calc(100vw - 24px);
  }

  /* Smaller font sizes for mobile */
  .text-lg { font-size: 16px; }
  .text-base { font-size: 14px; }
  .text-sm { font-size: 12px; }
  .text-xs { font-size: 10px; }

  /* Compact spacing for mobile */
  .px-4 { padding-left: 12px; padding-right: 12px; }
  .px-3 { padding-left: 8px; padding-right: 8px; }
  .py-2 { padding-top: 6px; padding-bottom: 6px; }
}

/* Small mobile screens */
@media (max-width: 320px) {
  .max-w-\[311px\] {
    max-width: calc(100vw - 16px);
  }

  .text-lg { font-size: 15px; }
  .text-base { font-size: 13px; }
  .text-sm { font-size: 11px; }
  .text-xs { font-size: 9px; }

  .px-4 { padding-left: 8px; padding-right: 8px; }
  .px-3 { padding-left: 6px; padding-right: 6px; }
  .gap-3 { gap: 8px; }
}

/* Telegram WebApp viewport handling */
@media (max-height: 600px) {
  .pb-6 {
    padding-bottom: 16px;
  }

  .mb-6 {
    margin-bottom: 16px;
  }
}

/* Mobile non-small screens (376px - 768px) */
@media (min-width: 376px) and (max-width: 768px) {
  .max-w-\[311px\] {
    max-width: 340px;
  }

  .text-lg { font-size: 18px; }
  .text-base { font-size: 16px; }
  .h-11 { height: 48px; }

  .sm\:w-\[270px\] {
    width: 270px !important;
  }

  /* Make TermsCheckbox smaller for mobile (not small mobile) to fit better */
  ::deep(.terms-checkbox-dark .terms-container) {
    width: 100% !important;
    max-width: calc(100% - 4px) !important;
  }

  ::deep(.terms-checkbox-dark .terms-text) {
    font-size: 14px !important;
    line-height: 20px !important;
  }

  ::deep(.terms-checkbox-dark .terms-checkbox) {
    width: 22px !important;
    height: 22px !important;
  }
}

/* Large screens */
@media (min-width: 769px) {
  .max-w-\[311px\] {
    max-width: 360px;
  }

  .text-lg { font-size: 20px; }
  .text-xl { font-size: 22px; }
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

/* Exchange rate section styling */
.bg-white {
  background: #ffffff;
  border: 1px solid #f4f4f4;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

/* Input field styling */
.border-dbd-gray {
  border-color: #4B4D50;
}

.bg-dbd-light-blue {
  background-color: #F4F3FF;
}

/* Input field styling */
input[type="number"] {
  -moz-appearance: textfield;
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input:focus {
  outline: none;
}

/* Terms and Conditions text wrapping */
.leading-relaxed {
  line-height: 1.375;
  word-wrap: break-word;
  overflow-wrap: break-word;
}

/* Override TermsCheckbox text color for light background */
:deep(.terms-checkbox-dark .terms-text) {
  color: #4B4D50 !important;
}

:deep(.terms-checkbox-dark .terms-link) {
  color: #FF6800 !important;
}

/* Responsive input adjustments */
@media (max-width: 375px) {
  .w-\[250px\] {
    width: calc(100% - 24px) !important;
    max-width: 250px !important;
  }

  .sm\:w-\[270px\] {
    width: calc(100% - 24px) !important;
    max-width: 250px !important;
  }

  .h-\[52px\] {
    height: 48px;
  }

  .w-9.h-9 {
    width: 32px;
    height: 32px;
  }

  .text-base {
    font-size: 14px;
  }

  /* Make TermsCheckbox smaller for mobile to fit better */
  ::deep(.terms-checkbox-dark .terms-container) {
    width: 100% !important;
    max-width: calc(100% - 8px) !important;
  }

  ::deep(.terms-checkbox-dark .terms-text) {
    font-size: 13px !important;
    line-height: 18px !important;
  }

  ::deep(.terms-checkbox-dark .terms-checkbox) {
    width: 20px !important;
    height: 20px !important;
  }
}
</style>
