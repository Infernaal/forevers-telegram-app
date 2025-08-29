<template>
  <div class="w-full mx-auto bg-gray-100 min-h-screen relative font-montserrat">
    <!-- Header (Rent Out style with Export) -->
    <div class="header-section sticky top-0 bg-gray-100 z-40 pb-2">
      <div class="h-12"></div>
      <div class="flex justify-between items-center px-4 py-3">
        <!-- Back -->
        <button @click="goBack" class="w-11 h-11 flex items-center justify-center rounded-full bg-dbd-off-white border border-gray-200 hover:bg-gray-100 transition-colors">
          <img src="https://img.icons8.com/ios-glyphs/30/4B4D50/macos-close.png" alt="Close" class="w-5 h-5" loading="lazy" decoding="async" referrerpolicy="no-referrer" />
        </button>

        <!-- Title -->
        <div class="flex-1 text-center">
          <h1 class="text-2xl font-semibold text-dbd-dark leading-tight">List of<br />Contracts</h1>
        </div>

        <!-- Export -->
        <div class="relative">
          <button
            @click="toggleExportMenu"
            :disabled="selectedContracts.length === 0"
            :class="[
              'export-btn w-32 h-13 flex items-center justify-center gap-3 rounded-full px-4 py-2.5 transition-colors',
              selectedContracts.length === 0
                ? 'bg-gray-300 border border-gray-300 cursor-not-allowed'
                : 'bg-white border border-gray-200 hover:bg-gray-50'
            ]"
          >
            <span :class="selectedContracts.length === 0 ? 'text-gray-500' : 'text-dbd-gray'" class="font-medium text-sm">Export</span>
            <img src="https://img.icons8.com/ios-glyphs/30/FF6800/export.png" alt="Export" class="w-6 h-6" loading="lazy" decoding="async" referrerpolicy="no-referrer" />
          </button>

          <div v-if="showExportMenu" class="export-dropdown">
            <div class="export-dropdown-arrow"></div>
            <div class="export-dropdown-container">
              <button @click="exportData('csv')" class="export-option">
                <div class="export-option-icon">
                  <svg width="20" height="22" viewBox="0 0 20 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7 1L2 6H5.75C6.44038 6 7 5.44037 7 4.75V1Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M2 10H18V18H2V10Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M17 10V2.22727C17 1.54945 16.4404 1 15.75 1H7L2 5.90909V10" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M2 18V19.5484C2 20.3501 2.55963 21 3.25 21H15.75C16.4404 21 17 20.3501 17 19.5484V18" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <span class="export-option-text">CSV</span>
              </button>
              <button @click="exportData('pdf')" class="export-option">
                <div class="export-option-icon">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M5.5 11v4h1a2 2 0 000-4H5.5zM10 15v-4h1.6c.77 0 1.4.63 1.4 1.4v1.2c0 .77-.63 1.4-1.4 1.4H10zM3 2h9l5 5v11a2 2 0 01-2 2H3a2 2 0 01-2-2V4a2 2 0 012-2z" fill="white"/></svg>
                </div>
                <span class="export-option-text">PDF</span>
              </button>
            </div>
          </div>
        </div>
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
          class="transaction-card bg-dbd-off-white rounded-3xl border border-gray-200 p-3 hover:bg-gray-50 transition-colors cursor-pointer"
          @click="openDetails(c)"
        >
          <!-- First row: checkbox + ID + Date -->
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center gap-2">
              <!-- Checkbox -->
              <div
                @click.stop="toggleSelection(idx)"
                :class="[
                  'w-6 h-6 border-2 rounded flex items-center justify-center cursor-pointer transition-colors',
                  selectedContracts.includes(idx)
                    ? 'bg-green-500 border-green-500'
                    : 'border-gray-400 bg-dbd-off-white hover:border-gray-500'
                ]"
              >
                <svg v-if="selectedContracts.includes(idx)" width="14" height="10" viewBox="0 0 14 10" fill="none">
                  <path d="M1 5L5 9L13 1" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Contract ID</span>
              <span class="text-sm font-semibold text-dbd-dark break-all">{{ c.txid }}</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-sm font-medium text-dbd-dark">{{ formatDate(c.processed_on).date }}</span>
              <span class="text-sm font-medium text-dbd-gray">{{ formatDate(c.processed_on).time }}</span>
            </div>
          </div>

          <!-- Label-value stack (vertical) -->
          <div class="space-y-2">
            <div class="flex items-center justify-between bg-white rounded-xl border border-gray-200 px-3 py-2">
              <span class="text-sm text-dbd-gray">Forevers</span>
              <span class="text-sm font-medium text-dbd-dark">ℱ {{ toFixed(c.forevers, 2) }}</span>
            </div>
            <div class="flex items-center justify-between bg-white rounded-xl border border-gray-200 px-3 py-2">
              <span class="text-sm text-dbd-gray">Price</span>
              <span class="text-sm font-medium text-dbd-dark">${{ toFixed(c.price, 2) }}</span>
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
              {{ c.access ? 'Activated' : 'Activate Access' }}
            </button>
            <button
              class="px-4 h-9 rounded-full text-sm font-semibold"
              :class="c.participation ? 'bg-gray-200 text-gray-700' : 'bg-gray-300 text-gray-700'"
              :disabled="c.participation"
              @click.stop="onActivateParticipation(c)"
            >
              {{ c.participation ? 'Activated' : 'Activate Loyalty' }}
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
            <img src="https://img.icons8.com/ios-glyphs/30/4B4D50/macos-close.png" alt="Close" class="w-5 h-5" loading="lazy" decoding="async" referrerpolicy="no-referrer" />
          </button>
        </div>
        <div v-if="selected" class="p-4 space-y-4 max-h-96 overflow-y-auto">
          <!-- Contract ID -->
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-purple-50 rounded-full flex items-center justify-center">
                <img src="https://img.icons8.com/ios-glyphs/20/4B4D50/key.png" alt="ID" class="w-5 h-5" loading="lazy" decoding="async" referrerpolicy="no-referrer" />
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
                <img src="https://img.icons8.com/ios-glyphs/20/4B4D50/user.png" alt="User" class="w-5 h-5" loading="lazy" decoding="async" referrerpolicy="no-referrer" />
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
                <img src="https://img.icons8.com/ios-glyphs/20/4B4D50/calendar--v1.png" alt="Date" class="w-5 h-5" loading="lazy" decoding="async" referrerpolicy="no-referrer" />
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
                <img src="https://img.icons8.com/ios-glyphs/20/4B4D50/money-bag.png" alt="Amount" class="w-5 h-5" loading="lazy" decoding="async" referrerpolicy="no-referrer" />
              </div>
              <span class="text-sm font-medium text-dbd-gray">Contract Amount</span>
            </div>
            <span class="text-sm font-medium text-dbd-dark">${{ toFixed(selected.paid, 2) }}</span>
          </div>
          <div class="h-px bg-gray-200"></div>

          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-green-50 rounded-full flex items-center justify-center">
                <img src="https://img.icons8.com/ios-glyphs/20/4B4D50/stack-of-coins.png" alt="Forevers" class="w-5 h-5" loading="lazy" decoding="async" referrerpolicy="no-referrer" />
              </div>
              <span class="text-sm font-medium text-dbd-gray">Forevers Amount</span>
            </div>
            <span class="text-sm font-medium text-dbd-dark">{{ toFixed(selected.forevers, 2) }}</span>
          </div>
          <div class="h-px bg-gray-200"></div>

          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-purple-50 rounded-full flex items-center justify-center">
                <img src="https://img.icons8.com/ios-glyphs/20/4B4D50/combo-chart--v1.png" alt="Rate" class="w-5 h-5" loading="lazy" decoding="async" referrerpolicy="no-referrer" />
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

