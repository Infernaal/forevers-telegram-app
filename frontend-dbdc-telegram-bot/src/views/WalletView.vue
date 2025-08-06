<template>
  <div class="w-full min-h-screen bg-gray-100 font-montserrat overflow-x-hidden wallet-view">
    <!-- Content Container -->
    <div class="px-4 pt-4 pb-32 min-h-[calc(100vh-100px)]">

      <!-- Forevers Balance Section -->
      <div class="mb-4">
        <div class="bg-[#EFEEFF] rounded-2xl p-4 shadow-md">
          <div class="flex items-center justify-between">
            <div>
              <h2 class="text-lg font-semibold text-[#02070E] leading-snug">
                Forevers<br />Balance
              </h2>
            </div>
            <div class="flex items-center gap-2">
              <svg class="w-8 h-8" viewBox="0 0 32 32" fill="none">
                <path d="M30.6666 7.38081V1.33337H7.1291V9.01148H1.33325V15.0589H7.1291V30.1076H13.894V22.7277H19.6153V16.6803H13.894V15.0589H25.1316V9.01148H13.894V7.38081H30.6666Z" fill="#2019CE"/>
              </svg>
              <span class="text-xl font-bold text-[#2019CE]">{{ foreversBalance.toLocaleString() }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Loyalty Program Section -->
      <div class="mb-4">
        <div class="bg-[#EFEEFF] border border-purple-400/20 rounded-2xl p-4 shadow-md">
          <div class="flex items-center gap-2 mb-4">
            <div class="w-10 h-10 rounded-full bg-[#FAFAFA] flex items-center justify-center border border-white/25 shadow">
              <svg width="21" height="21" viewBox="0 0 22 22" fill="none">
                <g clip-path="url(#clip0_2_23137)">
                  <path d="M10.8717 21.4348C10.6085 21.4348 10.3908 21.3526 10.2186 21.1884C10.0465 21.0241 9.9604 20.8164 9.9604 20.5652V19C8.98831 18.8454 8.15798 18.5169 7.46942 18.0145C6.78085 17.512 6.24418 16.8744 5.85939 16.1014C5.75813 15.8889 5.75813 15.6666 5.85939 15.4348C5.96065 15.2029 6.13279 15.0386 6.37581 14.942C6.59859 14.8454 6.82642 14.8454 7.05932 14.942C7.29221 15.0386 7.46942 15.1932 7.59093 15.4058C7.95546 16.0628 8.43138 16.5555 9.01869 16.884C9.60599 17.2125 10.2844 17.3768 11.054 17.3768C12.0261 17.3768 12.826 17.1449 13.4538 16.6811C14.0817 16.2174 14.3956 15.5797 14.3956 14.7681C14.3956 13.9178 14.1171 13.2608 13.5602 12.7971C13.0032 12.3333 11.9552 11.8599 10.4161 11.3768C8.95793 10.9323 7.86939 10.343 7.15045 9.60866C6.43151 8.87436 6.07204 7.95649 6.07204 6.85504C6.07204 5.79224 6.43151 4.90335 7.15045 4.18837C7.86939 3.4734 8.80604 3.0676 9.9604 2.97098V1.43475C9.9604 1.18354 10.0465 0.975814 10.2186 0.811562C10.3908 0.647311 10.6085 0.565186 10.8717 0.565186C11.135 0.565186 11.3527 0.647311 11.5249 0.811562C11.697 0.975814 11.7831 1.18354 11.7831 1.43475V2.97098C12.5121 3.0676 13.1653 3.28016 13.7424 3.60866C14.3196 3.93717 14.8006 4.36229 15.1854 4.88403C15.3271 5.07726 15.3575 5.28499 15.2765 5.50721C15.1955 5.72944 15.0335 5.88886 14.7905 5.98548C14.5677 6.08209 14.3348 6.09176 14.0918 6.01446C13.8488 5.93717 13.6462 5.79224 13.4842 5.57968C13.2007 5.23185 12.8514 4.97581 12.4362 4.81156C12.021 4.64731 11.5198 4.56519 10.9325 4.56519C10.0009 4.56519 9.26171 4.76808 8.71491 5.17388C8.16811 5.57968 7.89471 6.1304 7.89471 6.82606C7.89471 7.56035 8.19848 8.15456 8.80604 8.60866C9.4136 9.06277 10.5376 9.53137 12.178 10.0145C13.5551 10.4203 14.5728 11.0048 15.231 11.7681C15.8891 12.5314 16.2182 13.4927 16.2182 14.6521C16.2182 15.8695 15.8436 16.8502 15.0943 17.5942C14.3449 18.3381 13.2412 18.8164 11.7831 19.029V20.5652C11.7831 20.8164 11.697 21.0241 11.5249 21.1884C11.3527 21.3526 11.135 21.4348 10.8717 21.4348Z" fill="#2019CE"/>
                </g>
              </svg>
            </div>
            <span class="text-base font-medium text-[#02070E]">Loyalty program</span>
          </div>
          <div class="bg-[#FAFAFA] border border-[#2019CE]/20 rounded-2xl p-4 mb-4">
            <div class="flex flex-col gap-2">
              <span class="text-xl font-bold text-[#2019CE]">${{ loyaltyBalance.toLocaleString() }}</span>
              <span class="text-sm font-medium text-[#4B4D50]">Forevers Rent %</span>
            </div>
          </div>
          <button
            @click="navigateToTransactions"
            class="w-full text-sm font-bold text-[#4B4D50] bg-white border border-gray-300 rounded-full py-3 px-6 hover:bg-gray-50 active:scale-[0.98] shadow-md"
          >
            Rent Out History
          </button>
        </div>
      </div>

      <!-- Bonus Section -->
      <div class="mb-6">
        <div class="bg-[#FFF3E7] border border-purple-400/20 rounded-2xl p-4 shadow-md">
          <div class="flex items-center gap-2 mb-4">
            <div class="w-10 h-10 rounded-full bg-[#FAFAFA] flex items-center justify-center border border-white/25 shadow">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M19.8567 6.28571H17.4567C17.751 6.05915 17.9909 5.76969 18.159 5.43849C18.327 5.10729 18.419 4.74272 18.4281 4.37143C18.4151 3.74162 18.1572 3.14167 17.7091 2.69891C17.261 2.25615 16.658 2.00544 16.0281 2C14.3709 2 12.9138 3.04286 11.8709 4.92143C10.8281 3.04286 9.37094 2 7.7138 2C7.08388 2.00544 6.48088 2.25615 6.03279 2.69891C5.58469 3.14167 5.32678 3.74162 5.3138 4.37143C5.32289 4.74272 5.41483 5.10729 5.5829 5.43849C5.75098 5.76969 5.99093 6.05915 6.28523 6.28571H4.14237C3.57405 6.28571 3.029 6.51148 2.62714 6.91334C2.22528 7.31521 1.99951 7.86025 1.99951 8.42857V9.85714C2.00075 10.2992 2.13871 10.7301 2.39447 11.0908C2.65022 11.4514 3.01126 11.7241 3.42808 11.8714V19.8571C3.42808 20.4255 3.65385 20.9705 4.05571 21.3724C4.45758 21.7742 5.00262 22 5.57094 22H18.4281C18.9964 22 19.5414 21.7742 19.9433 21.3724C20.3452 20.9705 20.5709 20.4255 20.5709 19.8571V11.8714C20.9878 11.7241 21.3488 11.4514 21.6046 11.0908C21.8603 10.7301 21.9983 10.2992 21.9995 9.85714V8.42857C21.9995 7.86025 21.7737 7.31521 21.3719 6.91334C20.97 6.51148 20.425 6.28571 19.8567 6.28571ZM13.4281 10.5714H10.5709V7.71429H13.4281V10.5714ZM16.0281 3.42857C16.2787 3.43533 16.5177 3.536 16.6976 3.71063C16.8775 3.88526 16.9853 4.1211 16.9995 4.37143C16.9995 4.78571 16.6709 5.18571 16.0852 5.50714C15.0548 5.98085 13.9336 6.22458 12.7995 6.22143C13.3495 5.06429 14.3995 3.42857 16.0281 3.42857ZM7.7138 3.42857C9.34237 3.42857 10.3924 5.06429 10.9352 6.28571C9.80327 6.29036 8.68409 6.04653 7.65665 5.57143C7.0638 5.25 6.74237 4.85714 6.74237 4.43571C6.74039 4.17414 6.84099 3.92221 7.02259 3.73393C7.20418 3.54566 7.45232 3.43604 7.7138 3.42857ZM3.42808 8.42857C3.42808 8.23913 3.50334 8.05745 3.63729 7.9235C3.77125 7.78954 3.95293 7.71429 4.14237 7.71429H9.14237V10.5714H4.14237C3.95293 10.5714 3.77125 10.4962 3.63729 10.3622C3.50334 10.2283 3.42808 10.0466 3.42808 9.85714V8.42857ZM4.85665 19.8571V12H9.85665V20.5714H5.57094C5.3815 20.5714 5.19982 20.4962 5.06586 20.3622C4.93191 20.2283 4.85665 20.0466 4.85665 19.8571ZM11.2852 20.5714V12H12.7138V20.5714H11.2852ZM19.1424 19.8571C19.1424 20.0466 19.0671 20.2283 18.9332 20.3622C18.7992 20.4962 18.6175 20.5714 18.4281 20.5714H14.1424V12H19.1424V19.8571ZM20.5709 9.85714C20.5709 10.0466 20.4957 10.2283 20.3617 10.3622C20.2278 10.4962 20.0461 10.5714 19.8567 10.5714H14.8567V7.71429H19.8567C20.0461 7.71429 20.2278 7.78954 20.3617 7.9235C20.4957 8.05745 20.5709 8.23913 20.5709 8.42857V9.85714Z" fill="#2019CE"/>
              </svg>
            </div>
            <span class="text-base font-medium text-[#02070E]">Bonus</span>
          </div>
          <div class="bg-[#FAFAFA] border border-[#2019CE]/20 rounded-2xl p-4">
            <div class="flex flex-col gap-2">
              <span class="text-xl font-bold text-[#2019CE]">${{ bonusBalance.toLocaleString() }}</span>
              <span class="text-sm font-medium text-[#4B4D50]">Reward</span>
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
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import BottomNavigation from '../components/BottomNavigation.vue'

const router = useRouter()

const foreversBalance = ref(0)
const loyaltyBalance = ref(0)
const bonusBalance = ref(0)

const fetchWalletData = async () => {
  try {
    const response = await fetch('https://dbdc-mini.dubadu.com/api/v1/dbdc/api/v1/dbdc/forevers/96')
    const result = await response.json()
    // Forevers balance
    foreversBalance.value = parseFloat(result?.forevers_balance?.balance || 0)
    // Loyalty program
    const loyalty = result?.wallets?.find(w => w.type === 'loyalty_program')
    loyaltyBalance.value = loyalty ? parseFloat(loyalty.amount) : 0
    // Bonus
    const bonus = result?.wallets?.find(w => w.type === 'bonus')
    bonusBalance.value = bonus ? parseFloat(bonus.amount) : 0
  } catch (error) {
    console.error('Failed to fetch wallet data:', error)
  }
}

onMounted(() => {
  fetchWalletData()
})

const navigateToTransactions = () => {
  router.push('/rent-out-transactions')
}
</script>

<style scoped>
.wallet-view {
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

.wallet-view::-webkit-scrollbar {
  display: none; /* Chrome, Safari and Opera */
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
  background: #FAFAFA;
  border: 1px solid rgba(255, 255, 255, 0.24);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.04);
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
    background: #FAFAFA;
    box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.04);
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
    background: #FAFAFA;
    box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.04);
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
    width: 100%;
  }

  .content-container {
    padding: 24px 24px 140px 24px;
    max-width: 800px;
    margin: 0 auto;
  }

  .forevers-balance-section,
  .loyalty-section {
    margin-bottom: 24px;
  }

  .balance-card,
  .loyalty-card,
  .bonus-card {
    border-radius: 24px;
    padding: 28px;
  }

  .balance-title {
    font-size: 28px;
  }

  .forevers-logo {
    width: 48px;
    height: 48px;
  }

  .balance-value {
    font-size: 36px;
  }

  .loyalty-header,
  .bonus-header {
    margin-bottom: 24px;
  }

  .icon-wrapper {
    width: 56px;
    height: 56px;
    background: #FAFAFA;
    box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.04);
  }

  .loyalty-title,
  .bonus-title {
    font-size: 22px;
  }

  .amount-display {
    padding: 24px;
    margin-bottom: 24px;
    border-radius: 24px;
  }

  .amount-value {
    font-size: 36px;
  }

  .amount-label {
    font-size: 18px;
  }

  .history-btn {
    padding: 18px 36px;
    font-size: 18px;
    border-radius: 36px;
  }

  .bonus-section {
    margin-bottom: 32px;
  }
}

