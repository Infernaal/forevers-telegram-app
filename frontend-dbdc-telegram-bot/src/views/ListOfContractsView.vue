<template>
  <div class="w-full mx-auto bg-gray-100 min-h-screen relative font-montserrat">
    <!-- Header -->
    <div class="sticky top-0 bg-gray-100 z-40 pb-2">
      <div class="h-12"></div>
      <div class="flex justify-between items-center px-4 py-3">
        <button @click="goBack" class="w-11 h-11 flex items-center justify-center rounded-full bg-dbd-off-white border border-gray-200 hover:bg-gray-100 transition-colors">
          <div class="w-5 h-5 relative">
            <div class="absolute w-4 h-0.5 bg-dbd-dark rounded-full rotate-45 top-2.5 left-0.5"></div>
            <div class="absolute w-4 h-0.5 bg-dbd-dark rounded-full -rotate-45 top-2.5 left-0.5"></div>
          </div>
        </button>
        <div class="flex-1 text-center">
          <h1 class="text-2xl font-semibold text-dbd-dark leading-tight">List of Contracts</h1>
        </div>
        <div class="w-11"></div>
      </div>
    </div>

    <!-- Content -->
    <div class="bg-gray-100 px-4 pb-32">
      <!-- Empty -->
      <div v-if="contracts.length === 0" class="flex flex-col items-center justify-center text-center" style="min-height: calc(100vh - 200px);">
        <h2 class="text-xl font-bold text-dbd-dark mb-4 leading-tight max-w-60">No contracts yet</h2>
        <p class="text-base font-medium text-dbd-gray leading-relaxed max-w-72">Your contracts will appear here once you make a purchase.</p>
      </div>

      <!-- List -->
      <div v-else class="space-y-2 pt-4">
        <div
          v-for="(c, idx) in contracts"
          :key="idx"
          class="bg-dbd-off-white rounded-3xl border border-gray-200 p-3 hover:bg-gray-50 transition-colors cursor-pointer"
          @click="openDetails(c)"
        >
          <!-- First row: ID + Date -->
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center gap-2">
              <span class="text-sm font-medium text-dbd-gray">Contract ID</span>
              <span class="text-sm font-semibold text-dbd-dark break-all">{{ c.txid }}</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-sm font-medium text-dbd-dark">{{ formatDate(c.processed_on).date }}</span>
              <span class="text-sm font-medium text-dbd-gray">{{ formatDate(c.processed_on).time }}</span>
            </div>
          </div>

          <!-- Grid like table (mobile-friendly) -->
          <div class="grid grid-cols-2 gap-2 sm:grid-cols-4">
            <div class="flex items-center justify-between bg-white rounded-xl border border-gray-200 px-3 py-2">
              <span class="text-sm text-dbd-gray">Forevers</span>
              <span class="text-sm font-medium text-dbd-dark">ℱ {{ toFixed(c.forevers, 2) }}</span>
            </div>
            <div class="flex items-center justify-between bg-white rounded-xl border border-gray-200 px-3 py-2">
              <span class="text-sm text-dbd-gray">Price</span>
              <span class="text-sm font-medium text-dbd-blue">${{ toFixed(c.price, 2) }}</span>
            </div>
            <div class="flex items-center justify-between bg-white rounded-xl border border-gray-200 px-3 py-2">
              <span class="text-sm text-dbd-gray">Type</span>
              <div class="flex items-center gap-2">
                <CountryFlag :country="c.type" size="small" />
                <span class="text-sm font-medium text-dbd-dark">{{ c.type }}</span>
              </div>
            </div>
            <div class="flex items-center justify-between bg-white rounded-xl border border-gray-200 px-3 py-2">
              <span class="text-sm text-dbd-gray">Paid</span>
              <span class="text-sm font-medium text-dbd-dark">${{ toFixed(c.paid, 2) }}</span>
            </div>
          </div>

          <!-- Actions row -->
          <div class="flex items-center gap-2 mt-3">
            <button
              class="px-4 h-9 rounded-full text-sm font-semibold"
              :class="c.access ? 'bg-green-100 text-green-700' : 'bg-green-600 text-white'"
              @click.stop="onActivateAccess(c)"
            >
              {{ c.access ? 'Activated' : 'Activate' }}
            </button>
            <button
              class="px-4 h-9 rounded-full text-sm font-semibold"
              :class="c.participation ? 'bg-gray-200 text-gray-700' : 'bg-gray-300 text-gray-700'"
              :disabled="c.participation"
              @click.stop="onActivateParticipation(c)"
            >
              {{ c.participation ? 'Activated' : 'Activate' }}
            </button>
            <div class="ml-auto text-xs text-dbd-gray">Tap card to view details</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Navigation -->
    <BottomNavigation />

    <!-- Contract Details Modal (bottom sheet) -->
    <div v-if="showDetails" class="fixed inset-0 z-[10001] flex items-end justify-center bg-black bg-opacity-20 backdrop-blur-sm">
      <div class="w-full bg-white rounded-t-3xl shadow-xl animate-slide-up">
        <div class="flex items-center justify-between p-4 border-b">
          <h2 class="text-base font-medium text-dbd-dark">Contract Details</h2>
          <button @click="closeDetails" class="w-11 h-11 flex items-center justify-center rounded-full bg-dbd-off-white border border-gray-200">
            <div class="w-5 h-5 relative">
              <div class="absolute w-4 h-0.5 bg-dbd-dark rounded-full rotate-45 top-2.5 left-0.5"></div>
              <div class="absolute w-4 h-0.5 bg-dbd-dark rounded-full -rotate-45 top-2.5 left-0.5"></div>
            </div>
          </button>
        </div>
        <div v-if="selected" class="p-4 space-y-4 max-h-96 overflow-y-auto">
          <!-- Contract ID -->
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-purple-50 rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M14.168 3.75448C15.1859 3.82121 15.9909 4.66789 15.9909 5.70304V15.8918C15.9909 16.9706 15.1165 17.845 14.0378 17.845H5.96484C4.88607 17.845 4.01172 16.9706 4.01172 15.8918V5.70304C4.01172 4.66789 4.81673 3.82121 5.83464 3.75448" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round"/></svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Contract ID</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-sm font-medium text-dbd-dark break-all">{{ selected.txid }}</span>
              <button @click="copy(selected.txid)" class="px-3 py-1 rounded-full border border-dbd-blue text-dbd-blue text-sm bg-white">Copy</button>
            </div>
          </div>
          <div class="h-px bg-gray-200"></div>

          <!-- Full Name -->
          <div v-if="userFullName" class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-green-50 rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M10 10a4 4 0 100-8 4 4 0 000 8zM2 18a8 8 0 1116 0H2z" fill="#4B4D50"/></svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Full Name</span>
            </div>
            <span class="text-sm font-medium text-dbd-dark">{{ userFullName }}</span>
          </div>
          <div class="h-px bg-gray-200" v-if="userFullName"></div>

          <!-- Date -->
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-dbd-light-orange rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M15.5 3.25H4.5A2.5 2.5 0 002 5.75v9.75A2.5 2.5 0 004.5 18h11a2.5 2.5 0 002.5-2.5V5.75A2.5 2.5 0 0015.5 3.25Z" fill="#4B4D50"/></svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Date</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-sm font-medium text-dbd-dark">{{ formatDate(selected.processed_on).date }}</span>
              <span class="text-sm font-medium text-dbd-gray">{{ formatDate(selected.processed_on).time }}</span>
            </div>
          </div>
          <div class="h-px bg-gray-200"></div>

          <!-- Amounts -->
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-green-50 rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="8" stroke="#4B4D50"/><path d="M10 5v10M7 8h6M7 12h6" stroke="#4B4D50"/></svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Contract Amount</span>
            </div>
            <span class="text-sm font-medium text-dbd-dark">${{ toFixed(selected.paid, 2) }}</span>
          </div>
          <div class="h-px bg-gray-200"></div>

          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-green-50 rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M4 10h12" stroke="#4B4D50"/><path d="M10 4v12" stroke="#4B4D50"/></svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Forevers Amount</span>
            </div>
            <span class="text-sm font-medium text-dbd-dark">{{ toFixed(selected.forevers, 2) }}</span>
          </div>
          <div class="h-px bg-gray-200"></div>

          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-purple-50 rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M2 10h16" stroke="#4B4D50"/><path d="M10 2v16" stroke="#4B4D50"/></svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Rate at Deposit</span>
            </div>
            <span class="text-sm font-medium text-dbd-dark">${{ toFixed(selected.price, 2) }}</span>
          </div>
          <div class="h-px bg-gray-200"></div>

          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <CountryFlag :country="selected.type" size="small" />
              <span class="text-sm font-medium text-dbd-gray">Forevers Type</span>
            </div>
            <span class="text-sm font-medium text-dbd-dark">{{ selected.type }}</span>
          </div>

          <!-- Activate buttons -->
          <div class="mt-2 grid grid-cols-2 gap-2">
            <button class="h-10 rounded-full text-sm font-semibold" :class="selected.access ? 'bg-green-100 text-green-700' : 'bg-green-600 text-white'" @click="onActivateAccess(selected)">{{ selected.access ? 'Activated' : 'Activate Access' }}</button>
            <button class="h-10 rounded-full text-sm font-semibold" :class="selected.participation ? 'bg-gray-200 text-gray-700' : 'bg-gray-300 text-gray-700'" :disabled="selected.participation" @click="onActivateParticipation(selected)">{{ selected.participation ? 'Activated' : 'Activate Loyalty' }}</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import BottomNavigation from '../components/BottomNavigation.vue'
