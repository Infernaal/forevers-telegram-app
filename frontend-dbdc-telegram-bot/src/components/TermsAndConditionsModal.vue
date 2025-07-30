<template>
  <div v-if="isVisible" 
       class="fixed inset-0 bg-black/20 backdrop-blur-[9px] z-[10001] 
              animate-[fadeIn_0.3s_ease-out] terms-modal-overlay" 
       @click="closeModal">
    <div class="w-full h-full min-h-screen bg-gray-100 font-montserrat overflow-x-hidden terms-modal-view
                animate-[slideUp_0.3s_ease-out]" 
         @click.stop>
      <!-- Content Container with full screen responsive design -->
      <div class="content-container">

        <!-- Header -->
        <div class="terms-header-section">
          <h1 class="terms-title">
            Forevers Leasing Terms & Conditions
          </h1>
          <p class="terms-last-updated">
            Last Updated: July 16, 2025
          </p>
        </div>

        <!-- Scrollable Content -->
        <div class="terms-scroll-section">
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
              <section class="terms-section">
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
              <section class="terms-section">
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
              <section class="terms-section">
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
              <section class="terms-section">
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
              <section class="terms-section">
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
              <section class="terms-section">
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
              <section class="terms-section">
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
        <div class="terms-actions-section">
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
/* Modal Overlay Base Styles */
.terms-modal-overlay {
  animation: fadeIn 0.3s ease-out;
  touch-action: none;
  -webkit-overflow-scrolling: auto;
  overscroll-behavior: none;
}

.terms-modal-view {
  width: 100%;
  margin: 0 auto;
  background: #f3f4f6;
  min-height: 100vh;
  min-height: 100dvh; /* Dynamic viewport height */
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
  overflow-y: auto;
  overscroll-behavior: none;
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* IE and Edge */
}

.terms-modal-view::-webkit-scrollbar {
  display: none; /* Chrome, Safari and Opera */
}

.content-container {
  background: #f3f4f6;
  padding: 16px 16px 100px 16px; /* Bottom padding for buttons */
  box-sizing: border-box;
  min-height: calc(100vh - 0px);
  display: flex;
  flex-direction: column;
}

/* Header Section */
.terms-header-section {
  margin-bottom: 16px;
  flex-shrink: 0;
}

.terms-title {
  font-size: 18px;
  font-weight: 600;
  color: #02070E;
  margin: 0 0 12px 0;
  line-height: 1.3;
  text-transform: capitalize;
}

.terms-last-updated {
  font-size: 14px;
  font-weight: 500;
  color: #4B4D50;
  margin: 0 0 20px 0;
  line-height: 1.5;
  text-transform: capitalize;
}

/* Scrollable Section */
.terms-scroll-section {
  flex: 1;
  overflow-y: auto;
  scrollbar-width: none;
  -ms-overflow-style: none;
  overscroll-behavior: contain;
}

.terms-scroll-section::-webkit-scrollbar {
  display: none;
}

.terms-scroll-content {
  padding-bottom: 20px;
}

.terms-intro {
  color: #4B4D50;
  font-size: 14px;
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
  font-size: 20px;
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
  font-size: 14px;
  font-weight: 500;
  line-height: 1.4;
  margin: 0;
  flex: 1;
}

