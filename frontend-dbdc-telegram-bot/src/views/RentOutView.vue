<template>
  <div class="w-full min-h-screen bg-gray-100 font-montserrat overflow-x-hidden flex flex-col">
    <!-- Header Section -->
    <div class="w-full px-4 pt-6 pb-3 bg-gray-100 z-30">
      <div class="mb-2">
        <div class="bg-dbd-light-blue border border-purple-200 rounded-2xl p-4">
          <div class="flex items-center justify-between">
            <div>
              <h2 class="text-2xl font-semibold text-dbd-dark leading-tight mb-1">
                Forevers<br />Available
              </h2>
            </div>
            <div class="flex items-center gap-3">
              <svg class="text-dbd-primary w-9 h-9" viewBox="0 0 32 32">
                <path d="M30.6666 7.38069V1.33325H7.1291V9.01136H1.33325V15.0588H7.1291V30.1075H13.894V22.7276H19.6153V16.6801H13.894V15.0588H25.1316V9.01136H13.894V7.38069H30.6666Z" fill="currentColor"/>
              </svg>
              <span class="text-4xl font-bold text-dbd-primary">2,225</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Scrollable Cards -->
    <div class="flex-1 w-full overflow-y-auto px-4 pb-32">
      <div class="space-y-4">
        <div
          v-for="item in foreversList"
          :key="item.id"
          class="bg-dbd-off-white border border-purple-200 rounded-2xl p-3"
        >
          <!-- Header -->
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center gap-3">
              <CountryFlag :country="item.code" class="w-6 h-6" />
              <span class="text-dbd-gray text-base font-medium">{{ item.title }}</span>
            </div>
            <button
              @click="openRentModal(item)"
              :disabled="item.availableAmount === 0"
              :class="item.availableAmount === 0
                ? 'bg-gray-400 text-gray-600 cursor-not-allowed'
                : 'bg-dbd-orange text-white hover:bg-orange-600'"
              class="px-3 py-2 rounded-full text-sm font-bold transition-colors"
            >
              Loyality
            </button>
          </div>

          <!-- Exchange Rate -->
          <div class="flex items-center gap-1 mb-3">
            <span class="text-dbd-gray text-sm">1</span>
            <svg class="text-dbd-gray w-4 h-4" viewBox="0 0 16 16">
              <path d="M15.2636 2H4.61925C4.15063 2 3.8159 2.28571 3.8159 2.68571V5.48571H0.803347C0.334728 5.54286 0 5.82857 0 6.22857C0 6.62857 0.334728 6.91429 0.803347 6.91429H3.8159V13.3143C3.8159 13.7143 4.15063 14 4.61925 14C5.08787 14 5.42259 13.7143 5.42259 13.3143V10.3429H8.83682C9.30544 10.3429 9.64017 10.0571 9.64017 9.65714C9.64017 9.25714 9.30544 8.97143 8.83682 8.97143H5.42259V6.85714H11.9163C12.3849 6.85714 12.7197 6.57143 12.7197 6.17143C12.7197 5.77143 12.3849 5.48571 11.9163 5.48571H5.42259V3.37143H15.1967C15.6653 3.37143 16 3.08571 16 2.68571C16 2.28571 15.7322 2 15.2636 2Z" fill="currentColor"/>
            </svg>
            <span class="text-dbd-gray text-sm">{{ item.code }} / {{ item.usdRate }} USD</span>
            <div
              class="flex items-center gap-1 px-2 py-0.5 rounded font-semibold text-xs"
              :class="item.priceChange >= 0 ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'"
            >
              <svg class="w-2 h-2" :class="item.priceChange >= 0 ? '-rotate-45' : 'rotate-45'" viewBox="0 0 10 13">
                <path d="M0.720539 4.9362L4.6673 1.01033M4.6673 1.01033L8.58641 4.92944M4.6673 1.01033L4.65686 12.3136"
                      :stroke="item.priceChange >= 0 ? '#07B80E' : '#FF1919'"
                      stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              {{ item.priceChange >= 0 ? '+' : '' }}{{ item.priceChange }}%
            </div>
          </div>

          <!-- Values Section -->
          <div class="bg-dbd-light-blue rounded-xl p-3 mb-3">
            <div class="flex justify-between mb-2">
              <span class="text-sm text-dbd-gray">Rental cost per 1 Forevers</span>
              <span class="text-base font-semibold text-dbd-gray">${{ item.rentalCost }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-sm text-dbd-gray">Potential income per month</span>
              <span class="text-base font-semibold text-dbd-gray">${{ item.potentialIncome }}</span>
            </div>
          </div>

          <!-- Available Section -->
          <div class="bg-green-100 rounded-xl p-3 flex items-center justify-between">
            <div class="flex items-center gap-1">
              <span class="text-sm text-gray-600">{{ item.availableText }}</span>
              <span class="w-1.5 h-1.5 bg-gray-400 rounded-full"></span>
              <div class="flex items-center gap-1">
                <svg class="text-dbd-dark w-4 h-4" viewBox="0 0 14 14">
                  <path d="M12.8602 1.40015H4.3802C4.00686 1.40015 3.7402 1.66681 3.7402 2.04015V4.65348H1.3402C0.966862 4.70681 0.700195 4.97348 0.700195 5.34681C0.700195 5.72015 0.966862 5.98681 1.3402 5.98681H3.7402V11.9601C3.7402 12.3335 4.00686 12.6001 4.3802 12.6001C4.75353 12.6001 5.0202 12.3335 5.0202 11.9601V9.18681H7.7402C8.11353 9.18681 8.3802 8.92015 8.3802 8.54681C8.3802 8.17348 8.11353 7.90681 7.7402 7.90681H5.0202V5.93348H10.1935C10.5669 5.93348 10.8335 5.66681 10.8335 5.29348C10.8335 4.92015 10.5669 4.65348 10.1935 4.65348H5.0202V2.68015H12.8069C13.1802 2.68015 13.4469 2.41348 13.4469 2.04015C13.4469 1.66681 13.2335 1.40015 12.8602 1.40015Z" fill="currentColor"/>
                </svg>
                <span class="text-sm font-medium text-dbd-dark">{{ item.availableAmount }}</span>
              </div>
            </div>

            <button
              @click="showInfoTooltip = true"
              class="w-6 h-6 border border-gray-300 bg-white rounded-full flex items-center justify-center hover:bg-gray-50 transition-colors"
            >
              <svg class="text-dbd-gray w-5 h-5" viewBox="0 0 20 20">
                <path d="M10 2C5.5888 2 2 5.58885 2 10C2 14.4112 5.5888 18 10 18C14.4112 18 18 14.4112 18 10C18 5.58885 14.4112 2 10 2ZM10 16.5455C6.39079 16.5455 3.45455 13.6092 3.45455 10C3.45455 6.39088 6.39079 3.45455 10 3.45455C13.6092 3.45455 16.5455 6.39088 16.5455 10C16.5455 13.6092 13.6092 16.5455 10 16.5455Z" fill="currentColor"/>
                <path d="M10 5.39453C9.46543 5.39453 9.03052 5.82973 9.03052 6.36466C9.03052 6.89911 9.46543 7.33393 10 7.33393C10.5346 7.33393 10.9695 6.89911 10.9695 6.36466C10.9695 5.82973 10.5346 5.39453 10 5.39453Z" fill="currentColor"/>
                <path d="M9.99998 8.78711C9.59833 8.78711 9.27271 9.11273 9.27271 9.51438V13.878C9.27271 14.2797 9.59833 14.6053 9.99998 14.6053C10.4016 14.6053 10.7273 14.2797 10.7273 13.878V9.51438C10.7273 9.11273 10.4016 8.78711 9.99998 8.78711Z" fill="currentColor"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- Rent Out Modal -->
    <RentOutModal
      :is-visible="showRentModal"
      :selected-balance="selectedBalance"
      :rent-amount="calculatedRentAmount"
      :input-amount="inputAmount"
      :terms-agreed="termsAgreed"
      :bottom-offset="bottomNavRef?.bottomOffset || 0"
      @close="closeRentModal"
      @rent-out="handleRentOut"
      @open-terms="openTermsModal"
    />

    <!-- Terms Modal -->
    <TermsAndConditionsModal
      :isVisible="showTermsModal"
      @close="closeTermsModal"
      @agree="agreeToTerms"
    />

    <!-- Info Tooltip -->
    <InfoTooltip
      :is-visible="showInfoTooltip"
      title="Forevers Balance"
      description="Dubadu Forevers ads you own. You invest and own your own advertising billboard on dubadu.com, and we rent it out."
      @close="showInfoTooltip = false"
    />

    <!-- Success Notification -->
    <SuccessNotification
      :is-visible="showSuccessNotification"
      :class="{ 'blur-notification': isAnyModalOpen }"
      message="Rent Out Forevers Successfully"
      @close="showSuccessNotification = false"
    />

    <!-- Bottom Navigation -->
    <BottomNavigation />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import BottomNavigation from '../components/BottomNavigation.vue'
import CountryFlag from '../components/CountryFlag.vue'
import InfoTooltip from '../components/InfoTooltip.vue'
import RentOutModal from '../components/RentOutModal.vue'
import TermsAndConditionsModal from '../components/TermsAndConditionsModal.vue'
import SuccessNotification from '../components/SuccessNotification.vue'

const router = useRouter()

// Modal states
const showInfoTooltip = ref(false)
const showRentModal = ref(false)
const showTermsModal = ref(false)
const showSuccessNotification = ref(false)

// Check if any modal is open for blur effect
const isAnyModalOpen = computed(() => {
  return showRentModal.value || showTermsModal.value || showInfoTooltip.value
})
const selectedBalance = ref(null)
const inputAmount = ref('250')
const termsAgreed = ref(false)

// Computed property for rent amount calculation
const calculatedRentAmount = computed(() => {
  if (!selectedBalance.value) return '1,225'
  // Calculate based on selected balance and input amount
  const amount = parseInt(inputAmount.value) || 250
  const rate = parseInt(selectedBalance.value.usdRate) || 4
  return (amount * rate).toLocaleString()
})

// Telegram WebApp optimizations
onMounted(() => {
  // Set viewport height for mobile
  const setViewportHeight = () => {
    document.documentElement.style.setProperty('--vh', `${window.innerHeight * 0.01}px`)
  }
  setViewportHeight()
  window.addEventListener('resize', setViewportHeight)
  window.addEventListener('orientationchange', setViewportHeight)

  // Prevent pull-to-refresh on mobile
  document.body.style.overscrollBehavior = 'none'

  // Telegram WebApp API
  if (window.Telegram && window.Telegram.WebApp) {
    const webapp = window.Telegram.WebApp
    webapp.ready()
    webapp.expand()
  }
})

// Rent out data
const foreversList = ref([
  {
    id: 'de',
    title: 'Forevers DE Balance',
    code: 'DE',
    usdRate: '4',
    priceChange: 0.17,
    rentalCost: 4,
    potentialIncome: 120,
    availableText: 'Available',
    availableAmount: 0
  },
  {
    id: 'uae',
    title: 'Forevers UAE Balance',
    code: 'UAE',
    usdRate: '9',
    priceChange: 0.17,
    rentalCost: 4,
    potentialIncome: 120,
    availableText: 'Available',
    availableAmount: 250
  },
  {
    id: 'kz',
    title: 'Forevers KZ Balance',
    code: 'KZ',
    usdRate: '8',
    priceChange: -0.17,
    rentalCost: 4,
    potentialIncome: 120,
    availableText: 'Available',
    availableAmount: 250
  },
  {
    id: 'pl',
    title: 'Forevers PL Balance',
    code: 'PL',
    usdRate: '4',
    priceChange: -0.17,
    rentalCost: 4,
    potentialIncome: 120,
    availableText: 'Available',
    availableAmount: 250
  },
  {
    id: 'ua',
    title: 'Forevers UA Balance',
    code: 'UA',
    usdRate: '4',
    priceChange: -0.17,
    rentalCost: 4,
    potentialIncome: 120,
    availableText: 'Available',
    availableAmount: 250
  },
  {
    id: 'us',
    title: 'Forevers US Balance',
    code: 'US',
    usdRate: '4',
    priceChange: -0.17,
    rentalCost: 4,
    potentialIncome: 120,
    availableText: 'Available',
    availableAmount: 250
  }
])

// Modal handlers
const openRentModal = (item) => {
  // Don't open modal if no forevers available
  if (item.availableAmount === 0) {
    return
  }

  selectedBalance.value = item
  showRentModal.value = true

  // Haptic feedback
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'light')
  }
}

