<template>
  <div class="w-full min-h-screen bg-white font-montserrat flex flex-col">
    <!-- Content Container -->
    <div class="flex-1 bg-gray-100 rounded-t-2xl p-4 pt-8 pb-40">


      <!-- Payment Methods Grid -->
      <div class="grid grid-cols-2 gap-3 mb-8">
        <!-- Loyalty Program -->
        <div
          class="bg-white border rounded-xl p-4 flex flex-col items-center gap-2 cursor-pointer transition-all relative"
          :class="selectedPayment === 'loyalty' ? 'border-green-500 bg-green-50' : 'border-gray-200'"
          @click="selectPayment('loyalty')"
        >
          <!-- Selected Checkmark -->
          <div v-if="selectedPayment === 'loyalty'" class="absolute top-3 right-3 w-5 h-5 bg-green-500 rounded-full flex items-center justify-center">
            <svg width="8" height="8" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M8.80292 1.37621C8.42688 1.17372 8.00745 1.56423 7.76157 1.79564C7.19753 2.34524 6.72025 2.98162 6.18509 3.56015C5.5921 4.19653 5.0425 4.8329 4.43505 5.45484C4.08793 5.80196 3.71189 6.178 3.48048 6.6119C2.9598 6.10566 2.51145 5.55606 1.93292 5.10773C1.51349 4.78954 0.819255 4.55813 0.833719 5.32468C0.862645 6.32266 1.7449 7.39293 2.39574 8.07268C2.67054 8.36194 3.03212 8.66567 3.45155 8.68013C3.95776 8.70906 4.47843 8.1016 4.78216 7.76895C5.31732 7.19042 5.75122 6.53956 6.24294 5.94659C6.87932 5.16558 7.53016 4.39901 8.15208 3.60354C8.54258 3.11179 9.77195 1.89686 8.80292 1.37621ZM1.47007 5.26682C1.45561 5.26682 1.44115 5.26682 1.41222 5.28126C1.35437 5.26682 1.31098 5.25234 1.25313 5.22341C1.29652 5.19448 1.36883 5.20895 1.47007 5.26682Z" fill="white"/>
            </svg>
          </div>
          <div class="w-10 h-10 bg-gray-100 border border-gray-200 rounded-full flex items-center justify-center">
            <svg width="24" height="24" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M15.625 11.249C18.0411 11.2492 20 13.2079 20 15.624C19.9999 18.0401 18.041 19.9989 15.625 19.999C13.2088 19.999 11.2501 18.0402 11.25 15.624C11.25 13.2078 13.2087 11.249 15.625 11.249ZM17.6406 1.05762C18.1613 0.537054 19.0057 0.53702 19.5264 1.05762C20.0465 1.57814 20.0465 2.42185 19.5264 2.94238L3.52539 18.9404C3.00475 19.4606 2.16125 19.4606 1.64062 18.9404C1.11993 18.4198 1.11993 17.5753 1.64062 17.0547L17.6406 1.05762ZM15.625 13.749C14.5895 13.749 13.75 14.5885 13.75 15.624C13.7501 16.6594 14.5896 17.499 15.625 17.499C16.6603 17.4989 17.4999 16.6593 17.5 15.624C17.5 14.5886 16.6604 13.7492 15.625 13.749ZM4.375 0C6.79112 0.000153941 8.75 1.95883 8.75 4.375C8.7498 6.791 6.79099 8.74985 4.375 8.75C1.95888 8.75 0.00020412 6.79109 0 4.375C0 1.95873 1.95875 0 4.375 0ZM4.375 2.5C3.33946 2.5 2.5 3.33946 2.5 4.375C2.5002 5.41037 3.33959 6.25 4.375 6.25C5.41028 6.24985 6.2498 5.41028 6.25 4.375C6.25 3.33955 5.41041 2.50015 4.375 2.5Z" fill="#2019CE"/>
            </svg>
          </div>
          <div class="text-center">
            <h3 class="text-lg font-semibold text-dbd-dark">{{ loyaltyFormatted }}</h3>
            <p class="text-dbd-light-gray text-base">Loyalty</p>
          </div>
        </div>

        <!-- Bonus Reward -->
        <div 
          class="bg-white border rounded-xl p-4 flex flex-col items-center gap-2 cursor-pointer transition-all relative"
          :class="selectedPayment === 'bonus' ? 'border-green-500 bg-green-50' : 'border-gray-200'"
          @click="selectPayment('bonus')"
        >
          <!-- Selected Checkmark -->
          <div v-if="selectedPayment === 'bonus'" class="absolute top-3 right-3 w-5 h-5 bg-green-500 rounded-full flex items-center justify-center">
            <svg width="8" height="8" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M8.80292 1.37621C8.42688 1.17372 8.00745 1.56423 7.76157 1.79564C7.19753 2.34524 6.72025 2.98162 6.18509 3.56015C5.5921 4.19653 5.0425 4.8329 4.43505 5.45484C4.08793 5.80196 3.71189 6.178 3.48048 6.6119C2.9598 6.10566 2.51145 5.55606 1.93292 5.10773C1.51349 4.78954 0.819255 4.55813 0.833719 5.32468C0.862645 6.32266 1.7449 7.39293 2.39574 8.07268C2.67054 8.36194 3.03212 8.66567 3.45155 8.68013C3.95776 8.70906 4.47843 8.1016 4.78216 7.76895C5.31732 7.19042 5.75122 6.53956 6.24294 5.94659C6.87932 5.16558 7.53016 4.39901 8.15208 3.60354C8.54258 3.11179 9.77195 1.89686 8.80292 1.37621ZM1.47007 5.26682C1.45561 5.26682 1.44115 5.26682 1.41222 5.28126C1.35437 5.26682 1.31098 5.25234 1.25313 5.22341C1.29652 5.19448 1.36883 5.20895 1.47007 5.26682Z" fill="white"/>
            </svg>
          </div>
          
          <div class="w-10 h-10 bg-gray-100 border border-gray-200 rounded-full flex items-center justify-center">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M19.8571 6.28571H17.4571C17.7514 6.05915 17.9914 5.76969 18.1595 5.43849C18.3275 5.10729 18.4195 4.74272 18.4286 4.37143C18.4156 3.74162 18.1577 3.14167 17.7096 2.69891C17.2615 2.25615 16.6585 2.00544 16.0286 2C14.3714 2 12.9143 3.04286 11.8714 4.92143C10.8286 3.04286 9.37143 2 7.71429 2C7.08437 2.00544 6.48137 2.25615 6.03327 2.69891C5.58518 3.14167 5.32727 3.74162 5.31429 4.37143C5.32338 4.74272 5.41532 5.10729 5.58339 5.43849C5.75146 5.76969 5.99142 6.05915 6.28571 6.28571H4.14286C3.57454 6.28571 3.02949 6.51148 2.62763 6.91334C2.22576 7.31521 2 7.86025 2 8.42857V9.85714C2.00124 10.2992 2.1392 10.7301 2.39496 11.0908C2.65071 11.4514 3.01175 11.7241 3.42857 11.8714V19.8571C3.42857 20.4255 3.65434 20.9705 4.0562 21.3724C4.45806 21.7742 5.00311 22 5.57143 22H18.4286C18.9969 22 19.5419 21.7742 19.9438 21.3724C20.3457 20.9705 20.5714 20.4255 20.5714 19.8571V11.8714C20.9883 11.7241 21.3493 11.4514 21.605 11.0908C21.8608 10.7301 21.9988 10.2992 22 9.85714V8.42857C22 7.86025 21.7742 7.31521 21.3724 6.91334C20.9705 6.51148 20.4255 6.28571 19.8571 6.28571ZM13.4286 10.5714H10.5714V7.71429H13.4286V10.5714ZM16.0286 3.42857C16.2792 3.43533 16.5182 3.536 16.6981 3.71063C16.878 3.88526 16.9858 4.1211 17 4.37143C17 4.78571 16.6714 5.18571 16.0857 5.50714C15.0553 5.98085 13.9341 6.22458 12.8 6.22143C13.35 5.06429 14.4 3.42857 16.0286 3.42857ZM7.71429 3.42857C9.34286 3.42857 10.3929 5.06429 10.9357 6.28571C9.80376 6.29036 8.68458 6.04653 7.65714 5.57143C7.06429 5.25 6.74286 4.85714 6.74286 4.43571C6.74088 4.17414 6.84148 3.92221 7.02308 3.73393C7.20467 3.54566 7.45281 3.43604 7.71429 3.42857ZM3.42857 8.42857C3.42857 8.23913 3.50383 8.05745 3.63778 7.9235C3.77174 7.78954 3.95342 7.71429 4.14286 7.71429H9.14286V10.5714H4.14286C3.95342 10.5714 3.77174 10.4962 3.63778 10.3622C3.50383 10.2283 3.42857 10.0466 3.42857 9.85714V8.42857ZM4.85714 19.8571V12H9.85714V20.5714H5.57143C5.38199 20.5714 5.20031 20.4962 5.06635 20.3622C4.9324 20.2283 4.85714 20.0466 4.85714 19.8571ZM11.2857 20.5714V12H12.7143V20.5714H11.2857ZM19.1429 19.8571C19.1429 20.0466 19.0676 20.2283 18.9336 20.3622C18.7997 20.4962 18.618 20.5714 18.4286 20.5714H14.1429V12H19.1429V19.8571ZM20.5714 9.85714C20.5714 10.0466 20.4962 10.2283 20.3622 10.3622C20.2283 10.4962 20.0466 10.5714 19.8571 10.5714H14.8571V7.71429H19.8571C20.0466 7.71429 20.2283 7.78954 20.3622 7.9235C20.4962 8.05745 20.5714 8.23913 20.5714 8.42857V9.85714Z" fill="#2019CE"/>
            </svg>
          </div>
          <div class="text-center">
            <h3 class="text-lg font-semibold text-dbd-dark">{{ bonusFormatted }}</h3>
            <p class="text-dbd-light-gray text-base">Bonus</p>
          </div>
        </div>

        <!-- USDT Crypto Wallet -->
        <div
          class="bg-white border rounded-xl p-4 flex flex-col items-center gap-2 cursor-pointer transition-all col-span-1 relative"
          :class="selectedPayment === 'usdt' ? 'border-green-500 bg-green-50' : 'border-gray-200'"
          @click="selectPayment('usdt')"
        >
          <!-- Selected Checkmark -->
          <div v-if="selectedPayment === 'usdt'" class="absolute top-3 right-3 w-5 h-5 bg-green-500 rounded-full flex items-center justify-center">
            <svg width="8" height="8" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M8.80292 1.37621C8.42688 1.17372 8.00745 1.56423 7.76157 1.79564C7.19753 2.34524 6.72025 2.98162 6.18509 3.56015C5.5921 4.19653 5.0425 4.8329 4.43505 5.45484C4.08793 5.80196 3.71189 6.178 3.48048 6.6119C2.9598 6.10566 2.51145 5.55606 1.93292 5.10773C1.51349 4.78954 0.819255 4.55813 0.833719 5.32468C0.862645 6.32266 1.7449 7.39293 2.39574 8.07268C2.67054 8.36194 3.03212 8.66567 3.45155 8.68013C3.95776 8.70906 4.47843 8.1016 4.78216 7.76895C5.31732 7.19042 5.75122 6.53956 6.24294 5.94659C6.87932 5.16558 7.53016 4.39901 8.15208 3.60354C8.54258 3.11179 9.77195 1.89686 8.80292 1.37621ZM1.47007 5.26682C1.45561 5.26682 1.44115 5.26682 1.41222 5.28126C1.35437 5.26682 1.31098 5.25234 1.25313 5.22341C1.29652 5.19448 1.36883 5.20895 1.47007 5.26682Z" fill="white"/>
            </svg>
          </div>
          <div class="w-10 h-10 bg-gray-100 border border-gray-200 rounded-full flex items-center justify-center">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M14.7002 0.0917358C15.144 -0.0204478 15.6077 -0.0301851 16.0557 0.0643921C16.5037 0.15902 16.9246 0.355507 17.2852 0.637634C17.6662 0.961021 17.9702 1.36586 18.1738 1.8222C18.3521 2.22166 18.4496 2.65182 18.4619 3.08783V5.38959L18.4609 5.39056C18.6059 5.49919 18.7444 5.61844 18.874 5.74799C19.5951 6.46895 20 7.44724 20 8.46674V16.1552C19.9998 16.7817 18.7879 18 17.2988 18H2.70117C1.21206 18 0.0002339 16.7817 0 15.2842V2.71582C0.000233829 1.21827 1.21206 0 2.70117 0H15.3369ZM2.70117 3.67188C1.90768 3.67188 1.2618 4.32114 1.26172 5.11914V15.2842C1.26195 16.082 1.90778 16.7314 2.70117 16.7314H17.2988C18.0922 16.7314 18.738 16.082 18.7383 15.2842V13.1484H14.7158C13.1219 13.1484 11.8244 11.8443 11.8242 10.2412C11.8242 8.63803 13.1217 7.33301 14.7158 7.33301H18.7383V5.11914C18.7382 4.32114 18.0923 3.67188 17.2988 3.67188H2.70117ZM14.7158 8.60254C13.8174 8.60254 13.0859 9.33767 13.0859 10.2412C13.0861 11.1446 13.8175 11.8799 14.7158 11.8799H18.7383V8.60254H14.7158ZM15.9404 9.6748C16.3756 9.6748 16.7283 9.99219 16.7285 10.3838C16.7285 10.7755 16.3757 11.0938 15.9404 11.0938C15.5052 11.0937 15.1523 10.7755 15.1523 10.3838C15.1526 9.99222 15.5053 9.67484 15.9404 9.6748ZM2.70117 1.26855C1.90778 1.26855 1.26195 1.91796 1.26172 2.71582V2.82227C1.67869 2.5571 2.17244 2.40332 2.70117 2.40332H16.7422C16.5994 1.75535 16.0235 1.26855 15.3369 1.26855H2.70117Z" fill="#2019CE"/>
            </svg>
          </div>
          <div class="text-center">
            <h3 class="text-lg font-semibold text-dbd-dark">USDT</h3>
            <p class="text-dbd-light-gray text-base">Crypto</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Navigation -->
    <div class="fixed left-0 right-0 bottom-0 z-[9998]">
      <BottomNavigation />
    </div>

    <!-- Terms and Conditions Checkbox - positioned above CartBottom -->
    <div class="fixed left-1/2 transform -translate-x-1/2 z-[9999] bottom-[200px] sm:bottom-[240] md:bottom-[240px] lg:bottom-[240px]">
      <TermsCheckbox
        v-model="termsAccepted"
        @open-terms="openTerms"
      />
    </div>

    <!-- Cart Bottom Component -->
    <div class="fixed left-0 right-0 z-[9999]" style="bottom: 89px;">
      <CartBottomComponent
        :total-amount="numericTotal"
        :disabled="isBuyButtonDisabled"
        :button-text="buyButtonText"
        :loading="isConnectingWallet || isProcessingPurchase"
        @back="handleBack"
        @purchase="handlePurchase"
      />
    </div>

    <!-- Terms and Conditions Modal -->
    <TermsAndConditionsModal
      :isVisible="showTermsModal"
      @close="closeTermsModal"
      @agree="closeTermsModal"
    />

    <!-- Confirm Exchange Modal -->
    <ConfirmExchangeModal
      :is-visible="showConfirmModal"
      :amount="confirmModalData.amount"
      :price="confirmModalData.price"
      :wallet-type="confirmModalData.walletType"
      :forevers-type="confirmModalData.foreversType"
      :is-processing="isProcessingPurchase"
      @close="closeConfirmModal"
      @decline="closeConfirmModal"
      @agree="executeActualPurchase"
    />

    <!-- Success Modal -->
    <SuccessModal
      :is-visible="showSuccessModal"
      :amount="foreversAmountDisplay"
      :message="successMessage"
      @close="closeSuccessModal"
      @confirm="closeSuccessModal"
    />

    <!-- Crypto Transaction Modal -->
    <CryptoTransactionModal
      :is-visible="showCryptoModal"
      :status="cryptoModalStatus"
      :transaction-data="cryptoTransactionData"
      :polling-attempts="cryptoPollingAttempts"
      :custom-message="cryptoCustomMessage"
      :is-processing="isProcessingPurchase"
      @close="closeCryptoModal"
    />
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch, onUnmounted } from 'vue'
import { useApiErrorNotifier } from '../composables/useApiErrorNotifier.js'
import { useRouter, useRoute } from 'vue-router'
import BottomNavigation from '../components/BottomNavigation.vue'
import CartBottomComponent from '../components/CartBottomComponent.vue'
import CountryFlag from '../components/CountryFlag.vue'
import TermsCheckbox from '../components/TermsCheckbox.vue'
import TermsAndConditionsModal from '../components/TermsAndConditionsModal.vue'
import SuccessModal from '../components/SuccessModal.vue'
import ConfirmExchangeModal from '../components/ConfirmExchangeModal.vue'
import CryptoTransactionModal from '../components/CryptoTransactionModal.vue'
import { useCart } from '../composables/useCart.js'
import { formatUSDPrefix } from '../utils/formatNumber.js'
import { ForeversPurchaseService } from '../services/foreversPurchaseService.js'
import { tonConnectService } from '../services/tonConnectService.js'

