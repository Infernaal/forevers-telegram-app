<template>
  <div class="telegram-webapp-container">
    <!-- Заглушка для Desktop WebApp -->
    <div v-if="showDesktopOnly" class="desktop-only-overlay">
      <div class="desktop-only-card">
        <img src="https://img.icons8.com/ios-filled/100/2019CE/smartphone-tablet.png" alt="Mobile Only" class="icon" />
        <h2>Available on Mobile &amp; Tablet Only</h2>
        <p>This mini-app works exclusively in the Telegram<br/>Mobile App or on a Tablet.</p>
        <p class="hint">Please open this chat in Telegram on your phone or tablet.</p>
      </div>
    </div>

    <!-- Основное приложение для мобильных -->
    <RouterView v-else />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  name: 'App',
  setup() {
    // флаг для отображения заглушки на десктопе
    const showDesktopOnly = ref(false)

    onMounted(() => {
      if (window.Telegram && window.Telegram.WebApp) {
        const webapp = window.Telegram.WebApp

        // всегда надо вызвать ready()
        webapp.ready()

        // если десктоп — показываем заглушку и выходим
        if (webapp.isDesktop) {
          showDesktopOnly.value = true
          return
        }

        // иначе — продолжаем инициализацию для мобильных
        webapp.expand()
        webapp.disableVerticalSwipes()

        // Theme support
        const scheme = webapp.colorScheme
        document.body.classList.toggle('tg-dark', scheme === 'dark')
        
        // Set theme colors
        webapp.setHeaderColor('#2019CE')
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

    return {
      showDesktopOnly
    }
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

/* Заглушка “только на мобильных” */
.desktop-only-overlay {
  position: absolute;
  inset: 0;
  background: var(--tg-theme-bg-color, #fff);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  text-align: center;
}

.desktop-only-card {
  max-width: 300px;
  background: var(--tg-theme-bg-color, #fff);
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
  padding: 24px;
}

.desktop-only-card .icon {
  width: 64px;
  height: 64px;
  margin-bottom: 16px;
}

.desktop-only-card h2 {
  margin: 0 0 12px;
  font-size: 1.25rem;
  color: var(--tg-theme-text-color, #000);
}

.desktop-only-card p {
  margin: 4px 0;
  color: var(--tg-theme-text-color, #555);
  font-size: 0.9rem;
}

.desktop-only-card .hint {
  margin-top: 16px;
  font-style: italic;
  font-size: 0.8rem;
  color: var(--tg-theme-text-color, #888);
}
</style>
