import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/tailwind.css'
import telegramUserService from './services/telegramUserService'
import { useUserInfo } from './composables/useUserInfo'

import { Content } from '@builder.io/sdk-vue'

const app = createApp(App)

// Предварительно инициализируем данные пользователя для кеширования
const { initializeUserInfo } = useUserInfo()
initializeUserInfo()

app.component('BuilderComponent', Content)

if (window.Telegram && window.Telegram.WebApp) {
  const tg = window.Telegram.WebApp

  // Initialize the WebApp
  tg.ready()

  // Expand to full height
  tg.expand()

  // Set theme colors
  tg.setHeaderColor('#120B81')
  tg.setBackgroundColor('#FAFAFA')

  // Enable closing confirmation
  tg.enableClosingConfirmation()

  // Disable vertical swipes (prevents accidental page refresh)
  tg.disableVerticalSwipes()

  // Set viewport settings for better mobile experience
  document.documentElement.style.setProperty('--tg-viewport-height', tg.viewportHeight + 'px')
  document.documentElement.style.setProperty('--tg-viewport-stable-height', tg.viewportStableHeight + 'px')

  // Handle viewport changes
  tg.onEvent('viewportChanged', () => {
    document.documentElement.style.setProperty('--tg-viewport-height', tg.viewportHeight + 'px')
    document.documentElement.style.setProperty('--tg-viewport-stable-height', tg.viewportStableHeight + 'px')
  })

  // Handle theme changes
  tg.onEvent('themeChanged', () => {
    // Update CSS variables based on theme
    const themeParams = tg.themeParams
    if (themeParams.bg_color) {
      document.documentElement.style.setProperty('--tg-bg-color', themeParams.bg_color)
    }
    if (themeParams.text_color) {
      document.documentElement.style.setProperty('--tg-text-color', themeParams.text_color)
    }
  })

  // Add haptic feedback support
  window.triggerHaptic = (type = 'impact', style = 'medium') => {
    if (tg.HapticFeedback) {
      if (type === 'impact') {
        tg.HapticFeedback.impactOccurred(style) // light, medium, heavy
      } else if (type === 'notification') {
        tg.HapticFeedback.notificationOccurred(style) // error, success, warning
      } else if (type === 'selection') {
        tg.HapticFeedback.selectionChanged()
      }
    }
  }

  // Enhanced safe area handling
  const updateSafeArea = () => {
    const safeAreaTop = tg.safeAreaInset?.top || 0
    const safeAreaBottom = tg.safeAreaInset?.bottom || 0
    document.documentElement.style.setProperty('--tg-safe-area-inset-top', safeAreaTop + 'px')
    document.documentElement.style.setProperty('--tg-safe-area-inset-bottom', safeAreaBottom + 'px')
  }
  updateSafeArea()

  // Better keyboard handling for form inputs
  tg.onEvent('viewportChanged', () => {
    updateSafeArea()
    // Adjust viewport for keyboard
    const keyboardHeight = Math.max(0, window.innerHeight - tg.viewportHeight)
    document.documentElement.style.setProperty('--keyboard-height', keyboardHeight + 'px')

    // Prevent cursor jumping when keyboard opens/closes
    if (keyboardHeight > 100) {
      // Keyboard is open - add class to body
      document.body.classList.add('keyboard-open')
      // Prevent viewport shifting by maintaining scroll position
      const activeInput = document.activeElement
      if (activeInput && activeInput.tagName === 'INPUT') {
        // Small delay to ensure smooth transition
        setTimeout(() => {
          activeInput.scrollIntoView({ behavior: 'smooth', block: 'center' })
        }, 150)
      }
    } else {
      // Keyboard is closed
      document.body.classList.remove('keyboard-open')
    }
  })
  
  // Add to global for easy access
  window.Telegram.WebApp.utils = {
    haptic: window.triggerHaptic,
    isExpanded: () => tg.isExpanded,
    platform: tg.platform,
    version: tg.version
  }

  // Listen for main button / closing event to logout
  tg.onEvent('backButtonClicked', async () => {
    await telegramUserService.logout()
  })
  tg.onEvent('close', async () => {
    await telegramUserService.logout()
  })
  // Fallback: page visibility / unload
  window.addEventListener('beforeunload', () => {
    telegramUserService.logout()
    // Очищаем ресурсы composable
    const { cleanup } = useUserInfo()
    cleanup()
  })
}

app.use(router)

app.mount('#app')