// Export & selection
const selectedContracts = ref([])
const showExportMenu = ref(false)

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

const toggleSelection = (index) => {
  const i = selectedContracts.value.indexOf(index)
  if (i > -1) {
    selectedContracts.value.splice(i, 1)
    if (selectedContracts.value.length === 0) showExportMenu.value = false
  } else {
    selectedContracts.value.push(index)
  }
}

const toggleExportMenu = () => {
  if (selectedContracts.value.length > 0) showExportMenu.value = !showExportMenu.value
}

const exportData = (format) => {
  const data = selectedContracts.value.map(i => contracts.value[i])
  if (format === 'csv') exportToCSV(data)
  if (format === 'pdf') exportToPDF(data)
  showExportMenu.value = false
}

const exportToCSV = (data) => {
  const headers = ['Contract ID','Date','Time','Forevers','Price','Type','Paid','Access','Participation']
  const csvContent = [
    headers.join(','),
    ...data.map(d => [
      d.txid,
      formatDate(d.processed_on).date,
      formatDate(d.processed_on).time,
      d.forevers,
      d.price,
      d.type,
      d.paid,
      d.access ? 'yes' : 'no',
      d.participation ? 'yes' : 'no'
    ].join(','))
  ].join('\n')
  const blob = new Blob([csvContent], { type: 'text/csv' })
  const url = window.URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'contracts.csv'
  a.click()
  window.URL.revokeObjectURL(url)
}

const exportToPDF = (data) => {
  console.log('Export PDF', data)
  alert('PDF export would be generated here')
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

const onActivateAccess = (c) => { console.log('Activate access clicked for', c.txid) }
const onActivateParticipation = (c) => { console.log('Activate loyalty clicked for', c.txid) }

onMounted(() => { fetchContracts(); fetchUser() })
</script>

<style scoped>
@keyframes slide-up { from { transform: translateY(100%); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
.animate-slide-up { animation: slide-up 0.3s ease-out; }

/* Card hover like Rent Out */
.transaction-card { box-shadow: 2px 4px 12px rgba(0,0,0,0.04); transition: all .2s ease-in-out; }
.transaction-card:hover { transform: translateY(-1px); box-shadow: 0 6px 20px rgba(0,0,0,0.08); }

/* Export dropdown styles copied to match Rent Out */
.export-dropdown { position: absolute; right: 0; top: 100%; margin-top: 8px; z-index: 50; }
.export-dropdown-arrow { position: absolute; top: -8px; right: 40px; width: 0; height: 0; border-left: 8px solid transparent; border-right: 8px solid transparent; border-bottom: 8px solid #3A33D3; z-index: 10; }
.export-dropdown-container { width: 164px; padding: 12px; background-color: #3A33D3; border-radius: 10px; border: 1px solid #3A33D3; box-shadow: 2px 3px 6px 0 #3A33D3; display: flex; flex-direction: column; gap: 8px; }
.export-option { width: 140px; height: 52px; background: #3A33D3; border: 1px solid #3A33D3; border-radius: 100px; display: flex; align-items: center; gap: 12px; padding: 6px; cursor: pointer; transition: all .2s ease; }
.export-option:hover { background: #2A1FB5; }
.export-option-icon { width: 40px; height: 40px; background: rgba(64,64,64,.24); border: 1px solid white; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.export-option-text { font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif; font-weight: 400; font-size: 16px; color: #FAFAFA; line-height: 26px; }
</style>
