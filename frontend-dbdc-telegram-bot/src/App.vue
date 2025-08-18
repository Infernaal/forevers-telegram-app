<template>
  <div class="telegram-webapp-container">
    <RouterView />
    <ApiRouteErrorNotification />
  </div>
</template>

<script>
import { onMounted } from 'vue'
import ApiRouteErrorNotification from './components/ApiRouteErrorNotification.vue'
import { provideBottomOffset } from './composables/useBottomNavigation.js'

export default {
  name: 'App',
  components: { ApiRouteErrorNotification },
  setup() {
    // Используем composable для управления bottomOffset
    const { bottomOffset } = provideBottomOffset()

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
        webapp.setHeaderColor('#2019CE')
        webapp.setBackgroundColor('#FAFAFA')

        // Обработчик изменения viewport в Telegram
        webapp.onEvent('viewportChanged', () => {
          handleViewportChange()
        })
      }

      // Prevent zoom on mobile
      const viewport = document.querySelector('meta[name="viewport"]')
      if (!viewport) {
        const meta = document.createElement('meta')
        meta.name = 'viewport'
        meta.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover'
        document.head.appendChild(meta)
      }

      // Функция для обновления viewport высоты и устранения серых областей
      const handleViewportChange = () => {
        // Принудительно пересчитываем viewport высоту
        const vh = window.innerHeight * 0.01
        document.documentElement.style.setProperty('--vh', `${vh}px`)

        // Обновляем CSS переменные Telegram
        if (window.Telegram?.WebApp) {
          const safeAreaBottom = window.Telegram.WebApp.safeAreaInset?.bottom || 0
          document.documentElement.style.setProperty('--tg-safe-area-inset-bottom', `${safeAreaBottom}px`)
        }

        // Принудительная перерисовка для устранения серых областей
        requestAnimationFrame(() => {
          document.body.style.height = `${window.innerHeight}px`
          document.documentElement.style.height = `${window.innerHeight}px`

          // Еще один кадр для гарантии
          requestAnimationFrame(() => {
            document.body.style.height = ''
            document.documentElement.style.height = ''
          })
        })
      }

      // Обработчики для клавиатуры
      const handleKeyboardShow = () => {
        // Добавляем класс для стилизации при показе клавиатуры
        document.body.classList.add('keyboard-visible')
        setTimeout(handleViewportChange, 100)
      }

      const handleKeyboardHide = () => {
        // Убираем класс и принудительно обновляем layout
        document.body.classList.remove('keyboard-visible')
        setTimeout(() => {
          handleViewportChange()
          // Дополнительная принудительная перерисовка
          window.scrollTo(0, 0)
        }, 100)
      }

      // События для разных типов устройств
      window.addEventListener('resize', (e) => {
        // Опре��еляем, скрылась ли клавиатура по изменению высоты
        const heightDiff = screen.height - window.innerHeight
        if (heightDiff < 150) {
          handleKeyboardHide()
        } else if (heightDiff > 150) {
          handleKeyboardShow()
        }
        handleViewportChange()
      })

      window.addEventListener('orientationchange', () => {
        setTimeout(handleViewportChange, 500)
      })

      // Visual Viewport API для современных браузеров
      if (window.visualViewport) {
        window.visualViewport.addEventListener('resize', handleViewportChange)
        window.visualViewport.addEventListener('scroll', handleViewportChange)
      }

      // Обработчики для input элементов
      document.addEventListener('focusin', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
          setTimeout(handleKeyboardShow, 100)
        }
      })

      document.addEventListener('focusout', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
          setTimeout(handleKeyboardHide, 300)
        }
      })

      // Первичная установка
      handleViewportChange()
    })

    return {
      bottomOffset
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
</style>
