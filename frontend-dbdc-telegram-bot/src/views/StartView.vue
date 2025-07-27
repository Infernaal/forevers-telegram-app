<template>
  <div class="start-view-container">
    <!-- Main Content -->
    <div class="main-content">
      <div class="content-card" :style="cardStyle">
        <!-- Brand Section -->
        <div class="brand-section">
          <div class="logo-container">
            <div class="logo-circle">
              <svg
                width="32"
                height="32"
                viewBox="0 0 32 32"
                fill="none"
                class="logo-icon"
              >
                <path
                  d="M29.037 8.33839V2.96289H8.11476V9.78787H2.96289V15.1634H8.11476V28.54H14.128V21.9801H19.2136V16.6046H14.128V15.1634H24.117V9.78787H14.128V8.33839H29.037Z"
                  fill="#2019CE"
                />
              </svg>
            </div>
          </div>
          <div class="brand-text">
            <h2 class="brand-title">Forevers</h2>
            <p class="brand-subtitle">
              With us — you're always ahead
            </p>
          </div>
        </div>

        <!-- Features Section -->
        <div class="features-section">
          <h3 class="features-title">
            What can this bot do?
          </h3>
          <ul class="features-list">
            <li
              v-for="feature in features"
              :key="feature.id"
              class="feature-item"
            >
              <span class="feature-bullet"></span>
              <span class="feature-text">
                {{ feature.text }}
              </span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Bottom Section -->
    <div class="bottom-section">
      <button @click="handleStart" class="start-button">
        Start
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'

// Router instance
const router = useRouter()

// Features data
const features = ref([
  { id: 1, text: 'Discover the capabilities of this bot!' },
  { id: 2, text: 'Explore the features of this bot!' },
  { id: 3, text: 'Discover the amazing features this bot offers!' }
])

// Computed styles for better performance
const cardStyle = computed(() => ({
  background: `
    linear-gradient(0deg, rgba(0, 0, 0, 0.25) 0%, rgba(0, 0, 0, 0.25) 100%),
    linear-gradient(90deg, #2019CE 20.91%, #473FFF 68.93%)
  `
}))

// Handle start button click
const handleStart = () => {
  router.push('/favorites')
}

