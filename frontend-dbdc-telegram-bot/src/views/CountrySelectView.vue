<template>
  <div class="w-full h-screen bg-white font-montserrat flex flex-col overflow-hidden" style="padding-bottom: max(var(--tg-content-safe-area-inset-bottom, 0px), env(safe-area-inset-bottom, 0px));">
    <!-- Main Content -->
    <div class="flex-1 flex flex-col h-full px-4 md:px-6 pt-4 md:pt-6">
      <!-- Title -->
      <div class="mb-6 flex-shrink-0">
        <h1 class="text-dbd-dark text-lg font-semibold">Select your country</h1>
      </div>

      <!-- Search Section -->
      <div class="mb-4 flex-shrink-0">
        <div class="relative">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search country"
            class="w-full h-[50px] rounded-[29px] border border-[#D8D8D8] bg-[#FAFAFA] px-5 py-4 text-[15px] font-medium text-dbd-dark placeholder-dbd-light-gray outline-none"
          />
        </div>
      </div>

      <!-- Countries List (vertical scroll only) -->
      <div class="flex-1 min-h-0 overflow-hidden">
        <div class="h-full overflow-y-auto overflow-x-hidden scrollbar-hidden vertical-only">
          <div class="space-y-2">
            <div
              v-for="country in filteredCountries"
              :key="country.code"
              @click="selectCountry(country)"
              :class="[
                'flex items-center w-full h-[52px] px-3 gap-3 cursor-pointer transition-all duration-300 ease-in-out transform hover:scale-[1.02] active:scale-[0.98] hover:ml-2 hover:mr-2',
                selectedCountry?.code === country.code
                  ? 'bg-dbd-light-orange border border-dbd-orange rounded-l-[30px] scale-[1.02] ml-2 mr-2'
                  : 'rounded-l-[30px] hover:bg-gray-50'
              ]"
            >
              <!-- Selection Indicator -->
              <div v-if="selectedCountry?.code === country.code" class="w-6 h-6 flex items-center justify-center">
                <svg class="w-6 h-6" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                  <path
                    d="M19.3013 4.12255C18.5793 3.68245 17.774 4.53122 17.3019 5.0342C16.2189 6.22877 15.3026 7.61196 14.2751 8.8694C13.1365 10.2526 12.0813 11.6358 10.915 12.9876C10.2485 13.7421 9.52651 14.5594 9.0822 15.5025C8.08251 14.4022 7.22166 13.2076 6.11089 12.2331C5.30558 11.5415 3.97266 11.0385 4.00043 12.7047C4.05597 14.8738 5.74989 17.2001 6.99951 18.6775C7.52712 19.3062 8.22135 19.9664 9.02666 19.9978C9.99859 20.0607 10.9983 18.7404 11.5814 18.0174C12.6089 16.7599 13.442 15.3452 14.3861 14.0564C15.608 12.3589 16.8576 10.6927 18.0517 8.96371C18.8014 7.89488 21.1618 5.2542 19.3013 4.12255ZM5.22223 12.5789C5.19446 12.5789 5.16669 12.5789 5.11115 12.6103C5.00007 12.5789 4.91677 12.5474 4.80569 12.4846C4.889 12.4217 5.02784 12.4531 5.22223 12.5789Z"
                    fill="#FF6319"
                  />
                </svg>
              </div>

              <!-- Country Flag and Name -->
              <div class="flex items-center gap-2 flex-1">
                <CountryFlag :country="country.code" size="small" />
                <div class="flex flex-col justify-center">
                  <div
                    :class="[
                      'text-base font-medium',
                      selectedCountry?.code === country.code ? 'text-dbd-dark' : 'text-[#4D4F53]'
                    ]"
                  >
                    {{ country.name }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import CountryFlag from '@/components/CountryFlag.vue'
import { fullCountries } from '@/utils/allCountries.js'

const router = useRouter()
const emit = defineEmits(['select-country'])

// Search functionality
const searchQuery = ref('')

// Selected country
const selectedCountry = ref(null)

// Countries list (full automatic dataset)
const countries = ref(fullCountries)

// Computed filtered countries based on search
const filteredCountries = computed(() => {
  if (!searchQuery.value.trim()) {
    return countries.value
  }
  
  const query = searchQuery.value.toLowerCase().trim()
  return countries.value.filter(country => 
    country.name.toLowerCase().includes(query) ||
    country.code.toLowerCase().includes(query)
  )
})

// Methods
const selectCountry = (country) => {
  selectedCountry.value = country

  // Add haptic feedback if available
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'light')
  }

  // Store selected country in sessionStorage to pass back to Registration
  sessionStorage.setItem('selectedCountry', JSON.stringify(country))

  // Navigate back immediately with smooth transition
  router.back()
}

// Check if there's a pre-selected country from RegistrationView (for editing)
const preSelectedCountry = sessionStorage.getItem('currentCountry')
if (preSelectedCountry) {
  try {
    const country = JSON.parse(preSelectedCountry)
    selectedCountry.value = country
    sessionStorage.removeItem('currentCountry')
  } catch (error) {
    console.error('Error parsing pre-selected country:', error)
  }
}
</script>

<style scoped>
/* Hidden scrollbar */
.scrollbar-hidden {
  /* Firefox */
  scrollbar-width: none;
  /* Chrome, Safari and Opera */
  -ms-overflow-style: none;
}

.scrollbar-hidden::-webkit-scrollbar {
  display: none;
  width: 0;
  height: 0;
}

/* Remove default focus outline and blue square */
input {
  outline: none !important;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}

input:focus {
  outline: none !important;
  box-shadow: none !important;
  border-color: inherit;
}

/* Prevent zoom on mobile inputs */
@media (max-width: 768px) {
  input {
    font-size: 16px;
  }
}

/* Telegram WebApp support */
body {
  margin: 0;
  padding: 0;
  overflow: hidden;
}

/* Responsive adjustments for larger screens */
@media (min-width: 768px) {
  .w-full.h-screen {
    max-width: 600px;
    margin: 0 auto;
  }
}

@media (min-width: 1024px) {
  .w-full.h-screen {
    max-width: 800px;
    margin: 0 auto;
  }
}

/* Performance optimizations */
* {
  will-change: auto;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}
</style>
<style scoped>
/* Vertical only scrolling (prevent horizontal drag) */
.vertical-only {
  touch-action: pan-y;
  overscroll-behavior: contain;
}
</style>
