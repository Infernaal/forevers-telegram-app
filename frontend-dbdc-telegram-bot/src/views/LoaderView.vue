<template>
  <Loader
    :title="loaderTitle"
    :description="loaderDescription"
    :duration="5000"
    :auto-complete="true"
    @complete="handleComplete"
  />
</template>

<script setup>
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import Loader from '../components/Loader.vue'

const router = useRouter()
const route = useRoute()

// Get redirect target from query parameter, default to account-check
const redirectTo = computed(() => {
  return route.query.redirect || '/account-check'
})

// Get custom title and description based on redirect target
const loaderTitle = computed(() => {
  switch (redirectTo.value) {
    case '/favorites':
      return 'Authenticating...'
    default:
      return 'Welcome to'
  }
})

const loaderDescription = computed(() => {
  switch (redirectTo.value) {
    case '/favorites':
      return 'Setting up your Telegram account access'
    default:
      return 'Please wait a little, while we prepare everything for you'
  }
})

// Handle completion from Loader component
const handleComplete = () => {
  router.push(redirectTo.value)
}
</script>
