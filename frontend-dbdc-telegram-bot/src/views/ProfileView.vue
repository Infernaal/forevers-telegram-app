<template>
  <div class="profile-view w-full max-w-md mx-auto bg-gray-100 min-h-screen flex flex-col font-montserrat">
    <!-- Content Container -->
    <div class="content-container bg-gray-100 flex-1 flex flex-col relative">
      
      <!-- Profile Header Section -->
      <div class="profile-header-section">
        <div class="profile-header-card">
          <div class="profile-header-content">
            <!-- Large Avatar -->
            <div class="avatar-container">
              <div class="avatar-frame">
                <img 
                  :src="profileData.avatar" 
                  :alt="profileData.name"
                  class="avatar-image"
                />
              </div>
              <!-- Silver Badge -->
              <div class="profile-badge">
                <svg class="profile-star" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M14.0004 26.2497C7.24592 26.2497 1.75073 20.7545 1.75073 14.0001C1.75073 7.24564 7.24592 1.75085 14.0004 1.75085C20.7548 1.75085 26.25 7.24564 26.25 14.0001C26.25 20.7545 20.7544 26.2497 14.0004 26.2497Z" fill="white"/>
                  <path d="M20.2071 5.37145C20.73 5.37145 21.2468 5.39833 21.7567 5.4472C19.7049 3.58479 16.9828 2.44812 14 2.44812C7.63041 2.44812 2.448 7.63013 2.448 14.0001C2.448 16.2735 3.11102 18.3941 4.24973 20.1832C4.86143 11.9015 11.769 5.37145 20.2071 5.37145Z" fill="#E0E0E0"/>
                  <path d="M14.0006 25.5519C20.3702 25.5519 25.5526 20.3699 25.5526 13.9999C25.5526 10.6131 24.0873 7.56229 21.7577 5.44697C21.2478 5.39809 20.731 5.37122 20.2081 5.37122C11.7704 5.37122 4.86244 11.9017 4.25073 20.1829C6.30211 23.4072 9.90475 25.5519 14.0006 25.5519Z" fill="#B5B5B5"/>
                  <path d="M14.0004 23.1368C19.0464 23.1368 23.1369 19.0463 23.1369 14.0003C23.1369 8.95433 19.0464 4.86377 14.0004 4.86377C8.95445 4.86377 4.86389 8.95433 4.86389 14.0003C4.86389 19.0463 8.95445 23.1368 14.0004 23.1368Z" fill="#9E9E9E"/>
                  <path d="M19.4965 12.7667L15.6984 12.2148L14.0001 8.77307L12.3014 12.2148L8.50366 12.7667L11.2519 15.4452L10.6031 19.2279L14.0001 17.4421L17.397 19.2279L16.7483 15.4452L19.4965 12.7667Z" fill="#F6F6F6"/>
                </svg>
              </div>
            </div>
            
            <!-- User Info -->
            <div class="user-info">
              <!-- Silver Badge Label -->
              <div class="user-badge">
                <span class="badge-text">Silver</span>
              </div>
              <h1 class="user-name">{{ profileData.name }}</h1>
              <div class="user-id">
                <span class="id-label">ID:</span>
                <span class="id-value">{{ profileData.id }}</span>
                <button @click="copyUserId" class="copy-btn">
                  <svg width="14" height="14" viewBox="0 0 14 16" fill="none">
                    <path d="M10.1875 0H4.3125C3.86929 0 3.44433 0.1939 3.13388 0.539053C2.82343 0.884206 2.65625 1.35544 2.65625 1.84615V2.46154H2.09375C1.5378 2.46154 1.00476 2.68561 0.608253 3.08005C0.211748 3.47448 0 4.00354 0 4.55385V13.5385C0 14.0888 0.211748 14.6178 0.608253 15.0123C1.00476 15.4067 1.5378 15.6308 2.09375 15.6308H8.5C9.0560 15.6308 9.589 15.4067 9.98551 15.0123C10.382 14.6178 10.5938 14.0888 10.5938 13.5385V12.9231H10.1875C10.6205 12.9231 11.0356 12.7359 11.3414 12.3974C11.6472 12.0589 11.8125 11.5967 11.8125 11.1154V1.84615C11.8125 1.35544 11.6453 0.884206 11.3349 0.539053C11.0244 0.1939 10.5995 0 10.1875 0Z" fill="currentColor"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Menu Section -->
      <div class="menu-section">
        <div class="menu-items">
          <!-- Calculator -->
          <div @click="handleMenuClick('calculator')" class="menu-item">
            <div class="menu-icon">
              <svg width="16" height="20" viewBox="0 0 16 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M14.1377 0C15.1645 0 16 0.788555 16 1.75781V18.2422C16 19.2114 15.1645 20 14.1377 20H1.8623C0.835502 20 0 19.2114 0 18.2422V1.75781C0 0.788555 0.835502 0 1.8623 0H14.1377Z" fill="#4B4D50"/>
              </svg>
            </div>
            <span class="menu-text">Calculator</span>
          </div>

          <!-- Ambassador -->
          <div @click="handleMenuClick('ambassador')" class="menu-item">
            <div class="menu-icon">
              <svg width="14" height="20" viewBox="0 0 14 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M7 9.64844C9.76508 9.64858 12.0066 11.9652 12.0068 14.8242C12.0068 17.6826 9.76511 19.9999 7 20C4.23394 20 1.99219 17.6827 1.99219 14.8242C1.99243 11.9651 4.23409 9.64844 7 9.64844Z" fill="#4B4D50"/>
              </svg>
            </div>
            <span class="menu-text">Ambassador</span>
          </div>

          <!-- Verification with Badge -->
          <div @click="handleMenuClick('verification')" class="menu-item">
            <div class="menu-icon">
              <svg width="18" height="22" viewBox="0 0 18 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M14.2511 12.4974C15.4932 12.4974 16.5 13.5045 16.5 14.7467V15.3222C16.5 16.2166 16.1805 17.0816 15.5989 17.7611C14.0295 19.5949 11.6422 20.5 8.49673 20.5C5.35076 20.5 2.96466 19.5946 1.39831 17.7601C0.818531 17.081 0.5 16.2174 0.5 15.3245V14.7467C0.5 13.5045 1.50689 12.4974 2.74896 12.4974H14.2511Z" fill="#4B4D50"/>
              </svg>
            </div>
            <span class="menu-text">Verification</span>
            <!-- Red X Badge -->
            <div class="verification-badge">
              <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M8.5 3.5L3.5 8.5M3.5 3.5L8.5 8.5" stroke="#FF1919" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </div>

          <!-- Security -->
          <div @click="handleMenuClick('security')" class="menu-item">
            <div class="menu-icon">
              <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M8.78516 0.0354746C8.92389 -0.0121504 9.07611 -0.0121504 9.21484 0.0354746C10.6561 0.531013 12.1438 0.945188 13.6377 1.26497C14.8838 1.5317 16.1601 1.73823 17.4297 1.87922C17.7546 1.91522 18 2.18263 18 2.50032V8.7386C17.9998 13.165 15.3282 17.2234 11.1943 19.0784L9.26953 19.9427C9.18416 19.9808 9.09193 20.0003 9 20.0003C8.90802 20.0003 8.81583 19.9808 8.73047 19.9427L6.80566 19.0784C2.67178 17.2233 0.000192532 13.165 0 8.7386V2.50032C0 2.18263 0.245411 1.91529 0.570312 1.87922C1.83994 1.73823 3.11627 1.53164 4.3623 1.26497C5.85626 0.945192 7.34396 0.531005 8.78516 0.0354746Z" fill="#4B4D50"/>
              </svg>
            </div>
            <span class="menu-text">Security</span>
          </div>

          <!-- Settings -->
          <div @click="handleMenuClick('settings')" class="menu-item">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.2222 20L12.3457 19.375L12.8148 17.0913C13.5679 16.8029 14.2469 16.3972 14.8642 15.9135L17.1605 16.6827L17.7778 16.875L18.0988 16.3221L19.679 13.6778L20 13.125L19.5309 12.7163L17.7531 11.2019C17.8179 10.8083 17.9012 10.4147 17.9012 10C17.9012 9.58531 17.8179 9.19169 17.7531 8.79808L19.5309 7.28369L20 6.875L19.679 6.32215L18.0988 3.67785L17.7778 3.125L17.1605 3.31731L14.8642 4.08654C14.2469 3.60277 13.5679 3.19708 12.8148 2.90862L12.3457 0.625L12.2222 0H7.77775L7.65426 0.625L7.18516 2.90862C6.43209 3.19708 5.75306 3.60277 5.13581 4.08654L2.83947 3.31731L2.22215 3.125L1.9012 3.67785L0.32095 6.32215L0 6.875L0.469097 7.28369L2.24688 8.79808C2.18209 9.19169 2.09873 9.58531 2.09873 10C2.09873 10.4147 2.18209 10.8083 2.24688 11.2019L0.469097 12.7163L0 13.125L0.32095 13.6778L1.9012 16.3221L2.22215 16.875L2.83947 16.6827L5.13581 15.9135C5.75306 16.3972 6.43209 16.8029 7.18516 17.0913L7.65426 19.375L7.77775 20H12.2222Z" fill="#4B4D50"/>
              </svg>
            </div>
            <span class="menu-text">Settings</span>
          </div>

          <!-- Support -->
          <div @click="handleMenuClick('support')" class="menu-item">
            <div class="menu-icon">
              <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M8.99902 0C13.9325 0 17.998 3.80872 17.998 8.58691V10.1348C17.9981 10.1411 17.999 10.1479 17.999 10.1543V12.9561C17.9992 12.9624 18 12.9692 18 12.9756V14.543C17.9997 16.724 16.1499 18.4277 13.9502 18.4277H11.2695C10.9422 19.3551 10.0281 19.9951 8.99902 19.9951C7.71066 19.9949 6.59988 18.993 6.59961 17.6777C6.59962 16.3623 7.71051 15.3606 8.99902 15.3604C10.0286 15.3604 10.9435 15.9998 11.2705 16.9277H13.9502C15.1589 16.9277 16.1261 16.1539 16.4111 15.1514C16.155 15.2407 15.8817 15.293 15.5986 15.293C14.3103 15.2927 13.1995 14.2908 13.1992 12.9756V10.1543C13.1992 8.83884 14.3101 7.83714 15.5986 7.83691C15.9032 7.83691 16.1972 7.89422 16.4697 7.99707C16.1535 4.38853 12.9637 1.5 8.99902 1.5C5.03445 1.50011 1.84359 4.38856 1.52734 7.99707C1.80001 7.89396 2.09449 7.83697 2.39941 7.83691C3.6881 7.83691 4.7998 8.83869 4.7998 10.1543V12.9756C4.79953 14.291 3.68794 15.293 2.39941 15.293C1.11107 15.2927 0.000274862 14.2908 0 12.9756V8.58691C4.31105e-05 3.80879 4.0657 0.000121624 8.99902 0Z" fill="#4B4D50"/>
              </svg>
            </div>
            <span class="menu-text">Support</span>
          </div>

          <!-- Help -->
          <div @click="handleMenuClick('help')" class="menu-item">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M10 0C4.47328 0 0 4.47254 0 10V19.2188C0 19.6502 0.349766 20 0.78125 20H10C15.5267 20 20 15.5275 20 10C20 4.47328 15.5275 0 10 0ZM10 18.4375H1.5625V10C1.5625 5.33684 5.33621 1.5625 10 1.5625C14.6632 1.5625 18.4375 5.33621 18.4375 10C18.4375 14.6632 14.6638 18.4375 10 18.4375Z" fill="#4B4D50"/>
              </svg>
            </div>
            <span class="menu-text">Help</span>
          </div>
        </div>
      </div>

      <!-- Upgrade Section -->
      <div class="upgrade-section">
        <div class="upgrade-card">
          <!-- Star Icon -->
          <div class="upgrade-star">
            <svg class="star-icon" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="16" cy="16" r="15.06" fill="#8C4CD1"/>
              <path d="M28.998 8.39055C26.1133 12.4471 21.365 15.0918 16.0003 15.0918C10.6356 15.0918 5.88739 12.4471 3.00269 8.39055C5.61916 3.9341 10.4615 0.941162 16.0003 0.941162C21.5392 0.941162 26.3815 3.9341 28.998 8.39055Z" fill="#9C68E1"/>
              <path d="M15.9997 5.11792V15.4117L19.3443 11.8949L15.9997 5.11792Z" fill="#FF9F00"/>
            </svg>
          </div>

          <div class="upgrade-content">
            <div class="upgrade-info">
              <div class="upgrade-title">Start</div>
              <div class="upgrade-subtitle">
                buy <span class="upgrade-number">123</span> more Forevers to upgrade
              </div>
            </div>
            <button @click="handleUpgrade" class="upgrade-button">
              Upgrade
            </button>
          </div>
        </div>
      </div>

      <!-- Language Section -->
      <div class="language-section">
        <div class="language-card">
          <div class="language-header">
            <div class="language-icon-wrapper">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M10 0C4.477 0 0 4.477 0 10s4.477 10 10 10 10-4.477 10-10S15.523 0 10 0zM8.5 16.5c-.828 0-1.5-.672-1.5-1.5s.672-1.5 1.5-1.5 1.5.672 1.5 1.5-.672 1.5-1.5 1.5zM13 9H7c-.552 0-1-.448-1-1s.448-1 1-1h6c.552 0 1 .448 1 1s-.448 1-1 1z" fill="#4B4D50"/>
              </svg>
            </div>
            <span class="language-title">Language</span>
          </div>
          
          <!-- Language Selector -->
          <button @click="toggleLanguageSelector" class="language-selector">
            <div class="flag-wrapper">
              <CountryFlag :country="selectedLanguage.code" size="small" />
            </div>
            <span class="language-text">{{ selectedLanguage.name }}</span>
            <div class="arrow-wrapper">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none" class="arrow-icon" :class="{ 'rotate-180': isLanguageDropdownOpen }">
                <path d="M4 6L8 10L12 6" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </button>

          <!-- Language Dropdown -->
          <Transition
            name="dropdown"
            enter-active-class="transition-all duration-300 ease-out"
            leave-active-class="transition-all duration-200 ease-in"
            enter-from-class="opacity-0 scale-95 translate-y-2"
            enter-to-class="opacity-100 scale-100 translate-y-0"
            leave-from-class="opacity-100 scale-100 translate-y-0"
            leave-to-class="opacity-0 scale-95 translate-y-2"
          >
            <div v-if="isLanguageDropdownOpen" class="language-dropdown">
              <div class="dropdown-content">
                <button
                  v-for="language in availableLanguages"
                  :key="language.code"
                  @click="selectLanguage(language)"
                  class="dropdown-item"
                  :class="{
                    'dropdown-item-active': selectedLanguage.code === language.code,
                    'dropdown-item-inactive': selectedLanguage.code !== language.code
                  }"
                >
                  <div class="dropdown-flag">
                    <CountryFlag :country="language.code" size="small" />
                  </div>
                  <span class="dropdown-text">{{ language.name }}</span>
                  <div v-if="selectedLanguage.code === language.code" class="dropdown-indicator"></div>
                </button>
              </div>
            </div>
          </Transition>
        </div>
      </div>

    </div>

    <!-- Copy Success Toast -->
    <Transition
      name="copy-toast"
      enter-active-class="transition-all duration-400 ease-out"
      leave-active-class="transition-all duration-300 ease-in"
      enter-from-class="opacity-0 scale-90"
      enter-to-class="opacity-100 scale-100"
      leave-from-class="opacity-100 scale-100"
      leave-to-class="opacity-0 scale-90"
    >
      <div v-if="showCopyMessage" class="copy-toast">
        <div class="toast-icon">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
            <polyline points="20,6 9,17 4,12" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <span class="toast-text">Copied</span>
      </div>
    </Transition>

    <!-- Bottom Navigation Component -->
    <BottomNavigation />
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import BottomNavigation from '../components/BottomNavigation.vue'
import CountryFlag from '../components/CountryFlag.vue'

