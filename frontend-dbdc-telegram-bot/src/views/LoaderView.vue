<template>
  <div class="w-full min-h-screen bg-white font-montserrat overflow-hidden flex items-center justify-center">
    <!-- Main Content Container -->
    <div class="w-full flex-1 flex items-center justify-center p-3 sm:p-4 md:p-6 lg:p-8">
      <div class="w-full h-[372px] xs:h-[400px] sm:h-[450px] md:h-[500px] lg:h-[550px]
                  relative rounded-2xl sm:rounded-3xl md:rounded-[2rem] lg:rounded-[2.5rem]
                  p-4 xs:p-6 sm:p-8 md:p-10 lg:p-12 mx-auto
                  text-white flex flex-col items-center justify-center" :style="cardStyle">
        <!-- Welcome Section -->
        <div class="flex flex-col items-center gap-2 xs:gap-3 sm:gap-4 md:gap-5 mb-6 xs:mb-8 sm:mb-10 md:mb-12">
          <div class="text-xl xs:text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold text-white text-center leading-tight">
            Welcome to
          </div>

          <!-- DBD Capital Text Logo -->
          <div class="flex items-center justify-center">
            <img
              src="/dbd-logo.svg"
              alt="DBD Capital Logo"
              class="w-28 h-20 xs:w-36 xs:h-24 sm:w-40 sm:h-28 md:w-48 md:h-32 lg:w-56 lg:h-36"
            />
          </div>
        </div>

        <!-- Loading Section -->
        <div class="flex flex-col items-center gap-6 xs:gap-8 sm:gap-10 md:gap-12">
          <!-- Loading Text -->
          <div class="text-white text-center text-xs xs:text-sm sm:text-base md:text-lg font-medium
                      max-w-[280px] xs:max-w-[298px] sm:max-w-[350px] md:max-w-[400px] lg:max-w-[450px]
                      leading-4 xs:leading-5 sm:leading-6 md:leading-7 px-2">
            Please wait a little, while we prepare everything for you
          </div>

          <!-- Figma Design Loader -->
          <div class="w-12 h-12 xs:w-16 xs:h-16 sm:w-20 sm:h-20 md:w-24 md:h-24 lg:w-28 lg:h-28 relative">
            <!-- Orange semi-circle background -->
            <div class="w-full h-full absolute inset-0 loader-bg"></div>

            <!-- Spinning white gradient ring - smaller size -->
            <div class="absolute inset-0 flex items-center justify-center spinner">
              <svg
                class="w-8 h-8 xs:w-10 xs:h-10 sm:w-12 sm:h-12 md:w-14 md:h-14 lg:w-16 lg:h-16"
                viewBox="0 0 35 34"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <defs>
                  <linearGradient id="conicGradient" x1="50%" y1="50%" x2="50%" y2="0%">
                    <stop offset="0%" style="stop-color:white;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:white;stop-opacity:0" />
                  </linearGradient>
                </defs>
                <path
                  d="M35 17.0004C35 26.1904 27.2396 33.6404 17.6666 33.6404C8.09371 33.6404 0.333313 26.1904 0.333313 17.0004C0.333313 7.81033 8.09371 0.360352 17.6666 0.360352C27.2396 0.360352 35 7.81033 35 17.0004ZM3.79998 17.0004C3.79998 24.3524 10.0083 30.3124 17.6666 30.3124C25.325 30.3124 31.5333 24.3524 31.5333 17.0004C31.5333 9.64834 25.325 3.68835 17.6666 3.68835C10.0083 3.68835 3.79998 9.64834 3.79998 17.0004Z"
                  fill="url(#conicGradient)"
                />
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import telegramUserService from '../services/telegramUserService.js'
import authByEmailService from '../services/authByEmailService.js'
import registrationService from '../services/registrationService.js'
import { getStoredReferralContext } from '@/utils/telegramWebApp.js'

const router = useRouter()
const route = useRoute()

const isProcessing = ref(true)
const error = ref(null)

// Provided redirect (may be overridden by action result)
const providedRedirect = route.query.redirect || '/account-check'
const action = route.query.action || null
const minDelay = Number(route.query.minDelay || 400) // prevent flash
const duration = Number(route.query.duration || 0) // explicit duration (ms) for pure time-based loader
const startedAt = performance.now()

const cardStyle = {
  background: `
    linear-gradient(0deg, rgba(0, 0, 0, 0.25) 0%, rgba(0, 0, 0, 0.25) 100%),
    linear-gradient(90deg, #2019CE 20.91%, #473FFF 68.93%)
  `
}

const finish = async (target) => {
  const elapsed = performance.now() - startedAt
  const waitMore = minDelay - elapsed
  if (waitMore > 0) {
    await new Promise(r => setTimeout(r, waitMore))
  }
  // Mark login/registration success for FavoritesView notification
  if (target === '/favorites') {
    try { sessionStorage.setItem('loggedSuccess', '1') } catch (e) { /* ignore */ }
  }
  isProcessing.value = false
  router.replace(target)
}

const getTelegramUserId = () => {
  try {
    return window?.Telegram?.WebApp?.initDataUnsafe?.user?.id || null
  } catch (e) { return null }
}

const runAction = async () => {
  if (!action) {
    // Time-based loader: wait for duration (or fallback to default 5000) after minDelay
    const total = duration > 0 ? duration : 5000
    const elapsed = performance.now() - startedAt
    const remaining = Math.max(total - elapsed, 0)
    setTimeout(() => finish(providedRedirect), remaining)
    return
  }

  switch (action) {
    case 'check-telegram': {
      // Exchange initData for session (already done earlier if loader not first view; safe to repeat)
      const initData = window?.Telegram?.WebApp?.initData || ''
      if (!initData) {
        return finish('/account-check')
      }
      const res = await telegramUserService.authWithInitData(initData)
      const target = res.status === 'success' ? '/favorites' : '/account-check'
      return finish(target)
    }
    case 'check-email': {
      // email can be passed as query OR from sessionStorage
      const email = route.query.email || sessionStorage.getItem('verificationEmail')
      if (!email) {
        return finish('/account-check')
      }
      const initData = window?.Telegram?.WebApp?.initData || null
      const res = await authByEmailService.auth(email, { initData })
      return finish(res?.target || '/account-check')
    }
    case 'register': {
      // Expect registration form fields in sessionStorage (simple handoff) or query
      const regRaw = sessionStorage.getItem('pendingRegistration')
      if (!regRaw) return finish('/registration')
      let payload
      try { payload = JSON.parse(regRaw) } catch { return finish('/registration') }
      const res = await registrationService.register(payload)
      if (res.status === 'success') {
        // After success go favorites (or pending email verify -> email-verification)
        const target = res.email_verification_required ? '/email-verification' : '/favorites'
        sessionStorage.removeItem('pendingRegistration')
        return finish(target)
      }
  if (res.target) return finish(res.target)
  return finish('/registration')
    }
    default:
      return finish(providedRedirect)
  }
}

onMounted(() => {
  runAction().catch(() => finish(providedRedirect))
})
</script>

<style scoped>
/* Figma design loader background - orange semi-circle */
.loader-bg {
  border-radius: 0 100px 100px 0;
  background: #FF6319;
}

/* Spinning animation for the loader */
.spinner {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* Performance optimizations */
* {
  will-change: auto;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Global scrollbar hiding and Telegram optimizations */
::-webkit-scrollbar {
  width: 0;
}

* {
  -webkit-tap-highlight-color: transparent;
  scrollbar-width: none;
  -ms-overflow-style: none;
}
</style>
