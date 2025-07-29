<template>
  <div class="h-screen bg-gray-100 flex flex-col font-sans overflow-hidden">
    <!-- Main Content -->
    <template>
  <div class="h-screen bg-gray-100 flex flex-col font-sans overflow-hidden">
    <!-- Main Content -->
    <main class="flex-1 w-full max-w-md lg:max-w-6xl xl:max-w-7xl mx-auto px-4 sm:px-6 md:px-8 lg:px-12 xl:px-16 pt-4 sm:pt-6 md:pt-8 lg:pt-10 xl:pt-12 pb-4 sm:pb-6 md:pb-8 lg:pb-10 xl:pb-12 flex flex-col">

      <!-- Total Balance Card -->
      <div class="bg-purple-50 border border-purple-200 rounded-2xl p-4 sm:p-6 md:p-8 lg:p-10 xl:p-12 mb-6 flex-shrink-0">
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 mb-6">
          <h2 class="text-2xl md:text-3xl lg:text-4xl xl:text-5xl font-semibold text-black leading-snug">
            Forevers<br>Balance
          </h2>

          <div class="flex flex-col items-end gap-2">
            <div class="flex items-center gap-3">
              <svg width="32" height="32" viewBox="0 0 32 32" class="text-blue-700 w-8 h-8 md:w-10 md:h-10 lg:w-12 lg:h-12">
                <path d="M30.667 7.381V1.333H7.129V9.011H1.333V15.059H7.129V30.108H13.894V22.728H19.615V16.680H13.894V15.059H25.132V9.011H13.894V7.381H30.667Z" fill="currentColor"/>
              </svg>
              <span class="text-xl md:text-2xl lg:text-3xl font-bold text-blue-700">
                {{ totalBalance.toLocaleString() }}
              </span>
            </div>
            <p class="text-base md:text-lg lg:text-xl text-gray-600 font-medium">
              Worth ${{ totalWorth.toLocaleString() }}
            </p>
          </div>
        </div>

        <button
          @click="handleRentOut"
          class="w-full bg-gradient-to-r from-blue-700 to-purple-600 text-white font-bold py-3 px-6 md:py-4 md:px-10 lg:py-5 lg:px-12 xl:py-6 xl:px-16 rounded-full hover:from-blue-800 hover:to-purple-700 transition-all duration-200 text-sm md:text-base lg:text-lg xl:text-xl">
          Rent Out Forevers
        </button>
      </div>

      <!-- Scroll Content or Empty State -->
      <div class="flex-1 overflow-y-auto" v-if="balances.length > 0">
        <!-- Balance Cards and other content here... -->
      </div>
      <div v-else class="flex-1 flex items-center justify-center">
        <div class="text-center">
          <div class="w-16 h-16 md:w-24 md:h-24 lg:w-32 lg:h-32 bg-gray-200 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg width="32" height="32" viewBox="0 0 32 32" class="text-gray-400 w-8 h-8 md:w-12 md:h-12 lg:w-16 lg:h-16">
              <path d="M30.667 7.381V1.333H7.129V9.011H1.333V15.059H7.129V30.108H13.894V22.728H19.615V16.680H13.894V15.059H25.132V9.011H13.894V7.381H30.667Z" fill="currentColor"/>
            </svg>
          </div>
          <h3 class="text-base md:text-xl lg:text-2xl font-medium text-gray-900 mb-2">
            No Balances Found
          </h3>
          <p class="text-gray-600 text-sm md:text-base lg:text-lg">
            Your balance data will appear here when available.
          </p>
        </div>
      </div>
    </main>

    <!-- Success Notification -->
    <SuccessNotification
      :is-visible="showSuccessNotification"
      :class="{ 'blur-notification': isAnyModalOpen }"
      :message="successMessage"
      @close="hideSuccessNotification"
    />

    <!-- Error Notification -->
    <ErrorNotification
      :is-visible="showErrorNotification"
      :message="errorMessage"
      @close="hideErrorNotification"
    />

    <!-- Info Tooltip -->
    <InfoTooltip
      :is-visible="showInfoTooltip"
      title="Forevers Balance"
      description="Dubadu Forevers ads you own. You invest and own your own advertising billboard on dubadu.com, and we rent it out."
      @close="showInfoTooltip = false"
    />

    <!-- Bottom Navigation -->
    <BottomNavigation />

    <!-- Enter Amount Modal -->
    <EnterAmountModal
      :is-visible="showEnterAmountModal"
      :selected-balance="selectedBalance"
      @close="closeEnterAmountModal"
      @add-to-cart="handleAddToCart"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import BottomNavigation from '../components/BottomNavigation.vue'