/* Actions Section */
.terms-actions-section {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  background: #f3f4f6;
  border-top: 1px solid #F0F0F0;
  z-index: 10002;
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
  color: #FFF;
  text-align: center;
  font-size: 14px;
  font-weight: 700;
  line-height: 1.4;
  font-family: inherit;
  outline: none;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

.terms-agree-btn:hover {
  opacity: 0.9;
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(32, 25, 206, 0.35);
}

.terms-agree-btn:active {
  transform: translateY(0);
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
  color: #4B4D50;
  text-align: center;
  font-size: 16px;
  font-weight: 500;
  line-height: 1.4;
  font-family: inherit;
  outline: none;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

.terms-back-btn:hover {
  background: #f0f0f0;
  transform: translateY(-1px);
}

.terms-back-btn:active {
  transform: translateY(0);
}

/* Small mobile devices (iPhone SE, small Android) - ≤374px */
@media (max-width: 374px) {
  .terms-modal-view {
    max-width: 100%;
  }
  
  .content-container {
    padding: 12px 12px 90px 12px;
  }
  
  .terms-header-section {
    margin-bottom: 12px;
  }
  
  .terms-title {
    font-size: 16px;
  }
  
  .terms-last-updated {
    font-size: 12px;
  }
  
  .section-title {
    font-size: 18px;
  }
  
  .terms-intro,
  .bullet-text {
    font-size: 12px;
  }
  
  .terms-sections {
    gap: 24px;
  }
  
  .terms-section {
    gap: 12px;
  }
  
  .bullet-item {
    gap: 10px;
  }
  
  .bullet-point {
    width: 5px;
    height: 5px;
    margin-top: 6px;
  }
  
  .terms-actions-section {
    padding: 12px;
  }
  
  .terms-agree-btn {
    height: 48px;
    font-size: 12px;
    padding: 10px 40px;
  }
  
  .terms-back-btn {
    height: 40px;
    font-size: 14px;
    padding: 10px 20px;
  }
}

/* Regular mobile devices (iPhone 12, 13, 14) - 375px to 430px */
@media (min-width: 375px) and (max-width: 430px) {
  .terms-modal-view {
    max-width: 100%;
  }
  
  .content-container {
    padding: 14px 14px 95px 14px;
  }
  
  .terms-header-section {
    margin-bottom: 14px;
  }
  
  .terms-title {
    font-size: 17px;
  }
  
  .terms-last-updated {
    font-size: 13px;
  }
  
  .section-title {
    font-size: 19px;
  }
  
  .terms-intro,
  .bullet-text {
    font-size: 13px;
  }
  
  .terms-sections {
    gap: 28px;
  }
  
  .terms-section {
    gap: 14px;
  }
  
  .bullet-item {
    gap: 12px;
  }
  
  .bullet-point {
    width: 5.5px;
    height: 5.5px;
    margin-top: 7px;
  }
  
  .terms-actions-section {
    padding: 14px;
  }
  
  .terms-agree-btn {
    height: 50px;
    font-size: 13px;
    padding: 11px 44px;
  }
  
  .terms-back-btn {
    height: 42px;
    font-size: 15px;
    padding: 11px 22px;
  }
}

/* Large mobile and small tablets - 431px to 768px */
@media (min-width: 431px) and (max-width: 768px) {
  .terms-modal-view {
    width: 100%;
  }

  .content-container {
    padding: 24px 24px 140px 24px;
    max-width: 800px;
    margin: 0 auto;
  }

  .terms-header-section {
    margin-bottom: 24px;
  }

  .terms-title {
    font-size: 28px;
  }

  .terms-last-updated {
    font-size: 18px;
  }

  .section-title {
    font-size: 24px;
  }

  .terms-intro,
  .bullet-text {
    font-size: 18px;
  }

  .terms-sections {
    gap: 40px;
  }

  .terms-section {
    gap: 20px;
  }

  .bullet-item {
    gap: 18px;
  }

  .bullet-point {
    width: 8px;
    height: 8px;
    margin-top: 10px;
  }

  .terms-actions-section {
    padding: 24px;
  }

  .terms-agree-btn {
    height: 64px;
    font-size: 18px;
    padding: 18px 60px;
  }

  .terms-back-btn {
    height: 56px;
    font-size: 18px;
    padding: 16px 32px;
  }
}

/* Tablets and desktop - ≥769px */
@media (min-width: 769px) {
  .terms-modal-view {
    width: 100%;
    margin: 0;
  }

  .content-container {
    padding: 40px 40px 160px 40px;
    max-width: 1200px;
    margin: 0 auto;
  }

  .terms-header-section {
    margin-bottom: 32px;
  }

  .terms-title {
    font-size: 36px;
  }

  .terms-last-updated {
    font-size: 22px;
  }

  .section-title {
    font-size: 28px;
  }

  .terms-intro,
  .bullet-text {
    font-size: 22px;
  }

  .terms-sections {
    gap: 48px;
  }

  .terms-section {
    gap: 24px;
  }

  .bullet-item {
    gap: 20px;
  }

  .bullet-point {
    width: 10px;
    height: 10px;
    margin-top: 12px;
  }

  .terms-actions-section {
    padding: 40px;
  }

  .terms-agree-btn {
    height: 72px;
    font-size: 22px;
    padding: 24px 72px;
  }

  .terms-back-btn {
    height: 64px;
    font-size: 22px;
    padding: 20px 40px;
  }
}

/* Landscape orientation adjustments for phones */
@media (max-height: 500px) and (orientation: landscape) {
  .content-container {
    padding: 8px 16px 80px 16px;
  }
  
  .terms-header-section {
    margin-bottom: 8px;
  }
  
  .terms-title {
    font-size: 14px;
  }
  
  .terms-last-updated {
    font-size: 11px;
  }
  
  .section-title {
    font-size: 16px;
  }
  
  .terms-intro,
  .bullet-text {
    font-size: 11px;
  }
  
  .terms-sections {
    gap: 16px;
  }
  
  .terms-section {
    gap: 8px;
  }
  
  .bullet-item {
    gap: 8px;
  }
  
  .bullet-point {
    width: 4px;
    height: 4px;
    margin-top: 5px;
  }
  
  .terms-actions-section {
    padding: 8px;
  }
  
  .terms-agree-btn {
    height: 40px;
    font-size: 11px;
    padding: 8px 32px;
  }
  
  .terms-back-btn {
    height: 36px;
    font-size: 11px;
    padding: 8px 16px;
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

/* High DPI displays */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .bullet-point {
    image-rendering: -webkit-optimize-contrast;
    image-rendering: crisp-edges;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .terms-modal-view {
    background: #1a1a1a;
  }
  
  .content-container {
    background: #1a1a1a;
  }
  
  .terms-actions-section {
    background: #1a1a1a;
    border-top-color: rgba(255, 255, 255, 0.1);
  }
  
  .terms-title {
    color: #ffffff;
  }
  
  .terms-last-updated,
  .terms-intro,
  .bullet-text {
    color: #a0a0a0;
  }
  
  .section-title {
    color: #ffffff;
  }
  
  .bullet-point {
    background: #a0a0a0;
  }
  
  .terms-back-btn {
    background: #2a2a2a;
    border-color: rgba(255, 255, 255, 0.2);
    color: #ffffff;
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  .terms-agree-btn,
  .terms-back-btn {
    transition: none;
  }
  
  .terms-agree-btn:hover,
  .terms-back-btn:hover {
    transform: none;
  }
  
  .terms-agree-btn:active,
  .terms-back-btn:active {
    transform: none;
  }
}

/* Touch optimizations */
@media (hover: none) and (pointer: coarse) {
  .terms-agree-btn:hover,
  .terms-back-btn:hover {
    transform: none;
  }
  
  .terms-agree-btn:active {
    opacity: 0.8;
  }
  
  .terms-back-btn:active {
    background: #e0e0e0;
  }
}

/* Safe area support for different iOS versions */
@supports (padding-bottom: env(safe-area-inset-bottom)) {
  .content-container {
    padding-bottom: calc(100px + env(safe-area-inset-bottom));
  }
  
  .terms-actions-section {
    padding-bottom: calc(16px + env(safe-area-inset-bottom));
  }
}

@supports (padding-bottom: constant(safe-area-inset-bottom)) {
  .content-container {
    padding-bottom: calc(100px + constant(safe-area-inset-bottom));
  }
  
  .terms-actions-section {
    padding-bottom: calc(16px + constant(safe-area-inset-bottom));
  }
}

/* Performance optimizations */
.terms-agree-btn,
.terms-back-btn {
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Telegram WebApp specific optimizations */
* {
  -webkit-tap-highlight-color: transparent;
}
</style>
