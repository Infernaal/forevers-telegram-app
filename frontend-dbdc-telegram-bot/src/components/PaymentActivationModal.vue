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
    <div v-if="isVisible" class="fixed inset-0 z-[99999] flex items-center justify-center bg-black bg-opacity-20 backdrop-blur-md px-4" @click.self="emit('later')">
      <div @click.stop class="relative bg-white rounded-[20px] shadow-xl font-montserrat w-full max-w-[360px] mx-auto p-6">
        <!-- Header -->
        <div class="flex items-center justify-between mb-4">
          <div class="flex items-center gap-3 pr-8">
            <div class="w-8 h-8 aspect-square shrink-0 bg-[#B3FFB6] border-2 border-[#88EF8C] rounded-full flex items-center justify-center">
              <svg class="w-4 h-4" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M26.4264 2.07621C25.183 1.40975 23.7961 2.69507 22.9831 3.45674C21.118 5.26571 19.5397 7.36031 17.7701 9.26449C15.8093 11.3591 13.992 13.4537 11.9833 15.5007C10.8355 16.6433 9.5921 17.881 8.8269 19.3091C7.10521 17.6429 5.62264 15.8339 3.70964 14.3582C2.32272 13.3109 0.0271294 12.5493 0.0749543 15.0723C0.170604 18.3571 3.08792 21.8798 5.24004 24.1172C6.14871 25.0692 7.34433 26.0689 8.73125 26.1165C10.4051 26.2118 12.1268 24.2124 13.1311 23.1175C14.9007 21.2133 16.3355 19.071 17.9614 17.1193C20.0657 14.5487 22.2179 12.0255 24.2743 9.4073C25.5656 7.78875 29.6307 3.78989 26.4264 2.07621ZM2.17917 14.8819C2.13134 14.8819 2.08352 14.8819 1.98787 14.9294C1.79657 14.8819 1.6531 14.8342 1.4618 14.739C1.60527 14.6438 1.8444 14.6914 2.17917 14.8819Z" fill="#07B80E"/>
              </svg>
            </div>
            <div>
              <h2 class="text-lg font-extrabold text-[#292727] leading-tight">Congratulations!</h2>
            </div>
          </div>
          <button class="w-8 h-8 flex items-center justify-center text-[#7E7E7E] hover:text-[#4B4D50]" @click="emit('later')">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6L6 18"/><path d="M6 6l12 12"/></svg>
          </button>
        </div>
        <div class="h-px bg-[#E5E7EB] my-2"></div>

        <div class="text-[#4B4D50] space-y-3">
          <p class="leading-relaxed font-semibold">Your payment has been successfully processed.</p>
          <p class="leading-relaxed">
            Your purchased <span class="font-semibold">Dubadu Forevers</span> are now in your account.
          </p>
          <p>
            However, access and participation in the loyalty program are <span class="font-semibold">not yet activated</span>.
          </p>
          <p>To start using the product and receive monthly bonuses — please proceed with activation.</p>

          <div class="mt-3 p-3 rounded-xl border border-[#E5E7EB] bg-[#FAFAFA] space-y-1">
            <div class="text-sm text-[#4B4D50]"><span class="font-medium">ID:</span> <span class="break-all">{{ depositId }}</span></div>
            <div class="text-sm text-[#4B4D50]"><span class="font-medium">Date:</span> {{ formattedDate }}</div>
          </div>
        </div>

        <div class="mt-6 flex items-center gap-3">
          <button @click="emit('proceed')" class="flex-1 h-11 px-4 rounded-full bg-gradient-to-r from-[#2019CE] to-[#473FFF] text-white text-sm font-bold hover:opacity-90">PROCEED TO ACTIVATION</button>
          <button @click="emit('later')" class="h-11 px-5 rounded-full bg-[#FF6800] text-white text-sm font-bold hover:opacity-90">LATER</button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  isVisible: { type: Boolean, default: false },
  depositId: { type: String, default: '' },
  date: { type: [String, Number, Date], default: null }
})

const emit = defineEmits(['proceed', 'later'])

const formattedDate = computed(() => {
  if (!props.date) return ''
  const d = new Date(props.date)
  const yyyy = d.getFullYear()
  const mm = String(d.getMonth() + 1).padStart(2, '0')
  const dd = String(d.getDate()).padStart(2, '0')
  const hh = String(d.getHours()).padStart(2, '0')
  const mi = String(d.getMinutes()).padStart(2, '0')
  const ss = String(d.getSeconds()).padStart(2, '0')
  return `${yyyy}-${mm}-${dd} ${hh}:${mi}:${ss}`
})
</script>

<style scoped>
@media (max-width: 375px) {
  .max-w-\[360px\] { max-width: calc(100vw - 32px) !important; }
}

.modal-enter-active { transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
.modal-leave-active { transition: all 0.2s cubic-bezier(0.4, 0, 0.6, 1); }
.modal-enter-from, .modal-leave-to { opacity: 0; transform: scale(0.95) translateY(10px); }
</style>
