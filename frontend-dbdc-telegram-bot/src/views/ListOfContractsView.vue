<template>
  <div class="w-full mx-auto bg-gray-100 h-screen overflow-y-auto scrollbar-hide relative font-montserrat">
    <!-- Header (Rent Out style with Export) -->
    <div class="header-section sticky top-0 bg-gray-100 z-40 pb-2">
      <div class="h-4"></div>
      <div class="flex justify-between items-center px-4 py-3">
        <!-- Back -->
        <button @click="goBack" class="w-11 h-11 flex items-center justify-center rounded-full bg-dbd-off-white border border-gray-200 hover:bg-gray-100 transition-colors">
          <div class="w-5 h-5 relative">
            <div class="absolute w-4 h-0.5 bg-dbd-dark rounded-full rotate-45 top-2.5 left-0.5"></div>
            <div class="absolute w-4 h-0.5 bg-dbd-dark rounded-full -rotate-45 top-2.5 left-0.5"></div>
          </div>
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
            <svg width="32" height="32" viewBox="0 0 33 33" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M24.4294 12.4709H20.4441V14.7762H24.4294C25.6145 14.7762 26.5339 15.3663 26.5339 15.8742V26.0964C26.5339 26.6043 25.6145 27.1945 24.4294 27.1945H9.3657C8.18061 27.1945 7.26115 26.6043 7.26115 26.0964V15.8746C7.26115 15.3667 8.18061 14.7766 9.3657 14.7766H13.3502V12.4713H9.3657C6.85955 12.4713 4.89648 13.9663 4.89648 15.8746V26.0968C4.89648 28.0055 6.85955 29.5001 9.3657 29.5001H24.4298C26.9355 29.5001 28.899 28.0051 28.899 26.0968V15.8746C28.8986 13.9659 26.9355 12.4709 24.4294 12.4709Z" fill="#FF6800"/>
              <path d="M13.3976 9.24579C13.7002 9.24579 14.0025 9.13322 14.2335 8.90807L15.7138 7.465V12.4704V14.7757V19.1917C15.7138 19.8283 16.243 20.3443 16.8961 20.3443C17.5491 20.3443 18.0784 19.8283 18.0784 19.1917V14.7757V12.4704V7.387L19.6387 8.90807C19.8696 9.13322 20.1723 9.24579 20.4746 9.24579C20.7769 9.24579 21.0796 9.13322 21.3105 8.90807C21.7724 8.45817 21.7724 7.72818 21.3105 7.27827L17.7805 3.83695C17.5495 3.6118 17.2472 3.5 16.945 3.5C16.9418 3.5 16.939 3.5 16.9359 3.5C16.9327 3.5 16.93 3.5 16.9268 3.5C16.6245 3.5 16.3223 3.6118 16.0913 3.83695L12.5613 7.27827C12.0994 7.72818 12.0994 8.45817 12.5613 8.90807C12.7926 9.13322 13.0949 9.24579 13.3976 9.24579Z" fill="#FF6800"/>
            </svg>
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
          <!-- First row: checkbox + Date & Time -->
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center gap-2">
              <!-- Checkbox -->
              <div
                @click.stop="toggleSelection(idx)"
                :class="[
                  'w-6 h-6 aspect-square shrink-0 border-2 rounded flex items-center justify-center cursor-pointer transition-colors',
                  selectedContracts.includes(idx)
                    ? 'bg-green-500 border-green-500'
                    : 'border-gray-400 bg-dbd-off-white hover:border-gray-500'
                ]"
              >
                <svg v-if="selectedContracts.includes(idx)" width="14" height="10" viewBox="0 0 14 10" fill="none">
                  <path d="M1 5L5 9L13 1" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <!-- Calendar icon + label -->
              <div class="w-10 h-10 bg-dbd-light-orange rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M14.0615 9.1875C14.4067 9.1875 14.6865 8.90768 14.6865 8.5625C14.6865 8.21732 14.4067 7.9375 14.0615 7.9375C13.7163 7.9375 13.4365 8.21732 13.4365 8.5625C13.4365 8.90768 13.7163 9.1875 14.0615 9.1875Z" fill="#4B4D50"/>
                  <path d="M15.499 3.25H14.6865V2.625C14.6865 2.27981 14.4067 2 14.0615 2C13.7163 2 13.4365 2.27981 13.4365 2.625V3.25H10.5928V2.625C10.5928 2.27981 10.313 2 9.96777 2C9.62259 2 9.34277 2.27981 9.34277 2.625V3.25H6.53027V2.625C6.53027 2.27981 6.25046 2 5.90527 2C5.56009 2 5.28027 2.27981 5.28027 2.625V3.25H4.49902C3.12052 3.25 1.99902 4.3715 1.99902 5.75V15.5C1.99902 16.8785 3.12052 18 4.49902 18H9.28027C9.62546 18 9.90527 17.7202 9.90527 17.375C9.90527 17.0298 9.62546 16.75 9.28027 16.75H4.49902C3.80977 16.75 3.24902 16.1892 3.24902 15.5V5.75C3.24902 5.06075 3.80977 4.5 4.49902 4.5H5.28027V5.125C5.28027 5.47019 5.56009 5.75 5.90527 5.75C6.25046 5.75 6.53027 5.47019 6.53027 5.125V4.5H9.34277V5.125C9.34277 5.47019 9.62259 5.75 9.96777 5.75C10.313 5.75 10.5928 5.47019 10.5928 5.125V4.5H13.4365V5.125C13.4365 5.47019 13.7163 5.75 14.0615 5.75C14.4067 5.75 14.6865 5.47019 14.6865 5.125V4.5H15.499C16.1883 4.5 16.749 5.06075 16.749 5.75V9.3125C16.749 9.65769 17.0288 9.9375 17.374 9.9375C17.7192 9.9375 17.999 9.65769 17.999 9.3125V5.75C17.999 4.3715 16.8775 3.25 15.499 3.25Z" fill="#4B4D50"/>
                  <path d="M14.2178 10.4375C12.1328 10.4375 10.4365 12.1337 10.4365 14.2188C10.4365 16.3038 12.1328 18 14.2178 18C16.3028 18 17.999 16.3038 17.999 14.2188C17.999 12.1337 16.3028 10.4375 14.2178 10.4375ZM14.2178 16.75C12.8221 16.75 11.6865 15.6145 11.6865 14.2188C11.6865 12.823 12.8221 11.6875 14.2178 11.6875C15.6135 11.6875 16.749 12.823 16.749 14.2188C16.749 15.6145 15.6135 16.75 14.2178 16.75Z" fill="#4B4D50"/>
                  <path d="M15.124 13.5938H14.8428V12.9375C14.8428 12.5923 14.563 12.3125 14.2178 12.3125C13.8726 12.3125 13.5928 12.5923 13.5928 12.9375V14.2188C13.5928 14.5639 13.8726 14.8438 14.2178 14.8438H15.124C15.4692 14.8438 15.749 14.5639 15.749 14.2188C15.749 13.8736 15.4692 13.5938 15.124 13.5938Z" fill="#4B4D50"/>
                </svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Date & Time</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-sm font-medium text-dbd-dark">{{ formatDate(c.processed_on).date }}</span>
              <span class="text-sm font-medium text-dbd-gray">{{ formatDate(c.processed_on).time }}</span>
            </div>
          </div>

          <!-- Label-value stack (vertical) -->
          <div class="space-y-2">
            <div class="flex items-center justify-between bg-white rounded-xl border border-gray-200 px-3 py-2">
              <span class="text-sm text-dbd-gray">Contract ID</span>
              <span class="text-sm font-medium text-dbd-dark break-all">{{ c.txid }}</span>
            </div>
            <div class="flex items-center justify-between bg-white rounded-xl border border-gray-200 px-3 py-2">
              <span class="text-sm text-dbd-gray">Forevers</span>
              <div class="flex items-center gap-1">
                <svg class="text-dbd-dark w-4 h-4" viewBox="0 0 32 32"><path d="M30.6666 7.38069V1.33325H7.1291V9.01136H1.33325V15.0588H7.1291V30.1075H13.894V22.7276H19.6153V16.6801H13.894V15.0588H25.1316V9.01136H13.894V7.38069H30.6666Z" fill="currentColor"/></svg>
                <span class="text-sm font-medium text-dbd-dark">{{ toFixed(c.forevers, 2) }}</span>
              </div>
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

          <!-- Access (vertical label-value with action) -->
          <div class="flex items-center justify-between bg-white rounded-xl border border-gray-200 px-3 py-2 mt-2">
            <span class="text-sm text-dbd-gray">Access</span>
            <button
              class="px-3 h-8 rounded-full text-xs font-semibold"
              :class="c.access ? 'bg-green-100 text-green-700' : 'bg-green-600 text-white'"
              @click.stop="onActivateAccess(c)"
            >
              {{ c.access ? 'Activated' : 'Activate Access' }}
            </button>
          </div>
          <!-- Participation (vertical label-value with action) -->
          <div class="flex items-center justify-between bg-white rounded-xl border border-gray-200 px-3 py-2 mt-2">
            <span class="text-sm text-dbd-gray">Participation</span>
            <button
              class="px-3 h-8 rounded-full text-xs font-semibold"
              :class="(c.participation || !c.access) ? 'bg-gray-300 text-gray-700 cursor-not-allowed' : 'bg-gray-300 text-gray-700'"
              :disabled="c.participation || !c.access"
              @click.stop="openLoyaltyModal(c)"
            >
              {{ c.participation ? 'Activated' : 'Activate Loyalty' }}
            </button>
          </div>
          <div class="mt-2 text-xs text-dbd-gray">Tap card to view details</div>
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
        <div v-if="selected" class="p-4 space-y-4 max-h-96 overflow-y-auto scrollbar-hide">
          <!-- Contract ID -->
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-purple-50 rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
  <g clip-path="url(#clip0_id)">
    <path d="M11.043 13.5537H13.9076" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M11.043 9.73828H13.9076" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M6.09375 9.47806L6.61458 10.5176L7.91667 8.9583" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M6.09375 12.6009L7.39583 14.4238" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M7.39583 12.6009L6.09375 14.4238" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M14.168 3.75448C15.1859 3.82121 15.9909 4.66789 15.9909 5.70304V15.8918C15.9909 16.9706 15.1165 17.845 14.0378 17.845H5.96484C4.88607 17.845 4.01172 16.9706 4.01172 15.8918V5.70304C4.01172 4.66789 4.81673 3.82121 5.83464 3.75448" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M6.8125 5.3125H13.1927C13.732 5.3125 14.1693 4.87526 14.1693 4.33594V3.13151C14.1693 2.59219 13.732 2.15495 13.1927 2.15495H6.8125C6.27318 2.15495 5.83594 2.59219 5.83594 3.13151V4.33594C5.83594 4.87526 6.27318 5.3125 6.8125 5.3125Z" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <defs>
    <clipPath id="clip0_id">
      <rect width="20" height="20" fill="white"/>
    </clipPath>
  </defs>
