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
          
          <div class="profile-details">
            <!-- Silver Badge -->
            <div class="silver-badge">
              <svg width="28" height="28" viewBox="0 0 28 28" fill="none">
                <circle cx="14" cy="14" r="13.25" fill="white" stroke="#E0E0E0" stroke-width="0.5"/>
                <path d="M14.0004 25.5519C20.3702 25.5519 25.5526 20.3699 25.5526 13.9999C25.5526 10.6131 24.0873 7.56229 21.7577 5.44697L20.2081 5.37122C11.7704 5.37122 4.86244 11.9017 4.25073 20.1829C6.30211 23.4072 9.90475 25.5519 14.0006 25.5519Z" fill="#B5B5B5"/>
                <path d="M19.4965 12.7667L15.6984 12.2148L14.0001 8.77307L12.3014 12.2148L8.50366 12.7667L11.2519 15.4452L10.6031 19.2279L14.0001 17.4421L17.397 19.2279L16.7483 15.4452L19.4965 12.7667Z" fill="#F6F6F6"/>
              </svg>
              <span class="badge-text">Silver</span>
            </div>
            
            <!-- Profile Name -->
            <div class="profile-name">Jason Williams</div>
          </div>
          
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
                <path d="M14.1377 0C15.1645 0 16 0.788555 16 1.75781V18.2422C16 19.2114 15.1645 20 14.1377 20H1.8623C0.835502 20 0 19.2114 0 18.2422V1.75781C0 0.788555 0.835502 0 1.8623 0H14.1377ZM1.8623 1.17188C1.52004 1.17188 1.24121 1.43473 1.24121 1.75781V18.2422C1.24121 18.5653 1.52004 18.8281 1.8623 18.8281H14.1377C14.48 18.8281 14.7587 18.5653 14.7588 18.2422V1.75781C14.7588 1.43473 14.48 1.17188 14.1377 1.17188H1.8623ZM5.06445 14.5947C5.40691 14.595 5.68443 14.8573 5.68457 15.1807V16.9668C5.6844 17.2901 5.40693 17.5525 5.06445 17.5527H2.88477C2.54207 17.5527 2.26385 17.2903 2.26367 16.9668V15.1807C2.26381 14.8572 2.54205 14.5947 2.88477 14.5947H5.06445ZM13.1152 14.5947C13.4578 14.5949 13.7353 14.8573 13.7354 15.1807V16.9668C13.7352 17.2901 13.4577 17.5525 13.1152 17.5527H6.91016C6.56746 17.5527 6.28924 17.2903 6.28906 16.9668V15.1807C6.2892 14.8572 6.56744 14.5947 6.91016 14.5947H13.1152Z" fill="white"/>
              </svg>
            </div>
            <span class="menu-text">Calculator</span>
          </div>
          
          <!-- Ambassador -->
          <div class="menu-item">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 14 20" fill="none">
                <path d="M7 9.64844C9.76508 9.64858 12.0066 11.9652 12.0068 14.8242C12.0068 17.6826 9.76511 19.9999 7 20C4.23394 20 1.99219 17.6827 1.99219 14.8242C1.99243 11.9651 4.23409 9.64844 7 9.64844ZM6.09668 13.8418L4.07715 14.1465L5.53906 15.6182L5.19434 17.6992L7 16.7168L8.80566 17.6992L8.46191 15.6182L9.92383 14.1465L7.90332 13.8418L7 11.9512L6.09668 13.8418ZM4.60547 0L7 3.30078L9.39453 0H14L7 9.64844L0 0H4.60547Z" fill="white"/>
              </svg>
            </div>
            <span class="menu-text">Ambassador</span>
          </div>
          
          <!-- Verification with Alert Icon -->
          <div class="menu-item">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 18 22" fill="none">
                <path d="M14.2511 12.4974C15.4932 12.4974 16.5 13.5045 16.5 14.7467V15.3222C16.5 16.2166 16.1805 17.0816 15.5989 17.7611C14.0295 19.5949 11.6422 20.5 8.49673 20.5C5.35076 20.5 2.96466 19.5946 1.39831 17.7601C0.818531 17.081 0.5 16.2174 0.5 15.3245V14.7467C0.5 13.5045 1.50689 12.4974 2.74896 12.4974H14.2511ZM14.2511 13.9977H2.74896C2.33534 13.9977 2.00005 14.333 2.00005 14.7467V15.3245C2.00005 15.8602 2.19117 16.3784 2.53904 16.7858C3.79239 18.2538 5.75834 18.9997 8.49673 18.9997C11.2351 18.9997 13.2028 18.2537 14.4593 16.7855C14.8082 16.3779 14.9999 15.8589 14.9999 15.3222V14.7467C14.9999 14.333 14.6647 13.9977 14.2511 13.9977ZM8.49673 0.5C11.2582 0.5 13.4969 2.73897 13.4969 5.50088C13.4969 8.2628 11.2582 10.5017 8.49673 10.5017C5.73521 10.5017 3.49656 8.2628 3.49656 5.50088C3.49656 2.73897 5.73521 0.5 8.49673 0.5ZM8.49673 2.00026C6.56366 2.00026 4.99661 3.56755 4.99661 5.50088C4.99661 7.43422 6.56366 9.00148 8.49673 9.00148C10.4298 9.00148 11.9968 7.43422 11.9968 5.50088C11.9968 3.56755 10.4298 2.00026 8.49673 2.00026Z" fill="white"/>
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
                <path d="M12.2222 20L12.3457 19.375L12.8148 17.0913C13.5679 16.8029 14.2469 16.3972 14.8642 15.9135L17.1605 16.6827L17.7778 16.875L18.0988 16.3221L19.679 13.6778L20 13.125L19.5309 12.7163L17.7531 11.2019C17.8179 10.8083 17.9012 10.4147 17.9012 10C17.9012 9.58531 17.8179 9.19169 17.7531 8.79808L19.5309 7.28369L20 6.875L19.679 6.32215L18.0988 3.67785L17.7778 3.125L17.1605 3.31731L14.8642 4.08654C14.2469 3.60277 13.5679 3.19708 12.8148 2.90862L12.3457 0.625L12.2222 0H7.77775L7.65426 0.625L7.18516 2.90862C6.43209 3.19708 5.75306 3.60277 5.13581 4.08654L2.83947 3.31731L2.22215 3.125L1.9012 3.67785L0.32095 6.32215L0 6.875L0.469097 7.28369L2.24688 8.79808C2.18209 9.19169 2.09873 9.58531 2.09873 10C2.09873 10.4147 2.18209 10.8083 2.24688 11.2019L0.469097 12.7163L0 13.125L0.32095 13.6778L1.9012 16.3221L2.22215 16.875L2.83947 16.6827L5.13581 15.9135C5.75306 16.3972 6.43209 16.8029 7.18516 17.0913L7.65426 19.375L7.77775 20H12.2222ZM9.99998 13.8462C12.1728 13.8462 13.9506 12.1154 13.9506 10C13.9506 7.88461 12.1728 6.15385 9.99998 6.15385C7.82714 6.15385 6.04936 7.88461 6.04936 10C6.04936 12.1154 7.82714 13.8462 9.99998 13.8462Z" fill="white"/>
              </svg>
            </div>
            <span class="menu-text">Settings</span>
          </div>
          
          <!-- Support -->
          <div class="menu-item">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 18 20" fill="none">
                <path d="M8.99902 0C13.9325 0 17.998 3.80872 17.998 8.58691V10.1348C17.9981 10.1411 17.999 10.1479 17.999 10.1543V12.9561C17.9992 12.9624 18 12.9692 18 12.9756V14.543C17.9997 16.724 16.1499 18.4277 13.9502 18.4277H11.2695C10.9422 19.3551 10.0281 19.9951 8.99902 19.9951C7.71066 19.9949 6.59988 18.993 6.59961 17.6777C6.59962 16.3623 7.71051 15.3606 8.99902 15.3604C10.0286 15.3604 10.9435 15.9998 11.2705 16.9277H13.9502C15.1589 16.9277 16.1261 16.1539 16.4111 15.1514C16.155 15.2407 15.8817 15.293 15.5986 15.293C14.3103 15.2927 13.1995 14.2908 13.1992 12.9756V10.1543C13.1992 8.83884 14.3101 7.83714 15.5986 7.83691C15.9032 7.83691 16.1972 7.89422 16.4697 7.99707C16.1535 4.38853 12.9637 1.5 8.99902 1.5C5.03445 1.50011 1.84359 4.38856 1.52734 7.99707C1.80001 7.89396 2.09449 7.83697 2.39941 7.83691C3.6881 7.83691 4.7998 8.83869 4.7998 10.1543V12.9756C4.79953 14.291 3.68794 15.293 2.39941 15.293C1.11107 15.2927 0.000274862 14.2908 0 12.9756V8.58691C4.31105e-05 3.80879 4.0657 0.000121624 8.99902 0ZM8.99902 16.8604C8.4656 16.8606 8.09962 17.2622 8.09961 17.6777C8.0999 18.0931 8.4658 18.4949 8.99902 18.4951C9.53249 18.4951 9.89913 18.0932 9.89941 17.6777C9.89941 17.2621 9.53269 16.8604 8.99902 16.8604ZM2.39941 9.33691C1.866 9.33713 1.50001 9.73876 1.5 10.1543V12.9756C1.50029 13.391 1.86621 13.7927 2.39941 13.793C2.93286 13.793 3.29952 13.3911 3.2998 12.9756V10.1543C3.2998 9.73865 2.93306 9.33691 2.39941 9.33691ZM15.5986 9.33691C15.0652 9.33713 14.6992 9.73876 14.6992 10.1543V12.9756C14.6995 13.391 15.0654 13.7927 15.5986 13.793C16.1321 13.793 16.4987 13.3911 16.499 12.9756V10.1729C16.4989 10.1667 16.4981 10.1605 16.498 10.1543V10.1348C16.487 9.72598 16.1241 9.33691 15.5986 9.33691Z" fill="white"/>
              </svg>
            </div>
            <span class="menu-text">Support</span>
          </div>
          
          <!-- Help -->
          <div class="menu-item">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M9.69301 13.4082C9.12117 13.4082 8.6582 13.8848 8.6582 14.4566C8.6582 15.0149 9.10754 15.5051 9.69301 15.5051C10.2785 15.5051 10.7414 15.0149 10.7414 14.4566C10.7414 13.8848 10.2649 13.4082 9.69301 13.4082Z" fill="white"/>
                <path d="M9.86984 5.46875C8.03168 5.46875 7.1875 6.55801 7.1875 7.29328C7.1875 7.82434 7.6368 8.06941 8.00445 8.06941C8.73969 8.06941 8.44016 7.02098 9.82898 7.02098C10.5098 7.02098 11.0545 7.32055 11.0545 7.94687C11.0545 8.68219 10.292 9.10426 9.84262 9.48551C9.44777 9.8259 8.93035 10.3842 8.93035 11.5552C8.93035 12.2632 9.12094 12.4674 9.67922 12.4674C10.3464 12.4674 10.4825 12.1679 10.4825 11.9092C10.4825 11.2011 10.4962 10.7927 11.2451 10.2072C11.6127 9.92125 12.7701 8.99535 12.7701 7.71543C12.7701 6.43551 11.6127 5.46875 9.86984 5.46875Z" fill="white"/>
                <path d="M10 0C4.47328 0 0 4.47254 0 10V19.2188C0 19.6502 0.349766 20 0.78125 20H10C15.5267 20 20 15.5275 20 10C20 4.47328 15.5275 0 10 0ZM10 18.4375H1.5625V10C1.5625 5.33684 5.33621 1.5625 10 1.5625C14.6632 1.5625 18.4375 5.33621 18.4375 10C18.4375 14.6638 14.6638 18.4375 10 18.4375Z" fill="white"/>
              </svg>
            </div>
            <span class="menu-text">Help</span>
          </div>
        </div>
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
          <div class="user-id-container" :class="{ 'copied': isCopied }">
            <div class="user-id-content">
              <span class="id-label">ID:</span>
              <span class="id-number">515745</span>
            </div>
            <button @click="copyUserId" class="copy-button" :class="{ 'copied': isCopied }">
              <svg v-if="!isCopied" width="14" height="16" viewBox="0 0 24 24" fill="none">
                <path d="M18.2806 1.19995H8.98336C8.42322 1.19995 7.88603 1.43348 7.48995 1.84917C7.09387 2.26486 6.87136 2.82866 6.87136 3.41653V4.26906H5.81536C5.2278 4.26906 4.66431 4.51402 4.24885 4.95006C3.83338 5.3861 3.59998 5.97749 3.59998 6.59414V20.4749C3.59998 21.0915 3.83338 21.6829 4.24885 22.119C4.66431 22.555 5.2278 22.8 5.81536 22.8H14.9132C15.5008 22.8 16.0643 22.555 16.4797 22.119C16.8952 21.6829 17.1286 21.0915 17.1286 20.4749V19.6998H18.2806C18.8363 19.6999 19.3699 19.4709 19.7663 19.0621C20.1627 18.6533 20.3903 18.0975 20.4 17.5143V3.41653C20.398 2.82794 20.1739 2.26417 19.7766 1.8487C19.3794 1.43323 18.8414 1.19995 18.2806 1.19995Z" fill="currentColor"/>
              </svg>
              <div v-if="isCopied" class="copied-indicator">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                  <path d="M20 6L9 17L4 12" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <span class="copied-text">COPIED</span>
              </div>
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
  align-items: flex-start;
  gap: 16px;
  margin-top: 30px;
}

