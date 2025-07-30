<template>
  <div v-if="isVisible" 
       class="fixed inset-0 bg-black/20 backdrop-blur-[9px] z-[10000] 
              flex items-start justify-center 
              p-2 pt-4 sm:p-4 sm:pt-8 md:p-6 md:pt-12 lg:p-8 lg:pt-16
              animate-[fadeIn_0.3s_ease-out]" 
       @click="closeModal">
    <div class="w-full 
                max-w-[320px] sm:max-w-[400px] md:max-w-[500px] lg:max-w-[600px] xl:max-w-[650px]
                max-h-[88vh] sm:max-h-[85vh] md:max-h-[82vh] lg:max-h-[80vh]
                min-h-[75vh] sm:min-h-[70vh] md:min-h-[65vh] lg:min-h-[60vh]
                bg-white border border-gray-200 rounded-2xl sm:rounded-3xl
                shadow-[1.744px_2.616px_20.93px_0_rgba(2,7,14,0.04)]
                flex flex-col
                animate-[slideUp_0.3s_ease-out]" 
         @click.stop>
      <!-- Modal Content -->
      <div class="flex flex-col h-full max-h-[88vh] sm:max-h-[85vh] md:max-h-[82vh] lg:max-h-[80vh]">
        <!-- Header -->
        <div class="flex-shrink-0 p-3 sm:p-4 md:p-5 lg:p-6 pb-0">
          <h1 class="text-dbd-dark font-montserrat 
                     text-lg sm:text-xl md:text-2xl lg:text-3xl xl:text-4xl
                     font-bold leading-tight capitalize 
                     mb-2 sm:mb-3 md:mb-4">
            Forevers Leasing Terms & Conditions
          </h1>
          <p class="text-dbd-gray font-montserrat 
                    text-sm sm:text-base md:text-lg lg:text-xl
                    font-medium leading-relaxed capitalize 
                    mb-4 sm:mb-5 md:mb-6">
            Last Updated: July 16, 2025
          </p>
        </div>

        <!-- Scrollable Content -->
        <div class="flex-1 overflow-y-auto px-3 sm:px-4 md:px-5 lg:px-6
                    scrollbar-none [-ms-overflow-style:none] [scrollbar-width:none]
                    [&::-webkit-scrollbar]:hidden">
          <div class="pb-4 sm:pb-5 md:pb-6">
            <!-- Introduction -->
            <p class="text-dbd-gray font-montserrat 
                      text-sm sm:text-base md:text-lg lg:text-xl
                      font-medium leading-relaxed 
                      mb-6 sm:mb-8 md:mb-10 lg:mb-12">
              These Terms and Conditions govern your use of DBDC (the "Service"). By accessing or using the Service, you agree to be bound by these Terms. If you do not agree with these Terms, do not use the Service.
            </p>

            <!-- Sections -->
            <div class="flex flex-col gap-6 sm:gap-8 md:gap-10 lg:gap-12">
              <!-- Definitions -->
              <section class="flex flex-col gap-3 sm:gap-4 md:gap-5">
                <h2 class="text-dbd-dark font-montserrat 
                           text-base sm:text-lg md:text-xl lg:text-2xl xl:text-3xl
                           font-bold leading-tight capitalize">
                  Definitions
                </h2>
                <div class="flex flex-col gap-2 sm:gap-3">
                  <div class="flex items-start gap-3 sm:gap-4 md:gap-5">
                    <div class="w-1.5 h-1.5 sm:w-2 sm:h-2 
                                rounded-full bg-dbd-gray flex-shrink-0 
                                mt-2 sm:mt-2.5 md:mt-3"></div>
                    <p class="text-dbd-gray font-montserrat 
                             text-sm sm:text-base md:text-lg lg:text-xl
                             font-medium leading-relaxed flex-1">
                      "User" refers to any individual or entity that accesses or uses the Service.
                    </p>
                  </div>
                  <div class="flex items-start gap-3 sm:gap-4 md:gap-5">
                    <div class="w-1.5 h-1.5 sm:w-2 sm:h-2 
                                rounded-full bg-dbd-gray flex-shrink-0 
                                mt-2 sm:mt-2.5 md:mt-3"></div>
                    <p class="text-dbd-gray font-montserrat 
                             text-sm sm:text-base md:text-lg lg:text-xl
                             font-medium leading-relaxed flex-1">
                      "Service" refers to the cryptocurrency platform and any related services offered by DBDC.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Eligibility -->
              <section class="flex flex-col gap-3 sm:gap-4 md:gap-5">
                <h2 class="text-dbd-dark font-montserrat 
                           text-base sm:text-lg md:text-xl lg:text-2xl xl:text-3xl
                           font-bold leading-tight capitalize">
                  Eligibility
                </h2>
                <div class="flex flex-col gap-2 sm:gap-3">
                  <div class="flex items-start gap-3 sm:gap-4 md:gap-5">
                    <div class="w-1.5 h-1.5 sm:w-2 sm:h-2 
                                rounded-full bg-dbd-gray flex-shrink-0 
                                mt-2 sm:mt-2.5 md:mt-3"></div>
                    <p class="text-dbd-gray font-montserrat 
                             text-sm sm:text-base md:text-lg lg:text-xl
                             font-medium leading-relaxed flex-1">
                      You must be at least 18 years old and capable of entering into legally binding agreements to use the Service.
                    </p>
                  </div>
                </div>
              </section>

              <!-- User Accounts -->
              <section class="flex flex-col gap-3 sm:gap-4 md:gap-5">
                <h2 class="text-dbd-dark font-montserrat 
                           text-base sm:text-lg md:text-xl lg:text-2xl xl:text-3xl
                           font-bold leading-tight capitalize">
                  User Accounts
                </h2>
                <div class="flex flex-col gap-2 sm:gap-3">
                  <div class="flex items-start gap-3 sm:gap-4 md:gap-5">
                    <div class="w-1.5 h-1.5 sm:w-2 sm:h-2 
                                rounded-full bg-dbd-gray flex-shrink-0 
                                mt-2 sm:mt-2.5 md:mt-3"></div>
                    <p class="text-dbd-gray font-montserrat 
                             text-sm sm:text-base md:text-lg lg:text-xl
                             font-medium leading-relaxed flex-1">
                      Users may be required to create an account to access certain features of the Service. You agree to provide accurate, current, and complete information during the registration process.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Digital Currency Risks -->
              <section class="flex flex-col gap-3 sm:gap-4 md:gap-5">
                <h2 class="text-dbd-dark font-montserrat 
                           text-base sm:text-lg md:text-xl lg:text-2xl xl:text-3xl
                           font-bold leading-tight capitalize">
                  Digital Currency Risks
                </h2>
                <div class="flex flex-col gap-2 sm:gap-3">
                  <div class="flex items-start gap-3 sm:gap-4 md:gap-5">
                    <div class="w-1.5 h-1.5 sm:w-2 sm:h-2 
                                rounded-full bg-dbd-gray flex-shrink-0 
                                mt-2 sm:mt-2.5 md:mt-3"></div>
                    <p class="text-dbd-gray font-montserrat 
                             text-sm sm:text-base md:text-lg lg:text-xl
                             font-medium leading-relaxed flex-1">
                      You acknowledge that there are risks associated with the use of digital currencies, including market volatility and regulatory changes. DBDC is not responsible for any losses incurred.
                    </p>
                  </div>
                </div>
              </section>

              <!-- User Obligations -->
              <section class="flex flex-col gap-3 sm:gap-4 md:gap-5">
                <h2 class="text-dbd-dark font-montserrat 
                           text-base sm:text-lg md:text-xl lg:text-2xl xl:text-3xl
                           font-bold leading-tight capitalize">
                  User Obligations
                </h2>
                <div class="flex flex-col gap-2 sm:gap-3">
                  <div class="flex items-start gap-3 sm:gap-4 md:gap-5">
                    <div class="w-1.5 h-1.5 sm:w-2 sm:h-2 
                                rounded-full bg-dbd-gray flex-shrink-0 
                                mt-2 sm:mt-2.5 md:mt-3"></div>
                    <p class="text-dbd-gray font-montserrat 
                             text-sm sm:text-base md:text-lg lg:text-xl
                             font-medium leading-relaxed flex-1">
                      Users agree to use the Service in compliance with applicable laws and regulations. You will not engage in any fraudulent or illegal activities.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Intellectual Property -->
              <section class="flex flex-col gap-3 sm:gap-4 md:gap-5">
                <h2 class="text-dbd-dark font-montserrat 
                           text-base sm:text-lg md:text-xl lg:text-2xl xl:text-3xl
                           font-bold leading-tight capitalize">
                  Intellectual Property
                </h2>
                <div class="flex flex-col gap-2 sm:gap-3">
                  <div class="flex items-start gap-3 sm:gap-4 md:gap-5">
                    <div class="w-1.5 h-1.5 sm:w-2 sm:h-2 
                                rounded-full bg-dbd-gray flex-shrink-0 
                                mt-2 sm:mt-2.5 md:mt-3"></div>
                    <p class="text-dbd-gray font-montserrat 
                             text-sm sm:text-base md:text-lg lg:text-xl
                             font-medium leading-relaxed flex-1">
                      All content and materials available on the Service are the property of DBDC and protected by intellectual property laws.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Limitation of Liability -->
              <section class="flex flex-col gap-3 sm:gap-4 md:gap-5">
                <h2 class="text-dbd-dark font-montserrat 
                           text-base sm:text-lg md:text-xl lg:text-2xl xl:text-3xl
                           font-bold leading-tight capitalize">
                  Limitation of Liability
                </h2>
                <div class="flex flex-col gap-2 sm:gap-3">
                  <div class="flex items-start gap-3 sm:gap-4 md:gap-5">
                    <div class="w-1.5 h-1.5 sm:w-2 sm:h-2 
                                rounded-full bg-dbd-gray flex-shrink-0 
                                mt-2 sm:mt-2.5 md:mt-3"></div>
                    <p class="text-dbd-gray font-montserrat 
                             text-sm sm:text-base md:text-lg lg:text-xl
                             font-medium leading-relaxed flex-1">
                      DBDC shall not be liable for any indirect, incidental, or consequential damages arising from your use of the Service.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Amendments -->
              <section class="flex flex-col gap-3 sm:gap-4 md:gap-5">
                <h2 class="text-dbd-dark font-montserrat 
                           text-base sm:text-lg md:text-xl lg:text-2xl xl:text-3xl
                           font-bold leading-tight capitalize">
                  Amendments
                </h2>
                <div class="flex flex-col gap-2 sm:gap-3">
                  <div class="flex items-start gap-3 sm:gap-4 md:gap-5">
                    <div class="w-1.5 h-1.5 sm:w-2 sm:h-2 
                                rounded-full bg-dbd-gray flex-shrink-0 
                                mt-2 sm:mt-2.5 md:mt-3"></div>
                    <p class="text-dbd-gray font-montserrat 
                             text-sm sm:text-base md:text-lg lg:text-xl
                             font-medium leading-relaxed flex-1">
                      DBDC reserves the right to modify these Terms at any time. Changes will be effective immediately upon posting.
                    </p>
                  </div>
                </div>
              </section>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex-shrink-0 p-3 sm:p-4 md:p-5 lg:p-6 pt-3 sm:pt-4 md:pt-5
                    flex flex-col gap-2 sm:gap-3 md:gap-4
                    border-t border-gray-100">
          <button class="w-full 
                         h-12 sm:h-13 md:h-14 lg:h-16
                         px-6 sm:px-8 md:px-12 lg:px-16
                         flex items-center justify-center
                         rounded-full
                         bg-gradient-to-r from-dbd-primary to-[#473FFF]
                         text-white text-center font-montserrat 
                         text-xs sm:text-sm md:text-base lg:text-lg
                         font-bold leading-relaxed
                         border-none cursor-pointer
                         transition-all duration-200 ease-out
                         shadow-[0_4px_12px_rgba(32,25,206,0.25)]
                         hover:opacity-90 hover:-translate-y-0.5 hover:shadow-[0_6px_16px_rgba(32,25,206,0.35)]
                         active:translate-y-0
                         touch-manipulation [-webkit-tap-highlight-color:transparent]" 
                  @click="agreeToTerms">
            I agree with Terms & Conditions
          </button>
          <button class="w-full 
                         h-10 sm:h-11 md:h-12 lg:h-14
                         px-6 sm:px-8 md:px-12
                         flex items-center justify-center
                         rounded-full
                         border border-dbd-gray bg-dbd-off-white
                         text-dbd-gray text-center font-montserrat 
                         text-sm sm:text-base md:text-lg lg:text-xl
                         font-medium leading-relaxed
                         cursor-pointer
                         transition-all duration-200 ease-out
                         hover:bg-gray-100 hover:-translate-y-0.5
                         active:translate-y-0
                         touch-manipulation [-webkit-tap-highlight-color:transparent]" 
                  @click="closeModal">
            Back
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineEmits, defineProps } from 'vue'

// Props
const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  }
})

// Emits
const emit = defineEmits(['close', 'agree'])

// Methods
const closeModal = () => {
  emit('close')
}

const agreeToTerms = () => {
  emit('agree')
  emit('close')
}
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideUp {
  from {
    transform: translateY(50px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

/* Custom height utilities */
.h-13 {
  height: 3.25rem;
}
</style>
