<template>
  <div class="holders-view w-full max-w-md mx-auto min-h-screen" style="background: #f3f4f6 !important;">
    <!-- Content Container -->
    <div class="content-container px-4 pb-24" style="min-height: calc(100vh - 96px);">
      
      <!-- Main Content -->
      <div class="flex flex-col gap-5 pt-4">
        
        <!-- Header Section -->
        <div class="flex flex-col gap-1">
          <h1 class="text-xl font-bold text-dbd-dark leading-6">Referral Program</h1>
          <p class="text-base font-medium text-dbd-gray leading-6">Share the QR-code with your friends.</p>
        </div>

        <!-- QR Code Section -->
        <div class="qr-section relative">
          <!-- Background with gradient and decorative F icons -->
          <div class="qr-background">
            <!-- Decorative F Icons -->
            <div class="absolute -left-4 -top-1 w-24 h-24 opacity-10 transform rotate-45">
              <svg width="96" height="96" viewBox="0 0 96 96" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M88.5781 4.61296V0.833313H36.2715V5.63213H0.833496V9.41178H36.2715V18.8172H71.1973V14.2048H99.5684V10.4251H71.1973V9.41178H92.8164V5.63213H71.1973V4.61296H88.5781Z" fill="#FAFAFA"/>
              </svg>
            </div>
            
            <div class="absolute right-4 top-12 w-12 h-12 opacity-10 transform rotate-150">
              <svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M44.2891 4.61296V0.833313H18.1357V5.63213H0.833496V9.41178H18.1357V18.8172H35.6986V14.2048H49.7842V10.4251H35.6986V9.41178H46.4082V5.63213H35.6986V4.61296H44.2891Z" fill="#1E5DFF"/>
              </svg>
            </div>
            
            <div class="absolute -left-6 bottom-8 w-32 h-32 opacity-10 transform -rotate-30">
              <svg width="128" height="128" viewBox="0 0 128 128" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M118.104 4.61296V0.833313H48.3619V5.63213H0.833496V9.41178H48.3619V18.8172H94.9298V14.2048H132.746V10.4251H94.9298V9.41178H123.878V5.63213H94.9298V4.61296H118.104Z" fill="#FAFAFA"/>
              </svg>
            </div>
            
            <div class="absolute right-12 top-5 w-24 h-24 opacity-10 transform rotate-120">
              <svg width="96" height="96" viewBox="0 0 96 96" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M88.5781 4.61296V0.833313H36.2715V5.63213H0.833496V9.41178H36.2715V18.8172H71.1973V14.2048H99.5684V10.4251H71.1973V9.41178H92.8164V5.63213H71.1973V4.61296H88.5781Z" fill="#1E5DFF"/>
              </svg>
            </div>
          </div>
          
          <!-- QR Code Container -->
          <div class="qr-container">
            <!-- QR Code Image Placeholder -->
            <div class="qr-code-placeholder">
              <svg width="140" height="140" viewBox="0 0 140 140" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- QR Code Pattern Placeholder -->
                <rect width="140" height="140" fill="#000"/>
                <rect x="20" y="20" width="20" height="20" fill="#fff"/>
                <rect x="60" y="20" width="20" height="20" fill="#fff"/>
                <rect x="100" y="20" width="20" height="20" fill="#fff"/>
                <rect x="20" y="60" width="20" height="20" fill="#fff"/>
                <rect x="100" y="60" width="20" height="20" fill="#fff"/>
                <rect x="20" y="100" width="20" height="20" fill="#fff"/>
                <rect x="60" y="100" width="20" height="20" fill="#fff"/>
                <rect x="100" y="100" width="20" height="20" fill="#fff"/>
                <!-- Corner markers -->
                <rect x="0" y="0" width="40" height="40" fill="#000" stroke="#fff" stroke-width="4"/>
                <rect x="100" y="0" width="40" height="40" fill="#000" stroke="#fff" stroke-width="4"/>
                <rect x="0" y="100" width="40" height="40" fill="#000" stroke="#fff" stroke-width="4"/>
                <!-- Random pattern -->
                <rect x="50" y="10" width="10" height="10" fill="#fff"/>
                <rect x="70" y="30" width="10" height="10" fill="#fff"/>
                <rect x="30" y="50" width="10" height="10" fill="#fff"/>
                <rect x="80" y="70" width="10" height="10" fill="#fff"/>
                <rect x="40" y="80" width="10" height="10" fill="#fff"/>
                <rect x="90" y="40" width="10" height="10" fill="#fff"/>
                <rect x="110" y="80" width="10" height="10" fill="#fff"/>
                <rect x="60" y="130" width="10" height="10" fill="#fff"/>
              </svg>
            </div>
            
            <!-- QR Code Link -->
            <div class="qr-link">
              vm.dubadu/jjhI1uT4S
            </div>
          </div>
        </div>

        <!-- Terms and Conditions -->
        <div class="terms-section">
          <label class="flex items-center gap-2 cursor-pointer">
            <input 
              type="checkbox" 
              v-model="termsAccepted" 
              class="terms-checkbox"
            />
            <span class="terms-text">
              I agree that I have read the 
              <a href="#" class="terms-link" @click.prevent="openTerms">Terms and Conditions</a>
            </span>
          </label>
        </div>

        <!-- Share Button -->
        <button 
          class="share-button"
          :class="{ 'share-button-disabled': !termsAccepted }"
          :disabled="!termsAccepted"
          @click="shareQRCode"
        >
          Share QR code
        </button>

        <!-- How to use the Link Section -->
        <div class="how-to-section">
          <div class="how-to-header">
            <h2 class="text-xl font-bold text-dbd-dark leading-6">How to use the Link</h2>
            <p class="text-base font-medium text-dbd-gray leading-6 mt-3">Follow these 3 simple steps</p>
          </div>
          
          <!-- Steps -->
          <div class="steps-container">
            <!-- Step indicators with connecting lines -->
            <div class="steps-indicators">
              <div class="step-indicator active"></div>
              <div class="step-line"></div>
              <div class="step-indicator active"></div>
              <div class="step-line"></div>
              <div class="step-indicator active"></div>
            </div>
            
            <!-- Step descriptions -->
            <div class="steps-descriptions">
              <div class="step-description">
                <span class="step-number">1</span>
                <span class="step-text">Share your link</span>
              </div>
              <div class="step-description">
                <span class="step-number">2</span>
                <span class="step-text">Wait for joining</span>
              </div>
              <div class="step-description">
                <span class="step-number">3</span>
                <span class="step-text">Get rewards</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Web Referral Link Section -->
        <div class="web-link-section">
          <div class="web-link-content">
            <h3 class="web-link-title">Web Referral Link</h3>
            <p class="web-link-description">Copy the link bellow and share with your friends.</p>
            
            <!-- Copy Link Input -->
            <div class="copy-link-container">
              <input 
                type="text" 
                :value="referralLink" 
                readonly 
                class="copy-link-input"
              />
              <button 
                class="copy-button" 
                @click="copyLink"
                :class="{ 'copy-button-copied': linkCopied }"
              >
                <span v-if="!linkCopied">Copy</span>
                <span v-else>✓</span>
                <svg v-if="!linkCopied" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="copy-icon">
                  <path d="M10.6667 6.66667H13.3333C13.7015 6.66667 14 6.96514 14 7.33333V13.3333C14 13.7015 13.7015 14 13.3333 14H7.33333C6.96514 14 6.66667 13.7015 6.66667 13.3333V10.6667M10.6667 6.66667V2.66667C10.6667 2.29848 10.3682 2 10 2H2.66667C2.29848 2 2 2.29848 2 2.66667V10C2 10.3682 2.29848 10.6667 2.66667 10.6667H6.66667M10.6667 6.66667H6.66667V10.6667" stroke="currentColor" stroke-width="1.33333" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- Bottom Navigation Component -->
    <BottomNavigation />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import BottomNavigation from '../components/BottomNavigation.vue'