/* Tablets and desktop - ≥769px */
@media (min-width: 769px) {
  .wallet-view {
    width: 100%;
    margin: 0;
  }

  .content-container {
    padding: 40px 40px 160px 40px;
    max-width: 1200px;
    margin: 0 auto;
  }

  .forevers-balance-section,
  .loyalty-section {
    margin-bottom: 32px;
  }

  .balance-card,
  .loyalty-card,
  .bonus-card {
    border-radius: 32px;
    padding: 40px;
  }

  .balance-title {
    font-size: 36px;
  }

  .forevers-logo {
    width: 64px;
    height: 64px;
  }

  .balance-value {
    font-size: 48px;
  }

  .loyalty-header,
  .bonus-header {
    margin-bottom: 32px;
  }

  .icon-wrapper {
    width: 72px;
    height: 72px;
    background: #FAFAFA;
    box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.04);
  }

  .loyalty-title,
  .bonus-title {
    font-size: 28px;
  }

  .amount-display {
    padding: 32px;
    margin-bottom: 32px;
    border-radius: 32px;
  }

  .amount-value {
    font-size: 48px;
  }

  .amount-label {
    font-size: 22px;
  }

  .history-btn {
    padding: 24px 48px;
    font-size: 22px;
    border-radius: 48px;
  }

  .bonus-section {
    margin-bottom: 48px;
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
    background: #FAFAFA;
    box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.04);
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