// Initialize app
onMounted(() => {
  // Prevent zoom on mobile
  const viewport = document.querySelector('meta[name="viewport"]')
  if (!viewport) {
    const meta = document.createElement('meta')
    meta.name = 'viewport'
    meta.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no'
    document.head.appendChild(meta)
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap');

/* Container and layout */
.start-view-container {
  min-height: 100vh;
  min-height: 100dvh; /* Dynamic viewport height */
  background: white;
  display: flex;
  flex-direction: column;
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
  overscroll-behavior: none;
}

.main-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px 16px;
  box-sizing: border-box;
}

.content-card {
  width: 100%;
  max-width: 360px;
  position: relative;
  border-radius: 40px;
  padding: 24px;
  color: white;
  display: flex;
  flex-direction: column;
  min-height: 400px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  transform: translateZ(0);
  will-change: transform;
}

/* Brand section */
.brand-section {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 32px;
}

.logo-container {
  flex-shrink: 0;
}

.logo-circle {
  width: 48px;
  height: 48px;
  background: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.logo-icon {
  width: 32px;
  height: 32px;
}

.brand-text {
  flex: 1;
  min-width: 0;
}

.brand-title {
  font-size: 32px;
  font-weight: 700;
  line-height: 1.2;
  margin: 0 0 8px 0;
  color: white;
}

.brand-subtitle {
  font-size: 16px;
  font-weight: 500;
  line-height: 1.4;
  margin: 0;
  color: white;
  opacity: 0.95;
}

/* Features section */
.features-section {
  margin-top: 16px;
}

.features-title {
  font-size: 18px;
  font-weight: 500;
  margin: 0 0 16px 0;
  text-align: center;
  color: white;
}

.features-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.feature-item {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  line-height: 1.4;
}

.feature-bullet {
  width: 8px;
  height: 8px;
  background: rgba(255, 255, 255, 0.7);
  border-radius: 50%;
  flex-shrink: 0;
  margin-top: 6px;
}

.feature-text {
  font-size: 14px;
  font-weight: 500;
  color: white;
  opacity: 0.95;
}

/* Bottom section */
.bottom-section {
  background: white;
  padding: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-top: 1px solid rgba(0, 0, 0, 0.05);
  /* Safe area support */
  padding-bottom: calc(16px + env(safe-area-inset-bottom, 0px));
}

.start-button {
  width: 100%;
  max-width: 360px;
  height: 52px;
  background: linear-gradient(90deg, #2019CE 0%, #473FFF 100%);
  border: none;
  border-radius: 26px;
  color: white;
  font-weight: 700;
  font-size: 16px;
  font-family: inherit;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 12px rgba(32, 25, 206, 0.25);
  outline: none;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
  transform: translateZ(0);
}

.start-button:hover {
  box-shadow: 0 6px 16px rgba(32, 25, 206, 0.35);
  transform: translateY(-1px);
}

.start-button:active {
  transform: translateY(0) scale(0.98);
  box-shadow: 0 2px 8px rgba(32, 25, 206, 0.4);
}

/* Small mobile devices (iPhone SE, small Android) - ≤374px */
@media (max-width: 374px) {
  .main-content {
    padding: 16px 12px;
  }
  
  .content-card {
    max-width: 100%;
    border-radius: 32px;
    padding: 20px;
    min-height: 360px;
  }
  
  .brand-section {
    gap: 12px;
    margin-bottom: 24px;
  }
  
  .logo-circle {
    width: 40px;
    height: 40px;
  }
  
  .logo-icon {
    width: 24px;
    height: 24px;
  }
  
  .brand-title {
    font-size: 26px;
    margin-bottom: 6px;
  }
  
  .brand-subtitle {
    font-size: 14px;
  }
  
  .features-title {
    font-size: 16px;
    margin-bottom: 12px;
  }
  
  .features-list {
    gap: 10px;
  }
  
  .feature-text {
    font-size: 13px;
  }
  
  .feature-bullet {
    width: 6px;
    height: 6px;
    margin-top: 5px;
  }
  
  .bottom-section {
    padding: 12px;
    padding-bottom: calc(12px + env(safe-area-inset-bottom, 0px));
  }
  
  .start-button {
    height: 48px;
    font-size: 15px;
    border-radius: 24px;
  }
}

/* Regular mobile devices (iPhone 12, 13, 14) - 375px to 430px */
@media (min-width: 375px) and (max-width: 430px) {
  .main-content {
    padding: 18px 16px;
  }
  
  .content-card {
    max-width: 340px;
    border-radius: 36px;
    padding: 22px;
    min-height: 380px;
  }
  
  .brand-section {
    gap: 14px;
    margin-bottom: 28px;
  }
  
  .logo-circle {
    width: 44px;
    height: 44px;
  }
  
  .logo-icon {
    width: 28px;
    height: 28px;
  }
  
  .brand-title {
    font-size: 30px;
    margin-bottom: 7px;
  }
  
  .brand-subtitle {
    font-size: 15px;
  }
  
  .features-title {
    font-size: 17px;
    margin-bottom: 14px;
  }
  
  .features-list {
    gap: 11px;
  }
  
  .feature-text {
    font-size: 13.5px;
  }
  
  .feature-bullet {
    width: 7px;
    height: 7px;
    margin-top: 5.5px;
  }
  
  .bottom-section {
    padding: 14px;
    padding-bottom: calc(14px + env(safe-area-inset-bottom, 0px));
  }
  
  .start-button {
    height: 50px;
    font-size: 15.5px;
    border-radius: 25px;
  }
}

/* Large mobile and small tablets - 431px to 768px */
@media (min-width: 431px) and (max-width: 768px) {
  .main-content {
    padding: 24px 20px;
  }
  
  .content-card {
    max-width: 400px;
    border-radius: 44px;
    padding: 28px;
    min-height: 420px;
  }
  
  .brand-section {
    gap: 18px;
    margin-bottom: 36px;
  }
  
  .logo-circle {
    width: 52px;
    height: 52px;
  }
  
  .logo-icon {
    width: 36px;
    height: 36px;
  }
  
  .brand-title {
    font-size: 36px;
    margin-bottom: 9px;
  }
  
  .brand-subtitle {
    font-size: 17px;
  }
  
  .features-title {
    font-size: 19px;
    margin-bottom: 18px;
  }
  
  .features-list {
    gap: 14px;
  }
  
  .feature-text {
    font-size: 15px;
  }
  
  .feature-bullet {
    width: 9px;
    height: 9px;
    margin-top: 6px;
  }
  
  .bottom-section {
    padding: 18px 20px;
    padding-bottom: calc(18px + env(safe-area-inset-bottom, 0px));
  }
  
  .start-button {
    height: 56px;
    font-size: 17px;
    border-radius: 28px;
    max-width: 400px;
  }
}

/* Tablets and desktop - ≥769px */
@media (min-width: 769px) {
  .start-view-container {
    max-width: 480px;
    margin: 0 auto;
    box-shadow: 0 0 40px rgba(0, 0, 0, 0.1);
    border-radius: 20px 20px 0 0;
    overflow: hidden;
  }
  
  .main-content {
    padding: 32px 24px;
  }
  
  .content-card {
    max-width: 420px;
    border-radius: 48px;
    padding: 32px;
    min-height: 460px;
  }
  
  .brand-section {
    gap: 20px;
    margin-bottom: 40px;
  }
  
  .logo-circle {
    width: 56px;
    height: 56px;
  }
  
  .logo-icon {
    width: 40px;
    height: 40px;
  }
  
  .brand-title {
    font-size: 40px;
    margin-bottom: 10px;
  }
  
  .brand-subtitle {
    font-size: 18px;
  }
  
  .features-title {
    font-size: 20px;
    margin-bottom: 20px;
  }
  
  .features-list {
    gap: 16px;
  }
  
  .feature-text {
    font-size: 16px;
  }
  
  .feature-bullet {
    width: 10px;
    height: 10px;
    margin-top: 6px;
  }
  
  .bottom-section {
    padding: 20px 24px;
    padding-bottom: calc(20px + env(safe-area-inset-bottom, 0px));
  }
  
  .start-button {
    height: 60px;
    font-size: 18px;
    border-radius: 30px;
    max-width: 420px;
  }
}

/* Landscape orientation adjustments for phones */
@media (max-height: 500px) and (orientation: landscape) {
  .start-view-container {
    min-height: 100vh;
  }
  
  .main-content {
    padding: 12px 16px;
  }
  
  .content-card {
    min-height: 300px;
    padding: 16px;
    border-radius: 24px;
  }
  
  .brand-section {
    margin-bottom: 16px;
    gap: 12px;
  }
  
  .logo-circle {
    width: 36px;
    height: 36px;
  }
  
  .logo-icon {
    width: 24px;
    height: 24px;
  }
  
  .brand-title {
    font-size: 24px;
    margin-bottom: 4px;
  }
  
  .brand-subtitle {
    font-size: 13px;
  }
  
  .features-title {
    font-size: 14px;
    margin-bottom: 8px;
  }
  
  .features-list {
    gap: 6px;
  }
  
  .feature-text {
    font-size: 12px;
  }
  
  .feature-bullet {
    width: 5px;
    height: 5px;
    margin-top: 4px;
  }
  
  .bottom-section {
    padding: 10px 16px;
    padding-bottom: calc(10px + env(safe-area-inset-bottom, 0px));
  }
  
  .start-button {
    height: 44px;
    font-size: 14px;
    border-radius: 22px;
  }
}

/* High DPI displays */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .logo-icon, .start-button {
    image-rendering: -webkit-optimize-contrast;
    image-rendering: crisp-edges;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .start-view-container {
    background: #1a1a1a;
  }
  
  .bottom-section {
    background: #1a1a1a;
    border-top-color: rgba(255, 255, 255, 0.1);
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  .start-button,
  .content-card {
    transition: none;
  }
  
  .start-button:hover {
    transform: none;
  }
  
  .start-button:active {
    transform: scale(0.98);
  }
}

/* Touch optimizations */
@media (hover: none) and (pointer: coarse) {
  .start-button:hover {
    box-shadow: 0 4px 12px rgba(32, 25, 206, 0.25);
    transform: none;
  }
  
  .start-button:active {
    transform: scale(0.96);
    box-shadow: 0 2px 8px rgba(32, 25, 206, 0.4);
  }
}

/* Safe area support for different iOS versions */
@supports (padding-bottom: env(safe-area-inset-bottom)) {
  .bottom-section {
    padding-bottom: calc(16px + env(safe-area-inset-bottom));
  }
}

@supports (padding-bottom: constant(safe-area-inset-bottom)) {
  .bottom-section {
    padding-bottom: calc(16px + constant(safe-area-inset-bottom));
  }
}

/* Custom scrollbar for webkit browsers */
::-webkit-scrollbar {
  width: 0;
}

/* Telegram WebApp specific optimizations */
* {
  -webkit-tap-highlight-color: transparent;
}

body {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Performance optimizations */
.content-card,
.start-button {
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}
</style>
