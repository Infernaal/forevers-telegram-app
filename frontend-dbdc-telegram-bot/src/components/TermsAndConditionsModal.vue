<template>
  <div v-if="isVisible"
       class="fixed inset-0 bg-black/20 backdrop-blur-[9px] z-[10001]
              flex items-center justify-center
              p-2 sm:p-3 md:p-4 lg:p-6
              animate-[fadeIn_0.3s_ease-out] terms-modal-overlay
              touch-manipulation overscroll-contain
              supports-[height:100dvh]:min-h-[100dvh]"
       @click="closeModal"
       style="height: 100vh; height: 100dvh;">
    <div class="w-full max-w-[calc(100vw-16px)] sm:max-w-[calc(100vw-24px)] md:max-w-md lg:max-w-lg
                h-[calc(100vh-32px)] sm:h-[calc(100vh-48px)] md:h-[calc(100vh-64px)]
                max-h-[calc(100vh-32px)] sm:max-h-[calc(100vh-48px)] md:max-h-[calc(100vh-64px)]
                supports-[height:100dvh]:h-[calc(100dvh-32px)]
                supports-[height:100dvh]:max-h-[calc(100dvh-32px)]
                modal-container animate-[slideUp_0.3s_ease-out]"
         @click.stop
         style="height: calc(100vh - 32px); height: calc(100dvh - 32px);">
      <!-- Modal Content -->
      <div class="bg-white rounded-2xl sm:rounded-3xl border border-gray-200
                  shadow-lg flex flex-col h-full max-h-full overflow-hidden
                  modal-content">
        <!-- Header -->
        <div class="p-3 sm:p-4 md:p-5 flex-shrink-0 border-b border-gray-100
                    modal-header">
          <h1 class="text-dbd-dark font-bold text-base sm:text-lg md:text-xl lg:text-2xl
                     leading-tight mb-1 sm:mb-2 modal-title">
            Forevers Leasing Terms & Conditions
          </h1>
          <p class="text-dbd-gray font-medium text-xs sm:text-sm md:text-base
                    leading-relaxed modal-subtitle">
            Last Updated: July 16, 2025
          </p>
        </div>

        <!-- Scrollable Content -->
        <div class="flex-1 overflow-y-auto overflow-x-hidden p-3 sm:p-4 md:p-5
                    scrollbar-none overscroll-contain modal-scroll-section
                    min-h-0"
             style="max-height: calc(100vh - 200px)">
          <div class="pb-3">
            <!-- Introduction -->
            <p class="text-dbd-gray font-medium text-xs sm:text-sm md:text-base
                      leading-relaxed mb-4 sm:mb-6 modal-intro">
              These Terms and Conditions govern your use of DBDC (the "Service"). By accessing or using the Service, you agree to be bound by these Terms. If you do not agree with these Terms, do not use the Service.
            </p>

            <!-- Sections -->
            <div class="flex flex-col gap-4 sm:gap-6 modal-sections">
              <!-- Definitions -->
              <section class="flex flex-col gap-2 sm:gap-3">
                <h2 class="text-dbd-dark font-bold text-sm sm:text-base md:text-lg
                           leading-tight capitalize">Definitions</h2>
                <div class="flex flex-col gap-2">
                  <div class="flex items-start gap-2 sm:gap-3">
                    <div class="w-1 h-1 sm:w-1.5 sm:h-1.5 rounded-full bg-dbd-gray
                               flex-shrink-0 mt-1.5 sm:mt-2"></div>
                    <p class="text-dbd-gray font-medium text-xs sm:text-sm
                             leading-relaxed flex-1">
                      "User" refers to any individual or entity that accesses or uses the Service.
                    </p>
                  </div>
                  <div class="flex items-start gap-2 sm:gap-3">
                    <div class="w-1 h-1 sm:w-1.5 sm:h-1.5 rounded-full bg-dbd-gray
                               flex-shrink-0 mt-1.5 sm:mt-2"></div>
                    <p class="text-dbd-gray font-medium text-xs sm:text-sm
                             leading-relaxed flex-1">
                      "Service" refers to the cryptocurrency platform and any related services offered by DBDC.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Eligibility -->
              <section class="flex flex-col gap-2 sm:gap-3">
                <h2 class="text-dbd-dark font-bold text-sm sm:text-base md:text-lg
                           leading-tight capitalize">Eligibility</h2>
                <div class="flex flex-col gap-2">
                  <div class="flex items-start gap-2 sm:gap-3">
                    <div class="w-1 h-1 sm:w-1.5 sm:h-1.5 rounded-full bg-dbd-gray
                               flex-shrink-0 mt-1.5 sm:mt-2"></div>
                    <p class="text-dbd-gray font-medium text-xs sm:text-sm
                             leading-relaxed flex-1">
                      You must be at least 18 years old and capable of entering into legally binding agreements to use the Service.
                    </p>
                  </div>
                </div>
              </section>

              <!-- User Accounts -->
              <section class="flex flex-col gap-2 sm:gap-3">
                <h2 class="text-dbd-dark font-bold text-sm sm:text-base md:text-lg
                           leading-tight capitalize">User Accounts</h2>
                <div class="flex flex-col gap-2">
                  <div class="flex items-start gap-2 sm:gap-3">
                    <div class="w-1 h-1 sm:w-1.5 sm:h-1.5 rounded-full bg-dbd-gray
                               flex-shrink-0 mt-1.5 sm:mt-2"></div>
                    <p class="text-dbd-gray font-medium text-xs sm:text-sm
                             leading-relaxed flex-1">
                      Users may be required to create an account to access certain features of the Service. You agree to provide accurate, current, and complete information during the registration process.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Digital Currency Risks -->
              <section class="flex flex-col gap-2 sm:gap-3">
                <h2 class="text-dbd-dark font-bold text-sm sm:text-base md:text-lg
                           leading-tight capitalize">Digital Currency Risks</h2>
                <div class="flex flex-col gap-2">
                  <div class="flex items-start gap-2 sm:gap-3">
                    <div class="w-1 h-1 sm:w-1.5 sm:h-1.5 rounded-full bg-dbd-gray
                               flex-shrink-0 mt-1.5 sm:mt-2"></div>
                    <p class="text-dbd-gray font-medium text-xs sm:text-sm
                             leading-relaxed flex-1">
                      You acknowledge that there are risks associated with the use of digital currencies, including market volatility and regulatory changes. DBDC is not responsible for any losses incurred.
                    </p>
                  </div>
                </div>
              </section>

              <!-- User Obligations -->
              <section class="flex flex-col gap-2 sm:gap-3">
                <h2 class="text-dbd-dark font-bold text-sm sm:text-base md:text-lg
                           leading-tight capitalize">User Obligations</h2>
                <div class="flex flex-col gap-2">
                  <div class="flex items-start gap-2 sm:gap-3">
                    <div class="w-1 h-1 sm:w-1.5 sm:h-1.5 rounded-full bg-dbd-gray
                               flex-shrink-0 mt-1.5 sm:mt-2"></div>
                    <p class="text-dbd-gray font-medium text-xs sm:text-sm
                             leading-relaxed flex-1">
                      Users agree to use the Service in compliance with applicable laws and regulations. You will not engage in any fraudulent or illegal activities.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Intellectual Property -->
              <section class="flex flex-col gap-2 sm:gap-3">
                <h2 class="text-dbd-dark font-bold text-sm sm:text-base md:text-lg
                           leading-tight capitalize">Intellectual Property</h2>
                <div class="flex flex-col gap-2">
                  <div class="flex items-start gap-2 sm:gap-3">
                    <div class="w-1 h-1 sm:w-1.5 sm:h-1.5 rounded-full bg-dbd-gray
                               flex-shrink-0 mt-1.5 sm:mt-2"></div>
                    <p class="text-dbd-gray font-medium text-xs sm:text-sm
                             leading-relaxed flex-1">
                      All content and materials available on the Service are the property of DBDC and protected by intellectual property laws.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Limitation of Liability -->
              <section class="flex flex-col gap-2 sm:gap-3">
                <h2 class="text-dbd-dark font-bold text-sm sm:text-base md:text-lg
                           leading-tight capitalize">Limitation of Liability</h2>
                <div class="flex flex-col gap-2">
                  <div class="flex items-start gap-2 sm:gap-3">
                    <div class="w-1 h-1 sm:w-1.5 sm:h-1.5 rounded-full bg-dbd-gray
                               flex-shrink-0 mt-1.5 sm:mt-2"></div>
                    <p class="text-dbd-gray font-medium text-xs sm:text-sm
                             leading-relaxed flex-1">
                      DBDC shall not be liable for any indirect, incidental, or consequential damages arising from your use of the Service.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Amendments -->
              <section class="flex flex-col gap-2 sm:gap-3">
                <h2 class="text-dbd-dark font-bold text-sm sm:text-base md:text-lg
                           leading-tight capitalize">Amendments</h2>
                <div class="flex flex-col gap-2">
                  <div class="flex items-start gap-2 sm:gap-3">
                    <div class="w-1 h-1 sm:w-1.5 sm:h-1.5 rounded-full bg-dbd-gray
                               flex-shrink-0 mt-1.5 sm:mt-2"></div>
                    <p class="text-dbd-gray font-medium text-xs sm:text-sm
                             leading-relaxed flex-1">
                      DBDC reserves the right to modify these Terms at any time. Changes will be effective immediately upon posting.
                    </p>
                  </div>
                </div>
              </section>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="p-3 sm:p-4 md:p-5 flex flex-col gap-2 sm:gap-3
                    flex-shrink-0 border-t border-gray-100">
          <button
            class="w-full h-11 sm:h-12 md:h-14 px-4 sm:px-6 md:px-8
                   flex items-center justify-center rounded-full
                   bg-gradient-to-r from-dbd-primary to-blue-500
                   text-white font-bold text-xs sm:text-sm md:text-base
                   transition-all duration-200 ease-in-out
                   hover:opacity-90 hover:-translate-y-0.5 hover:shadow-lg
                   active:translate-y-0 active:scale-95
                   focus:outline-none focus:ring-2 focus:ring-dbd-primary focus:ring-opacity-50
                   disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
            @click="agreeToTerms">
            I agree with Terms & Conditions
          </button>
          <button
            class="w-full h-10 sm:h-11 md:h-12 px-4 sm:px-5 md:px-6
                   flex items-center justify-center rounded-full
                   border border-dbd-gray bg-dbd-off-white text-dbd-gray
                   font-medium text-xs sm:text-sm md:text-base
                   transition-all duration-200 ease-in-out
                   hover:bg-gray-100 hover:-translate-y-0.5
                   active:translate-y-0 active:scale-95
                   focus:outline-none focus:ring-2 focus:ring-dbd-gray focus:ring-opacity-50"
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
/* Дополнител��ные Tailwind утилиты для мобильной адаптивности */
.scrollbar-none {
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.scrollbar-none::-webkit-scrollbar {
  display: none;
}

.touch-manipulation {
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

.overscroll-contain {
  overscroll-behavior: contain;
  -webkit-overflow-scrolling: touch;
}

/* Modal Overlay */
.terms-modal-overlay {
  animation: fadeIn 0.3s ease-out;
  touch-action: none;
  -webkit-overflow-scrolling: auto;
  overscroll-behavior: none;
}

/* Базовые стили модального окна - работают с Tailwind */
.modal-container {
  /* Дополнительные стили при н��обходимости */
}

/* Только необходимые переопределения для очень маленьких экранов */
@media (max-width: 320px) {
  .modal-container {
    max-width: calc(100vw - 8px) !important;
    height: calc(100vh - 16px) !important;
  }
}

/* Small height screens (shorter mobile devices) */
@media (max-height: 600px) {
  .modal-container {
    height: calc(100vh - 16px) !important;
  }
  .modal-scroll-section {
    max-height: calc(100vh - 180px) !important;
  }
}

/* Very small height screens */
@media (max-height: 480px) {
  .modal-scroll-section {
    max-height: calc(100vh - 160px) !important;
  }
}

/* Убрано - адаптивность теперь через Tailwind CSS классы */

/* Landscape orientation - важно для мобильных */
@media (max-height: 500px) and (orientation: landscape) {
  .modal-container {
    height: calc(100vh - 16px) !important;
    max-height: calc(100vh - 16px) !important;
  }
  .modal-scroll-section {
    max-height: calc(100vh - 160px) !important;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .modal-content {
    background: #2a2a2a !important;
    border-color: rgba(255, 255, 255, 0.1) !important;
  }

  .modal-title {
    color: #ffffff !important;
  }

  .modal-subtitle,
  .modal-intro {
    color: #a0a0a0 !important;
  }
}

/* Touch optimizations */
@media (hover: none) and (pointer: coarse) {
  button:hover {
    transform: none !important;
  }

  button:active {
    opacity: 0.8 !important;
  }
}

/* Анимации */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
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

/* Touch optimizations */
@media (hover: none) and (pointer: coarse) {
  .agree-btn:hover,
  .back-btn:hover {
    transform: none;
  }
  
  .agree-btn:active {
    opacity: 0.8;
  }
  
  .back-btn:active {
    background: #e0e0e0;
  }
}

/* Performance optimizations */
.agree-btn,
.back-btn {
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}
</style>
