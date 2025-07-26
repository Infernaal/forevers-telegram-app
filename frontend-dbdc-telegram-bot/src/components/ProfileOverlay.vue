<template>
  <!-- Profile Overlay with Modern Responsive Design -->
  <Transition
    name="profile-overlay"
    enter-active-class="transition-all duration-400 ease-out"
    leave-active-class="transition-all duration-300 ease-in"
    enter-from-class="opacity-0"
    enter-to-class="opacity-100"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
  >
    <div
      v-if="isVisible"
      class="overlay-container"
      @click="$emit('close')"
    >
      <!-- Background Blur -->
      <div class="overlay-backdrop"></div>

      <!-- Main Content Container -->
      <div
        class="profile-content-container"
        @click.stop
      >
        <!-- Header Section -->
        <div class="profile-header">
          <!-- User Info Card -->
          <div class="user-card">
            <div class="user-info">
              <!-- Avatar -->
              <div class="avatar-container">
                <div class="avatar-wrapper">
                  <img 
                    :src="profileData.avatar" 
                    :alt="profileData.name"
                    class="avatar-image"
                  />
                  <!-- Status Badge -->
                  <div class="status-badge">
                    <svg class="badge-icon" viewBox="0 0 24 24" fill="none">
                      <circle cx="12" cy="12" r="10" fill="#E5E7EB"/>
                      <path d="M12 6L14 10H18L15 13L16 18L12 15L8 18L9 13L6 10H10L12 6Z" fill="#9CA3AF"/>
                    </svg>
                  </div>
                </div>
              </div>
              
              <!-- User Details -->
              <div class="user-details">
                <div class="user-level">
                  <div class="level-badge">
                    <svg class="level-icon" viewBox="0 0 24 24" fill="none">
                      <circle cx="12" cy="12" r="10" fill="currentColor"/>
                      <path d="M12 6L14 10H18L15 13L16 18L12 15L8 18L9 13L6 10H10L12 6Z" fill="white"/>
                    </svg>
                    <span class="level-text">Silver</span>
                  </div>
                </div>
                <h2 class="user-name">{{ profileData.name }}</h2>
              </div>
            </div>
            
            <!-- Close Button -->
            <button 
              @click="$emit('close')"
              class="close-button"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
              </svg>
            </button>
          </div>
        </div>

        <!-- Menu Section -->
        <div class="menu-section">
          <div class="menu-grid">
            <!-- Menu Items -->
            <div 
              v-for="item in menuItems" 
              :key="item.id"
              @click="handleMenuClick(item.id)"
              class="menu-item"
            >
              <div class="menu-icon-wrapper">
                <div class="menu-icon" v-html="item.icon"></div>
              </div>
              <span class="menu-label">{{ item.label }}</span>
              <div 
                v-if="item.badge" 
                class="menu-badge"
                :class="item.badgeType"
              >
                <svg v-if="item.badgeType === 'error'" width="12" height="12" viewBox="0 0 12 12" fill="none">
                  <path d="M9 3L3 9M3 3L9 9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                </svg>
              </div>
            </div>
          </div>
        </div>

        <!-- Upgrade Section -->
        <div class="upgrade-section">
          <div class="upgrade-card">
            <div class="upgrade-content">
              <!-- Star Icon -->
              <div class="upgrade-icon">
                <svg class="star-icon" viewBox="0 0 32 32" fill="none">
                  <circle cx="16" cy="16" r="15" fill="url(#starGradient)"/>
                  <path d="M16 6L18.5 13H26L20.5 17.5L23 24L16 20L9 24L11.5 17.5L6 13H13.5L16 6Z" fill="white"/>
                  <defs>
                    <linearGradient id="starGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" style="stop-color:#8B5CF6"/>
                      <stop offset="100%" style="stop-color:#A855F7"/>
                    </linearGradient>
                  </defs>
                </svg>
              </div>
              
              <!-- Upgrade Info -->
              <div class="upgrade-info">
                <div class="upgrade-title">Start Level</div>
                <div class="upgrade-description">
                  Buy <span class="upgrade-number">123</span> more Forevers to upgrade
                </div>
              </div>
              
              <!-- Upgrade Button -->
              <button @click="handleUpgrade" class="upgrade-button">
                Upgrade
              </button>
            </div>
          </div>
        </div>

        <!-- Bottom Controls -->
        <div class="bottom-controls">
          <!-- ID Section -->
          <div class="control-item">
            <button
              @click="copyUserId"
              class="control-button"
            >
              <div class="control-content">
                <span class="control-label">ID:</span>
                <span class="control-value">{{ profileData.id }}</span>
              </div>
              <div class="control-action">
                <!-- Copy Success State -->
                <Transition
                  name="copy-success"
                  enter-active-class="transition-all duration-300"
                  leave-active-class="transition-all duration-300"
                  enter-from-class="opacity-0 scale-90"
                  enter-to-class="opacity-100 scale-100"
                  leave-from-class="opacity-100 scale-100"
                  leave-to-class="opacity-0 scale-90"
                >
                  <div
                    v-if="showCopySuccess"
                    class="copy-success-indicator"
                  >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                      <path d="M20 6L9 17L4 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                    <span>Copied</span>
                  </div>
                  <div v-else class="copy-icon">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                      <rect x="9" y="9" width="13" height="13" rx="2" ry="2" stroke="currentColor" stroke-width="2" fill="none"/>
                      <path d="M5 15H4C2.9 15 2 14.1 2 13V4C2 2.9 2.9 2 4 2H13C14.1 2 15 2.9 15 4V5" stroke="currentColor" stroke-width="2" fill="none"/>
                    </svg>
                  </div>
                </Transition>
              </div>
            </button>
          </div>

          <!-- Language Section -->
          <div class="control-item">
            <button
              @click="toggleLanguageSelector"
              class="control-button"
            >
              <div class="control-content">
                <div class="flag-container">
                  <CountryFlag :country="selectedLanguage.code" size="small" />
                </div>
                <span class="control-value">{{ selectedLanguage.name }}</span>
              </div>
              <div class="control-action">
                <svg
                  width="16"
                  height="16"
                  viewBox="0 0 24 24"
                  fill="none"
                  class="dropdown-arrow"
                  :class="{ 'rotate-180': isLanguageDropdownOpen }"
                >
                  <path d="M6 9L12 15L18 9" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
              </div>
            </button>

            <!-- Language Dropdown -->
            <Transition
              name="dropdown"
              enter-active-class="transition-all duration-300 ease-out"
              leave-active-class="transition-all duration-200 ease-in"
              enter-from-class="opacity-0 scale-95 translate-y-1"
              enter-to-class="opacity-100 scale-100 translate-y-0"
              leave-from-class="opacity-100 scale-100 translate-y-0"
              leave-to-class="opacity-0 scale-95 translate-y-1"
            >
              <div
                v-if="isLanguageDropdownOpen"
                class="language-dropdown"
              >
                <div class="dropdown-content">
                  <button
                    v-for="language in availableLanguages"
                    :key="language.code"
                    @click="selectLanguage(language)"
                    class="dropdown-item"
                    :class="{ 'dropdown-item-active': selectedLanguage.code === language.code }"
                  >
                    <div class="dropdown-flag">
                      <CountryFlag :country="language.code" size="small" />
                    </div>
                    <span class="dropdown-text">{{ language.name }}</span>
                    <div
                      v-if="selectedLanguage.code === language.code"
                      class="dropdown-indicator"
                    ></div>
                  </button>
                </div>
              </div>
            </Transition>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted } from 'vue'
