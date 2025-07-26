<template>
  <div class="holders-view w-full max-w-md mx-auto bg-gray-100 min-h-screen">
    <!-- Content Container -->
    <div class="content-container bg-gray-100 px-4 pb-24 flex items-center justify-center" style="min-height: calc(100vh - 96px);">
      
      <!-- Holders Section -->
      <div class="holders-section">
        <div class="holders-card bg-gray-50 rounded-2xl p-6">
          <div class="flex flex-col items-center text-center">
            <div class="w-16 h-16 bg-dbd-gray rounded-lg flex items-center justify-center mb-4">
              <svg width="20" height="22" viewBox="0 0 18 20" class="text-white">
                <path d="M8.44238 12.1094C9.31973 12.1094 10.1776 12.2621 10.9922 12.5625C11.4039 12.7144 11.6127 13.1645 11.458 13.5684C11.3032 13.9722 10.8432 14.1763 10.4316 14.0244C9.79694 13.7904 9.12755 13.6719 8.44238 13.6719H7.24805C4.12994 13.6719 1.59277 16.1602 1.59277 19.2188C1.59277 19.6501 1.23657 19.9998 0.796875 20C0.35699 20 0 19.6502 0 19.2188C0 15.2986 3.25161 12.1094 7.24805 12.1094H8.44238ZM15.5312 10.3125C15.971 10.3126 16.3271 10.6624 16.3271 11.0938V11.6953C16.63 11.7604 16.9748 11.86 17.3701 12.0107C17.78 12.1671 17.9834 12.6195 17.8242 13.0215C17.6648 13.4236 17.2029 13.6232 16.793 13.4668C16.0335 13.1771 15.5576 13.1377 15.1924 13.1377C14.8301 13.1377 14.5352 13.4301 14.5352 13.7891C14.5352 14.1663 14.955 14.4405 15.5332 14.4404C16.8933 14.4404 17.9998 15.4329 18 16.6533C18 17.2476 17.7543 17.8071 17.3086 18.2285C17.0281 18.4937 16.6913 18.6817 16.3271 18.7822V19.2188C16.3271 19.6501 15.971 19.9999 15.5312 20C15.0914 20 14.7344 19.6502 14.7344 19.2188V18.7588C14.3074 18.6775 13.8264 18.5489 13.3652 18.3691C12.9565 18.2098 12.7564 17.7555 12.9189 17.3545C13.0814 16.9537 13.5445 16.758 13.9531 16.917C14.6767 17.1991 15.4104 17.3046 15.7031 17.3047C16.0779 17.3047 16.4072 17.0001 16.4072 16.6533C16.407 16.3005 16.0068 16.0029 15.5332 16.0029C14.0562 16.0029 12.9424 15.051 12.9424 13.7891C12.9424 12.7229 13.7127 11.8309 14.7344 11.6221V11.0938C14.7344 10.6623 15.0914 10.3125 15.5312 10.3125ZM7.76562 0C10.7299 7.33854e-05 13.1416 2.36571 13.1416 5.27344C13.1416 8.18117 10.7299 10.5468 7.76562 10.5469C4.80124 10.5469 2.38965 8.18121 2.38965 5.27344C2.38965 2.36566 4.80124 0 7.76562 0ZM7.76562 1.5625C5.67958 1.5625 3.98242 3.22723 3.98242 5.27344C3.98242 7.31965 5.67958 8.98438 7.76562 8.98438C9.85161 8.9843 11.5488 7.3196 11.5488 5.27344C11.5488 3.22727 9.85161 1.56257 7.76562 1.5625Z" fill="currentColor"/>
              </svg>
            </div>
            <h2 class="text-2xl font-bold text-dbd-dark mb-2">Holders</h2>
            <p class="text-dbd-gray">Coming soon...</p>
          </div>
        </div>
      </div>

    </div>

    <!-- Bottom Navigation Component -->
    <BottomNavigation />
  </div>
</template>

<script>
import BottomNavigation from '../components/BottomNavigation.vue'

export default {
  name: 'HoldersView',
  components: {
    BottomNavigation
  }
}
</script>