.profile-details {
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 1;
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
  width: fit-content;
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
  margin: 0;
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
  flex-shrink: 0;
}

.next-button:hover {
  background: #E8E6FF;
  transform: scale(1.05);
}

/* Menu Container with Hidden Scroll */
.menu-container {
  position: relative;
  max-height: 300px;
  overflow-y: auto;
  padding: 20px;
  
  /* Hide scrollbar */
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* IE and Edge */
}

.menu-container::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera */
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
  transition: all 0.3s ease;
}

.user-id-container.copied {
  background: #4CAF50;
  border-color: #4CAF50;
  transform: scale(1.05);
}

.user-id-content {
  padding: 8px 13px;
  display: flex;
  align-items: center;
  gap: 4px;
}

.user-id-container.copied .user-id-content {
  color: white;
}

.id-label {
  color: #B7B7B7;
  font-size: 14px;
  font-weight: 400;
  font-family: Montserrat, sans-serif;
}

.user-id-container.copied .id-label {
  color: white;
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
  width: auto;
  padding: 0 8px;
}

.copied-indicator {
  display: flex;
  align-items: center;
  gap: 4px;
  white-space: nowrap;
}

.copied-text {
  font-size: 10px;
  font-weight: 700;
  color: white;
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

/* Responsive Design - Very Small Mobile (до 320px) */
@media (max-width: 320px) {
  .profile-view-overlay {
    padding: 10px;
  }
  
  .profile-popup {
    max-width: 300px;
    max-height: 85vh;
  }
  
  .profile-header {
    padding: 15px;
  }
  
  .close-button {
    width: 36px;
    height: 36px;
    top: 10px;
    right: 10px;
  }
  
  .profile-info {
    gap: 12px;
    margin-top: 20px;
  }
  
  .profile-avatar {
    width: 60px;
    height: 60px;
  }
  
  .profile-name {
    font-size: 16px;
  }
  
  .silver-badge {
    padding: 2px 10px 2px 2px;
    height: 26px;
  }
  
  .badge-text {
    font-size: 11px;
  }
  
  .next-button {
    width: 36px;
    height: 36px;
  }
  
  .menu-container {
    padding: 15px;
    max-height: 220px;
  }
  
  .menu-item {
    padding: 8px;
    gap: 6px;
  }
  
  .menu-icon {
    width: 32px;
    height: 32px;
  }
  
  .menu-text {
    font-size: 13px;
  }
  
  .alert-icon {
    width: 18px;
    height: 18px;
  }
  
  .bottom-section {
    padding: 15px;
  }
  
  .upgrade-section {
    padding: 12px;
    gap: 8px;
    margin-bottom: 12px;
  }
  
  .upgrade-title {
    font-size: 16px;
  }
  
  .upgrade-text {
    font-size: 11px;
  }
  
  .upgrade-button {
    padding: 8px 16px;
    font-size: 13px;
  }
  
  .id-language-section {
    gap: 8px;
    flex-direction: column;
    align-items: stretch;
  }
  
  .user-id-content {
    padding: 6px 10px;
  }
  
  .id-label,
  .id-number {
    font-size: 11px;
  }
  
  .copy-button {
    width: 20px;
    height: 20px;
  }
  
  .language-text {
    font-size: 13px;
  }
}

/* Small Mobile (321px - 374px) */
@media (min-width: 321px) and (max-width: 374px) {
  .profile-view-overlay {
    padding: 15px;
  }
  
  .profile-popup {
    max-width: 320px;
    max-height: 88vh;
  }
  
  .profile-avatar {
    width: 70px;
    height: 70px;
  }
  
  .profile-name {
    font-size: 18px;
  }
  
  .silver-badge {
    height: 28px;
  }
  
  .badge-text {
    font-size: 12px;
  }
  
  .menu-container {
    max-height: 250px;
  }
  
  .menu-icon {
    width: 36px;
    height: 36px;
  }
  
  .menu-text {
    font-size: 14px;
  }
  
  .id-language-section {
    gap: 10px;
  }
  
  .id-label,
  .id-number {
    font-size: 12px;
  }
  
  .language-text {
    font-size: 14px;
  }
}

/* Regular Mobile (375px - 430px) */
@media (min-width: 375px) and (max-width: 430px) {
  .profile-popup {
    max-width: 340px;
  }
  
  .menu-container {
    max-height: 280px;
  }
}

/* Large Mobile and Small Tablets (431px - 768px) */
@media (min-width: 431px) and (max-width: 768px) {
  .profile-view-overlay {
    padding: 25px;
  }
  
  .profile-popup {
    max-width: 380px;
  }
  
  .profile-header {
    padding: 25px;
  }
  
  .profile-avatar {
    width: 90px;
    height: 90px;
  }
  
  .profile-name {
    font-size: 23px;
  }
  
  .silver-badge {
    height: 36px;
  }
  
  .badge-text {
    font-size: 15px;
  }
  
  .menu-container {
    max-height: 320px;
    padding: 25px;
  }
  
  .menu-icon {
    width: 44px;
    height: 44px;
  }
  
  .menu-text {
    font-size: 17px;
  }
  
  .upgrade-title {
    font-size: 21px;
  }
  
  .upgrade-text {
    font-size: 15px;
  }
  
  .upgrade-button {
    padding: 14px 28px;
    font-size: 17px;
  }
  
  .id-label,
  .id-number {
    font-size: 15px;
  }
  
  .language-text {
    font-size: 17px;
  }
}

/* Tablets and Desktop (769px+) */
@media (min-width: 769px) {
  .profile-view-overlay {
    padding: 30px;
  }
  
  .profile-popup {
    max-width: 400px;
  }
  
  .profile-header {
    padding: 30px;
  }
  
  .profile-avatar {
    width: 100px;
    height: 100px;
  }
  
  .profile-name {
    font-size: 25px;
  }
  
  .menu-container {
    max-height: 350px;
    padding: 30px;
  }
  
  .menu-icon {
    width: 48px;
    height: 48px;
  }
  
  .menu-text {
    font-size: 18px;
  }
  
  .bottom-section {
    padding: 25px;
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

/* Landscape orientation adjustments */
@media (max-height: 600px) and (orientation: landscape) {
  .profile-popup {
    max-height: 95vh;
  }
  
  .menu-container {
    max-height: 200px;
  }
  
  .profile-header {
    padding: 15px;
  }
  
  .profile-info {
    margin-top: 15px;
  }
  
  .bottom-section {
    padding: 15px;
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
  .dropdown-arrow,
  .user-id-container {
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
