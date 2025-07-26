<template>
  <div class="wallet-view">
    <!-- Content Container -->
    <div class="content-container">

      <!-- Forevers Balance Section -->
      <div class="forevers-balance-section">
        <div class="balance-card">
          <div class="balance-content">
            <div class="balance-info">
              <h2 class="balance-title">
                Forevers<br>Balance
              </h2>
            </div>
            <div class="balance-amount">
              <!-- Forevers Logo SVG -->
              <svg class="forevers-logo" viewBox="0 0 32 32" fill="none">
                <path d="M30.6666 7.38081V1.33337H7.1291V9.01148H1.33325V15.0589H7.1291V30.1076H13.894V22.7277H19.6153V16.6803H13.894V15.0589H25.1316V9.01148H13.894V7.38081H30.6666Z" fill="#2019CE"/>
              </svg>
              <span class="balance-value">10,196</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Loyalty Program Section -->
      <div class="loyalty-section">
        <div class="loyalty-card">
          <!-- Header -->
          <div class="loyalty-header">
            <div class="icon-wrapper">
              <svg width="21" height="21" viewBox="0 0 22 22" fill="none">
                <g clip-path="url(#clip0_2_23137)">
                  <path d="M10.8717 21.4348C10.6085 21.4348 10.3908 21.3526 10.2186 21.1884C10.0465 21.0241 9.9604 20.8164 9.9604 20.5652V19C8.98831 18.8454 8.15798 18.5169 7.46942 18.0145C6.78085 17.512 6.24418 16.8744 5.85939 16.1014C5.75813 15.8889 5.75813 15.6666 5.85939 15.4348C5.96065 15.2029 6.13279 15.0386 6.37581 14.942C6.59859 14.8454 6.82642 14.8454 7.05932 14.942C7.29221 15.0386 7.46942 15.1932 7.59093 15.4058C7.95546 16.0628 8.43138 16.5555 9.01869 16.884C9.60599 17.2125 10.2844 17.3768 11.054 17.3768C12.0261 17.3768 12.826 17.1449 13.4538 16.6811C14.0817 16.2174 14.3956 15.5797 14.3956 14.7681C14.3956 13.9178 14.1171 13.2608 13.5602 12.7971C13.0032 12.3333 11.9552 11.8599 10.4161 11.3768C8.95793 10.9323 7.86939 10.343 7.15045 9.60866C6.43151 8.87436 6.07204 7.95649 6.07204 6.85504C6.07204 5.79224 6.43151 4.90335 7.15045 4.18837C7.86939 3.4734 8.80604 3.0676 9.9604 2.97098V1.43475C9.9604 1.18354 10.0465 0.975814 10.2186 0.811562C10.3908 0.647311 10.6085 0.565186 10.8717 0.565186C11.135 0.565186 11.3527 0.647311 11.5249 0.811562C11.697 0.975814 11.7831 1.18354 11.7831 1.43475V2.97098C12.5121 3.0676 13.1653 3.28016 13.7424 3.60866C14.3196 3.93717 14.8006 4.36229 15.1854 4.88403C15.3271 5.07726 15.3575 5.28499 15.2765 5.50721C15.1955 5.72944 15.0335 5.88886 14.7905 5.98548C14.5677 6.08209 14.3348 6.09176 14.0918 6.01446C13.8488 5.93717 13.6462 5.79224 13.4842 5.57968C13.2007 5.23185 12.8514 4.97581 12.4362 4.81156C12.021 4.64731 11.5198 4.56519 10.9325 4.56519C10.0009 4.56519 9.26171 4.76808 8.71491 5.17388C8.16811 5.57968 7.89471 6.1304 7.89471 6.82606C7.89471 7.56035 8.19848 8.15456 8.80604 8.60866C9.4136 9.06277 10.5376 9.53137 12.178 10.0145C13.5551 10.4203 14.5728 11.0048 15.231 11.7681C15.8891 12.5314 16.2182 13.4927 16.2182 14.6521C16.2182 15.8695 15.8436 16.8502 15.0943 17.5942C14.3449 18.3381 13.2412 18.8164 11.7831 19.029V20.5652C11.7831 20.8164 11.697 21.0241 11.5249 21.1884C11.3527 21.3526 11.135 21.4348 10.8717 21.4348Z" fill="#2019CE"/>
                </g>
              </svg>
            </div>
            <span class="loyalty-title">Loyalty program</span>
          </div>
          
          <!-- Amount Display -->
          <div class="amount-display">
            <div class="amount-content">
              <span class="amount-value">$8,900</span>
              <span class="amount-label">Forevers Rent %</span>
            </div>
          </div>
          
          <!-- History Button -->
          <button
            @click="navigateToTransactions"
            class="history-btn"
          >
            Rent Out History
          </button>
        </div>
      </div>

      <!-- Bonus Section -->
      <div class="bonus-section">
        <div class="bonus-card">
          <!-- Header -->
          <div class="bonus-header">
            <div class="icon-wrapper">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M10 0L12.245 6.91L20 6.91L14.16 11.18L16.405 18.09L10 13.82L3.595 18.09L5.84 11.18L0 6.91L7.755 6.91L10 0Z" fill="#FF6800"/>
              </svg>
            </div>
            <span class="bonus-title">Bonus</span>
          </div>

          <!-- Amount Display -->
          <div class="amount-display">
            <div class="amount-content">
              <span class="amount-value">$56,200</span>
              <span class="amount-label">Reward</span>
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
import { useRouter } from 'vue-router'
import BottomNavigation from '../components/BottomNavigation.vue'

