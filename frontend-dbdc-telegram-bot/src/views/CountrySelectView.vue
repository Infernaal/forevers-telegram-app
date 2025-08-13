<template>
  <div class="w-full h-screen bg-white font-montserrat flex flex-col overflow-hidden" style="padding-bottom: max(var(--tg-content-safe-area-inset-bottom, 0px), env(safe-area-inset-bottom, 0px));">
    <!-- Main Content -->
    <div class="flex-1 flex flex-col h-full px-4 md:px-6 pt-4 md:pt-6">
      <!-- Title -->
      <div class="mb-6 flex-shrink-0">
        <h1 class="text-dbd-dark text-lg font-semibold">Select your country</h1>
      </div>

      <!-- Search Section -->
      <div class="mb-6 flex-shrink-0">
        <!-- Search Input -->
        <div class="relative mb-4">
          <div class="w-full h-[50px] rounded-[29px] border border-[#D8D8D8] bg-[#FAFAFA] flex items-center">
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search country"
              class="flex-1 px-5 py-4 text-[15px] font-medium text-dbd-dark placeholder-dbd-light-gray bg-transparent border-none outline-none rounded-l-[29px]"
            />
            <div class="w-12 h-[50px] rounded-r-[25px] border-l border-[#C7C7C7] bg-white flex items-center justify-center">
              <svg 
                class="w-6 h-6 text-dbd-light-gray" 
                fill="none" 
                xmlns="http://www.w3.org/2000/svg" 
                viewBox="0 0 24 24"
              >
                <path 
                  d="M10.0494 18.4507C11.837 18.4507 13.5735 17.8486 14.9838 16.7395L20.3045 22.1115C20.7019 22.499 21.3353 22.4879 21.7192 22.0866C22.0936 21.6952 22.0936 21.0746 21.7192 20.6831L16.3985 15.3111C19.1243 11.7685 18.4895 6.66563 14.9807 3.91356C11.472 1.1615 6.41791 1.80236 3.69215 5.34501C0.966393 8.88766 1.60113 13.9905 5.10992 16.7426C6.52252 17.8506 8.26058 18.4516 10.0494 18.4507ZM5.77429 6.01269C8.13538 3.62877 11.9635 3.62872 14.3246 6.0126C16.6857 8.39648 16.6858 12.2615 14.3247 14.6454C11.9636 17.0294 8.13551 17.0294 5.77438 14.6455C5.77434 14.6455 5.77434 14.6455 5.77429 14.6454C3.4132 12.2789 3.39929 8.42798 5.74318 6.04411C5.75354 6.0336 5.76389 6.02315 5.77429 6.01269Z" 
                  fill="currentColor"
                />
              </svg>
            </div>
          </div>
        </div>

        <!-- Results Count -->
        <div class="text-right px-5">
          <span class="text-[15px] font-bold text-dbd-dark">{{ filteredCountries.length }}</span>
          <span class="text-[15px] text-[#8F8F8F] ml-1">results</span>
        </div>
      </div>

      <!-- Countries List -->
      <div class="relative flex-1 min-h-0">
        <div class="h-full overflow-y-auto scrollbar-custom">
          <div class="space-y-2">
            <div
              v-for="country in filteredCountries"
              :key="country.code"
              @click="selectCountry(country)"
              :class="[
                'flex items-center w-full h-[52px] px-3 gap-3 cursor-pointer transition-all duration-200 hover:bg-gray-50',
                selectedCountry?.code === country.code 
                  ? 'bg-dbd-light-orange border border-dbd-orange rounded-l-[30px]' 
                  : 'rounded-l-[30px]'
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

        <!-- Custom Scrollbar Indicator -->
        <div
          v-if="filteredCountries.length > 8"
          class="absolute right-2 top-4 w-1.5 h-24 bg-[#D9D9D9] rounded-full pointer-events-none"
        ></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import CountryFlag from '@/components/CountryFlag.vue'

const router = useRouter()
const emit = defineEmits(['select-country'])

// Search functionality
const searchQuery = ref('')

// Selected country
const selectedCountry = ref(null)

// Countries list (matching the existing registration view)
const countries = ref([
  { name: 'India', code: 'IN' },
  { name: 'United Arab Emirates', code: 'UAE' },
  { name: 'United States', code: 'USA' },
  { name: 'United Kingdom', code: 'GB' },
  { name: 'Canada', code: 'CA' },
  { name: 'New Zealand', code: 'NZ' },
  { name: 'Spain', code: 'ES' },
  { name: 'Italy', code: 'IT' },
  { name: 'Japan', code: 'JP' },
  { name: 'Australia', code: 'AU' },
  { name: 'Germany', code: 'DE' },
  { name: 'France', code: 'FR' },
  { name: 'Netherlands', code: 'NL' },
  { name: 'Norway', code: 'NO' },
  { name: 'Ireland', code: 'IE' },
  { name: 'South Korea', code: 'KR' },
  { name: 'Singapore', code: 'SG' },
  { name: 'China', code: 'CN' },
  { name: 'Kazakhstan', code: 'KZ' },
  { name: 'Poland', code: 'PL' },
  { name: 'Ukraine', code: 'UA' },
  { name: 'Russia', code: 'RU' },
  { name: 'Portugal', code: 'PT' },
  { name: 'Malta', code: 'MT' }
])

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

  // Navigate back after a brief delay to show the selection
  setTimeout(() => {
    router.back()
  }, 300)
}

// Set default selection (like in the design - United States)
selectedCountry.value = countries.value.find(country => country.code === 'USA')
</script>

<style scoped>
/* Custom scrollbar */
.scrollbar-custom {
  scrollbar-width: thin;
  scrollbar-color: #D9D9D9 transparent;
}

.scrollbar-custom::-webkit-scrollbar {
  width: 6px;
}

.scrollbar-custom::-webkit-scrollbar-track {
  background: transparent;
}

.scrollbar-custom::-webkit-scrollbar-thumb {
  background-color: #D9D9D9;
  border-radius: 30px;
}

.scrollbar-custom::-webkit-scrollbar-thumb:hover {
  background-color: #C1C1C1;
}

/* Prevent zoom on mobile inputs */
@media (max-width: 768px) {
  input {
    font-size: 16px;
  }
}

/* Responsive adjustments */
@media (min-width: 768px) {
  .w-full {
    max-width: 600px;
    margin: 0 auto;
  }
}

@media (min-width: 1024px) {
  .w-full {
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
