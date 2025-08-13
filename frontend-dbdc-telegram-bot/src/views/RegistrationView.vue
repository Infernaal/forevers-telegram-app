<template>
  <div class="w-full min-h-screen bg-white font-montserrat overflow-hidden flex flex-col">
    <!-- Main Content -->
    <div class="flex-1 flex items-center justify-center p-4 sm:p-6 md:p-8">
      <div class="w-full max-w-[375px] mx-auto">
        <!-- Main Registration Card -->
        <div class="w-full rounded-3xl bg-gradient-to-r from-dbd-primary to-[#473FFF] relative overflow-hidden">
          <!-- Gradient overlay -->
          <div class="absolute inset-0 bg-black bg-opacity-25"></div>
          
          <!-- Content -->
          <div class="relative p-4 pb-8">
            <!-- Header Text -->
            <div class="text-center pt-5 pb-6">
              <h1 class="text-white text-lg sm:text-xl font-bold leading-6 mb-6">
                We require additional information to continue with your registration.
              </h1>
              <p class="text-white text-sm font-medium leading-6 opacity-90">
                Please enter additional details about yourself below.
              </p>
            </div>

            <!-- Registration Form -->
            <div class="space-y-6">
              <!-- Section Title -->
              <h2 class="text-white text-base font-medium">Complete Registration</h2>

              <!-- Email Field -->
              <div class="relative">
                <div class="w-full h-[52px] rounded-lg border border-[#B7B7B7] bg-white flex items-center px-3">
                  <svg class="w-6 h-6 mr-2 flex-shrink-0" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M21.4037 13.3072C21.8438 13.3072 22.2005 12.9775 22.2005 12.5706V7.7461C22.2005 6.12151 20.7706 4.7998 19.013 4.7998H4.98804C3.23045 4.7998 1.80054 6.12151 1.80054 7.7461V16.2535C1.80054 17.8781 3.23045 19.1998 4.98804 19.1998H19.013C20.7706 19.1998 22.2005 17.8781 22.2005 16.2535C22.2005 15.8467 21.8438 15.5169 21.4037 15.5169C20.9635 15.5169 20.6068 15.8467 20.6068 16.2535C20.6068 17.0658 19.8918 17.7267 19.013 17.7267H4.98804C4.10924 17.7267 3.39429 17.0658 3.39429 16.2535V7.90218L10.3173 11.8813C10.8365 12.1797 11.4185 12.3289 12.0005 12.3289C12.5826 12.3289 13.1646 12.1797 13.6837 11.8813L20.6068 7.90218V12.5706C20.6068 12.9775 20.9635 13.3072 21.4037 13.3072ZM12.8421 10.6303C12.323 10.9286 11.678 10.9287 11.159 10.6303L4.05924 6.54961C4.32093 6.37556 4.64176 6.27295 4.98804 6.27295H19.013C19.3593 6.27295 19.6801 6.37559 19.9418 6.54964L12.8421 10.6303Z" fill="#4B4D50"/>
                  </svg>
                  <input 
                    v-model="formData.email"
                    type="email" 
                    placeholder="Email *"
                    class="flex-1 text-sm font-medium text-dbd-light-gray placeholder-dbd-light-gray bg-transparent border-none outline-none"
                  />
                </div>
              </div>

              <!-- First Name Field -->
              <div class="relative">
                <div class="w-full h-[52px] rounded-lg border border-[#B7B7B7] bg-white flex items-center px-3">
                  <input 
                    v-model="formData.firstName"
                    type="text" 
                    placeholder="First name*"
                    class="flex-1 text-sm font-medium text-dbd-light-gray placeholder-dbd-light-gray bg-transparent border-none outline-none"
                  />
                </div>
              </div>

              <!-- Last Name Field -->
              <div class="relative">
                <div class="w-full h-[52px] rounded-lg border border-[#B7B7B7] bg-white flex items-center px-3">
                  <input 
                    v-model="formData.lastName"
                    type="text" 
                    placeholder="Last name*"
                    class="flex-1 text-sm font-medium text-dbd-light-gray placeholder-dbd-light-gray bg-transparent border-none outline-none"
                  />
                </div>
              </div>

              <!-- Divider Line -->
              <div class="w-full h-px bg-dbd-off-white opacity-50"></div>

              <!-- Country Selector -->
              <div class="relative">
                <div class="w-full h-[52px] rounded-lg border border-[#B7B7B7] bg-white flex items-center px-3 cursor-pointer" @click="toggleCountryDropdown">
                  <svg class="w-6 h-6 mr-2 flex-shrink-0" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M20.4375 12.75C20.8517 12.75 21.1875 12.4142 21.1875 12C21.1875 11.5858 20.8517 11.25 20.4375 11.25L20.4375 12L20.4375 12.75ZM21 12H20.25C20.25 16.5563 16.5563 20.25 12 20.25V21V21.75C17.3848 21.75 21.75 17.3848 21.75 12H21ZM12 21V20.25C7.44365 20.25 3.75 16.5563 3.75 12H3H2.25C2.25 17.3848 6.61522 21.75 12 21.75V21ZM3 12H3.75C3.75 7.44365 7.44365 3.75 12 3.75V3V2.25C6.61522 2.25 2.25 6.61522 2.25 12H3ZM12 3V3.75C16.5563 3.75 20.25 7.44365 20.25 12H21H21.75C21.75 6.61522 17.3848 2.25 12 2.25V3ZM12 21V20.25C11.7045 20.25 11.3639 20.1163 10.9886 19.7535C10.6098 19.3873 10.2344 18.8211 9.90289 18.0633C9.24079 16.55 8.8125 14.4069 8.8125 12H8.0625H7.3125C7.3125 14.5637 7.76565 16.9206 8.52865 18.6646C8.90966 19.5355 9.38272 20.2873 9.94605 20.8319C10.513 21.3801 11.2082 21.75 12 21.75V21ZM8.0625 12H8.8125C8.8125 9.59314 9.24079 7.45001 9.90289 5.93665C10.2344 5.17886 10.6098 4.61271 10.9886 4.24648C11.3639 3.88373 11.7045 3.75 12 3.75V3V2.25C11.2082 2.25 10.513 2.61995 9.94605 3.16805C9.38272 3.71267 8.90966 4.46454 8.52865 5.33542C7.76565 7.07943 7.3125 9.4363 7.3125 12H8.0625ZM12 21V21.75C12.7918 21.75 13.487 21.3801 14.054 20.8319C14.6173 20.2873 15.0903 19.5355 15.4714 18.6646C16.2344 16.9206 16.6875 14.5637 16.6875 12H15.9375H15.1875C15.1875 14.4069 14.7592 16.55 14.0971 18.0633C13.7656 18.8211 13.3902 19.3873 13.0114 19.7535C12.6361 20.1163 12.2955 20.25 12 20.25V21ZM15.9375 12H16.6875C16.6875 9.4363 16.2344 7.07943 15.4714 5.33542C15.0903 4.46454 14.6173 3.71267 14.054 3.16805C13.487 2.61995 12.7918 2.25 12 2.25V3V3.75C12.2955 3.75 12.6361 3.88373 13.0114 4.24648C13.3902 4.61271 13.7656 5.17886 14.0971 5.93665C14.7592 7.45001 15.1875 9.59314 15.1875 12H15.9375ZM3 12L3 12.75L20.4375 12.75L20.4375 12L20.4375 11.25L3 11.25L3 12Z" fill="#4B4D50"/>
                  </svg>
                  <span class="flex-1 text-sm font-medium text-dbd-light-gray">
                    {{ formData.country || 'Country' }}
                  </span>
                  <div class="w-5 h-5 rounded-full border border-[#CFCFCF] bg-white flex items-center justify-center transform -rotate-90">
                    <svg class="w-3 h-3" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                      <path d="M8 14L12 10L8 6" stroke="#4B4D50" stroke-linecap="round"/>
                    </svg>
                  </div>
                </div>
              </div>

              <!-- Phone Number Field -->
              <div class="relative">
                <div class="w-full h-[52px] rounded-lg border border-[#B7B7B7] bg-white flex items-center px-3">
                  <svg class="w-6 h-6 mr-2 flex-shrink-0" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M22.4979 18.4211C22.4686 17.6088 22.1303 16.8508 21.5452 16.2866C20.3996 15.1819 19.4397 14.5442 18.5245 14.2797C17.2635 13.9153 16.0954 14.2467 15.0529 15.2648C15.0513 15.2663 15.0498 15.2678 15.0482 15.2694L13.9392 16.3702C13.246 15.9795 11.8983 15.1216 10.4421 13.6654L10.3342 13.5576C8.8778 12.1012 8.01995 10.7532 7.62961 10.0608L8.73047 8.95173C8.73203 8.95018 8.73358 8.94862 8.73514 8.94702C9.75319 7.90464 10.0846 6.73659 9.72017 5.4754C9.45566 4.56021 8.81799 3.60036 7.71328 2.45475C7.14915 1.86974 6.39114 1.53136 5.57883 1.50207C4.76602 1.47274 3.98607 1.75567 3.38117 2.29864L3.35763 2.3198C3.34672 2.32961 3.33605 2.33974 3.32564 2.35011C2.12146 3.5543 1.49023 5.24009 1.50011 7.2253C1.51697 10.5977 3.37043 14.4543 6.45804 17.5419C7.04026 18.1241 7.70196 18.7003 8.42474 19.2545C8.78424 19.5302 9.29915 19.4622 9.57481 19.1027C9.85052 18.7432 9.78252 18.2282 9.42297 17.9526C8.75709 17.442 8.14985 16.9135 7.61812 16.3819C4.82923 13.593 3.15542 10.167 3.1407 7.21713C3.13311 5.68823 3.59302 4.4121 4.47087 3.52509L4.47715 3.51943C5.07339 2.98422 5.97611 3.01679 6.53236 3.59359C8.65611 5.79606 8.50234 6.83585 7.5639 7.79816L6.04329 9.33019C5.80482 9.57046 5.73842 9.93255 5.87611 10.2418C5.91471 10.3285 6.84859 12.3921 9.17438 14.7179L9.28237 14.8258C11.6079 17.1513 13.6715 18.0852 13.7582 18.1238C14.0674 18.2615 14.4296 18.1951 14.6698 17.9566L16.2019 16.436C17.1643 15.4975 18.2041 15.3438 20.4064 17.4676C20.9832 18.0237 21.0158 18.9265 20.4807 19.5227L20.4749 19.5291C19.5951 20.3998 18.3326 20.8594 16.8203 20.8594C16.8079 20.8594 16.7954 20.8594 16.7829 20.8593C15.5741 20.8533 14.1744 20.5219 12.7351 19.9011C12.3192 19.7216 11.8364 19.9134 11.657 20.3294C11.4776 20.7454 11.6693 21.2281 12.0853 21.4075C13.749 22.1252 15.3267 22.4927 16.7747 22.4999C16.7901 22.5 16.8054 22.5 16.8208 22.5C18.786 22.5 20.455 21.8692 21.6499 20.6744C21.6603 20.664 21.6704 20.6533 21.6802 20.6424L21.7014 20.6187C22.2444 20.0139 22.5273 19.2334 22.4979 18.4211Z" fill="#4B4D50"/>
                  </svg>
                  <div class="flex flex-col items-start justify-center flex-1">
                    <span class="text-xs text-dbd-gray font-medium leading-none">Your Phone #</span>
                    <div class="flex items-center w-full mt-1">
                      <span class="text-sm text-dbd-light-gray font-medium">Country code</span>
                      <div class="w-px h-7 bg-dbd-light-gray mx-2"></div>
                      <input 
                        v-model="formData.phone"
                        type="tel" 
                        placeholder="__ - ___ - ___"
                        class="flex-1 text-base font-medium text-dbd-gray bg-transparent border-none outline-none"
                      />
                    </div>
                  </div>
                  <div class="w-5 h-5 rounded-full border border-[#CFCFCF] bg-white flex items-center justify-center transform -rotate-90">
                    <svg class="w-3 h-3" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                      <path d="M8 14L12 10L8 6" stroke="#4B4D50" stroke-linecap="round"/>
                    </svg>
                  </div>
                </div>
              </div>

              <!-- Register Button -->
              <div class="pt-4">
                <button
                  @click="handleRegister"
                  :disabled="!isFormValid"
                  :class="[
                    'w-full h-[52px] rounded-full font-bold text-base flex items-center justify-center gap-2',
                    'border transition-all duration-200',
                    isFormValid 
                      ? 'bg-dbd-primary text-white border-dbd-primary active:scale-[0.98]' 
                      : 'bg-[#E2E2E2] text-[#989898] border-[#C7C7C7] cursor-not-allowed'
                  ]"
                >
                  Register
                  <svg class="w-6 h-6" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M1.03895 13.0391L20.4531 13.0391L15.8206 17.6718C15.4147 18.0774 15.4147 18.7354 15.8206 19.1409C16.2264 19.5468 16.8844 19.5468 17.2896 19.1409L23.6956 12.7348C24.1015 12.3292 24.1015 11.6712 23.6956 11.2657L17.2896 4.85927C17.0867 4.6563 16.8209 4.55496 16.5551 4.55496C16.2893 4.55496 16.0234 4.6563 15.8206 4.85927C15.4147 5.26487 15.4147 5.92282 15.8206 6.3283L20.4531 10.9613L1.03895 10.9613C0.465234 10.9613 -1.69986e-06 11.4265 -1.75002e-06 12.0002C-1.80017e-06 12.5739 0.465174 13.0391 1.03895 13.0391Z"/>
                  </svg>
                </button>
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

