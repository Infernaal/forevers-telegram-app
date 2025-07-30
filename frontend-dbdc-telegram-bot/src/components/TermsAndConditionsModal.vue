<template>
  <div v-if="isVisible"
       class="fixed inset-0 bg-black/20 backdrop-blur-[9px] z-[10001]
              flex items-center justify-center
              p-2 sm:p-3 md:p-4 lg:p-6
              animate-[fadeIn_0.3s_ease-out] terms-modal-overlay"
       @click="closeModal">
    <div class="w-full modal-container
                animate-[slideUp_0.3s_ease-out]" 
         @click.stop>
      <!-- Modal Content -->
      <div class="modal-content">
        <!-- Header -->
        <div class="modal-header">
          <h1 class="modal-title">
            Forevers Leasing Terms & Conditions
          </h1>
          <p class="modal-subtitle">
            Last Updated: July 16, 2025
          </p>
        </div>

        <!-- Scrollable Content -->
        <div class="modal-scroll-section">
          <div class="modal-scroll-content">
            <!-- Introduction -->
            <p class="modal-intro">
              These Terms and Conditions govern your use of DBDC (the "Service"). By accessing or using the Service, you agree to be bound by these Terms. If you do not agree with these Terms, do not use the Service.
            </p>

            <!-- Sections -->
            <div class="modal-sections">
              <!-- Definitions -->
              <section class="modal-section">
                <h2 class="section-title">Definitions</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">
                      "User" refers to any individual or entity that accesses or uses the Service.
                    </p>
                  </div>
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">
                      "Service" refers to the cryptocurrency platform and any related services offered by DBDC.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Eligibility -->
              <section class="modal-section">
                <h2 class="section-title">Eligibility</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">
                      You must be at least 18 years old and capable of entering into legally binding agreements to use the Service.
                    </p>
                  </div>
                </div>
              </section>

              <!-- User Accounts -->
              <section class="modal-section">
                <h2 class="section-title">User Accounts</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">
                      Users may be required to create an account to access certain features of the Service. You agree to provide accurate, current, and complete information during the registration process.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Digital Currency Risks -->
              <section class="modal-section">
                <h2 class="section-title">Digital Currency Risks</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">
                      You acknowledge that there are risks associated with the use of digital currencies, including market volatility and regulatory changes. DBDC is not responsible for any losses incurred.
                    </p>
                  </div>
                </div>
              </section>

              <!-- User Obligations -->
              <section class="modal-section">
                <h2 class="section-title">User Obligations</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">
                      Users agree to use the Service in compliance with applicable laws and regulations. You will not engage in any fraudulent or illegal activities.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Intellectual Property -->
              <section class="modal-section">
                <h2 class="section-title">Intellectual Property</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">
                      All content and materials available on the Service are the property of DBDC and protected by intellectual property laws.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Limitation of Liability -->
              <section class="modal-section">
                <h2 class="section-title">Limitation of Liability</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">
                      DBDC shall not be liable for any indirect, incidental, or consequential damages arising from your use of the Service.
                    </p>
                  </div>
                </div>
              </section>

              <!-- Amendments -->
              <section class="modal-section">
                <h2 class="section-title">Amendments</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">
                      DBDC reserves the right to modify these Terms at any time. Changes will be effective immediately upon posting.
                    </p>
                  </div>
                </div>
              </section>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="modal-actions">
          <button class="agree-btn" @click="agreeToTerms">
            I agree with Terms & Conditions
          </button>
          <button class="back-btn" @click="closeModal">
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
/* Modal Overlay */
.terms-modal-overlay {
  animation: fadeIn 0.3s ease-out;
  touch-action: none;
  -webkit-overflow-scrolling: auto;
  overscroll-behavior: none;
}

/* Modal Container - Responsive Widths */
.modal-container {
  max-width: min(340px, calc(100vw - 16px));
  max-height: min(85vh, calc(100vh - 32px));
  min-height: min(70vh, 500px);
  width: 100%;
}