import CountryFlag from '../components/CountryFlag.vue'
import SuccessNotification from '../components/SuccessNotification.vue'
import ErrorNotification from '../components/ErrorNotification.vue'
import InfoTooltip from '../components/InfoTooltip.vue'
import EnterAmountModal from '../components/EnterAmountModal.vue'
import { useCart } from '../composables/useCart.js'

const router = useRouter()

// App state
const isLoading = ref(false)
const showEnterAmountModal = ref(false)
const selectedBalance = ref(null)
const foreversAmount = ref(250)
const amountInput = ref(null)
const inputError = ref('')
const isInputFocused = ref(false)
let validationTimeout = null

// Cart functionality
const { addToCart, isAddingToCart } = useCart()

// Success notification
const showSuccessNotification = ref(false)
const successMessage = ref('')
let successTimeout = null

// Error notification
const showErrorNotification = ref(false)
const errorMessage = ref('')
let errorTimeout = null

// Info tooltip state
const showInfoTooltip = ref(false)

// Check if any modal is open for blur effect
const isAnyModalOpen = computed(() => {
  return showEnterAmountModal.value || showInfoTooltip.value
})
const dollarsAmount = computed(() => {
  if (!selectedBalance.value) return 1000
  return foreversAmount.value * selectedBalance.value.usdRate
})

// Data - Ready for backend integration
const totalBalance = ref(10196)
const totalWorth = ref(56000)
const balances = ref([]) // Will be populated from backend

// Flag classes are now handled by CountryFlag component

// Mock data for development (remove when connecting to backend)
const mockBalances = [
  {
    id: 'de',
    country: 'Forevers DE',
    code: 'DE',
    amount: 1000,
    usdRate: 4,
    priceChange: 0.17,
    currentValue: 4000,
    potentialWorth: 8000,
    availableAmount: 250
  },
  {
    id: 'uae',
    country: 'Forevers UAE',
    code: 'UAE',
    amount: 1000,
    usdRate: 9,
    priceChange: 0.17,
    currentValue: 4000,
    potentialWorth: 8000,
    availableAmount: null
  },
  {
    id: 'kz',
    country: 'Forevers KZ',
    code: 'KZ',
    amount: 1000,
    usdRate: 8,
    priceChange: -0.17,
    currentValue: 4000,
    potentialWorth: 8000,
    availableAmount: 250
  },
  {
    id: 'pl',
    country: 'Forevers PL',
    code: 'PL',
    amount: 1000,
    usdRate: 4,
    priceChange: -0.17,
    currentValue: 4000,
    potentialWorth: 8000,
    availableAmount: 250
  },
  {
    id: 'ua',
    country: 'Forevers UA',
    code: 'UA',
    amount: 1000,
    usdRate: 4,
    priceChange: -0.17,
    currentValue: 4000,
    potentialWorth: 8000,
    availableAmount: 250
  },
  {
    id: 'us',
    country: 'Forevers US',
    code: 'US',
    amount: 1000,
    usdRate: 4,
    priceChange: -0.17,
    currentValue: 4000,
    potentialWorth: 8000,
    availableAmount: 250
  }
]

// Backend integration functions
const fetchBalancesFromBackend = async () => {
  isLoading.value = true
  try {
    // TODO: Replace with actual API call to Python backend
    // const response = await fetch('/api/balances')
    // const data = await response.json()

    // For now, use mock data
    setTimeout(() => {
      balances.value = mockBalances
      isLoading.value = false
    }, 1000)

  } catch (error) {
    console.error('Failed to fetch balances:', error)
    isLoading.value = false
  }
}

const fetchTotalBalance = async () => {
  try {
    // TODO: Replace with actual API call to Python backend
    // const response = await fetch('/api/total-balance')
    // const data = await response.json()
    // totalBalance.value = data.balance
    // totalWorth.value = data.worth

    // For now, use mock data
    totalBalance.value = 10196
    totalWorth.value = 56000
  } catch (error) {
    console.error('Failed to fetch total balance:', error)
  }
}

