<template>
  <div class="telegram-webapp-container">
    <RouterView />
  </div>
</template>

<script>
import { onMounted } from 'vue'

export default {
  name: 'App',
  setup() {
    onMounted(() => {
      // Telegram WebApp configuration
      if (window.Telegram && window.Telegram.WebApp) {
        const webapp = window.Telegram.WebApp
        webapp.ready()
        webapp.expand()
        webapp.disableVerticalSwipes()

        // Theme support
        const scheme = webapp.colorScheme
        document.body.classList.toggle('tg-dark', scheme === 'dark')
        
        // Set theme colors
        webapp.setHeaderColor('#FFFFFF')
        webapp.setBackgroundColor('#FAFAFA')
      }

      // Prevent zoom on mobile
      const viewport = document.querySelector('meta[name="viewport"]')
      if (!viewport) {
        const meta = document.createElement('meta')
        meta.name = 'viewport'
        meta.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover'
        document.head.appendChild(meta)
      }

      // Set viewport height for mobile
      const setViewportHeight = () => {
        document.documentElement.style.setProperty('--vh', `${window.innerHeight * 0.01}px`)
      }
      setViewportHeight()
      window.addEventListener('resize', setViewportHeight)
      window.addEventListener('orientationchange', setViewportHeight)
    })
  }
}
</script>

<style>
/* Telegram WebApp container with enhanced scroll prevention */
.telegram-webapp-container {
  /* Viewport and positioning */
  width: 100%;
  height: 100vh;
  height: calc(var(--vh, 1vh) * 100);
  min-height: 100vh;
  min-height: calc(var(--vh, 1vh) * 100);

  /* 🟢 Поддержка Telegram темы */
  background: var(--tg-theme-bg-color, #ffffff);
  color: var(--tg-theme-text-color, #000000);

  /* Enhanced scroll and overscroll prevention */
  overflow: hidden;
  overscroll-behavior: none;
  overscroll-behavior-y: none;
  overscroll-behavior-x: none;

  /* Disable iOS rubber band effect */
  -webkit-overflow-scrolling: auto;

  /* Prevent touch callouts and selections that can interfere */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;

  /* Position and layout */
  position: relative;
  display: flex;
  flex-direction: column;

  /* GPU acceleration for better performance */
  transform: translateZ(0);
  will-change: transform;

  /* Prevent content shifting */
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Fix for content area to allow proper scrolling within views */
.telegram-webapp-container > * {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
  -webkit-overflow-scrolling: touch;
  overscroll-behavior: contain;
}

/* Additional body and html fixes for mobile */
body, html {
  overflow: hidden;
  overscroll-behavior: none;
  -webkit-overflow-scrolling: auto;
  touch-action: pan-y;
  height: 100%;
  width: 100%;
  
  /* 🟢 Telegram theme support */
  background-color: var(--tg-theme-bg-color, #ffffff);
  color: var(--tg-theme-text-color, #000000);
}
</style>