<style scoped>
.holders-view {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  min-height: 100vh;
  min-height: 100dvh; /* Dynamic viewport height */
  background: #f3f4f6;
  overflow-x: hidden;
  overscroll-behavior: none;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.content-container {
  padding: 20px 16px 100px 16px; /* Bottom padding for navigation */
  box-sizing: border-box;
}

.holders-section {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.holders-card {
  width: 100%;
  max-width: 360px;
  margin: 0 auto;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.2s ease;
  background: #f9fafb;
  border-radius: 16px;
  padding: 24px;
  border: 1px solid rgba(75, 77, 80, 0.1);
}

.holders-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

/* Icon styling */
.w-16.h-16 {
  width: 64px;
  height: 64px;
  background: #4B4D50;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
  box-shadow: 0 4px 12px rgba(75, 77, 80, 0.2);
}

/* Text styling */
.text-2xl {
  font-size: 24px;
  font-weight: 700;
  color: #02070E;
  margin-bottom: 8px;
  line-height: 1.3;
}

.text-dbd-gray {
  font-size: 16px;
  font-weight: 500;
  color: #4B4D50;
  line-height: 1.4;
}

/* Very small mobile devices (до 320px) */
@media (max-width: 320px) {
  .holders-view {
    max-width: 100%;
  }

  .content-container {
    padding: 12px 8px 80px 8px;
  }

  .holders-card {
    max-width: 100%;
    border-radius: 12px;
    padding: 16px;
  }

  .w-16.h-16 {
    width: 48px;
    height: 48px;
    border-radius: 8px;
    margin-bottom: 12px;
  }

  .w-16.h-16 svg {
    width: 16px;
    height: 18px;
  }

  .text-2xl {
    font-size: 18px;
    margin-bottom: 6px;
  }

  .text-dbd-gray {
    font-size: 14px;
  }
}

/* Small mobile devices (321px - 374px) */
@media (min-width: 321px) and (max-width: 374px) {
  .holders-view {
    max-width: 100%;
  }

  .content-container {
    padding: 14px 12px 85px 12px;
  }

  .holders-card {
    max-width: 100%;
    border-radius: 14px;
    padding: 18px;
  }

  .w-16.h-16 {
    width: 52px;
    height: 52px;
    border-radius: 10px;
    margin-bottom: 14px;
  }

  .w-16.h-16 svg {
    width: 17px;
    height: 19px;
  }

  .text-2xl {
    font-size: 20px;
    margin-bottom: 7px;
  }

  .text-dbd-gray {
    font-size: 15px;
  }
}

/* Regular small mobile devices (375px - 430px) */
@media (min-width: 375px) and (max-width: 430px) {
  .holders-view {
    max-width: 100%;
  }

  .content-container {
    padding: 16px 14px 90px 14px;
  }

  .holders-card {
    max-width: 100%;
    border-radius: 16px;
    padding: 20px;
  }

  .w-16.h-16 {
    width: 56px;
    height: 56px;
    border-radius: 12px;
    margin-bottom: 16px;
  }

  .w-16.h-16 svg {
    width: 18px;
    height: 20px;
  }

  .text-2xl {
    font-size: 22px;
    margin-bottom: 8px;
  }

  .text-dbd-gray {
    font-size: 15px;
  }
}

/* Large mobile and small tablets (431px - 768px) */
@media (min-width: 431px) and (max-width: 768px) {
  .holders-view {
    max-width: 480px;
    margin: 0 auto;
  }

  .content-container {
    padding: 20px 18px 95px 18px;
  }

  .holders-card {
    max-width: 420px;
    border-radius: 18px;
    padding: 28px;
  }

  .w-16.h-16 {
    width: 72px;
    height: 72px;
    border-radius: 14px;
    margin-bottom: 20px;
  }

  .w-16.h-16 svg {
    width: 22px;
    height: 24px;
  }

  .text-2xl {
    font-size: 28px;
    margin-bottom: 10px;
  }

  .text-dbd-gray {
    font-size: 17px;
  }
}

/* Tablets and desktop (769px+) */
@media (min-width: 769px) {
  .holders-view {
    max-width: 480px;
    margin: 20px auto;
    border-radius: 20px;
    box-shadow: 0 0 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
  }

  .content-container {
    padding: 32px 24px 110px 24px;
  }

  .holders-card {
    max-width: 440px;
    border-radius: 20px;
    padding: 32px;
  }

  .w-16.h-16 {
    width: 80px;
    height: 80px;
    border-radius: 16px;
    margin-bottom: 24px;
  }

  .w-16.h-16 svg {
    width: 24px;
    height: 26px;
  }

  .text-2xl {
    font-size: 32px;
    margin-bottom: 12px;
  }

  .text-dbd-gray {
    font-size: 18px;
  }
}

/* Landscape orientation adjustments for phones */
@media (max-height: 500px) and (orientation: landscape) {
  .content-container {
    padding: 8px 16px 70px 16px;
  }

  .holders-card {
    padding: 16px;
    border-radius: 12px;
  }

  .w-16.h-16 {
    width: 40px;
    height: 40px;
    border-radius: 8px;
    margin-bottom: 8px;
  }

  .w-16.h-16 svg {
    width: 14px;
    height: 16px;
  }

  .text-2xl {
    font-size: 16px;
    margin-bottom: 4px;
  }

  .text-dbd-gray {
    font-size: 13px;
  }
}

/* High DPI displays */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .w-16.h-16 svg {
    image-rendering: -webkit-optimize-contrast;
    image-rendering: crisp-edges;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .holders-view {
    background: #1a1a1a;
  }

  .holders-card {
    background: #2a2a2a;
    border-color: rgba(255, 255, 255, 0.1);
  }

  .text-2xl {
    color: #ffffff;
  }

  .text-dbd-gray {
    color: #a0a0a0;
  }

  .w-16.h-16 {
    background: #3a3a3a;
    border: 1px solid rgba(255, 255, 255, 0.1);
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  .holders-card {
    transition: none;
  }

  .holders-card:hover {
    transform: none;
  }
}

/* Touch optimizations */
@media (hover: none) and (pointer: coarse) {
  .holders-card:hover {
    transform: none;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  }
}

/* Safe area support for different iOS versions */
@supports (padding-bottom: env(safe-area-inset-bottom)) {
  .content-container {
    padding-bottom: calc(100px + env(safe-area-inset-bottom));
  }
}

@supports (padding-bottom: constant(safe-area-inset-bottom)) {
  .content-container {
    padding-bottom: calc(100px + constant(safe-area-inset-bottom));
  }
}

/* Performance optimizations */
.holders-card {
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Custom scrollbar for webkit browsers */
:::-webkit-scrollbar {
  width: 0;
}

/* Telegram WebApp specific optimizations */
* {
  -webkit-tap-highlight-color: transparent;
}
</style>