const router = useRouter()
const route = useRoute()

// Reactive data
const selectedPayment = ref('bonus') // default
const termsAccepted = ref(false)
const totalAmount = ref('0') // USD total (locale string)
const foreversAmount = ref(0) // numeric forevers amount
const isProcessingPurchase = ref(false) // loading state for purchase

// Ton Connect related state
const isWalletConnected = ref(false)
const walletAddress = ref('')
const isConnectingWallet = ref(false)
const showCryptoModal = ref(false)
const cryptoModalStatus = ref('processing')
const cryptoTransactionData = ref({})
const cryptoPollingAttempts = ref(0)
const cryptoCustomMessage = ref('')

// Robust locale-aware parser: handles forms like "26,106.00", "187,5", "1 234,56"
function parseLocaleAmount(val) {
  if (typeof val === 'number') return val
  if (val == null) return 0
  let s = String(val).trim()
  if (!s) return 0
  // Remove NBSP or spaces used as thousand separators
  s = s.replace(/\u00A0|\s/g, '')
  // If string has comma but no dot => treat comma as decimal separator
  if (s.includes(',') && !s.includes('.')) {
    // Remove any dots that might be thousands separators (rare in this case)
    s = s.replace(/\./g, '')
    // Replace the last comma with a dot (decimal)
    const lastComma = s.lastIndexOf(',')
    s = s.substring(0, lastComma).replace(/,/g, '') + '.' + s.substring(lastComma + 1)
  } else {
    // Remove commas that act as thousand separators (those followed by exactly 3 digits before decimal or end)
    s = s.replace(/,(?=\d{3}(?:\D|$))/g, '')
  }
  const num = parseFloat(s)
  return isNaN(num) ? 0 : num
}