import CountryFlag from './CountryFlag.vue'

// Props
const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  }
})

// Emits
defineEmits(['close'])

// Profile data
const profileData = ref({
  name: 'Jason Williams',
  id: '515745',
  avatar: 'https://images.pexels.com/photos/15023413/pexels-photo-15023413.jpeg?auto=compress&cs=tinysrgb&w=400'
})

// State
const isLanguageDropdownOpen = ref(false)
const selectedLanguage = ref({ code: 'us', name: 'ENG' })
const showCopySuccess = ref(false)

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
  { code: 'ae', name: 'UAE' }
])

// Menu items
const menuItems = ref([
  {
    id: 'calculator',
    label: 'Calculator',
    icon: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><rect x="4" y="2" width="16" height="20" rx="2" fill="currentColor"/><rect x="6" y="4" width="12" height="4" rx="1" fill="white"/><circle cx="8" cy="11" r="1" fill="white"/><circle cx="12" cy="11" r="1" fill="white"/><circle cx="16" cy="11" r="1" fill="white"/><circle cx="8" cy="14" r="1" fill="white"/><circle cx="12" cy="14" r="1" fill="white"/><circle cx="16" cy="14" r="1" fill="white"/><circle cx="8" cy="17" r="1" fill="white"/><circle cx="12" cy="17" r="1" fill="white"/><circle cx="16" cy="17" r="1" fill="white"/></svg>'
  },
  {
    id: 'ambassador',
    label: 'Ambassador',
    icon: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 2L15.09 8.26L22 9L17 14.74L18.18 22L12 18.27L5.82 22L7 14.74L2 9L8.91 8.26L12 2Z" fill="currentColor"/></svg>'
  },
  {
    id: 'verification',
    label: 'Verification',
    icon: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 1L20.5 6V11.5C20.5 16.75 16.75 21.5 12 21.5C7.25 21.5 3.5 16.75 3.5 11.5V6L12 1Z" fill="currentColor"/><path d="M9 12L11 14L15 9" stroke="white" stroke-width="2" fill="none"/></svg>',
    badge: true,
    badgeType: 'error'
  },
  {
    id: 'security',
    label: 'Security',
    icon: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M18 11V7C18 4.79 16.21 3 14 3H10C7.79 3 6 4.79 6 7V11C5.45 11 5 11.45 5 12V19C5 20.1 5.9 21 7 21H17C18.1 21 19 20.1 19 19V12C19 11.45 18.55 11 18 11ZM8 7C8 5.9 8.9 5 10 5H14C15.1 5 16 5.9 16 7V11H8V7Z" fill="currentColor"/></svg>'
  },
  {
    id: 'settings',
    label: 'Settings',
    icon: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 8C14.21 8 16 9.79 16 12C16 14.21 14.21 16 12 16C9.79 16 8 14.21 8 12C8 9.79 9.79 8 12 8ZM21.92 12.6C21.97 12.4 21.97 12.2 21.92 12L19.93 11.65C19.87 11.43 19.79 11.22 19.69 11.02L20.86 9.23C21 9.05 21.01 8.81 20.86 8.63L19.86 7.37C19.71 7.19 19.47 7.16 19.27 7.27L17.5 8.11C17.3 7.95 17.09 7.81 16.86 7.69L16.64 5.66C16.61 5.44 16.43 5.27 16.2 5.27H14.8C14.57 5.27 14.39 5.44 14.36 5.66L14.14 7.69C13.91 7.81 13.7 7.95 13.5 8.11L11.73 7.27C11.53 7.16 11.29 7.19 11.14 7.37L10.14 8.63C9.99 8.81 10 9.05 10.14 9.23L11.31 11.02C11.21 11.22 11.13 11.43 11.07 11.65L9.08 12C8.86 12.05 8.69 12.23 8.69 12.46V13.54C8.69 13.77 8.86 13.95 9.08 14L11.07 14.35C11.13 14.57 11.21 14.78 11.31 14.98L10.14 16.77C10 16.95 9.99 17.19 10.14 17.37L11.14 18.63C11.29 18.81 11.53 18.84 11.73 18.73L13.5 17.89C13.7 18.05 13.91 18.19 14.14 18.31L14.36 20.34C14.39 20.56 14.57 20.73 14.8 20.73H16.2C16.43 20.73 16.61 20.56 16.64 20.34L16.86 18.31C17.09 18.19 17.3 18.05 17.5 17.89L19.27 18.73C19.47 18.84 19.71 18.81 19.86 18.63L20.86 17.37C21.01 17.19 21 16.95 20.86 16.77L19.69 14.98C19.79 14.78 19.87 14.57 19.93 14.35L21.92 14C22.14 13.95 22.31 13.77 22.31 13.54V12.46C22.31 12.23 22.14 12.05 21.92 12.6Z" fill="currentColor"/></svg>'
  },
  {
    id: 'support',
    label: 'Support',
    icon: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M19 14.5V9C19 5.13 15.87 2 12 2S5 5.13 5 9V14.5C5 15.88 6.12 17 7.5 17H9V9C9 7.34 10.34 6 12 6S15 7.34 15 9V17H16.5C17.88 17 19 15.88 19 14.5Z" fill="currentColor"/><path d="M7 17V19C7 20.1 7.9 21 9 21H10V17H7Z" fill="currentColor"/></svg>'
  },
  {
    id: 'help',
    label: 'Help',
    icon: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" fill="currentColor"/><path d="M9.09 9C9.32 8.19 10.04 7.6 10.91 7.6C11.97 7.6 12.82 8.45 12.82 9.51C12.82 10.57 11.97 11.42 10.91 11.42" stroke="white" stroke-width="1.5" stroke-linecap="round"/><path d="M11 16H11.01" stroke="white" stroke-width="2" stroke-linecap="round"/></svg>'
  }
])

