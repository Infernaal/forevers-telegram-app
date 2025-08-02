<template>
  <div>
    <!-- Profile Overlay Component -->
    <ProfileOverlay
      :is-visible="isProfileMenuOpen"
      :trigger-position="profileButtonPosition"
      @close="closeProfileMenu"
    />

    <!-- Bottom Navigation -->
    <div class="fixed left-0 right-0 bottom-[env(safe-area-inset-bottom,0px)] z-[10001] bg-white dark:bg-[#1b1b1b] border-t border-black/10 shadow-[0_-4px_16px_rgba(0,0,0,0.08)] rounded-t-2xl">
      <div class="flex items-center justify-center px-4 pt-[clamp(0.75rem,2vh,1.25rem)] pb-[calc(clamp(0.75rem,2vh,1.25rem)+env(safe-area-inset-bottom,0px))]">
        <div class="flex items-center justify-between w-full gap-3">
          <!-- Кнопки -->
          <template v-for="tab in [
            { name: 'profile', label: 'Profile', icon: '', isProfile: true },
            { name: 'wallet', label: 'Wallet', icon: 'M15.3369 0C16.7553 0 17.9215 1.10571 18.0293 2.50488C19.1647 2.82612 19.9999 3.87598 20 5.11914V15.2842C19.9998 16.7817 18.7879 18 17.2988 18H2.70117C1.21206 18 0.0002339 16.7817 0 15.2842V2.71582C0.000233829 1.21827 1.21206 0 2.70117 0H15.3369ZM2.70117 3.67188C1.90768 3.67188 1.2618 4.32114 1.26172 5.11914V15.2842C1.26195 16.082 1.90778 16.7314 2.70117 16.7314H17.2988C18.0922 16.7314 18.738 16.082 18.7383 15.2842V13.1484H14.7158C13.1219 13.1484 11.8244 11.8443 11.8242 10.2412C11.8242 8.63803 13.1217 7.33301 14.7158 7.33301H18.7383V5.11914C18.7382 4.32114 18.0923 3.67188 17.2988 3.67188H2.70117ZM14.7158 8.60254C13.8174 8.60254 13.0859 9.33767 13.0859 10.2412C13.0861 11.1446 13.8175 11.8799 14.7158 11.8799H18.7383V8.60254H14.7158ZM15.9404 9.6748C16.3756 9.6748 16.7283 9.99219 16.7285 10.3838C16.7285 10.7755 16.3757 11.0938 15.9404 11.0938C15.5052 11.0937 15.1523 10.7755 15.1523 10.3838C15.1526 9.99222 15.5053 9.67484 15.9404 9.6748ZM2.70117 1.26855C1.90778 1.26855 1.26195 1.91796 1.26172 2.71582V2.82227C1.67869 2.5571 2.17244 2.40332 2.70117 2.40332H16.7422C16.5994 1.75535 16.0235 1.26855 15.3369 1.26855H2.70117Z', isProfile: false },
            { name: 'favorites', label: 'Favorites', icon: 'M19.0791 0C19.6648 0 19.9999 0.476058 20 1.14258C20 1.80914 19.5817 2.28598 18.9961 2.28613H6.77832V5.80957H14.8955C15.4812 5.80963 15.8993 6.28565 15.8994 6.95215C15.8994 7.61877 15.4812 8.09564 14.8955 8.0957H6.77832V11.6191H11.0459C11.6316 11.6191 12.0497 12.0951 12.0498 12.7617C12.0498 13.4284 11.6317 13.9043 11.0459 13.9043H6.77832V18.8574C6.7782 19.5238 6.35992 19.9998 5.77441 20C5.18872 20 4.76965 19.5239 4.76953 18.8574V8.19043H1.00391C0.418346 8.19028 9.72129e-05 7.71429 0 7.04785C0 6.38129 0.418278 5.90491 1.00391 5.80957H4.76953V1.14258C4.76965 0.476058 5.18872 0 5.77441 0H19.0791Z', isProfile: false },
            { name: 'cart', label: 'Cart', icon: 'M8.99992 0C11.2937 6.01927e-05 13.1601 1.71665 13.1601 3.82617V4.95801H15.8886C16.2926 4.95801 16.6298 5.24124 16.6659 5.61133L17.9892 19.165C17.996 19.2031 17.9998 19.2424 17.9999 19.2822C17.9999 19.6786 17.6508 19.9999 17.2197 20H0.781174C0.562191 20 0.352885 19.9152 0.205002 19.7666C0.0571058 19.6179 -0.0167136 19.4186 0.00285324 19.2178L1.33195 5.61133C1.3681 5.24123 1.70529 4.95801 2.1093 4.95801H4.83977V3.82617C4.83977 1.71662 6.70624 0 8.99992 0Z', isProfile: false },
            { name: 'holders', label: 'Holders', icon: 'M8.44238 12.1094C9.31973 12.1094 10.1776 12.2621 10.9922 12.5625C11.4039 12.7144 11.6127 13.1645 11.458 13.5684C11.3032 13.9722 10.8432 14.1763 10.4316 14.0244C9.79694 13.7904 9.12755 13.6719 8.44238 13.6719H7.24805C4.12994 13.6719 1.59277 16.1602 1.59277 19.2188C1.59277 19.6501 1.23657 19.9998 0.796875 20C0.35699 20 0 19.6502 0 19.2188C0 15.2986 3.25161 12.1094 7.24805 12.1094H8.44238Z', isProfile: false },
          ]" :key="tab.name">
            <button
              v-if="tab.name !== 'profile'"
              @click="navigateTo(tab.name)"
              :class="[
                'flex flex-col items-center justify-center flex-1 gap-[clamp(0.125rem,0.6vh,0.5rem)] text-center transition-all duration-200 ease-out transform-gpu active:scale-95 active:bg-black/[0.02] active:rounded-xl',
                activeTab === tab.name ? 'text-blue-700' : 'text-gray-600'
              ]"
            >
              <div
                :class="[
                  'flex items-center justify-center transition-all duration-200 ease-out rounded-xl',
                  activeTab === tab.name ? 'bg-blue-600' : ''
                ]"
                :style="{
                  width: 'clamp(1.75rem,5vw,2.5rem)',
                  height: 'clamp(1.75rem,5vw,2.5rem)'
                }"
              >
                <svg
                  viewBox="0 0 24 24"
                  :class="[
                    'fill-current transition-all duration-200',
                    activeTab === tab.name ? 'text-white' : 'text-gray-600'
                  ]"
                  :style="{
                    width: 'clamp(1rem,3.5vw,1.5rem)',
                    height: 'clamp(1rem,3.5vw,1.5rem)'
                  }"
                >
                  <path :d="tab.icon" />
                </svg>
              </div>
              <span class="text-[clamp(0.625rem,2.3vw,0.75rem)] font-medium leading-tight">{{ tab.label }}</span>
            </button>

            <!-- Profile отдельная логика -->
            <button
              v-else
              ref="profileButton"
              @click="toggleProfile"
              :class="[
                'flex flex-col items-center justify-center flex-1 gap-[clamp(0.125rem,0.6vh,0.5rem)] text-center transition-all duration-200 ease-out transform-gpu active:scale-95 active:bg-black/[0.02] active:rounded-xl',
                isProfileMenuOpen ? 'text-blue-700' : 'text-gray-600'
              ]"
            >
              <div class="relative">
                <div
                  :class="[
                    'flex items-center justify-center transition-all duration-200 ease-out rounded-xl',
                    isProfileMenuOpen ? 'bg-blue-600' : ''
                  ]"
                  :style="{
                    width: 'clamp(1.75rem,5vw,2.5rem)',
                    height: 'clamp(1.75rem,5vw,2.5rem)'
                  }"
                >
                  <svg
                    v-if="isProfileMenuOpen"
                    viewBox="0 0 20 20"
                    fill="none"
                    :class="'fill-current text-white'"
                    :style="{
                      width: 'clamp(1rem,3.5vw,1.5rem)',
                      height: 'clamp(1rem,3.5vw,1.5rem)'
                    }"
                  >
                    <path d="M15 5L5 15M5 5L15 15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <img
                    v-else
                    src="https://images.pexels.com/photos/15023413/pexels-photo-15023413.jpeg?auto=compress&cs=tinysrgb&w=400"
                    alt="Profile"
                    class="rounded-full border-2 border-purple-400 object-cover"
                    :style="{
                      width: 'clamp(1.75rem,5vw,2.5rem)',
                      height: 'clamp(1.75rem,5vw,2.5rem)'
                    }"
                  />
                </div>
              </div>
              <span class="text-[clamp(0.625rem,2.3vw,0.75rem)] font-medium leading-tight">Profile</span>
            </button>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, nextTick, onMounted, onUnmounted, reactive } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useCart } from '../composables/useCart.js'
