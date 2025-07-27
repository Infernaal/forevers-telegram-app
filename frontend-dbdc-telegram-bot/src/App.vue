<template>
  <div class="telegram-webapp-container">
    <!-- Mobile-first responsive wrapper -->
    <div class="w-full h-full xs:max-w-full sm:max-w-full ml:max-w-[480px] ml:mx-auto ml:shadow-lg ml:border-x ml:border-gray-200 md:max-w-full md:mx-0 md:shadow-none md:border-x-0 lg:max-w-full lg:mx-0 lg:shadow-none lg:border-x-0 xl:max-w-full xl:mx-0 xl:shadow-none xl:border-x-0 2xl:max-w-full 2xl:mx-0 2xl:shadow-none 2xl:border-x-0">
      <RouterView />
    </div>
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

  /* Background - responsive */
  background: white;

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

/* Responsive desktop background */
@media (min-width: 640px) {
  .telegram-webapp-container {
    background: #f5f5f5;
    padding: 20px 0;
  }
}

@media (min-width: 1024px) {
  .telegram-webapp-container {
    background: #f0f0f0;
    padding: 40px 0;
  }
}

/* Fix for content area to allow proper scrolling within views */
.telegram-webapp-container > div {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
  -webkit-overflow-scrolling: touch;
  overscroll-behavior: contain;

  /* Responsive container styles */
  position: relative;
}

/* Desktop container styling */
@media (min-width: 640px) {
  .telegram-webapp-container > div {
    border-radius: 12px 12px 0 0;
    overflow: hidden;
    background: white;
  }
}

/* Additional body and html fixes for mobile */
body, html {
  overflow: hidden;
  overscroll-behavior: none;
  -webkit-overflow-scrolling: auto;
  touch-action: pan-y;
  height: 100%;
  width: 100%;
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Responsive font scaling */
@media (max-width: 374px) {
  html {
    font-size: 14px;
  }
}

@media (min-width: 375px) and (max-width: 430px) {
  html {
    font-size: 15px;
  }
}

@media (min-width: 431px) and (max-width: 768px) {
  html {
    font-size: 16px;
  }
}

@media (min-width: 769px) {
  html {
    font-size: 17px;
  }
}

/* High DPI displays optimization */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  * {
    image-rendering: -webkit-optimize-contrast;
    image-rendering: crisp-edges;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .telegram-webapp-container {
    background: #1a1a1a;
  }

  .telegram-webapp-container > div {
    background: #1a1a1a;
  }
}

/* Landscape orientation adjustments */
@media (max-height: 500px) and (orientation: landscape) {
  .telegram-webapp-container {
    padding: 10px 0;
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
</style>