const numericTotal = computed(() => parseLocaleAmount(totalAmount.value))
const purchaseDetails = ref(null)
const showTermsModal = ref(false)
const showSuccessModal = ref(false)
const showConfirmModal = ref(false)
const confirmModalData = ref({
  amount: 0,
  price: '0.00',
  walletType: 'bonus',
  foreversType: 'UAE'
})
const loyaltyBalance = ref(0)
const bonusBalance = ref(0)
const successMessage = ref('Payment completed successfully')

// cart composable (for clearing cart after success)
const { clearCart } = useCart()

// API error notifier
const { showError: showApiError } = useApiErrorNotifier()

// Computed properties
const isAnyModalOpen = computed(() => {
  return showTermsModal.value || showSuccessModal.value || showConfirmModal.value || showCryptoModal.value
})

// Check if buy button should be disabled
const isBuyButtonDisabled = computed(() => {
  // Disable only when payment not selected, terms not accepted, or processing
  if (!selectedPayment.value || !termsAccepted.value || isProcessingPurchase.value) {
    return true
  }
  // Allow clicking even if wallet not connected (will trigger connect flow)
  return false
})

// Get button text based on payment method
const buyButtonText = computed(() => {
  if (selectedPayment.value === 'usdt') {
    if (isConnectingWallet.value) return 'Connecting...'
    return isWalletConnected.value ? 'Buy Forevers' : 'Connect Wallet'
  }
  return 'Buy Forevers'
})