const router = useRouter()

// Profile data
const profileData = ref({
  name: 'Jason Williams',
  id: '515745',
  avatar: 'https://images.pexels.com/photos/15023413/pexels-photo-15023413.jpeg?auto=compress&cs=tinysrgb&w=400'
})

// Language selector state
const isLanguageDropdownOpen = ref(false)
const selectedLanguage = ref({ code: 'us', name: 'ENG' })
const showCopyMessage = ref(false)

// Available languages
const availableLanguages = ref([
  { code: 'us', name: 'ENG' },
  { code: 'ru', name: 'RUS' },
  { code: 'de', name: 'DEU' },
  { code: 'fr', name: 'FRA' },
  { code: 'es', name: 'ESP' },
  { code: 'it', name: 'ITA' },
  { code: 'pl', name: 'POL' },
  { code: 'ua', name: 'UKR' },
  { code: 'kz', name: 'KAZ' },
  { code: 'uae', name: 'UAE' }
])

// Close dropdown when clicking outside
const handleClickOutside = (event) => {
  if (!event.target.closest('.language-card')) {
    isLanguageDropdownOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})

// Methods
const handleMenuClick = (section) => {
  console.log(`Navigate to ${section}`)
  // TODO: Add navigation logic
}

const handleUpgrade = () => {
  console.log('Upgrade clicked')
  // TODO: Add upgrade logic  
}