const router = useRouter()

// Wallet balances for display only
const loyaltyBalance = ref(8900)
const bonusBalance = ref(56200)
const userBalance = ref(10196) // Forevers balance converted to USD

// Navigation methods
const navigateToTransactions = () => {
  router.push('/rent-out-transactions')
}

// Methods (wallet doesn't need purchase methods)
// WalletView only displays balances, purchase logic is in CartView
</script>

<style scoped>
.wallet-view {
  width: 100%;
  max-width: 430px;
  margin: 0 auto;
  background: #f3f4f6;
  min-height: 100vh;
  min-height: 100dvh; /* Dynamic viewport height */
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
  overscroll-behavior: none;
}

.content-container {
  background: #f3f4f6;
  padding: 16px 16px 100px 16px; /* Bottom padding for navigation */
  box-sizing: border-box;
  min-height: calc(100vh - 100px);
}

/* Forevers Balance Section */
.forevers-balance-section {
  margin-bottom: 16px;
}

.balance-card {
  background: #EFEEFF;
  border-radius: 16px;
  padding: 16px;
  box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.04);
  transition: all 0.2s ease;
}

.balance-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.balance-info {
  flex: 1;
}

.balance-title {
  font-size: 18px;
  font-weight: 600;
  color: #02070E;
  margin: 0;
  line-height: 1.3;
}

.balance-amount {
  display: flex;
  align-items: center;
  gap: 8px;
}

.forevers-logo {
  width: 32px;
  height: 32px;
  flex-shrink: 0;
}

.balance-value {
  font-size: 24px;
  font-weight: 700;
  color: #2019CE;
}

/* Loyalty Program Section */
.loyalty-section {
  margin-bottom: 16px;
}

.loyalty-card {
  background: #EFEEFF;
  border-radius: 16px;
  border: 1px solid rgba(147, 51, 234, 0.2);
  padding: 16px;
  box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.04);
}

.loyalty-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
}