// Methods
const handleRentOut = () => {
  router.push('/rent-out')
}

const openEnterAmountModal = (balance) => {
  selectedBalance.value = balance
  showEnterAmountModal.value = true
}

const closeEnterAmountModal = () => {
  showEnterAmountModal.value = false
  selectedBalance.value = null
  foreversAmount.value = 250
  inputError.value = ''
  isInputFocused.value = false

  // Clear validation timeout
  if (validationTimeout) {
    clearTimeout(validationTimeout)
    validationTimeout = null
  }

  // Remove keyboard listener
  document.removeEventListener('keydown', handleKeydown)
}

const handleKeydown = (event) => {
  if (event.key === 'Escape') {
    closeEnterAmountModal()
  } else if (event.key === 'Enter') {
    handleAddToCart()
  }
}

const handleInputFocus = () => {
  isInputFocused.value = true
}

const handleInputBlur = () => {
  isInputFocused.value = false
  validateInput()
}

const handleInputChange = (event) => {
  // Filter out non-numeric characters in real-time
  const value = event.target.value
  const numericValue = value.replace(/[^0-9]/g, '')

  // Update the input value to only contain numbers
  if (value !== numericValue) {
    event.target.value = numericValue
    foreversAmount.value = numericValue
  }

  // Clear error when user starts typing
  if (inputError.value) {
    inputError.value = ''
  }

  // Clear previous timeout
  if (validationTimeout) {
    clearTimeout(validationTimeout)
  }

  // Validate input with debounce (only if user stops typing)
  validationTimeout = setTimeout(() => {
    if (numericValue) { // Only validate if there's content
      validateInput()
    }
  }, 800)
}

const getErrorTitle = () => {
  switch (inputError.value) {
    case 'empty':
      return "Can't be empty"
    case 'invalid':
      return "Can't be use"
    case 'limit':
      return "Can't be use"
    default:
      return "Error"
  }
}

const getErrorMessage = () => {
  switch (inputError.value) {
    case 'empty':
      return "Please, enter your amount"
    case 'invalid':
      return "Only numbers are allowed"
    case 'limit':
      return `Please enter the amount according to your limit (max: ${selectedBalance.value?.availableAmount})`
    case 'failed':
      return "Failed to add to cart. Please try again."
    default:
      return "Please check your input"
  }
}

const hideSuccessNotification = () => {
  showSuccessNotification.value = false
  if (successTimeout) {
    clearTimeout(successTimeout)
    successTimeout = null
  }
}

const hideErrorNotification = () => {
  showErrorNotification.value = false
  if (errorTimeout) {
    clearTimeout(errorTimeout)
    errorTimeout = null
  }
}

const validateInput = () => {
  // Clear previous errors
  inputError.value = ''

  // Convert to string to check for text
  const inputValue = String(foreversAmount.value).trim()

  // Check for empty value
  if (!inputValue || inputValue === '' || inputValue === '0') {
    inputError.value = 'empty'
    return false
  }

  // Check for non-numeric characters (including decimal points, special characters)
  if (!/^[0-9]+$/.test(inputValue)) {
    inputError.value = 'invalid'
    return false
  }

  // Convert to number for further validation
  const numValue = Number(inputValue)

  // Check if conversion to number is valid
  if (isNaN(numValue) || !isFinite(numValue)) {
    inputError.value = 'invalid'
    return false
  }

  // Check minimum value
  if (numValue < 1) {
    inputError.value = 'invalid'
    return false
  }

  // Check maximum value (available amount) - strict validation
  if (selectedBalance.value?.availableAmount && numValue > selectedBalance.value.availableAmount) {
    inputError.value = 'limit'
    // Force the value back to the maximum allowed
    foreversAmount.value = selectedBalance.value.availableAmount
    return false
  }

  // Update the reactive value with the validated number
  foreversAmount.value = numValue

  return true
}