// Methods
const selectPayment = (paymentType) => { selectedPayment.value = paymentType }

const getPaymentMethodDisplayName = (paymentMethod) => {
  switch (paymentMethod) {
    case 'loyalty':
      return 'Loyalty'
    case 'bonus':
      return 'Bonus'
    case 'usdt':
    case 'crypto':
      return 'Crypto'
    default:
      return 'Unknown'
  }
}

const handleBack = () => {
  router.go(-1)
}

const handlePurchase = async () => {
  if (!selectedPayment.value || !termsAccepted.value) {
    return
  }

  // Handle crypto payment
  if (selectedPayment.value === 'usdt') {
    if (!isWalletConnected.value) {
      await connectTonWallet()
      return
    }
    await handleCryptoPurchase()
    return
  }

  // Only show confirmation modal for bonus and loyalty payments
  if (selectedPayment.value === 'bonus' || selectedPayment.value === 'loyalty') {
    // Prepare confirmation modal data
    const totalForevers = foreversAmount.value || 0
    const firstCountryCode = purchaseDetails.value?.foreversDetails?.[0]?.code || 'UAE'

    confirmModalData.value = {
      amount: totalForevers,
      price: numericTotal.value.toFixed(2),
      walletType: selectedPayment.value,
      foreversType: firstCountryCode
    }

    // Show confirmation modal
    showConfirmModal.value = true
  }
}