const copyUserId = async () => {
  const showSuccessMessage = () => {
    showCopyMessage.value = true
    setTimeout(() => {
      showCopyMessage.value = false
    }, 2000)
  }

  // Check if modern clipboard API is available and allowed
  if (navigator.clipboard && window.isSecureContext) {
    try {
      await navigator.clipboard.writeText(profileData.value.id)
      showSuccessMessage()
      return
    } catch (err) {
      console.log('Clipboard API failed, using fallback:', err.message)
    }
  }

  // Fallback method for older browsers or when clipboard API is blocked
  try {
    const textArea = document.createElement('textarea')
    textArea.value = profileData.value.id
    textArea.style.position = 'fixed'
    textArea.style.left = '-999999px'
    textArea.style.top = '-999999px'
    document.body.appendChild(textArea)
    textArea.focus()
    textArea.select()
    const successful = document.execCommand('copy')
    document.body.removeChild(textArea)

    if (successful) {
      showSuccessMessage()
    } else {
      console.error('Fallback copy method failed')
    }
  } catch (err) {
    console.error('All copy methods failed:', err)
  }
}

const toggleLanguageSelector = () => {
  isLanguageDropdownOpen.value = !isLanguageDropdownOpen.value
}

const selectLanguage = (language) => {
  selectedLanguage.value = language
  isLanguageDropdownOpen.value = false
  console.log(`Language selected: ${language.name}`)
}
</script>

