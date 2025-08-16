<template>
  <div class="w-full min-h-screen bg-white font-montserrat flex flex-col items-center justify-center p-6">
    <div class="w-full max-w-[380px] rounded-3xl p-8 text-center text-white" :style="cardStyle">
      <h1 class="text-lg font-semibold mb-4">Registration Error</h1>
      <p class="text-sm leading-5 mb-6">
        Something went wrong while creating your account. This could be a temporary server issue. You can retry the registration process or return to the start.
      </p>
      <div class="flex flex-col gap-3">
        <button @click="retry" class="w-full h-12 rounded-full bg-dbd-orange font-bold hover:opacity-90 active:scale-[0.97] transition">Try Again</button>
        <button @click="goStart" class="w-full h-12 rounded-full border border-white font-semibold hover:bg-white/10 transition">Back to Start</button>
      </div>
    </div>
  </div>
</template>
<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const cardStyle = { background: 'linear-gradient(90deg, #2019CE 20.91%, #473FFF 68.93%)' }
const retry = () => router.replace('/registration')
const goStart = () => router.replace('/')
</script>
<style scoped>
* { will-change:auto }
</style>