import CountryFlag from '../components/CountryFlag.vue'
import DepositsService from '../services/depositsService.js'
import telegramUserService from '../services/telegramUserService.js'

const router = useRouter()
const contracts = ref([])
const showDetails = ref(false)
const selected = ref(null)
const userInfo = ref(null)

const goBack = () => router.push('/wallet')

const fetchContracts = async () => {
  const res = await DepositsService.getUserDeposits()
  if (res.status === 'success') {
    contracts.value = (res.data?.deposits || []).slice().sort((a,b) => new Date(b.processed_on||0) - new Date(a.processed_on||0))
  } else {
    contracts.value = []
  }
}

const fetchUser = async () => {
  const res = await telegramUserService.getUserInfo()
  if (res.status === 'success') userInfo.value = res.data
}

const openDetails = (c) => { selected.value = c; showDetails.value = true }
const closeDetails = () => { showDetails.value = false; selected.value = null }

const formatDate = (d) => {
  const dt = new Date(d || Date.now())
  const pad = (n) => String(n).padStart(2, '0')
  return { date: `${pad(dt.getDate())}.${pad(dt.getMonth()+1)}.${dt.getFullYear()}`, time: `${pad(dt.getHours())}:${pad(dt.getMinutes())}:${pad(dt.getSeconds())}` }
}

const toFixed = (v, n=2) => {
  const num = typeof v === 'number' ? v : parseFloat(v || 0)
  return num.toLocaleString(undefined, { minimumFractionDigits: n, maximumFractionDigits: n })
}

const userFullName = computed(() => userInfo.value?.full_name || '')

const copy = async (text) => {
  try {
    if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(text)
    else {
      const ta = document.createElement('textarea'); ta.value = text; ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); document.body.removeChild(ta)
    }
  } catch (_) {}
}

const onActivateAccess = (c) => {
  // Placeholder for future API; keep UI consistent
  console.log('Activate access clicked for', c.txid)
}
const onActivateParticipation = (c) => { console.log('Activate loyalty clicked for', c.txid) }

onMounted(() => {
  fetchContracts()
  fetchUser()
})
</script>

<style scoped>
@keyframes slide-up { from { transform: translateY(100%); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
.animate-slide-up { animation: slide-up 0.3s ease-out; }
</style>
