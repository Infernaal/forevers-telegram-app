<template>
  <Transition name="api-route-error-fade">
    <div v-if="visible" class="fixed left-1/2 -translate-x-1/2 z-[11000] px-4 w-full flex justify-center pointer-events-none" :style="{ bottom: computedBottom }">
      <div class="pointer-events-auto flex items-start gap-3 rounded-2xl px-4 py-3 shadow-lg border border-red-600/70 bg-red-600 text-white w-full max-w-[420px] font-montserrat relative overflow-hidden">
        <div class="mt-0.5 flex-shrink-0 w-7 h-7 rounded-full bg-white/15 flex items-center justify-center border border-white/20">
          <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M19.7408 16.2967L11.1162 1.64545C10.6472 0.784823 9.35324 0.784859 8.88114 1.6455C8.88114 1.64545 0.256622 16.2967 0.256622 16.2967C-0.427786 17.3687 0.337271 19.0391 1.60051 18.9993C1.60046 18.9993 18.3969 18.9993 18.3969 18.9993C19.6579 19.0374 20.4321 17.3725 19.7408 16.2967ZM8.86009 15.8781C9.15379 14.4507 11.1404 14.6596 11.1618 16.1205C11.0791 17.9021 8.59938 17.6324 8.86009 15.8781ZM11.1618 12.4632C11.1221 14.0415 8.87825 14.0442 8.83553 12.4631V6.86705C8.87991 5.28892 11.119 5.28691 11.1618 6.86707C11.1618 6.86705 11.1618 12.4632 11.1618 12.4632Z" fill="#FAFAFA"/>
          </svg>
        </div>
        <div class="flex-1 min-w-0">
          <div class="text-xs leading-snug font-semibold opacity-95 break-words whitespace-normal" v-html="message"></div>
          <div v-if="debugInfo" class="mt-1 text-[10px] opacity-60 select-text">{{ debugInfo }}</div>
        </div>
        <button class="absolute top-1.5 right-1.5 w-5 h-5 flex items-center justify-center rounded-full hover:bg-white/15 active:scale-95 transition" @click="hide" aria-label="Close">
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 3L11 11M11 3L3 11" stroke="#FFFFFF" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <div class="absolute left-0 bottom-0 h-0.5 bg-white/30" :style="{ width: progress + '%' }"></div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { computed, onMounted, onBeforeUnmount, ref, watch } from 'vue'
import { useApiErrorNotifier } from '../composables/useApiErrorNotifier.js'

const { visible, message, routeKey, status, timestamp, hide } = useApiErrorNotifier()
const TTL = 5000
const progress = ref(100)
let rafId = null

function anim() {
  const elapsed = Date.now() - timestamp.value
  const pct = 100 - (elapsed / TTL) * 100
  progress.value = Math.max(0, Math.min(100, pct))
  if (pct > 0 && visible.value) {
    rafId = requestAnimationFrame(anim)
  }
}

watch(() => visible.value, v => {
  if (v) {
    progress.value = 100
    if (rafId) cancelAnimationFrame(rafId)
    rafId = requestAnimationFrame(anim)
  } else if (rafId) {
    cancelAnimationFrame(rafId)
    rafId = null
  }
})

onMounted(() => { if (visible.value) anim() })
onBeforeUnmount(() => { if (rafId) cancelAnimationFrame(rafId) })

const computedBottom = computed(() => 'max(120px, calc(120px + var(--tg-content-safe-area-inset-bottom, 0px)))')
const debugInfo = computed(() => {
  if (import.meta.env.DEV && status.value) {
    return `${routeKey.value || ''} • status ${status.value}`
  }
  return ''
})
</script>

<style scoped>
.api-route-error-fade-enter-active, .api-route-error-fade-leave-active { transition: all .35s cubic-bezier(0.4,0,0.2,1); }
.api-route-error-fade-enter-from { opacity: 0; transform: translate(-50%, 16px) scale(.95); }
.api-route-error-fade-leave-to { opacity: 0; transform: translate(-50%, -8px) scale(.95); }
</style>