// Handle crypto purchase flow
const handleCryptoPurchase = async () => {
  try {
    isProcessingPurchase.value = true

    // Check if wallet is connected
    if (!isWalletConnected.value) {
      await connectTonWallet()
      if (!isWalletConnected.value) {
        return // User cancelled or connection failed
      }
    }

    // Prepare crypto purchase
    const amountUsd = numericTotal.value
    const rateAsDeposit = purchaseDetails.value?.purchaseSummary?.averagePrice || null

    console.log('Starting crypto purchase:', { amountUsd, rateAsDeposit })

    // Complete crypto purchase flow
    const result = await tonConnectService.completeCryptoPurchase(amountUsd, rateAsDeposit)

    if (result.success) {
      // Show verification modal
      cryptoTransactionData.value = result.initData
      cryptoModalStatus.value = 'processing'
      cryptoPollingAttempts.value = 0
      showCryptoModal.value = true

      // Start polling for verification
      tonConnectService.startTransactionPolling(
        result.requestId,
        (statusResult, attempts) => {
          cryptoPollingAttempts.value = attempts

          if (statusResult.transaction_status === 'success') {
            cryptoModalStatus.value = 'success'
            cryptoCustomMessage.value = 'Your crypto payment has been verified! Forevers will be credited to your account.'
          } else if (statusResult.transaction_status === 'failed' || statusResult.transaction_status === 'invalid') {
            cryptoModalStatus.value = 'failed'
            cryptoCustomMessage.value = statusResult.message || 'Transaction verification failed.'
          }
        }
      )
    }
  } catch (error) {
    console.error('Crypto purchase error:', error)
    showApiError('crypto_purchase', {
      status: 400,
      message: error.message || 'Crypto purchase failed. Please try again.'
    })
  } finally {
    isProcessingPurchase.value = false
  }
}