</svg>
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
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M10 10.5C12.0711 10.5 13.75 8.82107 13.75 6.75C13.75 4.67893 12.0711 3 10 3C7.92893 3 6.25 4.67893 6.25 6.75C6.25 8.82107 7.92893 10.5 10 10.5Z" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M4 16.75C4.93401 14.7447 7.29077 13.5 10 13.5C12.7092 13.5 15.066 14.7447 16 16.75" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
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
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M14.0625 9.1875C14.4077 9.1875 14.6875 8.90768 14.6875 8.5625C14.6875 8.21732 14.4077 7.9375 14.0625 7.9375C13.7173 7.9375 13.4375 8.21732 13.4375 8.5625C13.4375 8.90768 13.7173 9.1875 14.0625 9.1875Z" fill="#4B4D50"/>
  <path d="M15.5 3.25H14.6875V2.625C14.6875 2.27981 14.4077 2 14.0625 2C13.7173 2 13.4375 2.27981 13.4375 2.625V3.25H10.5938V2.625C10.5938 2.27981 10.3139 2 9.96875 2C9.62356 2 9.34375 2.27981 9.34375 2.625V3.25H6.53125V2.625C6.53125 2.27981 6.25144 2 5.90625 2C5.56106 2 5.28125 2.27981 5.28125 2.625V3.25H4.5C3.1215 3.25 2 4.3715 2 5.75V15.5C2 16.8785 3.1215 18 4.5 18H9.28125C9.62644 18 9.90625 17.7202 9.90625 17.375C9.90625 17.0298 9.62644 16.75 9.28125 16.75H4.5C3.81075 16.75 3.25 16.1892 3.25 15.5V5.75C3.25 5.06075 3.81075 4.5 4.5 4.5H5.28125V5.125C5.28125 5.47019 5.56106 5.75 5.90625 5.75C6.25144 5.75 6.53125 5.47019 6.53125 5.125V4.5H9.34375V5.125C9.34375 5.47019 9.62356 5.75 9.96875 5.75C10.3139 5.75 10.5938 5.47019 10.5938 5.125V4.5H13.4375V5.125C13.4375 5.47019 13.7173 5.75 14.0625 5.75C14.4077 5.75 14.6875 5.47019 14.6875 5.125V4.5H15.5C16.1892 4.5 16.75 5.06075 16.75 5.75V9.3125C16.75 9.65769 17.0298 9.9375 17.375 9.9375C17.7202 9.9375 18 9.65769 18 9.3125V5.75C18 4.3715 16.8785 3.25 15.5 3.25Z" fill="#4B4D50"/>
  <path d="M14.2188 10.4375C12.1337 10.4375 10.4375 12.1337 10.4375 14.2188C10.4375 16.3038 12.1337 18 14.2188 18C16.3038 18 18 16.3038 18 14.2188C18 12.1337 16.3038 10.4375 14.2188 10.4375ZM14.2188 16.75C12.823 16.75 11.6875 15.6145 11.6875 14.2188C11.6875 12.823 12.823 11.6875 14.2188 11.6875C15.6145 11.6875 16.75 12.823 16.75 14.2188C16.75 15.6145 15.6145 16.75 14.2188 16.75Z" fill="#4B4D50"/>
  <path d="M15.125 13.5938H14.8438V12.9375C14.8438 12.5923 14.5639 12.3125 14.2188 12.3125C13.8736 12.3125 13.5938 12.5923 13.5938 12.9375V14.2188C13.5938 14.5639 13.8736 14.8438 14.2188 14.8438H15.125C15.4702 14.8438 15.75 14.5639 15.75 14.2188C15.75 13.8736 15.4702 13.5938 15.125 13.5938Z" fill="#4B4D50"/>