const handleAddToCart = async (data) => {
  try {
    // Add to cart using the cart store
    const cartItem = {
      balance: data.balance,
      foreversAmount: data.amount,
    }

    const success = await addToCart(cartItem)

    if (success) {
      // Show success notification
      showSuccessNotification.value = true
      successMessage.value = 'Forevers added successfully'

      // Hide notification after 3 seconds
      if (successTimeout) {
        clearTimeout(successTimeout)
      }
      successTimeout = setTimeout(() => {
        showSuccessNotification.value = false
      }, 3000)

      console.log('Successfully added to cart!')
    } else {
      throw new Error('Failed to add to cart')
    }
  } catch (error) {
    console.error('Failed to add to cart:', error)

    // Show error notification
    showErrorNotification.value = true
    errorMessage.value = 'Failed to add to cart. Please try again.'

    // Hide notification after 3 seconds
    if (errorTimeout) {
      clearTimeout(errorTimeout)
    }
    errorTimeout = setTimeout(() => {
      showErrorNotification.value = false
    }, 3000)
  }
}

// Initialize
onMounted(async () => {
  // Fetch data from backend
  await Promise.all([
    fetchBalancesFromBackend(),
    fetchTotalBalance()
  ])
})

// Cleanup
onBeforeUnmount(() => {
  // Remove any remaining keyboard listeners
  document.removeEventListener('keydown', handleKeydown)

  // Clear success notification timeout
  if (successTimeout) {
    clearTimeout(successTimeout)
    successTimeout = null
  }

  // Clear error notification timeout
  if (errorTimeout) {
    clearTimeout(errorTimeout)
    errorTimeout = null
  }
})
</script>

<style scoped>
/* Blur effect for SuccessNotification when modal is open */
.blur-notification {
  filter: blur(4px);
  opacity: 0.6;
  transition: all 0.3s ease;
  pointer-events: none;
}

/* Basic styling for Telegram mini app */
* {
  -webkit-tap-highlight-color: transparent;
}

/* Hide scrollbar completely */
::-webkit-scrollbar {
  width: 0px;
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: transparent;
}

/* Hide scrollbar in Firefox */
.overflow-y-auto {
  scrollbar-width: none;
  -ms-overflow-style: none;
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
  overscroll-behavior: contain;
  will-change: scroll-position;
  overscroll-behavior-x: none;
}

/* Ensure main container takes full height properly */
main {
  min-height: calc(100vh - env(safe-area-inset-top, 0px));
  box-sizing: border-box;
  height: calc(100vh - 89px);
}

/* Better touch targets and interaction */
.balance-card {
  touch-action: manipulation;
  user-select: none;
  -webkit-user-select: none;
  padding: 12px;
  min-height: 180px;
}

/* Modal styles */
.modal-backdrop {
  backdrop-filter: blur(9px);
}

.modal-content input {
  min-height: 20px;
  padding: 2px 0;
  background: transparent;
  border: none;
  outline: none;
}

.modal-content input:focus {
  outline: none;
  background: transparent;
}

/* Remove input number arrows on mobile */
.modal-content input[type="number"] {
  -webkit-appearance: none;
  -moz-appearance: textfield;
}

.modal-content input[type="number"]::-webkit-outer-spin-button,
.modal-content input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Animation for modal */
.modal-enter-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.modal-leave-active {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.6, 1);
}

.modal-enter-from {
  opacity: 0;
  transform: scale(0.9) translateY(20px);
}

.modal-leave-to {
  opacity: 0;
  transform: scale(0.95) translateY(-10px);
}

/* Ensure modal stays above everything */
.modal-overlay {
  z-index: 9999;
}

/* Error message animations */
.error-message-enter-active,
.error-message-leave-active {
  transition: all 0.3s ease-out;
}

.error-message-enter-from {
  opacity: 0;
  transform: translateY(-10px) scale(0.95);
}

.error-message-leave-to {
  opacity: 0;
  transform: translateY(-5px) scale(0.98);
}

/* Cart badge animations */
.cart-badge-enter-active,
.cart-badge-leave-active {
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.cart-badge-enter-from {
  opacity: 0;
  transform: scale(0);
}

.cart-badge-leave-to {
  opacity: 0;
  transform: scale(0);
}

/* Input field states */
.input-focused {
  border-color: #2019CE !important;
  box-shadow: 0 0 0 2px rgba(32, 25, 206, 0.1);
}

.input-error {
  border-color: #FF1919 !important;
  box-shadow: 0 0 0 2px rgba(255, 25, 25, 0.1);
}

/* Optimize for mobile WebKit rendering */
@supports (-webkit-touch-callout: none) {
  .overflow-y-auto {
    -webkit-overflow-scrolling: touch;
    overscroll-behavior: contain;
  }

  main {
    -webkit-text-size-adjust: 100%;
  }
}
</style>
