<template>
  <div class="profile-view-overlay" @click="closeProfile">
    <!-- Background Overlay -->
    <div class="overlay-background"></div>
    
    <!-- Profile Popup with Triangle -->
    <div class="profile-popup" @click.stop>
      <!-- Popup Triangle -->
      <div class="popup-triangle"></div>
      
      <!-- Profile Header -->
      <div class="profile-header">
        <!-- Close Button -->
        <button @click="closeProfile" class="close-button">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        
        <!-- Profile Info -->
        <div class="profile-info">
          <div class="profile-avatar">
            <img
              src="https://images.pexels.com/photos/15023413/pexels-photo-15023413.jpeg?auto=compress&cs=tinysrgb&w=400"
              alt="Profile"
              class="avatar-image"
            />
          </div>
          
          <!-- Silver Badge -->
          <div class="silver-badge">
            <svg width="28" height="28" viewBox="0 0 28 28" fill="none">
              <path d="M14.0004 26.2497C7.24592 26.2497 1.75073 20.7545 1.75073 14.0001C1.75073 7.24564 7.24592 1.75085 14.0004 1.75085C20.7548 1.75085 26.25 7.24564 26.25 14.0001C26.25 20.7545 20.7544 26.2497 14.0004 26.2497Z" fill="white"/>
              <path d="M19.4971 12.7667L15.699 12.2144L14.0007 8.77307V17.4421L17.3977 19.2279L16.7489 15.4452L19.4971 12.7667Z" fill="#E0E0E0"/>
            </svg>
            <span class="badge-text">Silver</span>
          </div>
          
          <div class="profile-name">Jason Williams</div>
          
          <!-- Next Button -->
          <button class="next-button">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path d="M9 18L15 12L9 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </div>
      </div>
      
      <!-- Menu Items with Scroll -->
      <div class="menu-container">
        <div class="menu-items">
          <!-- Calculator -->
          <div class="menu-item">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 16 20" fill="none">
                <path d="M14.1377 0C15.1645 0 16 0.788555 16 1.75781V18.2422C16 19.2114 15.1645 20 14.1377 20H1.8623C0.835502 20 0 19.2114 0 18.2422V1.75781C0 0.788555 0.835502 0 1.8623 0H14.1377Z" fill="white"/>
              </svg>
            </div>
            <span class="menu-text">Calculator</span>
          </div>
          
          <!-- Ambassador -->
          <div class="menu-item">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 14 20" fill="none">
                <path d="M7 9.64844C9.76508 9.64858 12.0066 11.9652 12.0068 14.8242C12.0068 17.6826 9.76511 19.9999 7 20C4.23394 20 1.99219 17.6827 1.99219 14.8242C1.99243 11.9651 4.23409 9.64844 7 9.64844Z" fill="white"/>
              </svg>
            </div>
            <span class="menu-text">Ambassador</span>
          </div>
          
          <!-- Verification with Alert Icon -->
          <div class="menu-item">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 18 22" fill="none">
                <path d="M14.2511 12.4974C15.4932 12.4974 16.5 13.5045 16.5 14.7467V15.3222C16.5 16.2166 16.1805 17.0816 15.5989 17.7611C14.0295 19.5949 11.6422 20.5 8.49673 20.5C5.35076 20.5 2.96466 19.5946 1.39831 17.7601C0.818531 17.081 0.5 16.2174 0.5 15.3245V14.7467C0.5 13.5045 1.50689 12.4974 2.74896 12.4974H14.2511Z" fill="white"/>
              </svg>
            </div>
            <span class="menu-text">Verification</span>
            <div class="alert-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                <circle cx="12" cy="12" r="10" fill="#FF1919"/>
                <path d="M15 9L9 15M9 9L15 15" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </div>
          
          <!-- Security -->
          <div class="menu-item">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 18 20" fill="none">
                <path d="M8.78516 0.0354746C8.92389 -0.0121504 9.07611 -0.0121504 9.21484 0.0354746C10.6561 0.531013 12.1438 0.945188 13.6377 1.26497C14.8838 1.5317 16.1601 1.73823 17.4297 1.87922C17.7546 1.91522 18 2.18263 18 2.50032V8.7386C17.9998 13.165 15.3282 17.2234 11.1943 19.0784L9.26953 19.9427C9.18416 19.9808 9.09193 20.0003 9 20.0003C8.90802 20.0003 8.81583 19.9808 8.73047 19.9427L6.80566 19.0784C2.67178 17.2233 0.000192532 13.165 0 8.7386V2.50032C0 2.18263 0.245411 1.91529 0.570312 1.87922C1.83994 1.73823 3.11627 1.53164 4.3623 1.26497C5.85626 0.945192 7.34396 0.531005 8.78516 0.0354746Z" fill="white"/>
              </svg>
            </div>
            <span class="menu-text">Security</span>
          </div>
          
          <!-- Settings -->
          <div class="menu-item">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M12.2222 20L12.3457 19.375L12.8148 17.0913C13.5679 16.8029 14.2469 16.3972 14.8642 15.9135L17.1605 16.6827L17.7778 16.875L18.0988 16.3221L19.679 13.6778L20 13.125L19.5309 12.7163L17.7531 11.2019C17.8179 10.8083 17.9012 10.4147 17.9012 10C17.9012 9.58531 17.8179 9.19169 17.7531 8.79808L19.5309 7.28369L20 6.875L19.679 6.32215L18.0988 3.67785L17.7778 3.125L17.1605 3.31731L14.8642 4.08654C14.2469 3.60277 13.5679 3.19708 12.8148 2.90862L12.3457 0.625L12.2222 0H7.77775L7.65426 0.625L7.18516 2.90862C6.43209 3.19708 5.75306 3.60277 5.13581 4.08654L2.83947 3.31731L2.22215 3.125L1.9012 3.67785L0.32095 6.32215L0 6.875L0.469097 7.28369L2.24688 8.79808C2.18209 9.19169 2.09873 9.58531 2.09873 10C2.09873 10.4147 2.18209 10.8083 2.24688 11.2019L0.469097 12.7163L0 13.125L0.32095 13.6778L1.9012 16.3221L2.22215 16.875L2.83947 16.6827L5.13581 15.9135C5.75306 16.3972 6.43209 16.8029 7.18516 17.0913L7.65426 19.375L7.77775 20H12.2222Z" fill="white"/>
              </svg>
            </div>
            <span class="menu-text">Settings</span>
          </div>
          
          <!-- Support -->
          <div class="menu-item">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 18 20" fill="none">
                <path d="M8.99902 0C13.9325 0 17.998 3.80872 17.998 8.58691V10.1348C17.9981 10.1411 17.999 10.1479 17.999 10.1543V12.9561C17.9992 12.9624 18 12.9692 18 12.9756V14.543C17.9997 16.724 16.1499 18.4277 13.9502 18.4277H11.2695C10.9422 19.3551 10.0281 19.9951 8.99902 19.9951C7.71066 19.9949 6.59988 18.993 6.59961 17.6777C6.59962 16.3623 7.71051 15.3606 8.99902 15.3604C10.0286 15.3604 10.9435 15.9998 11.2705 16.9277H13.9502C15.1589 16.9277 16.1261 16.1539 16.4111 15.1514C16.155 15.2407 15.8817 15.293 15.5986 15.293C14.3103 15.2927 13.1995 14.2908 13.1992 12.9756V10.1543C13.1992 8.83884 14.3101 7.83714 15.5986 7.83691C15.9032 7.83691 16.1972 7.89422 16.4697 7.99707C16.1535 4.38853 12.9637 1.5 8.99902 1.5C5.03445 1.50011 1.84359 4.38856 1.52734 7.99707C1.80001 7.89396 2.09449 7.83697 2.39941 7.83691C3.6881 7.83691 4.7998 8.83869 4.7998 10.1543V12.9756C4.79953 14.291 3.68794 15.293 2.39941 15.293C1.11107 15.2927 0.000274862 14.2908 0 12.9756V8.58691C4.31105e-05 3.80879 4.0657 0.000121624 8.99902 0Z" fill="white"/>
              </svg>
            </div>
            <span class="menu-text">Support</span>
          </div>
          
          <!-- Help -->
          <div class="menu-item">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M9.69301 13.4082C9.12117 13.4082 8.6582 13.8848 8.6582 14.4566C8.6582 15.0149 9.10754 15.5051 9.69301 15.5051C10.2785 15.5051 10.7414 15.0149 10.7414 14.4566C10.7414 13.8848 10.2649 13.4082 9.69301 13.4082Z" fill="white"/>
                <path d="M10 0C4.47328 0 0 4.47254 0 10V19.2188C0 19.6502 0.349766 20 0.78125 20H10C15.5267 20 20 15.5275 20 10C20 4.47328 15.5275 0 10 0Z" fill="white"/>
              </svg>
            </div>
            <span class="menu-text">Help</span>
          </div>
        </div>
        
        <!-- Scroll Bar -->
        <div class="scroll-bar"></div>
      </div>
      
      <!-- Bottom Section with Start Upgrade and Language/ID -->
      <div class="bottom-section">
        <!-- Start Upgrade Section -->
        <div class="upgrade-section">
          <div class="upgrade-icon">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
              <circle cx="16" cy="16" r="16" fill="#8C4CD1"/>
              <path d="M15.9997 5.11792V15.4117L19.3443 11.8949L15.9997 5.11792Z" fill="#FF9F00"/>
              <path d="M15.9996 5.11792V15.4117L12.655 11.8949L15.9996 5.11792Z" fill="#FED110"/>
            </svg>
          </div>
          <div class="upgrade-content">
            <div class="upgrade-title">Start</div>
            <div class="upgrade-text">
              buy <span class="upgrade-number">123</span> more Forevers to upgrade
            </div>
          </div>
          <button class="upgrade-button">Upgrade</button>
        </div>
        
        <!-- ID and Language Section -->
        <div class="id-language-section">
          <!-- User ID with Copy Function -->
          <div class="user-id-container">
            <div class="user-id-content">
              <span class="id-label">ID:</span>
              <span class="id-number">515745</span>
            </div>
            <button @click="copyUserId" class="copy-button" :class="{ 'copied': isCopied }">
              <svg v-if="!isCopied" width="16" height="16" viewBox="0 0 24 24" fill="none">
                <path d="M8 4V16C8 16.55 8.45 17 9 17H19C19.55 17 20 16.55 20 16V7L17 4H9C8.45 4 8 4.45 8 5Z" stroke="currentColor" stroke-width="2" fill="none"/>
                <path d="M16 4V7H19" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M4 8V20C4 20.55 4.45 21 5 21H13" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span v-if="isCopied" class="copied-text">COPIED</span>
            </button>
          </div>
          
          <!-- Language Selector -->
          <div class="language-selector">
            <button @click="toggleLanguageDropdown" class="language-button">
              <CountryFlag :country="selectedLanguage.country" size="small" />
              <span class="language-text">{{ selectedLanguage.code }}</span>
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" 
                   :class="{ 'rotate-180': isLanguageDropdownOpen }" 
                   class="dropdown-arrow">
                <circle opacity="0.2" cx="10" cy="10" r="10" fill="white"/>
                <path d="M5.71387 8.57146L9.99958 12.8572L14.2853 8.57146" stroke="white" stroke-linecap="round"/>
              </svg>
            </button>
            
            <!-- Language Dropdown -->
            <div v-if="isLanguageDropdownOpen" class="language-dropdown">
              <div 
                v-for="language in availableLanguages" 
                :key="language.code"
                @click="selectLanguage(language)"
                class="language-option"
              >
                <CountryFlag :country="language.country" size="small" />
                <span>{{ language.code }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import CountryFlag from '../components/CountryFlag.vue'

const router = useRouter()

// Copy ID functionality
const isCopied = ref(false)

// Language selector
const isLanguageDropdownOpen = ref(false)
const selectedLanguage = ref({
  code: 'ENG',
  country: 'us'
})

const availableLanguages = [
  { code: 'ENG', country: 'us' },
  { code: 'ESP', country: 'spain' },
  { code: 'FRA', country: 'france' },
  { code: 'GER', country: 'germany' }
]

// Methods
const closeProfile = () => {
  router.go(-1) // Go back to previous page
}

const copyUserId = async () => {
  try {
    await navigator.clipboard.writeText('515745')
    isCopied.value = true
    setTimeout(() => {
      isCopied.value = false
    }, 2000)
  } catch (err) {
    console.error('Failed to copy user ID:', err)
  }
}

const toggleLanguageDropdown = () => {
  isLanguageDropdownOpen.value = !isLanguageDropdownOpen.value
}

const selectLanguage = (language) => {
  selectedLanguage.value = language
  isLanguageDropdownOpen.value = false
}

// Close dropdown when clicking outside
const handleClickOutside = (event) => {
  if (!event.target.closest('.language-selector')) {
    isLanguageDropdownOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style scoped>
/* Profile View Overlay */
.profile-view-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 9999;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding: 20px;
  animation: overlayFadeIn 0.3s ease-out;
}

.overlay-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(89, 89, 89, 0.1);
  backdrop-filter: blur(12px);
}

/* Profile Popup */
.profile-popup {
  position: relative;
  width: 100%;
  max-width: 347px;
  max-height: 90vh;
  background: linear-gradient(94deg, #120B81 33.64%, #09074E 76.52%);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 20px;
  backdrop-filter: blur(32px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  overflow: hidden;
  animation: popupSlideUp 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Popup Triangle */
.popup-triangle {
  position: absolute;
  bottom: -12px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 0;
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  border-top: 12px solid #120B81;
  z-index: 10;
}

/* Profile Header */
.profile-header {
  position: relative;
  padding: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.close-button {
  position: absolute;
  top: 15px;
  right: 15px;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #F4F3FF;
  border: 1px solid #2019CE;
  color: #4B4D50;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  z-index: 10;
}

.close-button:hover {
  background: #EFEEFF;
  transform: scale(1.05);
}

.profile-info {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-top: 30px;
}

.profile-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 2px solid #7E73D6;
  overflow: hidden;
  flex-shrink: 0;
}

.avatar-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.silver-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 2px 16px 2px 2px;
  background: rgba(110, 107, 169, 0.90);
  border: 1px solid #D8D8D8;
  border-radius: 24px;
  height: 32px;
}

.badge-text {
  color: #FAFAFA;
  font-size: 14px;
  font-weight: 400;
  font-family: Montserrat, sans-serif;
}

.profile-name {
  color: #FFF;
  font-size: 21px;
  font-weight: 700;
  font-family: Montserrat, sans-serif;
  flex: 1;
}

.next-button {
  width: 44px;
  height: 44px;
  border-radius: 0 1000px 1000px 0;
  border: 1px solid #2019CE;
  background: #EFEEFF;
  color: #B7B7B7;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.next-button:hover {
  background: #E8E6FF;
  transform: scale(1.05);
}

/* Menu Container with Scroll */
.menu-container {
  position: relative;
  max-height: 300px;
  overflow-y: auto;
  padding: 20px;
  
  /* Custom scrollbar */
  scrollbar-width: thin;
  scrollbar-color: rgba(183, 183, 183, 0.4) transparent;
}

.menu-container::-webkit-scrollbar {
  width: 6px;
}

.menu-container::-webkit-scrollbar-track {
  background: transparent;
}

.menu-container::-webkit-scrollbar-thumb {
  background: rgba(183, 183, 183, 0.4);
  border-radius: 3px;
}

.menu-container::-webkit-scrollbar-thumb:hover {
  background: rgba(183, 183, 183, 0.6);
}

.menu-items {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px;
  border-radius: 8px;
  transition: all 0.2s ease;
  position: relative;
}

.menu-item:hover {
  background: rgba(255, 255, 255, 0.05);
}

.menu-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(64, 64, 64, 0.24);
  border: 1px solid #FFF;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.menu-text {
  color: #FFF;
  font-size: 16px;
  font-weight: 700;
  font-family: Montserrat, sans-serif;
  flex: 1;
}

.alert-icon {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

.scroll-bar {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  width: 2px;
  height: 60px;
  background: rgba(183, 183, 183, 0.4);
  border-radius: 30px;
  border: 1px solid #B7B7B7;
}

/* Bottom Section */
.bottom-section {
  padding: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  background: linear-gradient(94deg, #120B81 33.64%, #09074E 76.52%);
}

/* Upgrade Section */
.upgrade-section {
  background: #F1E7FF;
  border: 1px solid #DCCCF1;
  border-radius: 16px;
  padding: 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
  position: relative;
  overflow: hidden;
}

.upgrade-section::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 140px;
  height: 100%;
  background: linear-gradient(90deg, #8C4CD1 0%, #C497FF 100%);
  opacity: 0.4;
  border-radius: 16px 0 0 16px;
}

.upgrade-icon {
  width: 32px;
  height: 32px;
  flex-shrink: 0;
  z-index: 2;
}

.upgrade-content {
  flex: 1;
  z-index: 2;
}

.upgrade-title {
  color: #02070E;
  font-size: 19px;
  font-weight: 700;
  font-family: Montserrat, sans-serif;
  margin-bottom: 4px;
}

.upgrade-text {
  color: #4B4D50;
  font-size: 14px;
  font-weight: 400;
  font-family: Montserrat, sans-serif;
}

.upgrade-number {
  color: #8C4CD1;
  font-weight: 700;
}

.upgrade-button {
  background: linear-gradient(90deg, #2019CE 0%, #473FFF 100%);
  color: #FFF;
  font-size: 16px;
  font-weight: 700;
  font-family: Montserrat, sans-serif;
  padding: 12px 24px;
  border-radius: 1000px;
  border: none;
  transition: all 0.2s ease;
  z-index: 2;
}

.upgrade-button:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(32, 25, 206, 0.3);
}

/* ID and Language Section */
.id-language-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

/* User ID */
.user-id-container {
  display: flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.30);
  border: 1px solid rgba(255, 255, 255, 0.40);
  border-radius: 100px;
  backdrop-filter: blur(32px);
  overflow: hidden;
}

.user-id-content {
  padding: 8px 13px;
  display: flex;
  align-items: center;
  gap: 4px;
}

.id-label {
  color: #B7B7B7;
  font-size: 14px;
  font-weight: 400;
  font-family: Montserrat, sans-serif;
}

.id-number {
  color: #FFF;
  font-size: 14px;
  font-weight: 400;
  font-family: Montserrat, sans-serif;
}

.copy-button {
  width: 24px;
  height: 24px;
  background: #FFF;
  border: 1.2px solid #D8D8D8;
  border-radius: 0 1200px 1200px 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #4B4D50;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

.copy-button:hover {
  background: #F0F0F0;
  transform: scale(1.05);
}

.copy-button.copied {
  background: #4CAF50;
  color: white;
  border-color: #4CAF50;
}

.copied-text {
  font-size: 10px;
  font-weight: 700;
  white-space: nowrap;
}

/* Language Selector */
.language-selector {
  position: relative;
}

.language-button {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px;
  background: rgba(255, 255, 255, 0.20);
  border: 1px solid rgba(255, 255, 255, 0.24);
  border-radius: 1000px;
  transition: all 0.2s ease;
}

.language-button:hover {
  background: rgba(255, 255, 255, 0.30);
}

.language-text {
  color: #FAFAFA;
  font-size: 16px;
  font-weight: 400;
  font-family: Montserrat, sans-serif;
  margin: 0 4px;
}

.dropdown-arrow {
  transition: transform 0.2s ease;
}

.rotate-180 {
  transform: rotate(180deg);
}

/* Language Dropdown */
.language-dropdown {
  position: absolute;
  bottom: 100%;
  right: 0;
  margin-bottom: 8px;
  background: rgba(18, 11, 129, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  backdrop-filter: blur(32px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  min-width: 120px;
  z-index: 1000;
  animation: dropdownSlideUp 0.2s ease-out;
}

.language-option {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  color: #FAFAFA;
  font-size: 14px;
  font-weight: 400;
  font-family: Montserrat, sans-serif;
  cursor: pointer;
  transition: background 0.2s ease;
}

.language-option:first-child {
  border-radius: 12px 12px 0 0;
}

.language-option:last-child {
  border-radius: 0 0 12px 12px;
}

.language-option:hover {
  background: rgba(255, 255, 255, 0.1);
}

/* Animations */
@keyframes overlayFadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes popupSlideUp {
  from {
    opacity: 0;
    transform: translateY(100%) scale(0.9);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@keyframes dropdownSlideUp {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive Design */
@media (max-width: 320px) {
  .profile-popup {
    max-width: 300px;
    margin: 10px;
  }
  
  .profile-header {
    padding: 15px;
  }
  
  .profile-info {
    gap: 12px;
  }
  
  .profile-avatar {
    width: 60px;
    height: 60px;
  }
  
  .profile-name {
    font-size: 18px;
  }
  
  .silver-badge {
    padding: 2px 12px 2px 2px;
    height: 28px;
  }
  
  .badge-text {
    font-size: 12px;
  }
  
  .menu-container {
    padding: 15px;
    max-height: 250px;
  }
  
  .menu-item {
    padding: 8px;
  }
  
  .menu-icon {
    width: 32px;
    height: 32px;
  }
  
  .menu-text {
    font-size: 14px;
  }
  
  .bottom-section {
    padding: 15px;
  }
  
  .upgrade-section {
    padding: 12px;
    gap: 8px;
  }
  
  .upgrade-title {
    font-size: 16px;
  }
  
  .upgrade-text {
    font-size: 12px;
  }
  
  .upgrade-button {
    padding: 8px 16px;
    font-size: 14px;
  }
  
  .id-language-section {
    gap: 8px;
  }
  
  .user-id-content {
    padding: 6px 10px;
  }
  
  .id-label,
  .id-number {
    font-size: 12px;
  }
  
  .copy-button {
    width: 20px;
    height: 20px;
  }
  
  .language-text {
    font-size: 14px;
  }
}

@media (min-width: 321px) and (max-width: 374px) {
  .profile-popup {
    max-width: 320px;
  }
  
  .profile-avatar {
    width: 70px;
    height: 70px;
  }
  
  .profile-name {
    font-size: 19px;
  }
  
  .menu-icon {
    width: 36px;
    height: 36px;
  }
  
  .menu-text {
    font-size: 15px;
  }
}

@media (min-width: 375px) and (max-width: 430px) {
  .profile-popup {
    max-width: 340px;
  }
}

@media (min-width: 431px) and (max-width: 768px) {
  .profile-popup {
    max-width: 380px;
  }
  
  .menu-container {
    max-height: 350px;
  }
}

@media (min-width: 769px) {
  .profile-popup {
    max-width: 400px;
  }
  
  .menu-container {
    max-height: 400px;
  }
}

/* Touch optimizations */
@media (hover: none) and (pointer: coarse) {
  .menu-item:active {
    background: rgba(255, 255, 255, 0.1);
    transform: scale(0.98);
  }
  
  .copy-button:active {
    transform: scale(0.95);
  }
  
  .language-button:active {
    transform: scale(0.98);
  }
  
  .upgrade-button:active {
    transform: scale(0.98);
  }
  
  .close-button:active {
    transform: scale(0.95);
  }
  
  .next-button:active {
    transform: scale(0.95);
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .overlay-background {
    background: rgba(0, 0, 0, 0.3);
  }
}

/* Accessibility */
@media (prefers-reduced-motion: reduce) {
  .profile-popup,
  .overlay-background,
  .language-dropdown {
    animation: none;
  }
  
  .copy-button,
  .language-button,
  .upgrade-button,
  .close-button,
  .next-button,
  .dropdown-arrow {
    transition: none;
  }
}

/* High contrast mode */
@media (prefers-contrast: high) {
  .profile-popup {
    border: 2px solid #FFF;
  }
  
  .menu-icon {
    border: 2px solid #FFF;
  }
  
  .upgrade-section {
    border: 2px solid #8C4CD1;
  }
  
  .user-id-container {
    border: 2px solid #FFF;
  }
  
  .language-button {
    border: 2px solid #FFF;
  }
}
</style>