</svg>
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
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
  <mask id="mask0_amt" style="mask-type:luminance" maskUnits="userSpaceOnUse" x="1" y="1" width="18" height="18">
    <path d="M1.66797 1.66675H18.3346V18.3334H1.66797V1.66675Z" fill="white"/>
  </mask>
  <g mask="url(#mask0_amt)">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M1.66797 10.0001C1.66797 5.39771 5.39893 1.66675 10.0013 1.66675C14.6037 1.66675 18.3346 5.39771 18.3346 10.0001C18.3346 14.6025 14.6037 18.3334 10.0013 18.3334C5.39893 18.3334 1.66797 14.6025 1.66797 10.0001ZM10.0013 3.05564C6.166 3.05564 3.05686 6.16478 3.05686 10.0001C3.05686 13.8354 6.166 16.9445 10.0013 16.9445C13.8366 16.9445 16.9457 13.8354 16.9457 10.0001C16.9457 6.16478 13.8366 3.05564 10.0013 3.05564ZM10.6957 5.48362C11.9036 5.62415 13.0909 6.30076 13.4528 7.74825C13.67 8.61712 12.3226 8.95398 12.1054 8.08511C11.9407 7.42662 11.4047 7.00437 10.6957 6.87983V9.2914C14.2044 9.41453 14.1444 13.6943 10.6957 14.4477C10.6957 15.7081 9.30686 15.7737 9.30686 14.5165C8.09901 14.3759 6.91169 13.6993 6.54982 12.2518C6.33259 11.3829 7.68001 11.0461 7.89723 11.9149C8.06186 12.5734 8.59786 12.9957 9.30686 13.1202V10.6606C5.51793 10.5417 6.03766 6.26661 9.30686 5.55244C9.30686 4.34379 10.6957 4.16055 10.6957 5.48362ZM9.30686 9.27017C7.42061 9.20597 7.70982 7.49672 9.30686 6.98585V9.27017ZM10.6957 13.0142V10.682C12.5887 10.7551 12.2913 12.5039 10.6957 13.0142Z" fill="#4B4D50"/>
  </g>
</svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Contract Amount</span>
            </div>
            <span class="text-sm font-medium text-dbd-dark">${{ toFixed(selected.paid, 2) }}</span>
          </div>
          <div class="h-px bg-gray-200"></div>

          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-green-50 rounded-full flex items-center justify-center">
                <svg class="text-dbd-dark" width="20" height="20" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
  <path d="M30.6666 7.38069V1.33325H7.1291V9.01136H1.33325V15.0588H7.1291V30.1075H13.894V22.7276H19.6153V16.6801H13.894V15.0588H25.1316V9.01136H13.894V7.38069H30.6666Z" fill="currentColor"/>
</svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Forevers Amount</span>
            </div>
            <span class="text-sm font-medium text-dbd-dark">{{ toFixed(selected.forevers, 2) }}</span>
          </div>
          <div class="h-px bg-gray-200"></div>

          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-purple-50 rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M3.5 13L7.5 9L10 11L15.5 5.5" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M15.5 5.5V9.5M15.5 5.5H11.5" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M3 16.5H17" stroke="#4B4D50" stroke-width="1.5" stroke-linecap="round"/>
</svg>
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
    <!-- Activate Access Modal -->
    <ActivateAccessModal
      :is-visible="showActivateModal"
      @cancel="showActivateModal = false"
      @confirm="confirmActivateAccess"
    />
    <ActivateAccessSuccessModal
      :is-visible="showActivateSuccessModal"
      :activated-at-ms="activatedAtMs"
      :title="successTitle"
      @close="showActivateSuccessModal = false"
    />
    <ActivateLoyaltyModal
      :is-visible="showLoyaltyModal"
      @cancel="showLoyaltyModal = false"
      @confirm="confirmActivateLoyalty"
    />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import BottomNavigation from '../components/BottomNavigation.vue'
