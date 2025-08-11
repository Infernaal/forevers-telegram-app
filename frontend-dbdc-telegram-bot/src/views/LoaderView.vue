<template>
  <Loader
    title="Welcome to"
    description="Please wait a little, while we prepare everything for you"
    :duration="5000"
    :auto-complete="true"
    @complete="handleComplete"
  />
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// Auto-redirect to AccountCheckView after 5 seconds
onMounted(() => {
  setTimeout(() => {
    router.push('/account-check')
  }, 5000) // 5 seconds
})

// Computed style for the gradient card background
const cardStyle = {
  background: `
    linear-gradient(0deg, rgba(0, 0, 0, 0.25) 0%, rgba(0, 0, 0, 0.25) 100%),
    linear-gradient(90deg, #2019CE 20.91%, #473FFF 68.93%)
  `
}
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
:::-webkit-scrollbar {
  width: 0;
}

* {
  -webkit-tap-highlight-color: transparent;
  scrollbar-width: none;
  -ms-overflow-style: none;
}
</style>