// Reactive data
const termsAccepted = ref(false)
const linkCopied = ref(false)
const referralLink = ref('vm.dubadu/jjhI1uT4S')

// Methods
const shareQRCode = () => {
  if (!termsAccepted.value) return
  
  // Placeholder for share functionality
  console.log('Sharing QR code...')
  
  // Implement share functionality here
  if (navigator.share) {
    navigator.share({
      title: 'DBD Capital Forevers Bot',
      text: 'Join me on DBD Capital Forevers Bot!',
      url: referralLink.value
    }).catch(console.error)
  } else {
    // Fallback - copy to clipboard
    copyLink()
  }
}

const copyLink = async () => {
  try {
    await navigator.clipboard.writeText(referralLink.value)
    linkCopied.value = true
    setTimeout(() => {
      linkCopied.value = false
    }, 2000)
  } catch (err) {
    console.error('Failed to copy link:', err)
  }
}

const openTerms = () => {
  // Placeholder for opening terms and conditions
  console.log('Opening terms and conditions...')
  // This would typically open a modal or navigate to a terms page
}
</script>

<style scoped>
.holders-view {
  font-family: 'Montserrat', sans-serif;
}

.content-container {
  background: #f3f4f6 !important;
}

/* QR Section Styles */
.qr-section {
  position: relative;
  width: 100%;
  height: 396px;
}