// Prevent body scroll when overlay is open
watch(() => props.isVisible, (isVisible) => {
  if (isVisible) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = ''
    isLanguageDropdownOpen.value = false
  }
})

// Close dropdown when clicking outside
const handleClickOutside = (event) => {
  if (!event.target.closest('.control-item')) {
    isLanguageDropdownOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
  document.body.style.overflow = ''
})

// Methods
const handleMenuClick = (menuId) => {
  console.log(`Navigate to ${menuId}`)
  // TODO: Add navigation logic
}

const handleUpgrade = () => {
  console.log('Upgrade clicked')
  // TODO: Add upgrade logic
}

const copyUserId = async () => {
  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(profileData.value.id)
      showCopySuccessMessage()
      return
    }
  } catch (err) {
    console.log('Clipboard API failed, using fallback:', err.message)
  }

  // Fallback method
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
      showCopySuccessMessage()
    }
  } catch (err) {
    console.error('All copy methods failed:', err)
  }
}

const showCopySuccessMessage = () => {
  showCopySuccess.value = true
  setTimeout(() => {
    showCopySuccess.value = false
  }, 2000)
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
/* Base Container */
.overlay-container {
  position: fixed;
  inset: 0;
  z-index: 50;
  overflow: hidden;
}

.overlay-backdrop {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

/* Main Content Container */
.profile-content-container {
  position: absolute;
  left: 1rem;
  right: 1rem;
  top: 2rem;
  bottom: 6rem;
  background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #1e1b4b 100%);
  border-radius: 1.5rem;
  overflow: hidden;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  flex-direction: column;
}

/* Header Section */
.profile-header {
  padding: 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  flex-shrink: 0;
}

.user-card {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
}

.avatar-container {
  position: relative;
}

.avatar-wrapper {
  position: relative;
  width: 4rem;
  height: 4rem;
}

.avatar-image {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid rgba(255, 255, 255, 0.2);
}

.status-badge {
  position: absolute;
  bottom: -2px;
  right: -2px;
  width: 1.25rem;
  height: 1.25rem;
  background: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #1e1b4b;
}

.badge-icon {
  width: 0.75rem;
  height: 0.75rem;
  color: #9CA3AF;
}

.user-details {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.user-level {
  display: flex;
  align-items: center;
}

.level-badge {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.375rem 0.75rem;
  background: rgba(156, 163, 175, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 1rem;
}

.level-icon {
  width: 1rem;
  height: 1rem;
  color: #9CA3AF;
}

.level-text {
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
}

.user-name {
  color: white;
  font-size: 1.25rem;
  font-weight: 700;
  margin: 0;
  line-height: 1.3;
}

.close-button {
  width: 2.5rem;
  height: 2.5rem;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  cursor: pointer;
  transition: all 0.2s ease;
  flex-shrink: 0;
}

.close-button:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.05);
}

/* Menu Section */
.menu-section {
  flex: 1;
  padding: 1rem;
  overflow-y: auto;
}

.menu-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(5rem, 1fr));
  gap: 1rem;
}

