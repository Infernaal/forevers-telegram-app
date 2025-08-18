/**
 * Enhanced Telegram WebApp viewport handling
 * Fixes issues with keyboard show/hide affecting viewport height
 */

export class TelegramViewportManager {
  constructor() {
    this.tg = window.Telegram?.WebApp
    this.isInitialized = false
    this.lastStableHeight = null
    this.keyboardTimeout = null
    this.resizeTimeout = null
    
    // Store original viewport height on load
    this.originalViewportHeight = window.innerHeight
    
    this.init()
  }

  init() {
    if (!this.tg || this.isInitialized) return
    
    this.isInitialized = true
    
    // Set initial viewport properties
    this.updateViewportProperties()
    
    // Listen to Telegram's viewport changes
    this.tg.onEvent('viewportChanged', () => {
      this.handleViewportChange()
    })
    
    // Additional window resize listener as fallback
    window.addEventListener('resize', () => {
      this.handleWindowResize()
    })
    
    // Keyboard detection through focus/blur events
    this.setupKeyboardDetection()
    
    // Force expansion on init
    this.tg.expand()
  }

  updateViewportProperties() {
    if (!this.tg) return

    const viewportHeight = this.tg.viewportHeight || window.innerHeight
    const stableHeight = this.tg.viewportStableHeight || window.innerHeight
    
    // Update CSS custom properties
    document.documentElement.style.setProperty('--tg-viewport-height', `${viewportHeight}px`)
    document.documentElement.style.setProperty('--tg-viewport-stable-height', `${stableHeight}px`)
    document.documentElement.style.setProperty('--vh', `${viewportHeight * 0.01}px`)
    
    // Calculate keyboard height
    const keyboardHeight = Math.max(0, stableHeight - viewportHeight)
    document.documentElement.style.setProperty('--keyboard-height', `${keyboardHeight}px`)
    
    // Store stable height
    if (keyboardHeight === 0) {
      this.lastStableHeight = viewportHeight
    }
  }

  handleViewportChange() {
    // Clear existing timeout
    if (this.resizeTimeout) {
      clearTimeout(this.resizeTimeout)
    }
    
    // Debounce viewport updates
    this.resizeTimeout = setTimeout(() => {
      this.updateViewportProperties()
      this.fixViewportIssues()
    }, 50)
  }

  handleWindowResize() {
    // Fallback for cases where Telegram's viewport event doesn't fire
    if (this.resizeTimeout) {
      clearTimeout(this.resizeTimeout)
    }
    
    this.resizeTimeout = setTimeout(() => {
      if (this.tg) {
        this.updateViewportProperties()
      } else {
        // Fallback viewport calculation
        const vh = window.innerHeight * 0.01
        document.documentElement.style.setProperty('--vh', `${vh}px`)
      }
      this.fixViewportIssues()
    }, 100)
  }

  setupKeyboardDetection() {
    // Detect keyboard show/hide through input focus/blur
    let isKeyboardOpen = false
    
    const inputElements = ['input', 'textarea', 'select']
    
    inputElements.forEach(selector => {
      document.addEventListener('focusin', (e) => {
        if (e.target.matches(selector)) {
          isKeyboardOpen = true
          this.onKeyboardShow()
        }
      })
      
      document.addEventListener('focusout', (e) => {
        if (e.target.matches(selector)) {
          // Delay to allow for focus switching between inputs
          setTimeout(() => {
            if (!document.activeElement || !inputElements.some(sel => document.activeElement.matches(sel))) {
              isKeyboardOpen = false
              this.onKeyboardHide()
            }
          }, 150)
        }
      })
    })
  }

  onKeyboardShow() {
    // Add class to body for keyboard-specific styling
    document.body.classList.add('keyboard-open')
    
    // Clear any existing keyboard timeout
    if (this.keyboardTimeout) {
      clearTimeout(this.keyboardTimeout)
    }
  }

  onKeyboardHide() {
    // Remove keyboard class
    document.body.classList.remove('keyboard-open')
    
    // Force viewport fix after keyboard hides
    this.keyboardTimeout = setTimeout(() => {
      this.forceViewportFix()
    }, 300)
  }

  forceViewportFix() {
    if (!this.tg) return
    
    try {
      // Force re-expansion
      this.tg.expand()
      
      // Update viewport properties
      this.updateViewportProperties()
      
      // Additional fix: scroll to top to reset viewport
      window.scrollTo(0, 0)
      
      // Force layout recalculation
      document.body.offsetHeight
      
      // One more expansion attempt
      setTimeout(() => {
        this.tg.expand()
        this.updateViewportProperties()
      }, 100)
      
    } catch (error) {
      console.warn('Error in forceViewportFix:', error)
    }
  }

  fixViewportIssues() {
    // Additional fixes for common viewport issues
    
    // Ensure body height matches viewport
    const currentViewportHeight = this.tg?.viewportHeight || window.innerHeight
    
    // Fix gray area issue by ensuring proper heights
    if (currentViewportHeight < this.originalViewportHeight * 0.7) {
      // Likely keyboard is open, don't force fix
      return
    }
    
    // Force scroll position reset
    if (window.scrollY > 0) {
      window.scrollTo(0, 0)
    }
    
    // Ensure container takes full height
    const container = document.querySelector('.telegram-webapp-container')
    if (container) {
      container.style.height = `${currentViewportHeight}px`
      
      // Force reflow
      container.offsetHeight
      
      // Reset to CSS values
      setTimeout(() => {
        container.style.height = ''
      }, 50)
    }
  }

  // Public method to manually trigger viewport fix
  refresh() {
    this.forceViewportFix()
  }
}

// Create singleton instance
let viewportManager = null

export function initTelegramViewport() {
  if (!viewportManager && window.Telegram?.WebApp) {
    viewportManager = new TelegramViewportManager()
  }
  return viewportManager
}

export function getTelegramViewport() {
  return viewportManager
}

// Helper function to fix viewport issues manually
export function fixTelegramViewport() {
  if (viewportManager) {
    viewportManager.refresh()
  }
}