.modal-content {
  background: #fff;
  border-radius: 20px;
  border: 1px solid #E8E8E8;
  box-shadow: 1.744px 2.616px 20.93px 0 rgba(2, 7, 14, 0.04);
  display: flex;
  flex-direction: column;
  height: 100%;
  max-height: 85vh;
  overflow: hidden;
}

/* Header */
.modal-header {
  padding: 12px;
  flex-shrink: 0;
  border-bottom: 1px solid #f0f0f0;
}

.modal-title {
  color: #02070E;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 18px;
  font-weight: 700;
  line-height: 1.4;
  text-transform: capitalize;
  margin: 0 0 8px 0;
}

.modal-subtitle {
  color: #4B4D50;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 14px;
  font-weight: 500;
  line-height: 1.5;
  text-transform: capitalize;
  margin: 0;
}

/* Scrollable Content */
.modal-scroll-section {
  flex: 1;
  overflow-y: auto;
  padding: 12px;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.modal-scroll-section::-webkit-scrollbar {
  display: none;
}

.modal-scroll-content {
  padding-bottom: 12px;
}

.modal-intro {
  color: #4B4D50;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 14px;
  font-weight: 500;
  line-height: 1.4;
  margin: 0 0 24px 0;
}

.modal-sections {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.modal-section {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.section-title {
  color: #02070E;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 16px;
  font-weight: 700;
  line-height: 1.3;
  text-transform: capitalize;
  margin: 0;
}

.section-content {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.bullet-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}

.bullet-point {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #4B4D50;
  flex-shrink: 0;
  margin-top: 6px;
}

.bullet-text {
  color: #4B4D50;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 13px;
  font-weight: 500;
  line-height: 1.4;
  margin: 0;
  flex: 1;
}

/* Actions */
.modal-actions {
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex-shrink: 0;
  border-top: 1px solid #F0F0F0;
}

.agree-btn {
  display: flex;
  width: 100%;
  height: 48px;
  padding: 12px 36px;
  justify-content: center;
  align-items: center;
  border-radius: 1000px;
  background: linear-gradient(90deg, #2019CE 0%, #473FFF 100%);
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(32, 25, 206, 0.25);
  color: #FFF;
  text-align: center;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 12px;
  font-weight: 700;
  line-height: 1.4;
  outline: none;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

.agree-btn:hover {
  opacity: 0.9;
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(32, 25, 206, 0.35);
}

.agree-btn:active {
  transform: translateY(0);
}

.back-btn {
  display: flex;
  width: 100%;
  height: 40px;
  padding: 8px 24px;
  justify-content: center;
  align-items: center;
  border-radius: 1000px;
  border: 1px solid #4B4D50;
  background: #FAFAFA;
  cursor: pointer;
  transition: all 0.2s ease;
  color: #4B4D50;
  text-align: center;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 14px;
  font-weight: 500;
  line-height: 1.4;
  outline: none;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

.back-btn:hover {
  background: #f0f0f0;
  transform: translateY(-1px);
}

.back-btn:active {
  transform: translateY(0);
}

/* Extra small mobile devices - ≤320px */
@media (max-width: 320px) {
  .modal-container {
    max-width: calc(100vw - 8px);
    max-height: min(95vh, calc(100vh - 16px));
    min-height: min(85vh, 400px);
  }

  .modal-content {
    border-radius: 12px;
  }

  .modal-header {
    padding: 8px;
  }

  .modal-title {
    font-size: 14px;
    line-height: 1.3;
  }

  .modal-subtitle {
    font-size: 11px;
  }

  .modal-scroll-section {
    padding: 8px;
  }

  .modal-intro {
    font-size: 11px;
    margin-bottom: 16px;
    line-height: 1.3;
  }

  .modal-sections {
    gap: 16px;
  }

  .modal-section {
    gap: 8px;
  }

  .section-title {
    font-size: 12px;
    line-height: 1.2;
  }

  .bullet-text {
    font-size: 10px;
    line-height: 1.3;
  }

  .bullet-item {
    gap: 8px;
  }

  .bullet-point {
    width: 3px;
    height: 3px;
    margin-top: 4px;
  }

  .modal-actions {
    padding: 8px;
    gap: 6px;
  }

  .agree-btn {
    height: 40px;
    font-size: 10px;
    padding: 8px 28px;
  }

  .back-btn {
    height: 32px;
    font-size: 11px;
    padding: 6px 16px;
  }
}

/* Small mobile devices (iPhone SE, small Android) - 321px to 374px */
@media (min-width: 321px) and (max-width: 374px) {
  .modal-container {
    max-width: min(300px, calc(100vw - 12px));
    max-height: min(90vh, calc(100vh - 20px));
    min-height: min(80vh, 450px);
  }
  
  .modal-content {
    border-radius: 16px;
  }
  
  .modal-header {
    padding: 10px;
  }
  
  .modal-title {
    font-size: 16px;
  }
  
  .modal-subtitle {
    font-size: 12px;
  }
  
  .modal-scroll-section {
    padding: 10px;
  }
  
  .modal-intro {
    font-size: 12px;
    margin-bottom: 20px;
  }
  
  .modal-sections {
    gap: 20px;
  }
  
  .modal-section {
    gap: 10px;
  }
  
  .section-title {
    font-size: 14px;
  }
  
  .bullet-text {
    font-size: 11px;
  }
  
  .bullet-item {
    gap: 10px;
  }
  
  .bullet-point {
    width: 4px;
    height: 4px;
    margin-top: 5px;
  }
  
  .modal-actions {
    padding: 10px;
  }
  
  .agree-btn {
    height: 44px;
    font-size: 11px;
    padding: 10px 32px;
  }
  
  .back-btn {
    height: 36px;
    font-size: 12px;
    padding: 8px 20px;
  }
}

/* Regular mobile devices (iPhone 12, 13, 14) - 375px to 430px */
@media (min-width: 375px) and (max-width: 430px) {
  .modal-container {
    max-width: min(360px, calc(100vw - 16px));
    max-height: min(88vh, calc(100vh - 24px));
    min-height: min(75vh, 480px);
  }
  
  .modal-content {
    border-radius: 18px;
  }
  
  .modal-header {
    padding: 14px;
  }
  
  .modal-title {
    font-size: 20px;
  }
  
  .modal-subtitle {
    font-size: 15px;
  }
  
  .modal-scroll-section {
    padding: 14px;
  }
  
  .modal-intro {
    font-size: 15px;
    margin-bottom: 28px;
  }
  
  .modal-sections {
    gap: 28px;
  }
  
  .modal-section {
    gap: 14px;
  }
  
  .section-title {
    font-size: 18px;
  }
  
  .bullet-text {
    font-size: 14px;
  }
  
  .bullet-item {
    gap: 14px;
  }
  
  .bullet-point {
    width: 6px;
    height: 6px;
    margin-top: 7px;
  }
  
  .modal-actions {
    padding: 14px;
  }
  
  .agree-btn {
    height: 52px;
    font-size: 14px;
    padding: 12px 40px;
  }
  
  .back-btn {
    height: 44px;
    font-size: 16px;
    padding: 10px 24px;
  }
}

/* Large mobile and small tablets - 431px to 768px */
@media (min-width: 431px) and (max-width: 768px) {
  .modal-container {
    max-width: 500px;
    max-height: 82vh;
    min-height: 65vh;
  }

  .modal-content {
    border-radius: 24px;
  }

  .modal-header {
    padding: 20px;
  }

  .modal-title {
    font-size: 26px;
  }

  .modal-subtitle {
    font-size: 18px;
  }

  .modal-scroll-section {
    padding: 20px;
  }

  .modal-intro {
    font-size: 18px;
    margin-bottom: 32px;
  }

  .modal-sections {
    gap: 32px;
  }

  .modal-section {
    gap: 16px;
  }

  .section-title {
    font-size: 22px;
  }

  .bullet-text {
    font-size: 16px;
  }

  .bullet-item {
    gap: 16px;
  }

  .bullet-point {
    width: 7px;
    height: 7px;
    margin-top: 8px;
  }

  .modal-actions {
    padding: 20px;
  }

  .agree-btn {
    height: 56px;
    font-size: 16px;
    padding: 16px 48px;
  }

  .back-btn {
    height: 48px;
    font-size: 18px;
    padding: 12px 32px;
  }
}

/* Tablets and desktop - ≥769px */
@media (min-width: 769px) {
  .modal-container {
    max-width: 600px;
    max-height: 80vh;
    min-height: 60vh;
  }

  .modal-content {
    border-radius: 28px;
  }

  .modal-header {
    padding: 24px;
  }

  .modal-title {
    font-size: 32px;
  }

  .modal-subtitle {
    font-size: 20px;
  }

  .modal-scroll-section {
    padding: 24px;
  }

  .modal-intro {
    font-size: 20px;
    margin-bottom: 36px;
  }

  .modal-sections {
    gap: 36px;
  }

  .modal-section {
    gap: 20px;
  }

  .section-title {
    font-size: 26px;
  }

  .bullet-text {
    font-size: 18px;
  }

  .bullet-item {
    gap: 18px;
  }

  .bullet-point {
    width: 8px;
    height: 8px;
    margin-top: 9px;
  }

  .modal-actions {
    padding: 24px;
  }

  .agree-btn {
    height: 64px;
    font-size: 18px;
    padding: 18px 56px;
  }

  .back-btn {
    height: 52px;
    font-size: 20px;
    padding: 14px 36px;
  }
}

/* Landscape orientation adjustments for phones */
@media (max-height: 500px) and (orientation: landscape) {
  .modal-container {
    max-height: min(95vh, calc(100vh - 16px));
    min-height: min(85vh, 300px);
    max-width: min(500px, calc(100vw - 16px));
  }
  
  .modal-header {
    padding: 8px;
  }
  
  .modal-title {
    font-size: 14px;
  }
  
  .modal-subtitle {
    font-size: 11px;
  }
  
  .modal-scroll-section {
    padding: 8px;
  }
  
  .modal-intro {
    font-size: 11px;
    margin-bottom: 12px;
  }
  
  .modal-sections {
    gap: 12px;
  }
  
  .modal-section {
    gap: 6px;
  }
  
  .section-title {
    font-size: 12px;
  }
  
  .bullet-text {
    font-size: 10px;
  }
  
  .bullet-item {
    gap: 6px;
  }
  
  .bullet-point {
    width: 3px;
    height: 3px;
    margin-top: 4px;
  }
  
  .modal-actions {
    padding: 8px;
  }
  
  .agree-btn {
    height: 36px;
    font-size: 10px;
    padding: 8px 24px;
  }
  
  .back-btn {
    height: 32px;
    font-size: 10px;
    padding: 6px 16px;
  }
}

/* Animations */
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

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .modal-content {
    background: #2a2a2a;
    border-color: rgba(255, 255, 255, 0.1);
  }
  
  .modal-header {
    border-bottom-color: rgba(255, 255, 255, 0.1);
  }
  
  .modal-actions {
    border-top-color: rgba(255, 255, 255, 0.1);
  }
  
  .modal-title {
    color: #ffffff;
  }
  
  .modal-subtitle,
  .modal-intro,
  .bullet-text {
    color: #a0a0a0;
  }
  
  .section-title {
    color: #ffffff;
  }
  
  .bullet-point {
    background: #a0a0a0;
  }
  
  .back-btn {
    background: #3a3a3a;
    border-color: rgba(255, 255, 255, 0.2);
    color: #ffffff;
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  .agree-btn,
  .back-btn {
    transition: none;
  }
  
  .agree-btn:hover,
  .back-btn:hover {
    transform: none;
  }
  
  .agree-btn:active,
  .back-btn:active {
    transform: none;
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