.menu-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 0.5rem;
  border-radius: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
}

.menu-item:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateY(-2px);
}

.menu-icon-wrapper {
  position: relative;
}

.menu-icon {
  width: 2.5rem;
  height: 2.5rem;
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.menu-badge {
  position: absolute;
  top: -4px;
  right: -4px;
  width: 1.25rem;
  height: 1.25rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #1e1b4b;
}

.menu-badge.error {
  background: #ef4444;
  color: white;
}

.menu-label {
  color: white;
  font-size: 0.75rem;
  font-weight: 500;
  text-align: center;
  line-height: 1.2;
}

/* Upgrade Section */
.upgrade-section {
  padding: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  flex-shrink: 0;
}

.upgrade-card {
  background: linear-gradient(135deg, #8b5cf6 0%, #a855f7 100%);
  border-radius: 1rem;
  padding: 1rem;
  position: relative;
  overflow: hidden;
}

.upgrade-content {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.upgrade-icon {
  flex-shrink: 0;
}

.star-icon {
  width: 2.5rem;
  height: 2.5rem;
}

.upgrade-info {
  flex: 1;
}

.upgrade-title {
  color: white;
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.upgrade-description {
  color: rgba(255, 255, 255, 0.9);
  font-size: 0.75rem;
  line-height: 1.3;
}

.upgrade-number {
  font-weight: 700;
  color: #fbbf24;
}

.upgrade-button {
  padding: 0.5rem 1rem;
  background: white;
  color: #8b5cf6;
  font-weight: 600;
  border-radius: 0.5rem;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 0.75rem;
  flex-shrink: 0;
}

.upgrade-button:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Bottom Controls */
.bottom-controls {
  padding: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(255, 255, 255, 0.05);
  display: flex;
  gap: 0.75rem;
  flex-shrink: 0;
}

.control-item {
  flex: 1;
  position: relative;
}

.control-button {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 0.75rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.control-button:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateY(-1px);
}

.control-content {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex: 1;
  min-width: 0;
}

.control-label {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.75rem;
  font-weight: 500;
}

.control-value {
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
  truncate: true;
}

.control-action {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 1.5rem;
  height: 1.5rem;
  color: rgba(255, 255, 255, 0.7);
  flex-shrink: 0;
}

.copy-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}

.copy-success-indicator {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  color: #10b981;
  font-size: 0.625rem;
  font-weight: 600;
}

.flag-container {
  width: 1.25rem;
  height: 1.25rem;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.dropdown-arrow {
  transition: transform 0.2s ease;
}

/* Language Dropdown */
.language-dropdown {
  position: absolute;
  bottom: 100%;
  left: 0;
  right: 0;
  margin-bottom: 0.5rem;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 0.75rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  z-index: 10;
}

.dropdown-content {
  padding: 0.5rem;
  max-height: 8rem;
  overflow-y: auto;
}

.dropdown-item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem;
  border-radius: 0.5rem;
  border: none;
  background: none;
  cursor: pointer;
  transition: all 0.2s ease;
  color: #374151;
}

.dropdown-item:hover {
  background: rgba(139, 92, 246, 0.1);
}

.dropdown-item-active {
  background: rgba(139, 92, 246, 0.2);
  color: #8b5cf6;
}

.dropdown-flag {
  width: 1.25rem;
  height: 1.25rem;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
}

.dropdown-text {
  font-size: 0.75rem;
  font-weight: 500;
  flex: 1;
}

.dropdown-indicator {
  width: 0.5rem;
  height: 0.5rem;
  background: #8b5cf6;
  border-radius: 50%;
  flex-shrink: 0;
}

/* Responsive Styles */

/* Small Mobile (≤374px) */
@media (max-width: 374px) {
  .profile-content-container {
    left: 0.5rem;
    right: 0.5rem;
    top: 1rem;
    bottom: 5rem;
    border-radius: 1rem;
  }

  .profile-header {
    padding: 0.75rem;
  }

  .avatar-wrapper {
    width: 3rem;
    height: 3rem;
  }

  .user-name {
    font-size: 1rem;
  }

  .close-button {
    width: 2rem;
    height: 2rem;
  }

  .menu-section {
    padding: 0.75rem;
  }

  .menu-grid {
    grid-template-columns: repeat(4, 1fr);
    gap: 0.75rem;
  }

  .menu-item {
    padding: 0.75rem 0.25rem;
  }

  .menu-icon {
    width: 2rem;
    height: 2rem;
  }

  .menu-label {
    font-size: 0.625rem;
  }

  .upgrade-section,
  .bottom-controls {
    padding: 0.75rem;
  }

  .upgrade-content {
    gap: 0.75rem;
  }

  .star-icon {
    width: 2rem;
    height: 2rem;
  }

  .upgrade-title {
    font-size: 0.875rem;
  }

  .upgrade-description {
    font-size: 0.625rem;
  }

  .bottom-controls {
    gap: 0.5rem;
  }

  .control-button {
    padding: 0.5rem;
  }
}

/* Regular Mobile (375px-430px) */
@media (min-width: 375px) and (max-width: 430px) {
  .profile-content-container {
    left: 0.75rem;
    right: 0.75rem;
    top: 1.5rem;
    bottom: 5.5rem;
  }

  .menu-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* Tablets (431px-768px) */
@media (min-width: 431px) and (max-width: 768px) {
  .profile-content-container {
    left: 2rem;
    right: 2rem;
    top: 3rem;
    bottom: 7rem;
    border-radius: 2rem;
  }

  .profile-header {
    padding: 1.5rem;
  }

  .avatar-wrapper {
    width: 5rem;
    height: 5rem;
  }

  .user-name {
    font-size: 1.5rem;
  }

  .close-button {
    width: 3rem;
    height: 3rem;
  }

  .menu-section {
    padding: 1.5rem;
  }

  .menu-grid {
    grid-template-columns: repeat(5, 1fr);
    gap: 1.5rem;
  }

  .menu-icon {
    width: 3rem;
    height: 3rem;
  }

  .menu-label {
    font-size: 0.875rem;
  }

  .upgrade-section,
  .bottom-controls {
    padding: 1.5rem;
  }

  .star-icon {
    width: 3rem;
    height: 3rem;
  }

  .upgrade-title {
    font-size: 1.125rem;
  }

  .upgrade-description {
    font-size: 0.875rem;
  }
}

/* Desktop (≥769px) */
@media (min-width: 769px) {
  .profile-content-container {
    left: 50%;
    right: auto;
    top: 2rem;
    bottom: 6rem;
    width: 28rem;
    transform: translateX(-50%);
    border-radius: 2rem;
  }

  .menu-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* Landscape (height ≤500px) */
@media (max-height: 500px) and (orientation: landscape) {
  .profile-content-container {
    top: 0.5rem;
    bottom: 4rem;
  }

  .profile-header {
    padding: 0.5rem;
  }

  .avatar-wrapper {
    width: 2.5rem;
    height: 2.5rem;
  }

  .user-name {
    font-size: 0.875rem;
  }

  .close-button {
    width: 1.75rem;
    height: 1.75rem;
  }

  .menu-section {
    padding: 0.5rem;
  }

  .menu-grid {
    grid-template-columns: repeat(7, 1fr);
    gap: 0.5rem;
  }

  .menu-item {
    padding: 0.5rem 0.25rem;
  }

  .menu-icon {
    width: 1.75rem;
    height: 1.75rem;
  }

  .menu-label {
    font-size: 0.5rem;
  }

  .upgrade-section,
  .bottom-controls {
    padding: 0.5rem;
  }

  .star-icon {
    width: 1.5rem;
    height: 1.5rem;
  }

  .upgrade-title {
    font-size: 0.75rem;
  }

  .upgrade-description {
    font-size: 0.5rem;
  }
}

/* Animations */
.profile-overlay-enter-active {
  transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.profile-overlay-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.6, 1);
}

.profile-overlay-enter-from {
  opacity: 0;
}

.profile-overlay-enter-to {
  opacity: 1;
}

.profile-overlay-leave-from {
  opacity: 1;
}

.profile-overlay-leave-to {
  opacity: 0;
}

/* Scrollbar */
.menu-section::-webkit-scrollbar,
.dropdown-content::-webkit-scrollbar {
  width: 2px;
}

.menu-section::-webkit-scrollbar-track,
.dropdown-content::-webkit-scrollbar-track {
  background: transparent;
}

.menu-section::-webkit-scrollbar-thumb,
.dropdown-content::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.3);
  border-radius: 1px;
}

/* Touch Optimizations */
@media (hover: none) and (pointer: coarse) {
  .menu-item:hover {
    background: rgba(255, 255, 255, 0.05);
    transform: none;
  }

  .menu-item:active {
    background: rgba(255, 255, 255, 0.15);
    transform: scale(0.95);
  }

  .control-button:hover {
    background: rgba(255, 255, 255, 0.1);
    transform: none;
  }

  .control-button:active {
    background: rgba(255, 255, 255, 0.2);
    transform: scale(0.98);
  }
}

/* Performance */
.profile-content-container,
.menu-item,
.control-button,
.upgrade-button {
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}
</style>