.icon-wrapper {
  width: 40px;
  height: 40px;
  background: rgba(64, 64, 64, 0.24);
  border: 1px solid rgba(255, 255, 255, 0.24);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.loyalty-title {
  font-size: 16px;
  font-weight: 500;
  color: #02070E;
}

.amount-display {
  background: #FAFAFA;
  border-radius: 16px;
  border: 1px solid rgba(32, 25, 206, 0.2);
  padding: 16px;
  margin-bottom: 16px;
}

.amount-content {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.amount-value {
  font-size: 24px;
  font-weight: 700;
  color: #2019CE;
}

.amount-label {
  font-size: 14px;
  font-weight: 500;
  color: #4B4D50;
}

.history-btn {
  width: 100%;
  background: white;
  border: 1px solid #d1d5db;
  border-radius: 24px;
  padding: 12px 24px;
  font-size: 14px;
  font-weight: 700;
  color: #4B4D50;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: inherit;
  outline: none;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

.history-btn:hover {
  background: #f9fafb;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.history-btn:active {
  transform: translateY(0);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

/* Bonus Section */
.bonus-section {
  margin-bottom: 24px;
}

.bonus-card {
  background: #FFF3E7;
  border-radius: 16px;
  border: 1px solid rgba(147, 51, 234, 0.2);
  padding: 16px;
  box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.04);
}

.bonus-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
}

.bonus-title {
  font-size: 16px;
  font-weight: 500;
  color: #02070E;
}

/* Small mobile devices (iPhone SE, small Android) - ≤374px */
@media (max-width: 374px) {
  .wallet-view {
    max-width: 100%;
  }
  
  .content-container {
    padding: 12px 12px 90px 12px;
  }
  
  .forevers-balance-section,
  .loyalty-section {
    margin-bottom: 12px;
  }
  
  .balance-card,
  .loyalty-card,
  .bonus-card {
    border-radius: 12px;
    padding: 12px;
  }
  
  .balance-title {
    font-size: 16px;
  }
  
  .forevers-logo {
    width: 28px;
    height: 28px;
  }
  
  .balance-value {
    font-size: 20px;
  }
  
  .loyalty-header,
  .bonus-header {
    margin-bottom: 12px;
  }
  
  .icon-wrapper {
    width: 36px;
    height: 36px;
  }
  
  .loyalty-title,
  .bonus-title {
    font-size: 14px;
  }
  
  .amount-display {
    padding: 12px;
    margin-bottom: 12px;
    border-radius: 12px;
  }
  
  .amount-value {
    font-size: 20px;
  }
  
  .amount-label {
    font-size: 12px;
  }
  
  .history-btn {
    padding: 10px 20px;
    font-size: 12px;
    border-radius: 20px;
  }
  
  .bonus-section {
    margin-bottom: 16px;
  }
}

/* Regular mobile devices (iPhone 12, 13, 14) - 375px to 430px */
@media (min-width: 375px) and (max-width: 430px) {
  .wallet-view {
    max-width: 100%;
  }
  
  .content-container {
    padding: 14px 14px 95px 14px;
  }
  
  .forevers-balance-section,
  .loyalty-section {
    margin-bottom: 14px;
  }
  
  .balance-card,
  .loyalty-card,
  .bonus-card {
    border-radius: 14px;
    padding: 14px;
  }
  
  .balance-title {
    font-size: 17px;
  }
  
  .forevers-logo {
    width: 30px;
    height: 30px;
  }
  
  .balance-value {
    font-size: 22px;
  }
  
  .loyalty-header,
  .bonus-header {
    margin-bottom: 14px;
  }
  
  .icon-wrapper {
    width: 38px;
    height: 38px;
  }
  
  .loyalty-title,
  .bonus-title {
    font-size: 15px;
  }
  
  .amount-display {
    padding: 14px;
    margin-bottom: 14px;
    border-radius: 14px;
  }
  
  .amount-value {
    font-size: 22px;
  }
  
  .amount-label {
    font-size: 13px;
  }
  
  .history-btn {
    padding: 11px 22px;
    font-size: 13px;
    border-radius: 22px;
  }
  
  .bonus-section {
    margin-bottom: 20px;
  }
}

/* Large mobile and small tablets - 431px to 768px */
@media (min-width: 431px) and (max-width: 768px) {
  .wallet-view {
    max-width: 480px;
  }
  
  .content-container {
    padding: 18px 18px 100px 18px;
  }
  
  .forevers-balance-section,
  .loyalty-section {
    margin-bottom: 18px;
  }
  
  .balance-card,
  .loyalty-card,
  .bonus-card {
    border-radius: 18px;
    padding: 18px;
  }
  
  .balance-title {
    font-size: 20px;
  }
  
  .forevers-logo {
    width: 36px;
    height: 36px;
  }
  
  .balance-value {
    font-size: 28px;
  }
  
  .loyalty-header,
  .bonus-header {
    margin-bottom: 18px;
  }
  
  .icon-wrapper {
    width: 44px;
    height: 44px;
  }
  
  .loyalty-title,
  .bonus-title {
    font-size: 17px;
  }
  
  .amount-display {
    padding: 18px;
    margin-bottom: 18px;
    border-radius: 18px;
  }
  
  .amount-value {
    font-size: 28px;
  }
  
  .amount-label {
    font-size: 15px;
  }
  
  .history-btn {
    padding: 14px 28px;
    font-size: 15px;
    border-radius: 28px;
  }
  
  .bonus-section {
    margin-bottom: 24px;
  }
}

/* Tablets and desktop - ≥769px */
@media (min-width: 769px) {
  .wallet-view {
    max-width: 480px;
    margin: 20px auto;
    border-radius: 20px;
    box-shadow: 0 0 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
  }
  
  .content-container {
    padding: 24px 24px 110px 24px;
  }
  
  .forevers-balance-section,
  .loyalty-section {
    margin-bottom: 24px;
  }
  
  .balance-card,
  .loyalty-card,
  .bonus-card {
    border-radius: 20px;
    padding: 24px;
  }
  
  .balance-title {
    font-size: 22px;
  }
  
  .forevers-logo {
    width: 40px;
    height: 40px;
  }
  
  .balance-value {
    font-size: 32px;
  }
  
  .loyalty-header,
  .bonus-header {
    margin-bottom: 20px;
  }
  
  .icon-wrapper {
    width: 48px;
    height: 48px;
  }
  
  .loyalty-title,
  .bonus-title {
    font-size: 18px;
  }
  
  .amount-display {
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 20px;
  }
  
  .amount-value {
    font-size: 32px;
  }
  
  .amount-label {
    font-size: 16px;
  }
  
  .history-btn {
    padding: 16px 32px;
    font-size: 16px;
    border-radius: 32px;
  }
  
  .bonus-section {
    margin-bottom: 32px;
  }
}

/* Landscape orientation adjustments for phones */
@media (max-height: 500px) and (orientation: landscape) {
  .content-container {
    padding: 8px 16px 80px 16px;
  }
  
  .forevers-balance-section,
  .loyalty-section {
    margin-bottom: 8px;
  }
  
  .balance-card,
  .loyalty-card,
  .bonus-card {
    border-radius: 10px;
    padding: 10px;
  }
  
  .balance-title {
    font-size: 14px;
  }
  
  .forevers-logo {
    width: 24px;
    height: 24px;
  }
  
  .balance-value {
    font-size: 18px;
  }
  
  .loyalty-header,
  .bonus-header {
    margin-bottom: 8px;
  }
  
  .icon-wrapper {
    width: 32px;
    height: 32px;
  }
  
  .loyalty-title,
  .bonus-title {
    font-size: 13px;
  }
  
  .amount-display {
    padding: 10px;
    margin-bottom: 8px;
    border-radius: 10px;
  }
  
  .amount-value {
    font-size: 18px;
  }
  
  .amount-label {
    font-size: 11px;
  }
  
  .history-btn {
    padding: 8px 16px;
    font-size: 11px;
    border-radius: 16px;
  }
  
  .bonus-section {
    margin-bottom: 12px;
  }
}

/* High DPI displays */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .forevers-logo,
  .icon-wrapper svg {
    image-rendering: -webkit-optimize-contrast;
    image-rendering: crisp-edges;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .wallet-view {
    background: #1a1a1a;
  }
  
  .content-container {
    background: #1a1a1a;
  }
  
  .balance-card {
    background: #2a2a2a;
    border-color: rgba(255, 255, 255, 0.1);
  }
  
  .loyalty-card,
  .bonus-card {
    background: #2a2a2a;
    border-color: rgba(255, 255, 255, 0.1);
  }
  
  .amount-display {
    background: #1e1e1e;
    border-color: rgba(255, 255, 255, 0.1);
  }
  
  .history-btn {
    background: #2a2a2a;
    border-color: rgba(255, 255, 255, 0.2);
    color: #ffffff;
  }
  
  .balance-title,
  .loyalty-title,
  .bonus-title {
    color: #ffffff;
  }
  
  .amount-label {
    color: #a0a0a0;
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  .balance-card,
  .history-btn {
    transition: none;
  }
  
  .history-btn:hover {
    transform: none;
  }
  
  .history-btn:active {
    transform: none;
  }
}

/* Touch optimizations */
@media (hover: none) and (pointer: coarse) {
  .history-btn:hover {
    background: white;
    transform: none;
  }
  
  .history-btn:active {
    background: #f3f4f6;
    transform: scale(0.98);
  }
}

/* Safe area support for different iOS versions */
@supports (padding-bottom: env(safe-area-inset-bottom)) {
  .content-container {
    padding-bottom: calc(100px + env(safe-area-inset-bottom));
  }
}

@supports (padding-bottom: constant(safe-area-inset-bottom)) {
  .content-container {
    padding-bottom: calc(100px + constant(safe-area-inset-bottom));
  }
}

/* Performance optimizations */
.balance-card,
.loyalty-card,
.bonus-card,
.history-btn {
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Custom scrollbar for webkit browsers */
::-webkit-scrollbar {
  width: 0;
}

/* Telegram WebApp specific optimizations */
* {
  -webkit-tap-highlight-color: transparent;
}
</style>