const closeRentModal = () => {
  showRentModal.value = false
  selectedBalance.value = null
  termsAgreed.value = false
}

const handleRentOut = (data) => {
  console.log('Rent out data:', data)

  // Update the available amount for the selected balance
  const rentedAmount = parseInt(data.amount) || 0
  const balanceItem = foreversList.value.find(item => item.id === data.balance.id)
  if (balanceItem) {
    balanceItem.availableAmount = Math.max(0, balanceItem.availableAmount - rentedAmount)
  }

  // Close the modal first
  closeRentModal()

  // Show success notification
  showSuccessNotification.value = true

  // Auto-hide notification after 3 seconds
  setTimeout(() => {
    showSuccessNotification.value = false
  }, 3000)

  // Haptic feedback for success
  if (window.triggerHaptic) {
    window.triggerHaptic('notification', 'success')
  }
}

const openTermsModal = () => {
  showTermsModal.value = true
}

const closeTermsModal = () => {
  showTermsModal.value = false
}

const agreeToTerms = () => {
  showTermsModal.value = false
  // Auto-check the terms checkbox in the rent modal
  termsAgreed.value = true
}

const goBack = () => {
  router.push('/favorites')
}
</script>

<style scoped>
/* Blur effect for SuccessNotification when modal is open */
.blur-notification {
  filter: blur(4px);
  opacity: 0.6;
  transition: all 0.3s ease;
  pointer-events: none;
}

/* Global scrollbar hiding and Telegram optimizations */
::-webkit-scrollbar {
  width: 0;
}

* {
  -webkit-tap-highlight-color: transparent;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

/* Performance optimizations */
* {
  will-change: auto;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Hide scrollbar in scrollable area */
.overflow-y-auto {
  scrollbar-width: none;
  -ms-overflow-style: none;
  -webkit-overflow-scrolling: touch;
}

.overflow-y-auto::-webkit-scrollbar {
  display: none;
}

/* Better touch targets */
button {
  min-height: 44px;
  min-width: 44px;
  touch-action: manipulation;
}

/* Button enhancements */
.bg-dbd-orange {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.bg-dbd-orange:active {
  background-color: #e55a00;
  transform: scale(0.95);
}


</style>
