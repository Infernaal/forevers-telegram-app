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
        <div class="flex items-start justify-between mb-2 relative">
          <h2 class="text-xl font-semibold text-dbd-dark">{{ title }}</h2>
          <button @click="close" class="w-8 h-8 rounded-full bg-dbd-off-white border border-gray-200 flex items-center justify-center absolute -top-3 -right-3 shadow">
            <div class="w-4 h-4 relative">
              <div class="absolute w-3.5 h-0.5 bg-dbd-dark rounded-full rotate-45 top-2 left-0.5"></div>
              <div class="absolute w-3.5 h-0.5 bg-dbd-dark rounded-full -rotate-45 top-2 left-0.5"></div>
            </div>
          </button>
        </div>

        <div class="flex justify-center my-3">
          <div class="w-16 h-16 rounded-r-full border-2 border-[#88EF8C] bg-[#B3FFB6] flex items-center justify-center">
            <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
              <g clip-path="url(#clip0_success_tick)">
                <path d="M26.4264 2.07621C25.183 1.40975 23.7961 2.69507 22.9831 3.45674C21.118 5.26571 19.5397 7.36031 17.7701 9.26449C15.8093 11.3591 13.992 13.4537 11.9833 15.5007C10.8355 16.6433 9.5921 17.881 8.8269 19.3091C7.10521 17.6429 5.62264 15.8339 3.70964 14.3582C2.32272 13.3109 0.0271294 12.5493 0.0749543 15.0723C0.170604 18.3571 3.08792 21.8798 5.24004 24.1172C6.14871 25.0692 7.34433 26.0689 8.73125 26.1165C10.4051 26.2118 12.1268 24.2124 13.1311 23.1175C14.9007 21.2133 16.3355 19.071 17.9614 17.1193C20.0657 14.5487 22.2179 12.0255 24.2743 9.4073C25.5656 7.78875 29.6307 3.78989 26.4264 2.07621ZM2.17917 14.8819C2.13134 14.8819 2.08352 14.8819 1.98787 14.9294C1.79657 14.8819 1.6531 14.8342 1.4618 14.739C1.60527 14.6438 1.8444 14.6914 2.17917 14.8819Z" fill="#07B80E"/>
              </g>
              <defs>
                <clipPath id="clip0_success_tick">
                  <rect width="27.5556" height="27.4286" fill="white" transform="translate(0.0742188 0.289062)"/>
                </clipPath>
              </defs>
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
  activatedAtMs: { type: Number, default: () => Date.now() },
  title: { type: String, default: 'Activate Access' }
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
