<template>
  <div v-if="isVisible" class="fixed inset-0 z-50 font-montserrat bg-black bg-opacity-10 backdrop-blur-xl">
    <!-- Dropdown Wrapper -->
    <div class="relative w-full flex justify-center items-end pb-32 sm:pb-40 md:pb-44 lg:pb-48 xl:pb-52">
      <!-- Dropdown Menu -->
      <div class="relative w-[92%] max-w-[460px] sm:max-w-[500px] md:max-w-[560px] lg:max-w-[620px] xl:max-w-[680px]
                  h-[500px] sm:h-[600px] lg:h-[650px] max-h-[calc(100vh-140px)]
                  bg-gradient-to-r from-[#120B81] via-[#09074E] to-[#09074E]
                  border border-[#09074E] backdrop-blur-[32px] 
                  rounded-[20px] z-[50] overflow-hidden shadow-lg">
        <div class="p-4 text-white text-center">
        <!-- Профильный контент -->
        </div>
      </div>
      <!-- Triangle (ниже dropdown'а) -->
      <div class="absolute top-[100%] mt-3 left-[2.25rem] sm:left-[3.75rem] md:left-[4.5rem] lg:left-[6rem] z-[55]">
        <div class="w-0 h-0 border-l-[12px] border-r-[12px] border-t-[15px]
                border-l-transparent border-r-transparent 
                border-t-[rgba(18,11,129,0.95)] drop-shadow-md"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CountryFlag from './CountryFlag.vue'

// Props
defineProps({
  isVisible: {
    type: Boolean,
    default: false
  }
})

// Emits
const emit = defineEmits(['close'])

// State
const showCopySuccess = ref(false)
const showLanguageDropdown = ref(false)

// Language state
const languages = ref([
  { code: 'ENG', name: 'English', country: 'uk' },
  { code: 'ESP', name: 'Español', country: 'spain' },
  { code: 'FRA', name: 'Français', country: 'france' },
  { code: 'DEU', name: 'Deutsch', country: 'germany' },
  { code: 'ITA', name: 'Italiano', country: 'italy' },
  { code: 'RUS', name: 'Русский', country: 'ukraine' },
  { code: 'CHN', name: '中文', country: 'china' },
  { code: 'JPN', name: '日本語', country: 'japan' },
  { code: 'KOR', name: '한국어', country: 'new zealand' },
  { code: 'ARA', name: 'العربية', country: 'uae' },
  { code: 'POR', name: 'Português', country: 'spain' },
  { code: 'NLD', name: 'Nederlands', country: 'norway' }
])

const selectedLanguage = ref(languages.value[0])

// Methods
const handleMenuClick = (menuItem) => {
  console.log(`Menu clicked: ${menuItem}`)
  // Handle menu navigation
}

const handleUpgrade = () => {
  console.log('Upgrade clicked')
  // Handle upgrade
}

const copyUserID = async () => {
  let copySuccess = false

  // Try modern clipboard API first
  if (navigator.clipboard) {
    try {
      await navigator.clipboard.writeText('515745')
      copySuccess = true
    } catch (clipboardErr) {
      console.log('Clipboard API failed, trying fallback method')
    }
  }

  // If clipboard API failed or is not available, use fallback
  if (!copySuccess) {
    try {
      const textArea = document.createElement('textarea')
      textArea.value = '515745'
      textArea.style.position = 'fixed'
      textArea.style.left = '-999999px'
      textArea.style.top = '-999999px'
      textArea.style.opacity = '0'
      document.body.appendChild(textArea)
      textArea.focus()
      textArea.select()

      const successful = document.execCommand('copy')
      document.body.removeChild(textArea)

      if (!successful) {
        console.log('Fallback copy method also failed')
      }
    } catch (fallbackErr) {
      console.error('Fallback copy failed:', fallbackErr)
    }
  }

  // Show copied state for user feedback
  showCopySuccess.value = true
  setTimeout(() => {
    showCopySuccess.value = false
  }, 2500)
}

const toggleLanguageDropdown = () => {
  showLanguageDropdown.value = !showLanguageDropdown.value
}

const selectLanguage = (language) => {
  selectedLanguage.value = language
  showLanguageDropdown.value = false
  console.log('Language selected:', language)
}
</script>

<style scoped>
/* Custom animations */
@keyframes fadeInScale {
  0% {
    opacity: 0;
    transform: scale(0.9);
  }
  50% {
    opacity: 0.8;
    transform: scale(1.05);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes bounceIn {
  0% {
    opacity: 0;
    transform: scale(0.3) rotate(-10deg);
  }
  50% {
    opacity: 0.9;
    transform: scale(1.1) rotate(5deg);
  }
  80% {
    transform: scale(0.95) rotate(-2deg);
  }
  100% {
    opacity: 1;
    transform: scale(1) rotate(0deg);
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

/* Custom utilities */
.scrollbar-none {
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.scrollbar-none::-webkit-scrollbar {
  display: none;
}

/* Tablet specific positioning */
@media (min-width: 768px) and (max-width: 1023px) {
  .tablet-triangle-position {
    bottom: 20rem !important;
  }

  .tablet-dropdown-position {
    bottom: 7rem !important;
  }
}

/* Copied State Styling - matching HoldersView */
.id-copied-state {
  border: 1px solid #07B80E !important;
  background: #129E0F !important;
  transform: scale(1.02) !important;
}

.id-copied-content {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 6px;
  box-sizing: border-box;
  animation: fadeInScale 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.id-copied-text {
  color: #FFF;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 14px;
  font-weight: 600;
  line-height: 22px;
  text-align: center;
  animation: slideInLeft 0.3s ease-out 0.1s both;
}

.id-copied-icon {
  position: relative;
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: bounceIn 0.5s ease-out 0.2s both;
}

.id-tick-svg {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

/* Height utilities */
.h-13 {
  height: 3.25rem;
}

.h-21 {
  height: 5.25rem;
}

/* Fade in animation for overlay */
.fixed.inset-0.z-50 {
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
</style>