import CountryFlag from '../components/CountryFlag.vue'
import ActivateAccessModal from '../components/ActivateAccessModal.vue'
import ActivateAccessSuccessModal from '../components/ActivateAccessSuccessModal.vue'
import ActivateLoyaltyModal from '../components/ActivateLoyaltyModal.vue'
import DepositsService from '../services/depositsService.js'
import telegramUserService from '../services/telegramUserService.js'
import { useApiErrorNotifier } from '../composables/useApiErrorNotifier.js'

const router = useRouter()
const contracts = ref([])
const showDetails = ref(false)
const selected = ref(null)
const userInfo = ref(null)
const showActivateModal = ref(false)
const showActivateSuccessModal = ref(false)
const activatedAtMs = ref(Date.now())
const successTitle = ref('Activate Access')
const showLoyaltyModal = ref(false)
const { showError: showApiError } = useApiErrorNotifier()
let pendingActivation = null
let pendingLoyalty = null

// Export & selection
const selectedContracts = ref([])
const showExportMenu = ref(false)

const goBack = () => router.push('/wallet')

const fetchContracts = async () => {
  const res = await DepositsService.getUserContractsForList()
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

const onActivateAccess = (c) => {
  pendingActivation = c
  showActivateModal.value = true
}

const confirmActivateAccess = async () => {
  const c = pendingActivation
  showActivateModal.value = false
  if (!c) return
  const depositId = c?._raw?.id
  const txid = c?.txid
  if (!depositId || !txid) return
  const res = await DepositsService.activateForevers(depositId, txid)
  if (res.status === 'success') {
    await fetchContracts()
    activatedAtMs.value = Date.now()
    successTitle.value = 'Activate Access'
    showActivateSuccessModal.value = true
  }
  pendingActivation = null
}
const openLoyaltyModal = (c) => { pendingLoyalty = c; showLoyaltyModal.value = true }
const confirmActivateLoyalty = async () => {
  showLoyaltyModal.value = false
  const c = pendingLoyalty
  pendingLoyalty = null
  if (!c) return
  const depositId = c?._raw?.id
  const txid = c?.txid
  if (!depositId || !txid) return
  const res = await DepositsService.activateLoyalty(depositId, txid)
  if (res.status === 'success') {
    await fetchContracts()
    activatedAtMs.value = Date.now()
    successTitle.value = 'Loyalty Program Activation'
    showActivateSuccessModal.value = true
  } else {
    showApiError('forevers_user_balance', { status: 400, message: res.message || 'Failed to activate loyalty program' })
  }
}
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

/* Hide scrollbars in this view */
.scrollbar-hide { -ms-overflow-style: none; scrollbar-width: none; }
.scrollbar-hide::-webkit-scrollbar { width: 0; height: 0; }
</style>

