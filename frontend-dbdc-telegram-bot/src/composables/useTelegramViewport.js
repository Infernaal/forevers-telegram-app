import { ref, onMounted, onUnmounted } from 'vue'
import { getTelegramViewport, fixTelegramViewport } from '../utils/telegramViewport.js'

export function useTelegramViewport() {
  const viewportHeight = ref(window.innerHeight)
  const stableHeight = ref(window.innerHeight)
  const keyboardHeight = ref(0)
  const isKeyboardOpen = ref(false)
  
  let tg = null
  let resizeHandler = null
  
  onMounted(() => {
    tg = window.Telegram?.WebApp
    
    if (tg) {
      // Initialize values
      updateViewportData()
      
      // Listen for viewport changes
      tg.onEvent('viewportChanged', updateViewportData)
      
      // Fallback resize listener
      resizeHandler = () => updateViewportData()
      window.addEventListener('resize', resizeHandler)
    }
  })
  
  onUnmounted(() => {
    if (resizeHandler) {
      window.removeEventListener('resize', resizeHandler)
    }
  })
  
  function updateViewportData() {
    if (tg) {
      viewportHeight.value = tg.viewportHeight || window.innerHeight
      stableHeight.value = tg.viewportStableHeight || window.innerHeight
      keyboardHeight.value = Math.max(0, stableHeight.value - viewportHeight.value)
      isKeyboardOpen.value = keyboardHeight.value > 50 // threshold for keyboard detection
    } else {
      viewportHeight.value = window.innerHeight
      stableHeight.value = window.innerHeight
      keyboardHeight.value = 0
      isKeyboardOpen.value = false
    }
  }
  
  // Manual viewport fix function
  function fixViewport() {
    fixTelegramViewport()
    setTimeout(updateViewportData, 100)
  }
  
  // Expand webapp
  function expand() {
    if (tg) {
      tg.expand()
    }
  }
  
  // Get viewport manager instance
  function getViewportManager() {
    return getTelegramViewport()
  }
  
  return {
    viewportHeight,
    stableHeight,
    keyboardHeight,
    isKeyboardOpen,
    fixViewport,
    expand,
    getViewportManager
  }
}

// Helper hook for components that need keyboard-aware styling
export function useKeyboardAware() {
  const { isKeyboardOpen, keyboardHeight, fixViewport } = useTelegramViewport()
  
  // Auto-fix viewport when keyboard closes
  let keyboardWasOpen = false
  
  const keyboardWatcher = () => {
    if (keyboardWasOpen && !isKeyboardOpen.value) {
      // Keyboard just closed, fix viewport
      setTimeout(() => {
        fixViewport()
      }, 300)
    }
    keyboardWasOpen = isKeyboardOpen.value
  }
  
  onMounted(() => {
    // Watch for keyboard changes
    const unwatch = watch(isKeyboardOpen, keyboardWatcher)
    
    onUnmounted(() => {
      unwatch()
    })
  })
  
  return {
    isKeyboardOpen,
    keyboardHeight,
    fixViewport
  }
}
