<template>
  <div class="w-full min-h-screen bg-white font-montserrat flex flex-col items-center justify-center p-6">
    <div class="w-full max-w-[380px] rounded-3xl p-8 text-center text-white" :style="cardStyle">
      <h1 class="text-lg font-semibold mb-4">Phone Already Registered</h1>
      <p class="text-sm leading-5 mb-6">
        This phone number is already linked to an existing account. If it's yours, log in with the email attached to that phone. Otherwise, use a different phone number.
      </p>
      <div class="flex flex-col gap-3">
        <button @click="goStart" class="w-full h-12 rounded-full bg-dbd-orange font-bold hover:opacity-90 active:scale-[0.97] transition">Back to Start</button>
        <button @click="retry" class="w-full h-12 rounded-full border border-white font-semibold hover:bg-white/10 transition">Try Another Phone</button>
      </div>
    </div>
  </div>
</template>
<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const cardStyle = { background: 'linear-gradient(90deg, #2019CE 20.91%, #473FFF 68.93%)' }
const goStart = () => router.replace('/')
const retry = () => router.replace('/registration')
</script>
<style scoped>
* { will-change:auto }
</style>
