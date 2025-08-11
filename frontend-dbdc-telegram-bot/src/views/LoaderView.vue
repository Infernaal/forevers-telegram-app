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
import { useRouter } from 'vue-router'
import Loader from '../components/Loader.vue'

const router = useRouter()

// Handle completion from Loader component
const handleComplete = () => {
  router.push('/account-check')
}
</script>