// Connect TON wallet
const connectTonWallet = async () => {
  try {
    isConnectingWallet.value = true

    // Initialize and connect
    await tonConnectService.init()
    const wallet = await tonConnectService.connectWallet()

    if (wallet) {
      isWalletConnected.value = true
      walletAddress.value = tonConnectService.getWalletAddress()
      console.log('Wallet connected:', walletAddress.value)
    }
  } catch (error) {
    console.error('Wallet connection error:', error)
    showApiError('wallet_connection', {
      status: 400,
      message: error.message || 'Failed to connect wallet. Please try again.'
    })
  } finally {
    isConnectingWallet.value = false
  }
}

// Disconnect TON wallet
const disconnectTonWallet = async () => {
  try {
    await tonConnectService.disconnectWallet()
    isWalletConnected.value = false
    walletAddress.value = ''
    console.log('Wallet disconnected')
  } catch (error) {
    console.error('Wallet disconnection error:', error)
  }
}

// Close crypto modal
const closeCryptoModal = () => {
  showCryptoModal.value = false

  // If transaction was successful, navigate to wallet view
  if (cryptoModalStatus.value === 'success') {
    clearCart()
    sessionStorage.removeItem('purchaseDetails')
    router.push({ name: 'wallet', query: { loyalty: loyaltyBalance.value, bonus: bonusBalance.value } })
  }
}