<style scoped>
.profile-view {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  min-height: 100vh;
  min-height: 100dvh; /* Dynamic viewport height */
  background: #f3f4f6;
  overflow-x: hidden;
  overscroll-behavior: none;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.content-container {
  background: #f3f4f6;
  padding: 16px 16px 100px 16px; /* Bottom padding for navigation */
  box-sizing: border-box;
  min-height: calc(100vh - 100px);
}

/* Profile Header Section */
.profile-header-section {
  margin-bottom: 20px;
}

.profile-header-card {
  background: linear-gradient(135deg, #2019CE 0%, #473FFF 100%);
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 8px 24px rgba(32, 25, 206, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.profile-header-content {
  display: flex;
  align-items: center;
  gap: 16px;
}

.avatar-container {
  position: relative;
  flex-shrink: 0;
}

.avatar-frame {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 2px solid rgba(255, 255, 255, 0.3);
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.avatar-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-badge {
  position: absolute;
  bottom: -4px;
  right: -4px;
  background: #f3f4f6;
  border-radius: 50%;
  padding: 4px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.profile-star {
  width: 28px;
  height: 28px;
}

.user-info {
  flex: 1;
  min-width: 0;
}

.user-badge {
  margin-bottom: 8px;
}

.badge-text {
  display: inline-block;
  background: rgba(255, 255, 255, 0.2);
  color: white;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.user-name {
  color: white;
  font-size: 20px;
  font-weight: 700;
  margin: 0 0 8px 0;
  line-height: 1.2;
}

.user-id {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 6px 10px;
  width: fit-content;
}

.id-label {
  color: rgba(255, 255, 255, 0.8);
  font-size: 12px;
  font-weight: 500;
}

.id-value {
  color: white;
  font-size: 12px;
  font-weight: 600;
}

.copy-btn {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  border-radius: 6px;
  padding: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
}

.copy-btn:hover {
  background: rgba(255, 255, 255, 0.3);
}

/* Menu Section */
.menu-section {
  margin-bottom: 20px;
}

.menu-items {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: white;
  border-radius: 16px;
  border: 1px solid rgba(75, 77, 80, 0.1);
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.menu-item:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  border-color: rgba(32, 25, 206, 0.2);
}

.menu-icon {
  width: 40px;
  height: 40px;
  background: #f3f4f6;
  border: 1px solid rgba(75, 77, 80, 0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.menu-text {
  color: #02070E;
  font-weight: 600;
  font-size: 16px;
  flex: 1;
}

.verification-badge {
  width: 24px;
  height: 24px;
  background: #FFF0F3;
  border: 1px solid #FF1919;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

/* Upgrade Section */
.upgrade-section {
  margin-bottom: 20px;
}

.upgrade-card {
  background: #F1E7FF;
  border: 1px solid #DCCCF1;
  border-radius: 16px;
  padding: 16px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(140, 76, 209, 0.1);
}

.upgrade-star {
  position: absolute;
  left: 16px;
  top: 16px;
}

.star-icon {
  width: 32px;
  height: 32px;
}

.upgrade-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-left: 48px;
}

.upgrade-title {
  color: #02070E;
  font-weight: 700;
  font-size: 18px;
  margin-bottom: 4px;
}

.upgrade-subtitle {
  font-size: 13px;
  color: #4B4D50;
  line-height: 1.3;
}

.upgrade-number {
  font-weight: 700;
  color: #8C4CD1;
}

.upgrade-button {
  padding: 10px 20px;
  background: linear-gradient(90deg, #2019CE 0%, #473FFF 100%);
  color: white;
  font-weight: 600;
  border-radius: 20px;
  font-size: 14px;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(32, 25, 206, 0.25);
  flex-shrink: 0;
}

.upgrade-button:hover {
  box-shadow: 0 6px 16px rgba(32, 25, 206, 0.35);
  transform: translateY(-1px);
}

/* Language Section */
.language-section {
  margin-bottom: 24px;
}

.language-card {
  background: white;
  border-radius: 16px;
  border: 1px solid rgba(75, 77, 80, 0.1);
  padding: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  position: relative;
}

.language-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.language-icon-wrapper {
  width: 40px;
  height: 40px;
  background: #f3f4f6;
  border: 1px solid rgba(75, 77, 80, 0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.language-title {
  color: #02070E;
  font-weight: 600;
  font-size: 16px;
}

.language-selector {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: #f9fafb;
  border: 1px solid rgba(75, 77, 80, 0.15);
  border-radius: 12px;
  transition: all 0.2s ease;
  width: 100%;
  cursor: pointer;
}

.language-selector:hover {
  background: #f3f4f6;
  border-color: rgba(32, 25, 206, 0.3);
}

.flag-wrapper {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  border: 1px solid rgba(75, 77, 80, 0.1);
}

.language-text {
  color: #02070E;
  font-size: 14px;
  font-weight: 500;
  flex: 1;
  text-align: left;
}

.arrow-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.arrow-icon {
  transition: transform 0.3s ease;
}

/* Language Dropdown */
.language-dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  margin-top: 8px;
  background: white;
  border: 1px solid rgba(75, 77, 80, 0.15);
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  overflow: hidden;
  z-index: 50;
  max-height: 200px;
}

.dropdown-content {
  padding: 8px;
  max-height: 184px;
  overflow-y: auto;
  overflow-x: hidden;
}

.dropdown-item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  border-radius: 8px;
  transition: all 0.2s ease;
  text-align: left;
  border: none;
  background: none;
  cursor: pointer;
}

.dropdown-item-active {
  background: rgba(32, 25, 206, 0.1);
  color: #2019CE;
}

.dropdown-item-inactive {
  color: #374151;
}

.dropdown-item-inactive:hover {
  background: rgba(32, 25, 206, 0.05);
}

.dropdown-flag {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  border: 1px solid rgba(75, 77, 80, 0.1);
}

.dropdown-text {
  font-size: 14px;
  font-weight: 500;
}

.dropdown-indicator {
  margin-left: auto;
  width: 8px;
  height: 8px;
  background: #2019CE;
  border-radius: 50%;
}

/* Copy Toast */
.copy-toast {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border-radius: 16px;
  padding: 16px 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  z-index: 100;
  box-shadow: 0 8px 20px rgba(16, 185, 129, 0.4);
}

.toast-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  flex-shrink: 0;
}

.toast-text {
  color: white;
  font-weight: 600;
  font-size: 16px;
}

/* Very small mobile devices (до 320px) */
@media (max-width: 320px) {
  .profile-view {
    max-width: 100%;
  }
  
  .content-container {
    padding: 8px 8px 80px 8px;
  }
  
  .profile-header-section {
    margin-bottom: 12px;
  }
  
  .profile-header-card {
    border-radius: 12px;
    padding: 12px;
  }
  
  .profile-header-content {
    gap: 10px;
  }
  
  .avatar-frame {
    width: 60px;
    height: 60px;
  }
  
  .profile-badge {
    bottom: -2px;
    right: -2px;
    padding: 2px;
  }
  
  .profile-star {
    width: 20px;
    height: 20px;
  }
  
  .badge-text {
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 8px;
  }
  
  .user-name {
    font-size: 16px;
    margin-bottom: 6px;
  }
  
  .user-id {
    padding: 4px 8px;
    border-radius: 8px;
  }
  
  .id-label, .id-value {
    font-size: 10px;
  }
  
  .copy-btn {
    padding: 2px;
    border-radius: 4px;
  }
  
  .copy-btn svg {
    width: 10px;
    height: 10px;
  }
  
  .menu-section {
    margin-bottom: 12px;
  }
  
  .menu-items {
    gap: 6px;
  }
  
  .menu-item {
    padding: 10px 12px;
    border-radius: 12px;
    gap: 10px;
  }
  
  .menu-icon {
    width: 32px;
    height: 32px;
    border-radius: 8px;
  }
  
  .menu-icon svg {
    width: 14px;
    height: 14px;
  }
  
  .menu-text {
    font-size: 13px;
  }
  
  .verification-badge {
    width: 20px;
    height: 20px;
  }
  
  .verification-badge svg {
    width: 10px;
    height: 10px;
  }
  
  .upgrade-section {
    margin-bottom: 12px;
  }
  
  .upgrade-card {
    padding: 12px;
    border-radius: 12px;
  }
  
  .upgrade-star {
    left: 12px;
    top: 12px;
  }
  
  .star-icon {
    width: 24px;
    height: 24px;
  }
  
  .upgrade-content {
    margin-left: 36px;
  }
  
  .upgrade-title {
    font-size: 14px;
    margin-bottom: 2px;
  }
  
  .upgrade-subtitle {
    font-size: 11px;
  }
  
  .upgrade-button {
    padding: 6px 12px;
    font-size: 11px;
    border-radius: 14px;
  }
  
  .language-section {
    margin-bottom: 16px;
  }
  
  .language-card {
    padding: 12px;
    border-radius: 12px;
  }
  
  .language-header {
    gap: 10px;
    margin-bottom: 12px;
  }
  
  .language-icon-wrapper {
    width: 32px;
    height: 32px;
    border-radius: 8px;
  }
  
  .language-icon-wrapper svg {
    width: 16px;
    height: 16px;
  }
  
  .language-title {
    font-size: 13px;
  }
  
  .language-selector {
    padding: 8px 12px;
    gap: 8px;
    border-radius: 8px;
  }
  
  .flag-wrapper {
    width: 20px;
    height: 20px;
  }
  
  .language-text {
    font-size: 12px;
  }
  
  .arrow-wrapper {
    width: 16px;
    height: 16px;
  }
  
  .arrow-wrapper svg {
    width: 12px;
    height: 12px;
  }
  
  .dropdown-item {
    padding: 8px 10px;
    gap: 8px;
  }
  
  .dropdown-flag {
    width: 16px;
    height: 16px;
  }
  
  .dropdown-text {
    font-size: 12px;
  }
  
  .dropdown-indicator {
    width: 6px;
    height: 6px;
  }
  
  .copy-toast {
    padding: 12px 16px;
    gap: 8px;
    border-radius: 12px;
  }
  
  .toast-icon {
    width: 16px;
    height: 16px;
  }
  
  .toast-icon svg {
    width: 12px;
    height: 12px;
  }
  
  .toast-text {
    font-size: 14px;
  }
}

/* Small mobile devices (321px - 374px) */
@media (min-width: 321px) and (max-width: 374px) {
  .profile-view {
    max-width: 100%;
  }
  
  .content-container {
    padding: 10px 10px 85px 10px;
  }
  
  .profile-header-section {
    margin-bottom: 14px;
  }
  
  .profile-header-card {
    border-radius: 14px;
    padding: 14px;
  }
  
  .profile-header-content {
    gap: 12px;
  }
  
  .avatar-frame {
    width: 70px;
    height: 70px;
  }
  
  .profile-star {
    width: 24px;
    height: 24px;
  }
  
  .user-name {
    font-size: 18px;
  }
  
  .menu-items {
    gap: 7px;
  }
  
  .menu-item {
    padding: 11px 14px;
    border-radius: 14px;
  }
  
  .menu-icon {
    width: 36px;
    height: 36px;
    border-radius: 10px;
  }
  
  .menu-text {
    font-size: 14px;
  }
  
  .upgrade-card {
    padding: 14px;
    border-radius: 14px;
  }
  
  .star-icon {
    width: 28px;
    height: 28px;
  }
  
  .upgrade-content {
    margin-left: 42px;
  }
  
  .upgrade-title {
    font-size: 16px;
  }
  
  .upgrade-subtitle {
    font-size: 12px;
  }
  
  .language-card {
    padding: 14px;
    border-radius: 14px;
  }
  
  .language-icon-wrapper {
    width: 36px;
    height: 36px;
    border-radius: 10px;
  }
  
  .language-title {
    font-size: 14px;
  }
  
  .language-selector {
    padding: 10px 14px;
    border-radius: 10px;
  }
  
  .language-text {
    font-size: 13px;
  }
}

/* Large mobile and small tablets (431px - 768px) */
@media (min-width: 431px) and (max-width: 768px) {
  .profile-view {
    max-width: 480px;
    margin: 0 auto;
  }
  
  .content-container {
    padding: 18px 18px 100px 18px;
  }
  
  .profile-header-card {
    border-radius: 22px;
    padding: 24px;
  }
  
  .profile-header-content {
    gap: 20px;
  }
  
  .avatar-frame {
    width: 90px;
    height: 90px;
  }
  
  .profile-star {
    width: 32px;
    height: 32px;
  }
  
  .user-name {
    font-size: 22px;
  }
  
  .menu-item {
    padding: 16px 20px;
    border-radius: 18px;
    gap: 16px;
  }
  
  .menu-icon {
    width: 44px;
    height: 44px;
    border-radius: 14px;
  }
  
  .menu-text {
    font-size: 17px;
  }
  
  .upgrade-card {
    padding: 20px;
    border-radius: 18px;
  }
  
  .star-icon {
    width: 36px;
    height: 36px;
  }
  
  .upgrade-content {
    margin-left: 56px;
  }
  
  .upgrade-title {
    font-size: 20px;
  }
  
  .upgrade-subtitle {
    font-size: 14px;
  }
  
  .upgrade-button {
    padding: 12px 24px;
    font-size: 15px;
    border-radius: 22px;
  }
  
  .language-card {
    padding: 20px;
    border-radius: 18px;
  }
  
  .language-icon-wrapper {
    width: 44px;
    height: 44px;
    border-radius: 14px;
  }
  
  .language-title {
    font-size: 17px;
  }
  
  .language-selector {
    padding: 14px 18px;
    border-radius: 14px;
  }
  
  .flag-wrapper {
    width: 28px;
    height: 28px;
  }
  
  .language-text {
    font-size: 15px;
  }
}

/* Tablets and desktop (769px+) */
@media (min-width: 769px) {
  .profile-view {
    max-width: 480px;
    margin: 20px auto;
    border-radius: 20px;
    box-shadow: 0 0 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
  }
  
  .content-container {
    padding: 24px 24px 110px 24px;
  }
  
  .profile-header-card {
    border-radius: 24px;
    padding: 28px;
  }
  
  .avatar-frame {
    width: 100px;
    height: 100px;
  }
  
  .profile-star {
    width: 36px;
    height: 36px;
  }
  
  .user-name {
    font-size: 24px;
  }
  
  .menu-item {
    padding: 18px 22px;
    border-radius: 20px;
    gap: 18px;
  }
  
  .menu-icon {
    width: 48px;
    height: 48px;
    border-radius: 16px;
  }
  
  .menu-text {
    font-size: 18px;
  }
  
  .upgrade-card {
    padding: 24px;
    border-radius: 20px;
  }
  
  .star-icon {
    width: 40px;
    height: 40px;
  }
  
  .upgrade-title {
    font-size: 22px;
  }
  
  .upgrade-subtitle {
    font-size: 15px;
  }
  
  .language-card {
    padding: 24px;
    border-radius: 20px;
  }
  
  .language-title {
    font-size: 18px;
  }
  
  .language-selector {
    padding: 16px 20px;
    border-radius: 16px;
  }
  
  .language-text {
    font-size: 16px;
  }
}

/* Landscape orientation adjustments for phones */
@media (max-height: 500px) and (orientation: landscape) {
  .content-container {
    padding: 8px 16px 70px 16px;
  }
  
  .profile-header-section {
    margin-bottom: 8px;
  }
  
  .profile-header-card {
    padding: 12px;
    border-radius: 12px;
  }
  
  .profile-header-content {
    gap: 8px;
  }
  
  .avatar-frame {
    width: 50px;
    height: 50px;
  }
  
  .profile-star {
    width: 18px;
    height: 18px;
  }
  
  .user-name {
    font-size: 14px;
    margin-bottom: 4px;
  }
  
  .menu-section {
    margin-bottom: 8px;
  }
  
  .menu-items {
    gap: 4px;
  }
  
  .menu-item {
    padding: 6px 10px;
    border-radius: 10px;
    gap: 8px;
  }
  
  .menu-icon {
    width: 28px;
    height: 28px;
    border-radius: 6px;
  }
  
  .menu-text {
    font-size: 12px;
  }
  
  .upgrade-card {
    padding: 10px;
    border-radius: 10px;
  }
  
  .star-icon {
    width: 22px;
    height: 22px;
  }
  
  .upgrade-title {
    font-size: 14px;
  }
  
  .upgrade-subtitle {
    font-size: 10px;
  }
  
  .upgrade-button {
    padding: 6px 12px;
    font-size: 11px;
    border-radius: 12px;
  }
  
  .language-card {
    padding: 10px;
    border-radius: 10px;
  }
  
  .language-selector {
    padding: 6px 10px;
    border-radius: 8px;
  }
  
  .language-text {
    font-size: 11px;
  }
}

/* High DPI displays */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .profile-star,
  .menu-icon svg,
  .copy-btn svg {
    image-rendering: -webkit-optimize-contrast;
    image-rendering: crisp-edges;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .profile-view {
    background: #1a1a1a;
  }
  
  .content-container {
    background: #1a1a1a;
  }
  
  .menu-item {
    background: #2a2a2a;
    border-color: rgba(255, 255, 255, 0.1);
  }
  
  .menu-text {
    color: #ffffff;
  }
  
  .menu-icon {
    background: #3a3a3a;
    border-color: rgba(255, 255, 255, 0.1);
  }
  
  .upgrade-card {
    background: #2a2a2a;
    border-color: rgba(255, 255, 255, 0.1);
  }
  
  .language-card {
    background: #2a2a2a;
    border-color: rgba(255, 255, 255, 0.1);
  }
  
  .language-title {
    color: #ffffff;
  }
  
  .language-selector {
    background: #3a3a3a;
    border-color: rgba(255, 255, 255, 0.1);
  }
  
  .language-text {
    color: #ffffff;
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  .menu-item,
  .upgrade-button,
  .language-selector,
  .copy-btn {
    transition: none;
  }
  
  .menu-item:hover,
  .upgrade-button:hover {
    transform: none;
  }
  
  .arrow-icon {
    transition: none;
  }
}

/* Touch optimizations */
@media (hover: none) and (pointer: coarse) {
  .menu-item:hover {
    transform: none;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  }
  
  .menu-item:active {
    transform: scale(0.98);
    background: #f3f4f6;
  }
  
  .upgrade-button:hover {
    transform: none;
  }
  
  .upgrade-button:active {
    transform: scale(0.96);
  }
  
  .language-selector:active {
    transform: scale(0.98);
    background: #f0f0f0;
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
.profile-header-card,
.menu-item,
.upgrade-card,
.language-card,
.upgrade-button,
.copy-btn {
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Telegram WebApp specific optimizations */
* {
  -webkit-tap-highlight-color: transparent;
}
</style>
