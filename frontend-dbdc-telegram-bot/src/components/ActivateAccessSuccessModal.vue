<template>
  <Transition
    name="modal"
    enter-active-class="transition-all duration-300 ease-out"
    leave-active-class="transition-all duration-200 ease-in"
    enter-from-class="opacity-0 backdrop-blur-0 scale-95"
    leave-to-class="opacity-0 backdrop-blur-0 scale-95"
    enter-to-class="opacity-100 backdrop-blur-md scale-100"
    leave-from-class="opacity-100 backdrop-blur-md scale-100"
  >
    <div
      v-if="isVisible"
      class="fixed inset-0 flex items-center justify-center z-[99999] px-4"
      style="background: rgba(2, 7, 14, 0.20); backdrop-filter: blur(9px);"
      @click="close"
    >
      <div
        @click.stop
        class="relative bg-white rounded-[20px] shadow-xl font-montserrat w-full max-w-[360px] mx-auto transition-all duration-300 p-6 text-center"
      >
        <div class="flex items-start justify-between mb-2">
          <h2 class="text-xl font-semibold text-dbd-dark">Activate Access</h2>
          <button @click="close" class="w-8 h-8 rounded-full bg-dbd-off-white border border-gray-200 flex items-center justify-center">
            <div class="w-4 h-4 relative">
              <div class="absolute w-3.5 h-0.5 bg-dbd-dark rounded-full rotate-45 top-2 left-0.5"></div>
              <div class="absolute w-3.5 h-0.5 bg-dbd-dark rounded-full -rotate-45 top-2 left-0.5"></div>
            </div>
          </button>
        </div>

        <div class="flex justify-center my-3">
          <div class="w-16 h-16 rounded-xl bg-green-100 flex items-center justify-center">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
              <path d="M20 7L9 18L4 13" stroke="#16a34a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
        </div>

        <div class="text-lg font-bold text-dbd-dark tracking-wide">ACTIVATED!</div>
        <div class="mt-3 text-sm text-dbd-dark font-medium">
          Activation has been completed {{ formattedDate }}
        </div>
        <div class="mt-3 text-base text-dbd-dark font-semibold">Congratulations!</div>
        <div class="mt-4 text-xs text-dbd-gray">This window will close automatically in {{ countdown }} seconds</div>

        <div class="mt-6">
          <button
            @click="close"
            class="px-8 h-11 rounded-full bg-gradient-to-r from-[#2019CE] to-[#473FFF] text-white font-bold text-sm hover:opacity-90"
          >
            OK
          </button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, watch, computed } from 'vue'

const props = defineProps({
  isVisible: { type: Boolean, default: false },
  activatedAtMs: { type: Number, default: () => Date.now() }
})

const emit = defineEmits(['close'])

const countdown = ref(8)
let intervalId = null

const startTimer = () => {
  clearTimer()
  countdown.value = 8
  intervalId = setInterval(() => {
    countdown.value -= 1
    if (countdown.value <= 0) {
      close()
    }
  }, 1000)
}

const clearTimer = () => {
  if (intervalId) {
    clearInterval(intervalId)
    intervalId = null
  }
}

const close = () => {
  clearTimer()
  emit('close')
}

const pad = (n) => String(n).padStart(2, '0')
const formattedDate = computed(() => {
  const dt = new Date(props.activatedAtMs)
  const d = pad(dt.getDate())
  const m = pad(dt.getMonth() + 1)
  const y = dt.getFullYear()
  const hh = pad(dt.getHours())
  const mm = pad(dt.getMinutes())
  const ss = pad(dt.getSeconds())
  return `${d}.${m}.${y}, ${hh}:${mm}:${ss}`
})

watch(() => props.isVisible, (v) => {
  if (v) startTimer()
  else clearTimer()
})
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active { transition: all 0.25s cubic-bezier(0.4,0,0.2,1); }
.modal-enter-from,
.modal-leave-to { opacity: 0; transform: scale(0.96) translateY(8px); }
</style>