const executeActualPurchase = async () => {
  isProcessingPurchase.value = true

  try {
    const result = await ForeversPurchaseService.processMultiplePurchases(
      purchaseDetails.value,
      selectedPayment.value
    )

    if (result.success) {
      // Close confirmation modal first
      showConfirmModal.value = false

      // Ensure forevers amount is available before showing success
      if (foreversAmount.value === 0 && purchaseDetails.value?.foreversAmount) {
        foreversAmount.value = purchaseDetails.value.foreversAmount
      }

      // Update wallet data after successful purchase
      await fetchWalletData()

      // Set success message
      const paymentMethodName = getPaymentMethodDisplayName(selectedPayment.value)
      successMessage.value = `Forevers purchased successfully using ${paymentMethodName} wallet!`

      // Show success modal
      showSuccessModal.value = true

    } else {
      // Handle errors
      const errorMessage = result.errors.length > 0
        ? result.errors.map(e => e.error).join(', ')
        : 'Purchase failed. Please try again.'

      // Close confirmation modal
      showConfirmModal.value = false

      showApiError('forevers_purchase', {
        status: 400,
        message: errorMessage
      })
    }
  } catch (error) {
    // Close confirmation modal
    showConfirmModal.value = false

    showApiError('forevers_purchase', {
      status: 500,
      message: error.message || 'An unexpected error occurred during purchase. Please try again.'
    })
  } finally {
    isProcessingPurchase.value = false
  }
}

const closeConfirmModal = () => {
  showConfirmModal.value = false
}

const openTerms = () => {
  showTermsModal.value = true
}

const closeTermsModal = () => {
  showTermsModal.value = false
}

const closeSuccessModal = () => {
  showSuccessModal.value = false
  clearCart() // empty cart after success
  // Clear purchase details from sessionStorage
  sessionStorage.removeItem('purchaseDetails')
  router.push({ name: 'wallet', query: { loyalty: loyaltyBalance.value, bonus: bonusBalance.value } })
}

// Get purchase details from route params if available
// Formatters for loyalty & bonus
const loyaltyFormatted = computed(() => formatUSDPrefix(loyaltyBalance.value))
const bonusFormatted = computed(() => formatUSDPrefix(bonusBalance.value))

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

async function fetchWalletData() {
  try {
    const response = await fetch(`${API_BASE_URL}/forevers/me`, { credentials: 'include' })
    const result = await response.json()
    if (result.status !== 'success') {
      showApiError('forevers_user_balance', { status: response.status, message: result.message })
      return
    }
    const loyalty = result?.wallets?.find(w => w.type === 'loyalty_program')
    loyaltyBalance.value = loyalty ? parseFloat(loyalty.amount) : 0
    const bonus = result?.wallets?.find(w => w.type === 'bonus')
    bonusBalance.value = bonus ? parseFloat(bonus.amount) : 0
  } catch (e) { showApiError('forevers_user_balance', { error: e }) }
}

// Computed for SuccessModal display
const foreversAmountDisplay = computed(() => {
  return foreversAmount.value ? foreversAmount.value.toLocaleString() : '0'
})

