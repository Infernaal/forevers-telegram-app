import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/tailwind.css'

import { Content } from '@builder.io/sdk-vue'

const app = createApp(App)

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

  // Set responsive breakpoint variables
  const updateBreakpoints = () => {
    const width = window.innerWidth
    document.documentElement.style.setProperty('--screen-width', width + 'px')

    // Set current breakpoint
    if (width < 375) {
      document.documentElement.setAttribute('data-breakpoint', 'xs')
    } else if (width < 430) {
      document.documentElement.setAttribute('data-breakpoint', 'sm')
    } else if (width < 640) {
      document.documentElement.setAttribute('data-breakpoint', 'ml')
    } else if (width < 768) {
      document.documentElement.setAttribute('data-breakpoint', 'md')
    } else if (width < 1024) {
      document.documentElement.setAttribute('data-breakpoint', 'lg')
    } else {
      document.documentElement.setAttribute('data-breakpoint', 'xl')
    }
  }
  updateBreakpoints()

  // Handle viewport changes
  tg.onEvent('viewportChanged', () => {
    document.documentElement.style.setProperty('--tg-viewport-height', tg.viewportHeight + 'px')
    document.documentElement.style.setProperty('--tg-viewport-stable-height', tg.viewportStableHeight + 'px')
    updateBreakpoints()
  })

  // Handle window resize for breakpoint updates
  window.addEventListener('resize', updateBreakpoints)

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
  })

  // Add to global for easy access
  window.Telegram.WebApp.utils = {
    haptic: window.triggerHaptic,
    isExpanded: () => tg.isExpanded,
    platform: tg.platform,
    version: tg.version
  }
}

app.use(router)

app.mount('#app')