import ProfileOverlay from './ProfileOverlay.vue'

// Router
const router = useRouter()
const route = useRoute()

// Cart
const { cartItemsCount } = useCart()

// Profile menu state
const isProfileMenuOpen = ref(false)
const profileButton = ref(null)
const profileButtonPosition = reactive({
  left: 0,
  width: 0
})

// Computed active tab based on current route
const activeTab = ref('wallet')

// Watch route changes to update active tab
watch(() => route.path, (newPath) => {
  const pathToTab = {
    '/wallet': 'wallet',
    '/favorites': 'favorites',
    '/rent-out': 'favorites', // RentOut is part of Favorites section
    '/cart': 'cart',
    '/holders': 'holders'
  }
  activeTab.value = pathToTab[newPath] || 'wallet'
}, { immediate: true })

// Methods
const navigateTo = (tab) => {
  // Close profile menu if open
  if (isProfileMenuOpen.value) {
    isProfileMenuOpen.value = false
  }

  // Map tab names to routes
  const routeMap = {
    wallet: '/wallet',
    favorites: '/favorites',
    cart: '/cart',
    holders: '/holders'
  }

  router.push(routeMap[tab])
}

const updateProfileButtonPosition = () => {
  if (profileButton.value) {
    const rect = profileButton.value.getBoundingClientRect()
    profileButtonPosition.left = rect.left
    profileButtonPosition.width = rect.width
  }
}