// Computed properties for Forevers details
const foreversTypes = computed(() => {
  return purchaseDetails.value?.foreversDetails?.map(detail => detail.code) || []
})

const totalForeversTypes = computed(() => {
  return foreversTypes.value.length
})

const averagePricePerForevers = computed(() => {
  return purchaseDetails.value?.purchaseSummary?.averagePrice?.toFixed(2) || '0.00'
})

// Get unique country codes and their details
const uniqueCountries = computed(() => {
  if (!purchaseDetails.value?.foreversDetails) return []
  return purchaseDetails.value.foreversDetails.reduce((acc, detail) => {
    if (!acc.find(item => item.code === detail.code)) {
      acc.push({
        code: detail.code,
        country: detail.country,
        totalAmount: detail.amount,
        pricePerUnit: detail.usdRate,
        totalCost: detail.totalCost
      })
    }
    return acc
  }, [])
})

// Add watchers for debugging



onMounted(() => {
  // Retrieve purchase details from sessionStorage
  try {
    const savedPurchaseDetails = sessionStorage.getItem('purchaseDetails')
    if (savedPurchaseDetails) {
      purchaseDetails.value = JSON.parse(savedPurchaseDetails)
    }
  } catch (error) {
    // Silently handle error
  }

  // Parse USD total (for potential future logic)
  const incomingTotal = route.params.totalAmount || route.query.totalRaw || route.query.total || purchaseDetails.value?.amount
  if (incomingTotal !== undefined) {
    const num = parseLocaleAmount(incomingTotal)
    totalAmount.value = num.toLocaleString(undefined, { maximumFractionDigits: 6 })
  }

  // Prefer explicit forevers amount from query, then purchaseDetails
  const incomingForevers = route.query.foreversAmount || purchaseDetails.value?.foreversAmount
  if (incomingForevers !== undefined) {
    foreversAmount.value = parseLocaleAmount(incomingForevers)
  }

  // Log detailed Forevers information if available

  // Log query parameters for Forevers types and prices
  if (route.query.foreversTypes) {
    const types = route.query.foreversTypes.split(',')
    const prices = route.query.pricesPerType ? route.query.pricesPerType.split(',') : []
  }


  fetchWalletData()

  // Initialize TonConnect
  initializeTonConnect()
})

// Initialize TonConnect and check connection status
const initializeTonConnect = async () => {
  try {
    await tonConnectService.init()

    // Check if wallet is already connected
    if (tonConnectService.isWalletConnected()) {
      isWalletConnected.value = true
      walletAddress.value = tonConnectService.getWalletAddress()
      console.log('Wallet already connected:', walletAddress.value)
    }

    // Listen for wallet connection changes
    tonConnectService.onStatusChange((wallet) => {
      if (wallet) {
        isWalletConnected.value = true
        walletAddress.value = wallet.account?.address || ''
      } else {
        isWalletConnected.value = false
        walletAddress.value = ''
      }
    })
  } catch (error) {
    console.error('TonConnect initialization error:', error)
  }
}

// Cleanup on component unmount
onUnmounted(() => {
  // Remove TonConnect event listeners
  if (tonConnectService.tonConnect) {
    tonConnectService.off()
  }
})
</script>

<style scoped>
.font-montserrat {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Responsive adjustments */
@media (min-width: 768px) {
  .grid-cols-2 {
    grid-template-columns: repeat(3, 1fr);
  }
  
  .col-span-1:last-child {
    grid-column: span 1;
  }
}

/* Touch feedback */
.cursor-pointer:active {
  transform: scale(0.98);
  transition: transform 0.1s ease;
}

/* Telegram WebApp optimizations */
* {
  -webkit-tap-highlight-color: transparent;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  user-select: none;
}

button {
  touch-action: manipulation;
}

/* Custom styles for TermsCheckbox on payment screen */
:deep(.terms-text) {
  color: #4B4D50 !important; /* Use dark gray instead of white for this screen */
}

:deep(.terms-checkbox) {
  border-color: #7E7E7E;
}

:deep(.terms-checkbox:checked) {
  background: #129E0F !important; /* Use green color to match design */
  border-color: #129E0F !important;
}

</style>
