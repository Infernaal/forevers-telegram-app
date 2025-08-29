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
      @click="onCancel"
    >
      <div
        @click.stop
        class="relative bg-white rounded-[20px] shadow-xl font-montserrat w-full max-w-[480px] mx-auto transition-all duration-300 p-6"
      >
        <div class="flex items-start justify-between mb-2">
          <h2 class="text-xl font-semibold text-dbd-dark">Loyalty Program Activation</h2>
          <button @click="onCancel" class="w-8 h-8 rounded-full bg-dbd-off-white border border-gray-200 flex items-center justify-center">
            <div class="w-4 h-4 relative">
              <div class="absolute w-3.5 h-0.5 bg-dbd-dark rounded-full rotate-45 top-2 left-0.5"></div>
              <div class="absolute w-3.5 h-0.5 bg-dbd-dark rounded-full -rotate-45 top-2 left-0.5"></div>
            </div>
          </button>
        </div>

        <div class="text-[15px] text-[#292727] leading-7">
          <p class="mb-4">
            By activating my participation in the Loyalty Program, I confirm my voluntary, informed, and explicit consent to the transfer of my personal data from DBD Capital LLC to DUBADU PORTAL LLC for the proper provision of services within the Loyalty Program.
          </p>
          <p class="mb-4">
            I understand that my personal data will be processed in accordance with applicable laws, strictly within the companies’ authority, and will not be shared with third parties without my separate explicit consent.
          </p>
          <p class="mb-2">I also confirm my full agreement with:</p>
          <ul class="list-disc pl-5 space-y-1">
            <li>
              <a href="https://2-dbd-dev.dubadu.com/uploads/docs/03_ENG_DUBADU_FOREVERS_LOYALTY_PROGRAM.pdf" target="_blank" rel="noopener noreferrer" class="text-[#2019CE] underline">the terms of the Loyalty Program</a>
            </li>
            <li>
              <a href="https://2-dbd-dev.dubadu.com/uploads/docs/02_ENG_DUBADU_FOREVERS_COMMISSION_POLICY.pdf" target="_blank" rel="noopener noreferrer" class="text-[#2019CE] underline">the Dubadu Forevers Commission Policy</a>
            </li>
          </ul>
        </div>

        <div class="flex items-center gap-3 mt-6">
          <button
            @click="onConfirm"
            class="flex-1 h-11 rounded-full bg-gradient-to-r from-[#2019CE] to-[#473FFF] text-white font-bold text-sm hover:opacity-90"
          >
            ACTIVATE ACCESS
          </button>
          <button
            @click="onCancel"
            class="flex-1 h-11 rounded-full bg-[#FF6800] text-white font-bold text-sm hover:opacity-90"
          >
            CANCEL
          </button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { watch } from 'vue'

const props = defineProps({
  isVisible: { type: Boolean, default: false }
})

const emit = defineEmits(['cancel', 'confirm'])

const onCancel = () => {
  if (window.triggerHaptic) window.triggerHaptic('impact', 'light')
  emit('cancel')
}

const onConfirm = () => {
  if (window.triggerHaptic) window.triggerHaptic('notification', 'success')
  emit('confirm')
}

const handleKeyDown = (event) => {
  if (event.key === 'Escape' && props.isVisible) onCancel()
  else if (event.key === 'Enter' && props.isVisible) onConfirm()
}

watch(() => props.isVisible, (v) => {
  if (v) {
    document.addEventListener('keydown', handleKeyDown)
    document.body.style.overflow = 'hidden'
  } else {
    document.removeEventListener('keydown', handleKeyDown)
    document.body.style.overflow = ''
  }
})
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active { transition: all 0.25s cubic-bezier(0.4,0,0.2,1); }
.modal-enter-from,
.modal-leave-to { opacity: 0; transform: scale(0.96) translateY(8px); }
</style>
