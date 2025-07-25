<template>
  <div class="min-h-screen bg-white telegram-webapp">
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
/* Telegram WebApp viewport height */
.telegram-webapp {
  height: 100vh;
  height: calc(var(--vh, 1vh) * 100);
}

/* Prevent overscroll bouncing */
.telegram-webapp {
  overscroll-behavior: none;
  -webkit-overflow-scrolling: touch;
}
</style>