.qr-background {
  position: absolute;
  inset: 0;
  border-radius: 24px;
  background: linear-gradient(93deg, #000482 33.15%, rgba(3, 0, 155, 0.84) 76.97%);
  backdrop-filter: blur(32px);
}

.qr-container {
  position: absolute;
  top: 24px;
  left: 50%;
  transform: translateX(-50%);
  width: 222px;
  height: 220px;
  border-radius: 20px;
  border: 1px solid #f2f2f2;
  background: #fafafa;
  box-shadow: 2px 4px 12px 0 rgba(0, 0, 0, 0.04);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
}

.qr-code-placeholder {
  width: 140px;
  height: 140px;
  border-radius: 8px;
  overflow: hidden;
}

.qr-link {
  color: #2019ce;
  font-family: Montserrat;
  font-size: 17px;
  font-weight: 600;
  line-height: 24px;
  text-align: center;
}

/* Terms Section Styles */
.terms-section {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: -40px;
  position: relative;
  z-index: 10;
}

.terms-checkbox {
  width: 24px;
  height: 24px;
  border-radius: 4px;
  border: 1px solid #7e7e7e;
  background: #fafafa;
  cursor: pointer;
}

.terms-text {
  color: #4b4d50;
  font-family: Montserrat;
  font-size: 16px;
  font-weight: 500;
  line-height: 22px;
}

.terms-link {
  color: #ff6800;
  text-decoration: underline;
}

/* Share Button Styles */
.share-button {
  display: flex;
  width: 100%;
  max-width: 300px;
  padding: 12px 48px;
  justify-content: center;
  align-items: center;
  gap: 10px;
  border-radius: 1000px;
  background: linear-gradient(90deg, #2019ce 0%, #473fff 100%);
  color: white;
  text-align: center;
  font-family: Montserrat;
  font-size: 16px;
  font-weight: 600;
  line-height: 26px;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  margin: 0 auto;
  height: 50px;
}

.share-button:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(32, 25, 206, 0.3);
}

.share-button-disabled {
  background: #e2e2e2 !important;
  color: #989898 !important;
  cursor: not-allowed;
}

/* How to Section Styles */
.how-to-section {
  margin-top: 20px;
}

.how-to-header {
  margin-bottom: 32px;
}

.steps-container {
  position: relative;
}

.steps-indicators {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
  margin-bottom: 16px;
}

.step-indicator {
  width: 38px;
  height: 40px;
  border-radius: 0 100px 100px 0;
  background: #2019ce;
}

.step-line {
  width: 44px;
  height: 1px;
  background: #7e7e7e;
}

.steps-descriptions {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
}

.step-description {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  flex: 1;
  text-align: center;
}

.step-number {
  color: #4b4d50;
  font-family: Montserrat;
  font-size: 16px;
  font-weight: 500;
  line-height: 24px;
}

.step-text {
  color: #4b4d50;
  font-family: Montserrat;
  font-size: 12px;
  font-weight: 500;
  line-height: 16px;
}

/* Web Link Section Styles */
.web-link-section {
  margin-top: 20px;
  border-radius: 24px;
  background: linear-gradient(93deg, #000482 33.15%, rgba(3, 0, 155, 0.84) 76.97%);
  backdrop-filter: blur(32px);
  padding: 20px;
  position: relative;
  overflow: hidden;
}

.web-link-content {
  position: relative;
  z-index: 10;
}

.web-link-title {
  color: #fff;
  font-family: Montserrat;
  font-size: 26px;
  font-weight: 700;
  line-height: 30px;
  margin-bottom: 12px;
}

.web-link-description {
  color: #fff;
  font-family: Montserrat;
  font-size: 16px;
  font-weight: 500;
  line-height: 24px;
  margin-bottom: 24px;
}

.copy-link-container {
  position: relative;
  display: flex;
  align-items: center;
  border-radius: 100px;
  border: 1px solid rgba(32, 25, 206, 0.6);
  background: rgba(255, 255, 255, 0.1);
  overflow: hidden;
}

.copy-link-input {
  flex: 1;
  padding: 14px 24px;
  background: transparent;
  border: none;
  color: #fafafa;
  font-family: Montserrat;
  font-size: 17px;
  font-weight: 600;
  line-height: 24px;
  text-decoration: underline;
  outline: none;
}

.copy-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  width: 50px;
  height: 52px;
  border-radius: 0 100px 100px 0;
  border: 1px solid #443fcc;
  background: #fafafa;
  color: #2019ce;
  font-family: Montserrat;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.copy-button:hover {
  background: #e8e8ff;
}

.copy-button-copied {
  background: #4caf50 !important;
  color: white !important;
}

.copy-icon {
  width: 16px;
  height: 16px;
}

/* Mobile optimizations */
@media (max-width: 375px) {
  .content-container {
    padding-left: 16px;
    padding-right: 16px;
  }
  
  .qr-container {
    width: calc(100vw - 64px);
    max-width: 300px;
  }
  
  .qr-code-placeholder {
    width: 120px;
    height: 120px;
  }
  
  .share-button {
    max-width: 100%;
  }
  
  .web-link-title {
    font-size: 22px;
    line-height: 26px;
  }
  
  .copy-link-input {
    font-size: 15px;
    padding: 12px 20px;
  }
}

@media (max-width: 320px) {
  .content-container {
    padding-left: 12px;
    padding-right: 12px;
  }
  
  .qr-container {
    width: calc(100vw - 48px);
    max-width: 280px;
  }
  
  .qr-code-placeholder {
    width: 100px;
    height: 100px;
  }
  
  .steps-descriptions {
    gap: 8px;
  }
  
  .step-text {
    font-size: 11px;
    line-height: 14px;
  }
}

/* Tablet optimizations */
@media (min-width: 376px) and (max-width: 768px) {
  .holders-view {
    max-width: 400px;
    background: #f3f4f6 !important;
  }
  
  body {
    background: #f3f4f6 !important;
  }
}

/* Desktop optimizations */
@media (min-width: 769px) {
  .holders-view {
    max-width: 480px;
    background: #f3f4f6 !important;
  }
  
  body {
    background: #f3f4f6 !important;
  }
}

/* Touch-friendly for Telegram */
.holders-view {
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

/* Button touch feedback */
button {
  touch-action: manipulation;
  -webkit-user-select: none;
  user-select: none;
}

button:active {
  transform: scale(0.98);
  transition: transform 0.1s ease;
}
</style>
