<template>
  <div class="w-full min-h-screen bg-gray-100 font-montserrat overflow-x-hidden flex flex-col">
    <!-- Header Section -->
    <div class="w-full px-4 pt-6 pb-3 bg-gray-100 z-30">
      <div class="mb-2">
        <!-- Total Balance Card -->
        <div class="bg-purple-50 border border-purple-200 rounded-2xl p-4">
          <div class="flex items-start justify-between mb-4">
            <h2 class="text-2xl font-semibold text-black leading-7">
              Forevers<br>Balance
            </h2>

            <div class="flex flex-col items-end gap-2">
              <div class="flex items-center gap-2">
                <svg width="32" height="32" viewBox="0 0 32 32" class="text-blue-700">
                  <path d="M30.667 7.381V1.333H7.129V9.011H1.333V15.059H7.129V30.108H13.894V22.728H19.615V16.680H13.894V15.059H25.132V9.011H13.894V7.381H30.667Z" fill="currentColor"/>
                </svg>
                <span class="text-3xl font-bold text-blue-700">{{ totalBalance.toLocaleString() }}</span>
              </div>
              <p class="text-lg text-gray-600 font-medium">Worth ${{ totalWorth.toLocaleString() }}</p>
            </div>
          </div>

          <button
            @click="handleRentOut"
            class="w-full bg-gradient-to-r from-blue-700 to-purple-600 text-white font-bold py-3 px-12 rounded-full hover:from-blue-800 hover:to-purple-700 transition-all duration-200 text-sm"
          >
            Rent Out Forevers
          </button>
        </div>
      </div>
    </div>

    <!-- Scrollable Cards -->
    <div class="flex-1 w-full overflow-y-auto px-4 pb-32" v-if="balances.length > 0">
      <div class="space-y-4">
        <div
          v-for="balance in balances"
          :key="balance.id"
          class="bg-white border border-purple-200 rounded-2xl balance-card relative flex flex-col justify-between"
        >
          <!-- Country Header -->
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center gap-2">
              <CountryFlag :country="balance.code" class="w-6 h-6" />
              <span class="text-gray-700 font-medium text-base">{{ balance.country }} Balance</span>
            </div>

            <button
              @click="openEnterAmountModal(balance)"
              class="w-16 h-11 border border-blue-700 bg-purple-50 rounded-full flex items-center justify-center hover:bg-purple-100 transition-colors"
            >
              <svg width="24" height="24" viewBox="0 0 24 24" class="text-blue-700">
                <path d="M18 13H6C5.4 13 5 12.6 5 12C5 11.4 5.4 11 6 11H18C18.6 11 19 11.4 19 12C19 12.6 18.6 13 18 13Z" fill="currentColor"/>
                <path d="M12 19C11.4 19 11 18.6 11 18V6C11 5.4 11.4 5 12 5C12.6 5 13 5.4 13 6V18C13 18.6 12.6 19 12 19Z" fill="currentColor"/>
              </svg>
            </button>
          </div>

          <!-- Token Info -->
          <div class="flex items-center gap-1 mb-3 flex-wrap">
            <svg width="24" height="24" viewBox="0 0 24 24" class="text-blue-700">
              <path d="M23 5.536V1H5.347V6.759H1V11.294H5.347V22.581H10.421V17.046H14.712V12.510H10.421V11.294H18.849V6.759H10.421V5.536H23Z" fill="currentColor"/>
            </svg>
            <span class="text-lg font-semibold text-blue-700">{{ balance.amount.toLocaleString() }}</span>
            <span class="w-1 h-1 bg-gray-400 rounded-full"></span>
            <div class="flex items-center gap-0.5 text-sm text-gray-600 font-medium">
              <span>1</span>
              <svg width="16" height="16" viewBox="0 0 16 16" class="text-gray-600">
                <path d="M15.2636 2H4.61925C4.15063 2 3.8159 2.28571 3.8159 2.68571V5.48571H0.803347C0.334728 5.54286 0 5.82857 0 6.22857C0 6.62857 0.334728 6.91429 0.803347 6.91429H3.8159V13.3143C3.8159 13.7143 4.15063 14 4.61925 14C5.08787 14 5.42259 13.7143 5.42259 13.3143V10.3429H8.83682C9.30544 10.3429 9.64017 10.0571 9.64017 9.65714C9.64017 9.25714 9.30544 8.97143 8.83682 8.97143H5.42259V6.85714H11.9163C12.3849 6.85714 12.7197 6.57143 12.7197 6.17143C12.7197 5.77143 12.3849 5.48571 11.9163 5.48571H5.42259V3.37143H15.1967C15.6653 3.37143 16 3.08571 16 2.68571C16 2.28571 15.7322 2 15.2636 2Z" fill="currentColor"/>
              </svg>
              <span>{{ balance.code }}/{{ balance.usdRate }} USD</span>
            </div>

            <div
              :class="[
                'px-2 py-0.5 rounded text-xs font-semibold flex items-center gap-1 ml-1',
                balance.priceChange > 0 ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'
              ]"
            >
              <svg
                :class="[
                  'w-2 h-2 transform',
                  balance.priceChange > 0 ? '-rotate-45' : 'rotate-45'
                ]"
                viewBox="0 0 10 13"
                fill="none"
              >
                <path
                  d="M0.720539 4.9362L4.6673 1.01033M4.6673 1.01033L8.58641 4.92944M4.6673 1.01033L4.65686 12.3136"
                  :stroke="balance.priceChange > 0 ? '#07B80E' : '#FF1919'"
                  stroke-width="1.25"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              <span class="font-semibold">{{ balance.priceChange > 0 ? '+' : '' }}{{ balance.priceChange.toFixed(2) }}%</span>
            </div>
          </div>

          <!-- Available and Discount Section -->
          <div class="flex gap-2 mb-3 sm:gap-3" v-if="balance.discount && balance.discount > 0">
            <!-- Available Section -->
            <div class="bg-green-100 rounded-xl p-1.5 sm:p-3 flex-1 min-w-0 sm:flex sm:items-center">
              <!-- Mobile: vertical layout, Desktop: horizontal layout matching no-discount version -->
              <div class="flex flex-col gap-0 sm:flex-row sm:items-center sm:justify-between sm:gap-0 sm:w-full">
                <!-- Mobile: separate rows, Desktop: left side content group -->
                <div class="flex items-center justify-between sm:justify-start sm:gap-2 sm:flex-1 pl-1 sm:pl-0">
                  <span class="text-sm text-gray-600 font-medium">Available</span>
                  <!-- Mobile: info button on right, Desktop: hidden (will show at end) -->
                  <button
                    @click="showInfoTooltip = true"
                    class="w-3.5 h-3.5 flex items-center justify-center transition-colors flex-shrink-0 sm:hidden"
                  >
                    <svg width="18" height="18" viewBox="0 0 20 20" class="text-gray-600">
                      <path d="M10 2C5.5888 2 2 5.58885 2 10C2 14.4112 5.5888 18 10 18C14.4112 18 18 14.4112 18 10C18 5.58885 14.4112 2 10 2ZM10 16.5455C6.39079 16.5455 3.45455 13.6092 3.45455 10C3.45455 6.39088 6.39079 3.45455 10 3.45455C13.6092 3.45455 16.5455 6.39088 16.5455 10C16.5455 13.6092 13.6092 16.5455 10 16.5455Z" fill="currentColor"/>
                      <path d="M10 5.39453C9.46543 5.39453 9.03052 5.82973 9.03052 6.36466C9.03052 6.89911 9.46543 7.33393 10 7.33393C10.5346 7.33393 10.9695 6.89911 10.9695 6.36466C10.9695 5.82973 10.5346 5.39453 10 5.39453Z" fill="currentColor"/>
                      <path d="M9.99998 8.78711C9.59833 8.78711 9.27271 9.11273 9.27271 9.51438V13.878C9.27271 14.2797 9.59833 14.6053 9.99998 14.6053C10.4016 14.6053 10.7273 14.2797 10.7273 13.878V9.51438C10.7273 9.11273 10.4016 8.78711 9.99998 8.78711Z" fill="currentColor"/>
                    </svg>
                  </button>
                  <!-- Desktop: dot separator and F icon + amount in same left group -->
                  <template v-if="balance.availableAmount">
                    <span class="w-1.5 h-1.5 bg-gray-400 rounded-full hidden sm:block"></span>
                    <div class="hidden sm:flex items-center gap-1">
                      <svg width="14" height="14" viewBox="0 0 14 14" class="text-black">
                        <path d="M12.86 1.4H4.38C4.007 1.4 3.74 1.667 3.74 2.04V4.654H1.34C0.967 4.707 0.7 4.974 0.7 5.347C0.7 5.72 0.967 5.987 1.34 5.987H3.74V11.96C3.74 12.334 4.007 12.6 4.38 12.6C4.754 12.6 5.02 12.334 5.02 11.96V9.187H7.74C8.114 9.187 8.38 8.92 8.38 8.547C8.38 8.174 8.114 7.907 7.74 7.907H5.02V5.934H10.194C10.567 5.934 10.834 5.667 10.834 5.294C10.834 4.92 10.567 4.654 10.194 4.654H5.02V2.68H12.807C13.18 2.68 13.447 2.414 13.447 2.04C13.447 1.667 13.234 1.4 12.86 1.4Z" fill="currentColor"/>
                      </svg>
                      <span class="text-sm font-medium text-black">{{ balance.availableAmount }}</span>
                    </div>
                  </template>
                  <template v-else>
                    <span class="text-sm text-gray-600 font-medium hidden sm:inline">without restrictions</span>
                  </template>
                </div>
                <!-- Mobile: F icon + amount row -->
                <div class="flex items-center gap-1 sm:hidden pl-1 -mt-2">
                  <template v-if="balance.availableAmount">
                    <svg width="14" height="14" viewBox="0 0 14 14" class="text-black">
                      <path d="M12.86 1.4H4.38C4.007 1.4 3.74 1.667 3.74 2.04V4.654H1.34C0.967 4.707 0.7 4.974 0.7 5.347C0.7 5.72 0.967 5.987 1.34 5.987H3.74V11.96C3.74 12.334 4.007 12.6 4.38 12.6C4.754 12.6 5.02 12.334 5.02 11.96V9.187H7.74C8.114 9.187 8.38 8.92 8.38 8.547C8.38 8.174 8.114 7.907 7.74 7.907H5.02V5.934H10.194C10.567 5.934 10.834 5.667 10.834 5.294C10.834 4.92 10.567 4.654 10.194 4.654H5.02V2.68H12.807C13.18 2.68 13.447 2.414 13.447 2.04C13.447 1.667 13.234 1.4 12.86 1.4Z" fill="currentColor"/>
                    </svg>
                    <span class="text-sm font-medium text-black">{{ balance.availableAmount }}</span>
                  </template>
                  <template v-else>
                    <span class="text-sm text-gray-600 font-medium">without restrictions</span>
                  </template>
                </div>
                <!-- Desktop: info button on right -->
                <button
                  @click="showInfoTooltip = true"
                  class="w-6 h-6 items-center justify-center transition-colors flex-shrink-0 hidden sm:flex"
                >
                  <svg width="20" height="20" viewBox="0 0 20 20" class="text-gray-600">
                    <path d="M10 2C5.5888 2 2 5.58885 2 10C2 14.4112 5.5888 18 10 18C14.4112 18 18 14.4112 18 10C18 5.58885 14.4112 2 10 2ZM10 16.5455C6.39079 16.5455 3.45455 13.6092 3.45455 10C3.45455 6.39088 6.39079 3.45455 10 3.45455C13.6092 3.45455 16.5455 6.39088 16.5455 10C16.5455 13.6092 13.6092 16.5455 10 16.5455Z" fill="currentColor"/>
                    <path d="M10 5.39453C9.46543 5.39453 9.03052 5.82973 9.03052 6.36466C9.03052 6.89911 9.46543 7.33393 10 7.33393C10.5346 7.33393 10.9695 6.89911 10.9695 6.36466C10.9695 5.82973 10.5346 5.39453 10 5.39453Z" fill="currentColor"/>
                    <path d="M9.99998 8.78711C9.59833 8.78711 9.27271 9.11273 9.27271 9.51438V13.878C9.27271 14.2797 9.59833 14.6053 9.99998 14.6053C10.4016 14.6053 10.7273 14.2797 10.7273 13.878V9.51438C10.7273 9.11273 10.4016 8.78711 9.99998 8.78711Z" fill="currentColor"/>
                  </svg>
                </button>
              </div>
            </div>

            <!-- Discount Section -->
            <div class="bg-gray-100 rounded-xl p-1.5 sm:p-3 flex flex-col justify-center items-end text-right min-w-0 flex-1">
              <div class="flex items-center justify-between w-full mb-0.5 sm:mb-1">
                <div class="text-white text-xs font-bold px-1.5 py-0.5 rounded sm:px-2" style="background-color: #FF0000">
                  {{ balance.discountPrice.toFixed(2) }} USD
                </div>
                <div class="text-sm sm:text-base font-semibold text-gray-700">
                  {{ balance.discount }}% OFF
                </div>
              </div>
              <div class="text-[10px] sm:text-xs text-gray-500 leading-tight">
                Offer valid until {{ balance.discountEnd || '...' }}
              </div>
            </div>
          </div>

          <!-- Available Section (no discount) - Always horizontal layout -->
          <div v-else class="bg-green-100 rounded-xl p-2 sm:p-3 flex items-center justify-between mb-3">
            <div class="flex items-center gap-2">
              <span class="text-sm text-gray-600 font-medium">Available</span>
              <template v-if="balance.availableAmount">
                <span class="w-1.5 h-1.5 bg-gray-400 rounded-full"></span>
                <div class="flex items-center gap-1">
                  <svg width="14" height="14" viewBox="0 0 14 14" class="text-black">
                    <path d="M12.86 1.4H4.38C4.007 1.4 3.74 1.667 3.74 2.04V4.654H1.34C0.967 4.707 0.7 4.974 0.7 5.347C0.7 5.72 0.967 5.987 1.34 5.987H3.74V11.96C3.74 12.334 4.007 12.6 4.38 12.6C4.754 12.6 5.02 12.334 5.02 11.96V9.187H7.74C8.114 9.187 8.38 8.92 8.38 8.547C8.38 8.174 8.114 7.907 7.74 7.907H5.02V5.934H10.194C10.567 5.934 10.834 5.667 10.834 5.294C10.834 4.92 10.567 4.654 10.194 4.654H5.02V2.68H12.807C13.18 2.68 13.447 2.414 13.447 2.04C13.447 1.667 13.234 1.4 12.86 1.4Z" fill="currentColor"/>
                  </svg>
                  <span class="text-sm font-medium text-black">{{ balance.availableAmount }}</span>
                </div>
              </template>
              <template v-else>
                <span class="text-sm text-gray-600 font-medium">without restrictions</span>
              </template>
            </div>
            <button
              @click="showInfoTooltip = true"
              class="w-6 h-6 flex items-center justify-center transition-colors"
            >
              <svg width="20" height="20" viewBox="0 0 20 20" class="text-gray-600">
                <path d="M10 2C5.5888 2 2 5.58885 2 10C2 14.4112 5.5888 18 10 18C14.4112 18 18 14.4112 18 10C18 5.58885 14.4112 2 10 2ZM10 16.5455C6.39079 16.5455 3.45455 13.6092 3.45455 10C3.45455 6.39088 6.39079 3.45455 10 3.45455C13.6092 3.45455 16.5455 6.39088 16.5455 10C16.5455 13.6092 13.6092 16.5455 10 16.5455Z" fill="currentColor"/>
                <path d="M10 5.39453C9.46543 5.39453 9.03052 5.82973 9.03052 6.36466C9.03052 6.89911 9.46543 7.33393 10 7.33393C10.5346 7.33393 10.9695 6.89911 10.9695 6.36466C10.9695 5.82973 10.5346 5.39453 10 5.39453Z" fill="currentColor"/>
                <path d="M9.99998 8.78711C9.59833 8.78711 9.27271 9.11273 9.27271 9.51438V13.878C9.27271 14.2797 9.59833 14.6053 9.99998 14.6053C10.4016 14.6053 10.7273 14.2797 10.7273 13.878V9.51438C10.7273 9.11273 10.4016 8.78711 9.99998 8.78711Z" fill="currentColor"/>
              </svg>
            </button>
          </div>

          <!-- Values Section -->
          <div class="bg-purple-50 rounded-xl p-3 mb-3">
            <div class="flex justify-between items-center mb-2">
              <span class="text-sm text-gray-600 font-medium">Current value</span>
              <span class="text-base font-semibold text-gray-700">${{ balance.currentValue.toLocaleString() }}</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="text-sm text-gray-600 font-medium">Potential worth</span>
              <span class="text-base font-semibold text-gray-700">${{ balance.potentialWorth.toLocaleString() }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State (when no balances from backend) -->
    <div v-else class="flex-1 flex items-center justify-center">
      <div class="text-center">
        <div class="w-16 h-16 bg-gray-200 rounded-full flex items-center justify-center mx-auto mb-4">
          <svg width="32" height="32" viewBox="0 0 32 32" class="text-gray-400">
            <path d="M30.667 7.381V1.333H7.129V9.011H1.333V15.059H7.129V30.108H13.894V22.728H19.615V16.680H13.894V15.059H25.132V9.011H13.894V7.381H30.667Z" fill="currentColor"/>
          </svg>
        </div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">No Balances Found</h3>
        <p class="text-gray-600 mb-4">Your balance data will appear here when available.</p>
      </div>
    </div>

    <!-- Success Notification -->
    <SuccessNotification
      :is-visible="showSuccessNotification"
      :class="{ 'blur-notification': isAnyModalOpen }"
      :bottom-offset="bottomNavRef?.bottomOffset || 120"
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
    <BottomNavigation ref="bottomNavRef" />

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
const bottomNavRef = ref(null)
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
const totalBalance = ref(0)
const totalWorth = ref(0)
const balances = ref([]) // Will be populated from backend

// Store user balances and available amounts
const userBalances = ref({})
const availableForevers = ref({})

// API base URL
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

// Fetch user balances and available forevers
const fetchUserBalances = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/forevers/me`, { credentials: 'include' })
    const result = await response.json()
    if (result.status !== 'success') return
    userBalances.value = result?.forevers_balance || {}
    availableForevers.value = result?.available_forevers || {}
    totalBalance.value = parseFloat(userBalances.value.balance || 0)
  } catch (error) {
    console.error('Failed to fetch user balances:', error)
  }
}

const fetchBalancesFromBackend = async () => {
  isLoading.value = true
  try {
    // Fetch prices and discounts
    const pricesResponse = await fetch('https://dbdc-mini.dubadu.com/api/v1/dbdc/prices/forevers')
    const pricesResult = await pricesResponse.json()
    const prices = pricesResult?.data?.prices || []
    const discounts = pricesResult?.data?.discounts || []
    const discountedPrices = pricesResult?.data?.discounted_prices || []

    // Fetch user balances
    await fetchUserBalances()

    // Map by type for easier lookup
    const priceMap = Object.fromEntries(prices.map(p => [p.type, p.value]))
    const discountMap = Object.fromEntries(discounts.map(d => [d.type, d]))
    const discountedPriceMap = Object.fromEntries(discountedPrices.map(dp => [dp.type, dp.value]))

    // Compose balances array using user balances and available forevers
    // Helper: parse end_date strings that may be just a date (YYYY-MM-DD) or full ISO.
    const parseDiscountEnd = (value) => {
      if (!value) return null
      // Trim and normalize
      const v = String(value).trim()
      // If only date part (no time), treat as end of that day in UTC (23:59:59)
      if (/^\d{4}-\d{2}-\d{2}$/.test(v)) {
        return new Date(v + 'T23:59:59Z').getTime()
      }
      // Replace space with T if present (e.g. '2025-08-10 23:59:59') and assume UTC
      const candidate = v.includes(' ') && !v.endsWith('Z') ? v.replace(' ', 'T') + 'Z' : v
      const ts = Date.parse(candidate)
      return isNaN(ts) ? null : ts
    }

    const nowTs = Date.now()

    const rawBalances = prices.map(p => {
      const type = p.type
      const discountObj = discountMap[type] || {}
      const discountedPrice = discountedPriceMap[type] || priceMap[type]
      const discount = parseFloat(discountObj.discount || '0')
      const discountEnd = discountObj.end_date || null
      const discountEndTs = parseDiscountEnd(discountEnd)
      const discountActive = discount > 0 && discountEndTs !== null && discountEndTs >= nowTs

      // Use actual user balance and available amount
      const amount = parseFloat(userBalances.value[`balance_${type.toLowerCase()}`] || 0)
      const usdRate = parseFloat(priceMap[type])
      // If discount expired -> reset discount related values
      const effectiveDiscount = discountActive ? discount : 0
      const discountPrice = discountActive ? parseFloat(discountedPrice) : usdRate

      // UAE potential worth special case
      let potentialWorth
      if (type === 'UAE') {
        potentialWorth = amount * 20
      } else {
        potentialWorth = usdRate * amount
      }

      // priceChange calculation: percent difference between price and discount price
      let priceChange = 0
      if (usdRate > discountPrice) {
        priceChange = ((usdRate - discountPrice) / usdRate) * 100
      } else {
        priceChange = 0
      }

      const availableAmount = availableForevers.value[type] !== undefined ? availableForevers.value[type] : null

      // currentValue = discount price * count forevers
      const currentValue = discountPrice * amount

      return {
        id: type.toLowerCase(),
        country: `Forevers ${type}`,
        code: type,
        amount,
        usdRate,
        discountPrice,
        priceChange,
        currentValue,
        potentialWorth,
        availableAmount,
  discount: effectiveDiscount,
  discountEnd: discountActive ? discountEnd : null,
  discountExpired: discount > 0 && !discountActive && discountEndTs !== null
      }
    })

    balances.value = rawBalances

    // totalWorth сейчас считается так:
    // Это сумма всех currentValue (discount price * count forevers)
    totalWorth.value = balances.value.reduce((sum, b) => sum + b.currentValue, 0)

    isLoading.value = false
  } catch (error) {
    console.error('Failed to fetch balances:', error)
    isLoading.value = false
  }
}

const fetchTotalBalance = async () => {
  // Now handled in fetchBalancesFromBackend
  // Remove mock data and API call here
}

// Methods
const handleRentOut = () => {
  router.push('/rent-out')
}

const openEnterAmountModal = (balance) => {
  // Передаем в selectedBalance цену для модального окна: discountPrice если есть скидка, иначе usdRate
  const modalPrice = balance.discount && balance.discount > 0 ? balance.discountPrice : balance.usdRate
  selectedBalance.value = { ...balance, modalPrice }
  console.log('Opening modal for balance:', selectedBalance.value)
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

/* Performance optimizations */
* {
  will-change: auto;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
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

/* Hide scrollbar in scrollable area */
.overflow-y-auto {
  scrollbar-width: none;
  -ms-overflow-style: none;
  -webkit-overflow-scrolling: touch;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
  will-change: scroll-position;
  overscroll-behavior-x: none;
}

.overflow-y-auto::-webkit-scrollbar {
  display: none;
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
