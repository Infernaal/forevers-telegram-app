<template>
  <div v-if="isVisible" class="terms-modal-overlay" @click="closeModal">
    <div class="terms-modal-container" @click.stop>
      <!-- Modal Content -->
      <div class="terms-content">
        <!-- Header -->
        <div class="terms-header">
          <h1 class="terms-title">Forevers Leasing Terms & Conditions</h1>
          <p class="terms-last-updated">Last Updated: July 16, 2025</p>
        </div>

        <!-- Scrollable Content -->
        <div class="terms-scroll-container">
          <div class="terms-scroll-content">
            <!-- Introduction -->
            <p class="terms-intro">
              These Terms and Conditions govern your use of DBDC (the "Service"). By accessing or using the Service, you agree to be bound by these Terms. If you do not agree with these Terms, do not use the Service.
            </p>

            <!-- Sections -->
            <div class="terms-sections">
              <!-- Definitions -->
              <section class="terms-section">
                <h2 class="section-title">Definitions</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">"User" refers to any individual or entity that accesses or uses the Service.</p>
                  </div>
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">"Service" refers to the cryptocurrency platform and any related services offered by DBDC.</p>
                  </div>
                </div>
              </section>

              <!-- Eligibility -->
              <section class="terms-section">
                <h2 class="section-title">Eligibility</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">You must be at least 18 years old and capable of entering into legally binding agreements to use the Service.</p>
                  </div>
                </div>
              </section>

              <!-- User Accounts -->
              <section class="terms-section">
                <h2 class="section-title">User Accounts</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">Users may be required to create an account to access certain features of the Service. You agree to provide accurate, current, and complete information during the registration process.</p>
                  </div>
                </div>
              </section>

              <!-- Digital Currency Risks -->
              <section class="terms-section">
                <h2 class="section-title">Digital Currency Risks</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">You acknowledge that there are risks associated with the use of digital currencies, including market volatility and regulatory changes. DBDC is not responsible for any losses incurred.</p>
                  </div>
                </div>
              </section>

              <!-- User Obligations -->
              <section class="terms-section">
                <h2 class="section-title">User Obligations</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">Users agree to use the Service in compliance with applicable laws and regulations. You will not engage in any fraudulent or illegal activities.</p>
                  </div>
                </div>
              </section>

              <!-- Intellectual Property -->
              <section class="terms-section">
                <h2 class="section-title">Intellectual Property</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">All content and materials available on the Service are the property of DBDC and protected by intellectual property laws.</p>
                  </div>
                </div>
              </section>

              <!-- Limitation of Liability -->
              <section class="terms-section">
                <h2 class="section-title">Limitation of Liability</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">DBDC shall not be liable for any indirect, incidental, or consequential damages arising from your use of the Service.</p>
                  </div>
                </div>
              </section>

              <!-- Amendments -->
              <section class="terms-section">
                <h2 class="section-title">Amendments</h2>
                <div class="section-content">
                  <div class="bullet-item">
                    <div class="bullet-point"></div>
                    <p class="bullet-text">DBDC reserves the right to modify these Terms at any time. Changes will be effective immediately upon posting.</p>
                  </div>
                </div>
              </section>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="terms-actions">
          <button class="terms-agree-btn" @click="agreeToTerms">
            I agree with Terms & Conditions
          </button>
          <button class="terms-back-btn" @click="closeModal">
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
.terms-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(2, 7, 14, 0.20);
  backdrop-filter: blur(9px);
  z-index: 1000;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 60px 20px 20px 20px;
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.terms-modal-container {
  width: 100%;
  max-width: 375px;
  max-height: 88vh;
  min-height: 75vh;
  background: #fff;
  border-radius: 20px;
  border: 1px solid #E8E8E8;
  box-shadow: 1.744px 2.616px 20.93px 0 rgba(2, 7, 14, 0.04);
  display: flex;
  flex-direction: column;
  animation: slideUp 0.3s ease-out;
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

.terms-content {
  display: flex;
  flex-direction: column;
  height: 100%;
  max-height: 88vh;
}

.terms-header {
  padding: 12px 12px 0 12px;
  flex-shrink: 0;
}

.terms-title {
  color: #02070E;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: clamp(22px, 6vw, 26px);
  font-weight: 700;
  line-height: 1.4;
  text-transform: capitalize;
  margin: 0 0 12px 0;
}

.terms-last-updated {
  color: #4B4D50;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: clamp(14px, 4vw, 16px);
  font-weight: 500;
  line-height: 1.5;
  text-transform: capitalize;
  margin: 0 0 20px 0;
}

.terms-scroll-container {
  flex: 1;
  overflow-y: auto;
  padding: 0 12px;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.terms-scroll-container::-webkit-scrollbar {
  display: none;
}

.terms-scroll-content {
  padding-bottom: 20px;
}

.terms-intro {
  color: #4B4D50;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: clamp(14px, 4vw, 16px);
  font-weight: 500;
  line-height: 1.4;
  margin: 0 0 32px 0;
}

.terms-sections {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.terms-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.section-title {
  color: #02070E;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: clamp(20px, 5vw, 24px);
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
  gap: 14px;
}

.bullet-point {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #4B4D50;
  flex-shrink: 0;
  margin-top: 8px;
}

.bullet-text {
  color: #4B4D50;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: clamp(14px, 4vw, 16px);
  font-weight: 500;
  line-height: 1.4;
  margin: 0;
  flex: 1;
}

.terms-actions {
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex-shrink: 0;
  border-top: 1px solid #F0F0F0;
}

.terms-agree-btn {
  display: flex;
  width: 100%;
  height: 52px;
  padding: 12px 48px;
  justify-content: center;
  align-items: center;
  border-radius: 1000px;
  background: linear-gradient(90deg, #2019CE 0%, #473FFF 100%);
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(32, 25, 206, 0.25);
}

.terms-agree-btn:hover {
  opacity: 0.9;
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(32, 25, 206, 0.35);
}

.terms-agree-btn:active {
  transform: translateY(0);
}

.terms-agree-btn {
  color: #FFF;
  text-align: center;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: clamp(12px, 3.5vw, 14px);
  font-weight: 700;
  line-height: 1.4;
}

.terms-back-btn {
  display: flex;
  width: 100%;
  height: 44px;
  padding: 12px 24px;
  justify-content: center;
  align-items: center;
  border-radius: 1000px;
  border: 1px solid #4B4D50;
  background: #FAFAFA;
  cursor: pointer;
  transition: all 0.2s ease;
}

.terms-back-btn:hover {
  background: #f0f0f0;
  transform: translateY(-1px);
}

.terms-back-btn:active {
  transform: translateY(0);
}

.terms-back-btn {
  color: #4B4D50;
  text-align: center;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: clamp(14px, 4vw, 16px);
  font-weight: 500;
  line-height: 1.4;
}

/* Mobile responsiveness */
@media (max-width: 480px) {
  .terms-modal-overlay {
    padding: 8px;
  }

  .terms-modal-container {
    max-height: 92vh;
    min-height: 80vh;
  }

  .terms-header {
    padding: 8px 8px 0 8px;
  }

  .terms-scroll-container {
    padding: 0 8px;
  }

  .terms-actions {
    padding: 8px;
  }
}

/* Tablet styles */
@media (min-width: 481px) and (max-width: 768px) {
  .terms-modal-container {
    max-width: 500px;
  }
}

/* Desktop styles */
@media (min-width: 769px) {
  .terms-modal-container {
    max-width: 600px;
  }
}

/* Touch optimizations */
.terms-agree-btn,
.terms-back-btn {
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}
</style>
