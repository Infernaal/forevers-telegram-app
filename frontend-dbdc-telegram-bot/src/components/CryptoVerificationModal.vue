<template>
  <Transition
    name="modal"
    enter-active-class="transition-all duration-300 ease-out"
    leave-active-class="transition-all duration-200 ease-in"
    enter-from-class="opacity-0"
    enter-to-class="opacity-100"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
  >
    <div v-if="isVisible" class="fixed inset-0 z-[99999] bg-black/30 backdrop-blur-sm flex items-center justify-center px-4" @click.self="emit('close')">
      <div class="bg-white rounded-[20px] shadow-xl font-montserrat w-full max-w-[347px] mx-auto p-6 flex flex-col items-center text-center">
        <div class="w-12 h-12 rounded-full border-4 border-[#2019CE]/15 border-t-[#2019CE] animate-spin mb-4"></div>
        <h2 class="text-lg font-bold text-[#292727] mb-2">Processing payment</h2>
        <p class="text-sm text-[#4B4D50] leading-5">
          We are checking the transaction, please wait for the credit within 5–10 minutes.
        </p>
      </div>
    </div>
  </Transition>
</template>

<script setup>
const props = defineProps({
  isVisible: { type: Boolean, default: false }
})
const emit = defineEmits(['close'])
</script>

<style scoped>
.modal-enter-active { transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
.modal-leave-active { transition: all 0.2s cubic-bezier(0.4, 0, 0.6, 1); }
.modal-enter-from, .modal-leave-to { opacity: 0; transform: scale(0.98) translateY(6px); }
</style>