const toggleProfile = () => {
  isProfileMenuOpen.value = !isProfileMenuOpen.value

  if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {
    window.Telegram.WebApp.HapticFeedback.impactOccurred('medium')
  }
}

const closeProfileMenu = () => {
  isProfileMenuOpen.value = false
}

watch(isProfileMenuOpen, async (val) => {
  if (val) {
    await nextTick()
    updateProfileButtonPosition()
  }
})

const handleResize = () => {
  updateProfileButtonPosition()
}

onMounted(() => {
  updateProfileButtonPosition()
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
})


</script>

<style scoped>
/* Touch optimizations */
* {
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
  user-select: none;
}

/* Performance optimizations */
.fixed {
  transform: translateZ(0);
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Cart badge animations */
.cart-badge-enter-active,
.cart-badge-leave-active {
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.cart-badge-enter-from {
  opacity: 0;
  transform: scale(0);
}

.cart-badge-leave-to {
  opacity: 0;
  transform: scale(0);
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .fixed {
    background-color: #1a1a1a !important;
    border-top-color: rgba(255, 255, 255, 0.1) !important;
    box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.3), 0 -2px 6px rgba(0, 0, 0, 0.2) !important;
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  .transition-all,
  .transition-transform {
    transition: none !important;
  }

  .active\:scale-95:active {
    transform: none !important;
  }
}
</style>