const router = useRouter()

// Form data
const formData = ref({
  email: '',
  firstName: '',
  lastName: '',
  country: '',
  phone: ''
})

// Computed properties
const isFormValid = computed(() => {
  return formData.value.email && 
         formData.value.firstName && 
         formData.value.lastName && 
         formData.value.country && 
         formData.value.phone
})

// Methods
const toggleCountryDropdown = () => {
  // Handle country dropdown toggle
  console.log('Country dropdown clicked')
}

const handleRegister = () => {
  if (!isFormValid.value) return
  
  // Add haptic feedback if available
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'medium')
  }

  console.log('Registration submitted:', formData.value)
  // Handle registration logic here
}
</script>

<style scoped>
/* Mobile-first responsive design */
@media (min-width: 768px) {
  .w-full.max-w-\[375px\] {
    max-width: 500px;
  }
}

@media (min-width: 1024px) {
  .w-full.max-w-\[375px\] {
    max-width: 600px;
  }
}

/* Prevent zoom on mobile inputs */
@media (max-width: 768px) {
  input, button, select, textarea {
    font-size: 16px;
  }
}

/* Button hover states for touch devices */
@media (hover: none) and (pointer: coarse) {
  button:hover {
    transform: none;
  }
  
  button:active {
    opacity: 0.8;
  }
}

/* Performance optimizations */
* {
  will-change: auto;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}
</style>
