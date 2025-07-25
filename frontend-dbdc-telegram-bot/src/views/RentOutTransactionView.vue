<template>
  <div class="rent-out-transaction-view w-full max-w-md mx-auto bg-gray-100 min-h-screen relative">
    <!-- Header Section -->
    <div class="header-section sticky top-0 bg-gray-100 z-40 pb-2">
      <!-- Status Bar Spacing -->
      <div class="h-12"></div>
      
      <!-- Header Content -->
      <div class="flex justify-between items-center px-4 py-3">
        <!-- Close Button -->
        <button 
          @click="goBack"
          class="w-11 h-11 flex items-center justify-center rounded-full bg-dbd-off-white border border-gray-200 hover:bg-gray-100 transition-colors"
        >
          <div class="w-5 h-5 relative">
            <div class="absolute w-4 h-0.5 bg-dbd-dark rounded-full rotate-45 top-2.5 left-0.5"></div>
            <div class="absolute w-4 h-0.5 bg-dbd-dark rounded-full -rotate-45 top-2.5 left-0.5"></div>
          </div>
        </button>

        <!-- Title -->
        <div class="flex-1 text-center">
          <h1 class="text-2xl font-semibold text-dbd-dark leading-tight">
            Rented Out<br>History
          </h1>
        </div>

        <!-- Export Button -->
        <div class="relative">
          <button
            @click="toggleExportMenu"
            :disabled="selectedTransactions.length === 0"
            :class="[
              'export-btn w-32 h-13 flex items-center justify-center gap-3 rounded-full px-4 py-2.5 transition-colors',
              selectedTransactions.length === 0
                ? 'bg-gray-300 border border-gray-300 cursor-not-allowed'
                : 'bg-white border border-gray-200 hover:bg-gray-50'
            ]"
          >
            <span :class="selectedTransactions.length === 0 ? 'text-gray-500 font-medium' : 'text-dbd-gray font-medium'">Export</span>
            <svg width="32" height="32" viewBox="0 0 33 33" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M24.4294 12.4709H20.4441V14.7762H24.4294C25.6145 14.7762 26.5339 15.3663 26.5339 15.8742V26.0964C26.5339 26.6043 25.6145 27.1945 24.4294 27.1945H9.3657C8.18061 27.1945 7.26115 26.6043 7.26115 26.0964V15.8746C7.26115 15.3667 8.18061 14.7766 9.3657 14.7766H13.3502V12.4713H9.3657C6.85955 12.4713 4.89648 13.9663 4.89648 15.8746V26.0968C4.89648 28.0055 6.85955 29.5001 9.3657 29.5001H24.4298C26.9355 29.5001 28.899 28.0051 28.899 26.0968V15.8746C28.8986 13.9659 26.9355 12.4709 24.4294 12.4709Z" fill="#FF6800"/>
              <path d="M13.3976 9.24579C13.7002 9.24579 14.0025 9.13322 14.2335 8.90807L15.7138 7.465V12.4704V14.7757V19.1917C15.7138 19.8283 16.243 20.3443 16.8961 20.3443C17.5491 20.3443 18.0784 19.8283 18.0784 19.1917V14.7757V12.4704V7.387L19.6387 8.90807C19.8696 9.13322 20.1723 9.24579 20.4746 9.24579C20.7769 9.24579 21.0796 9.13322 21.3105 8.90807C21.7724 8.45817 21.7724 7.72818 21.3105 7.27827L17.7805 3.83695C17.5495 3.6118 17.2472 3.5 16.945 3.5C16.9418 3.5 16.939 3.5 16.9359 3.5C16.9327 3.5 16.93 3.5 16.9268 3.5C16.6245 3.5 16.3223 3.6118 16.0913 3.83695L12.5613 7.27827C12.0994 7.72818 12.0994 8.45817 12.5613 8.90807C12.7926 9.13322 13.0949 9.24579 13.3976 9.24579Z" fill="#FF6800"/>
            </svg>
          </button>

          <!-- Export Dropdown Menu -->
          <div v-if="showExportMenu" class="absolute right-0 top-full mt-2 z-50">
            <!-- Dropdown Arrow -->
            <div class="w-0 h-0 border-l-8 border-r-8 border-b-8 border-transparent border-b-blue-600 absolute -top-2 right-10 z-10"></div>

            <!-- Dropdown Content -->
            <div class="w-41 bg-gradient-to-br from-indigo-500 via-blue-600 to-purple-700 rounded-2xl shadow-2xl overflow-hidden backdrop-blur-sm">
              <div class="p-3 space-y-2">
                <!-- CSV Option -->
                <button @click="exportData('csv')" class="w-full flex items-center gap-3 p-3 rounded-full bg-white/20 backdrop-blur-md border border-white/16 text-white hover:bg-white/25 transition-all duration-200">
                  <div class="w-10 h-10 bg-black/24 rounded-full flex items-center justify-center backdrop-blur-sm border border-white">
                    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M7 1L2 6H5.75C6.44038 6 7 5.44037 7 4.75V1Z" stroke="white" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                      <path d="M2 10H18V18H2V10Z" stroke="white" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                      <path d="M17 10V2.22727C17 1.54945 16.4404 1 15.75 1H7L2 5.90909V10" stroke="white" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                      <path d="M2 18V19.5484C2 20.3501 2.55963 21 3.25 21H15.75C16.4404 21 17 20.3501 17 19.5484V18" stroke="white" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                      <path d="M6.91304 13.2562C6.7172 13.0944 6.48113 13 6.22701 13C5.54933 13 5 13.6715 5 14.5C5 15.3284 5.54933 16 6.22701 16C6.50223 16 6.72862 15.8892 6.90043 15.7021C6.93598 15.6634 6.96917 15.6215 7 15.5765" stroke="white" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                      <path d="M10.8982 13.3145C10.8544 13.2348 10.3456 12.863 9.69389 13.0538C9.09546 13.229 9.01177 13.8996 9.4447 14.1739C9.4447 14.1739 9.86949 14.3581 10.3407 14.527C11.4749 14.9336 10.9863 16 10.0733 16C9.61602 16 9.23225 15.8054 9 15.5563" stroke="white" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                      <path d="M13 13L13.9617 15.955C13.9818 16.0155 14.0622 16.0149 14.0816 15.9541L15 13.0055" stroke="white" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>
                  <span class="text-base font-medium text-dbd-off-white">CSV</span>
                </button>

                <!-- PDF Option -->
                <button @click="exportData('pdf')" class="w-full flex items-center gap-3 p-3 rounded-full bg-white/20 backdrop-blur-md border border-white/16 text-white hover:bg-white/25 transition-all duration-200">
                  <div class="w-10 h-10 bg-black/24 rounded-full flex items-center justify-center backdrop-blur-sm border border-white">
                    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M5.50142 11C5.43556 10.9999 5.37033 11.0127 5.30945 11.0378C5.24857 11.0629 5.19325 11.0997 5.14666 11.1463C5.10008 11.1928 5.06314 11.248 5.03797 11.3088C5.0128 11.3696 4.9999 11.4348 5 11.5005V14.5C5 14.6326 5.05273 14.7598 5.14659 14.8536C5.24044 14.9473 5.36774 15 5.50047 15C5.63321 15 5.76051 14.9473 5.85436 14.8536C5.94822 14.7598 6.00095 14.6326 6.00095 14.5V14.0006H6.49858C6.89678 14.0006 7.27867 13.8426 7.56024 13.5613C7.84181 13.28 8 12.8985 8 12.5007C8 12.1029 7.84181 11.7214 7.56024 11.4401C7.27867 11.1588 6.89678 11.0008 6.49858 11.0008L5.50142 11ZM6.49972 12.9999H6.00171V11.9996H6.49934C6.63212 11.9996 6.75947 12.0523 6.85336 12.1461C6.94725 12.2399 7 12.3671 7 12.4997C7 12.6324 6.94725 12.7596 6.85336 12.8534C6.75947 12.9472 6.63212 12.9999 6.49934 12.9999H6.49972Z" fill="white"/>
                      <path d="M13.0001 11.4986C13.0001 11.433 13.0104 11.3682 13.0304 11.3076C13.0505 11.2471 13.0799 11.1921 13.117 11.1458C13.1541 11.0995 13.1982 11.0628 13.2466 11.0377C13.2951 11.0127 13.347 10.9999 13.3995 11H14.6C14.7058 11 14.8073 11.0525 14.8821 11.146C14.9569 11.2394 14.9989 11.3662 14.9989 11.4984C14.9989 11.6305 14.9569 11.7573 14.8821 11.8508C14.8073 11.9442 14.7058 11.9967 14.6 11.9967H13.798V12.995H14.6012C14.707 12.995 14.8084 13.0475 14.8832 13.1409C14.958 13.2343 15 13.361 15 13.4932C15 13.6253 14.958 13.752 14.8832 13.8454C14.8084 13.9389 14.707 13.9914 14.6012 13.9914H13.7973V14.4865C13.799 14.553 13.7899 14.6193 13.7707 14.6814C13.7515 14.7435 13.7225 14.8002 13.6855 14.848C13.6485 14.8959 13.6042 14.934 13.5551 14.9601C13.5061 14.9862 13.4534 14.9998 13.4001 15C13.3468 15.0002 13.2941 14.9871 13.2449 14.9614C13.1957 14.9357 13.1512 14.898 13.1139 14.8505C13.0766 14.8029 13.0473 14.7465 13.0278 14.6846C13.0083 14.6227 12.9988 14.5565 13.0001 14.4899V13.4951V13.4928V11.4986Z" fill="white"/>
                      <path d="M9.50032 11C9.43455 11 9.36943 11.013 9.30868 11.0381C9.24793 11.0633 9.19274 11.1002 9.14627 11.1467C9.0998 11.1932 9.06297 11.2483 9.03787 11.3091C9.01277 11.3698 8.9999 11.4349 9 11.5006V14.5002C9 14.6327 9.05271 14.7599 9.14654 14.8536C9.24037 14.9473 9.36762 15 9.50032 15H9.99836C10.5292 15 11.0384 14.7893 11.4137 14.4143C11.7891 14.0393 12 13.5307 12 13.0004C12 12.47 11.7891 11.9614 11.4137 11.5864C11.0384 11.2114 10.5292 11.0008 9.99836 11.0008L9.50032 11ZM10.0006 13.9992V12.0008C10.2627 12.0059 10.5123 12.1134 10.6958 12.3004C10.8794 12.4873 10.9822 12.7387 10.9822 13.0006C10.9822 13.2624 10.8794 13.5138 10.6958 13.7008C10.5123 13.8877 10.2627 13.9953 10.0006 14.0004V13.9992Z" fill="white"/>
                      <path d="M17.9998 18V16.8357C18.2991 16.6937 18.552 16.4698 18.729 16.1898C18.9061 15.9098 19 15.5854 19 15.2541V10.75C19 10.4188 18.9061 10.0943 18.729 9.81436C18.552 9.5344 18.2991 9.31042 17.9998 9.16847V7.82793C17.9997 7.29755 17.7889 6.78893 17.4139 6.41387L11.585 0.585939C11.5697 0.571266 11.5535 0.557594 11.5364 0.545007C11.5239 0.535532 11.5118 0.526057 11.4985 0.515823C11.4297 0.450883 11.3565 0.390733 11.2795 0.335797C11.2538 0.319276 11.2269 0.304585 11.1991 0.291832C11.1832 0.283873 11.1673 0.276293 11.1518 0.267576L11.1017 0.238772C11.0482 0.206389 10.9928 0.177279 10.9357 0.151601C10.7367 0.0721007 10.526 0.0255068 10.3119 0.0136441C10.2922 0.0136441 10.274 0.0098541 10.2532 0.00720108C10.2262 0.00296932 10.199 0.000563477 10.1717 0H4.00013C3.46977 0.000200898 2.96119 0.210979 2.58616 0.586008C2.21114 0.961038 2.00037 1.46963 2.00017 2V9.16847C1.70088 9.31042 1.44802 9.5344 1.27097 9.81436C1.09393 10.0943 0.999962 10.4188 1 10.75V15.2541C0.999928 15.5853 1.09384 15.9098 1.27081 16.1897C1.44779 16.4697 1.70057 16.6937 1.99979 16.8357V18C1.99999 18.5304 2.21076 19.039 2.58579 19.414C2.96081 19.789 3.46939 19.9998 3.99975 20H15.9999C16.5302 19.9998 17.0388 19.789 17.4138 19.414C17.7889 19.039 17.9996 18.5304 17.9998 18ZM15.9999 18.4999H4.00013C3.86781 18.4994 3.74106 18.4465 3.6476 18.3529C3.55414 18.2592 3.50157 18.1323 3.50137 18V17.0044H16.5009V18C16.5007 18.1327 16.4478 18.2599 16.3539 18.3537C16.2599 18.4474 16.1326 18.5 15.9999 18.4999ZM16.4998 8.00152V9.00171H3.50137V2C3.50157 1.86748 3.5543 1.74044 3.64801 1.64674C3.74171 1.55303 3.86874 1.5003 4.00126 1.50009H10V6C10.0002 6.53037 10.211 7.03896 10.586 7.41399C10.961 7.78902 11.4696 7.9998 12 8L16.4998 8.00152ZM15.3779 6.50142H12C11.9341 6.50157 11.8688 6.48871 11.8078 6.46357C11.7469 6.43842 11.6916 6.4015 11.6449 6.35492C11.5983 6.30833 11.5614 6.253 11.5362 6.19209C11.511 6.13119 11.4981 6.06591 11.4982 6V2.62119L15.3779 6.50142ZM2.74982 10.4984H17.2498C17.3161 10.4984 17.3798 10.5247 17.4267 10.5717C17.4736 10.6186 17.4999 10.6822 17.4999 10.7485V15.2541C17.4999 15.3205 17.4736 15.3841 17.4267 15.431C17.3798 15.4779 17.3161 15.5043 17.2498 15.5043H2.74982C2.68348 15.5043 2.61986 15.4779 2.57295 15.431C2.52604 15.3841 2.49968 15.3205 2.49968 15.2541V10.75C2.49948 10.7171 2.50581 10.6844 2.51829 10.6539C2.53077 10.6233 2.54916 10.5956 2.57241 10.5722C2.59566 10.5488 2.6233 10.5302 2.65375 10.5176C2.68419 10.5049 2.71684 10.4984 2.74982 10.4984Z" fill="white"/>
                    </svg>
                  </div>
                  <span class="text-base font-medium text-dbd-off-white">PDF</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Content Container -->
    <div class="content-container bg-gray-100 pb-24 px-4">
      <!-- Empty State -->
      <div v-if="transactions.length === 0" class="empty-state flex flex-col items-center justify-center text-center" style="min-height: calc(100vh - 200px);">
        <h2 class="text-xl font-bold text-dbd-dark mb-4 leading-tight max-w-60">
          No deals<br>have been opened yet.
        </h2>
        <p class="text-base font-medium text-dbd-gray leading-relaxed max-w-72">
          All the transaction will be displayed inside this table after you make one.
        </p>
      </div>

      <!-- Scrollable Transaction List -->
      <div v-else class="transaction-list space-y-2 pt-4">
        <!-- Transaction Cards -->
        <div
          v-for="(transaction, index) in transactions"
          :key="index"
          class="transaction-card bg-dbd-off-white rounded-3xl border border-gray-200 p-3 cursor-pointer hover:bg-gray-50 transition-colors"
          @click="openTransactionDetails(transaction, index)"
        >
          <!-- Date and Time Row -->
          <div class="flex justify-between items-center mb-4">
            <div class="flex items-center gap-2">
              <!-- Checkbox -->
              <div
                @click.stop="toggleTransactionSelection(index)"
                :class="[
                  'w-6 h-6 border-2 rounded flex items-center justify-center cursor-pointer transition-colors',
                  selectedTransactions.includes(index)
                    ? 'bg-green-500 border-green-500'
                    : 'border-gray-400 bg-dbd-off-white hover:border-gray-500'
                ]"
              >
                <svg v-if="selectedTransactions.includes(index)" width="14" height="10" viewBox="0 0 14 10" fill="none">
                  <path d="M1 5L5 9L13 1" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              
              <!-- Calendar Icon -->
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
              <span class="text-sm font-medium text-dbd-dark">{{ transaction.date }}</span>
              <span class="text-sm font-medium text-dbd-gray">{{ transaction.time }}</span>
            </div>
          </div>

          <!-- Type & Amount Row -->
          <div class="flex justify-between items-center mb-4">
            <div class="flex items-center gap-2">
              <span class="text-base font-semibold text-dbd-gray">Type & Amount</span>
            </div>
            
            <div class="flex items-center gap-2">
              <div class="flex items-center gap-1">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M13.7564 1.77783H4.78285C4.38779 1.77783 4.1056 2.06002 4.1056 2.45508V5.22051H1.56592C1.17086 5.27695 0.888672 5.55914 0.888672 5.9542C0.888672 6.34926 1.17086 6.63145 1.56592 6.63145H4.1056V12.9524C4.1056 13.3475 4.38779 13.6297 4.78285 13.6297C5.17791 13.6297 5.4601 13.3475 5.4601 12.9524V10.0177H8.33841C8.73347 10.0177 9.01566 9.7355 9.01566 9.34044C9.01566 8.94538 8.73347 8.66319 8.33841 8.66319H5.4601V6.57501H10.9345C11.3296 6.57501 11.6118 6.29282 11.6118 5.89776C11.6118 5.5027 11.3296 5.22051 10.9345 5.22051H5.4601V3.13233H13.7C14.095 3.13233 14.3772 2.85014 14.3772 2.45508C14.3772 2.06002 14.1515 1.77783 13.7564 1.77783Z" fill="#4B4D50"/>
                </svg>
                <span class="text-base font-medium text-dbd-gray">UAE</span>
              </div>
              <div class="w-px h-4 bg-gray-600"></div>
              <span class="text-base font-medium text-dbd-gray">{{ transaction.amount.toLocaleString() }}</span>
            </div>
          </div>

          <!-- Purchased Row -->
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <span class="text-base font-semibold text-dbd-gray">Purchased</span>
            </div>
            
            <div class="flex items-center gap-1">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M11.8525 24C11.5497 24 11.2994 23.9056 11.1014 23.7167C10.9035 23.5278 10.8045 23.2889 10.8045 23V21.2C9.68657 21.0222 8.73169 20.6444 7.93984 20.0667C7.14799 19.4889 6.53082 18.7556 6.08831 17.8667C5.97186 17.6222 5.97186 17.3667 6.08831 17.1C6.20476 16.8333 6.40272 16.6444 6.6822 16.5333C6.93839 16.4222 7.20039 16.4222 7.46823 16.5333C7.73606 16.6444 7.93984 16.8222 8.07958 17.0667C8.49879 17.8222 9.0461 18.3889 9.7215 18.7667C10.3969 19.1444 11.1771 19.3333 12.0621 19.3333C13.18 19.3333 14.1 19.0667 14.8219 18.5333C15.5439 18 15.9049 17.2667 15.9049 16.3333C15.9049 15.3556 15.5847 14.6 14.9442 14.0667C14.3037 13.5333 13.0985 12.9889 11.3285 12.4333C9.65163 11.9222 8.39981 11.2444 7.57303 10.4C6.74625 9.55556 6.33285 8.5 6.33285 7.23333C6.33285 6.01111 6.74625 4.98889 7.57303 4.16667C8.39981 3.34444 9.47696 2.87778 10.8045 2.76667V1C10.8045 0.711111 10.9035 0.472222 11.1014 0.283333C11.2994 0.0944446 11.5497 0 11.8525 0C12.1553 0 12.4056 0.0944446 12.6036 0.283333C12.8016 0.472222 12.9005 0.711111 12.9005 1V2.76667C13.739 2.87778 14.4901 3.12222 15.1538 3.5C15.8176 3.87778 16.3707 4.36667 16.8132 4.96667C16.9762 5.18889 17.0112 5.42778 16.918 5.68333C16.8248 5.93889 16.6385 6.12222 16.3591 6.23333C16.1029 6.34444 15.835 6.35556 15.5556 6.26667C15.2761 6.17778 15.0432 6.01111 14.8569 5.76667C14.5308 5.36667 14.1291 5.07222 13.6516 4.88333C13.1742 4.69444 12.5978 4.6 11.9224 4.6C10.851 4.6 10.001 4.83333 9.37216 5.3C8.74333 5.76667 8.42892 6.4 8.42892 7.2C8.42892 8.04444 8.77827 8.72778 9.47696 9.25C10.1756 9.77222 11.4682 10.3111 13.3547 10.8667C14.9384 11.3333 16.1087 12.0056 16.8656 12.8833C17.6225 13.7611 18.001 14.8667 18.001 16.2C18.001 17.6 17.5701 18.7278 16.7084 19.5833C15.8467 20.4389 14.5774 20.9889 12.9005 21.2333V23C12.9005 23.2889 12.8016 23.5278 12.6036 23.7167C12.4056 23.9056 12.1553 24 11.8525 24Z" fill="#2019CE"/>
              </svg>
              <span class="text-base font-medium text-dbd-gray">{{ formatCurrency(transaction.purchased) }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Navigation Component -->
    <BottomNavigation />

    <!-- Transaction Details Modal -->
    <div v-if="showTransactionModal" class="fixed inset-0 z-50 flex items-end justify-center bg-black bg-opacity-20 backdrop-blur-sm">
      <div class="w-full max-w-md bg-white rounded-t-3xl shadow-xl animate-slide-up">
        <!-- Modal Header -->
        <div class="flex items-center justify-between p-4" @touchstart="handleTouchStart" @touchmove="handleTouchMove" @touchend="handleTouchEnd">
          <div class="flex-1">
            <h2 class="text-base font-medium text-dbd-dark">Transaction Details</h2>
          </div>
          <button @click="closeTransactionModal" class="w-11 h-11 flex items-center justify-center rounded-full bg-dbd-off-white border border-gray-200">
            <div class="w-5 h-5 relative">
              <div class="absolute w-4 h-0.5 bg-dbd-dark rounded-full rotate-45 top-2.5 left-0.5"></div>
              <div class="absolute w-4 h-0.5 bg-dbd-dark rounded-full -rotate-45 top-2.5 left-0.5"></div>
            </div>
          </button>
        </div>

        <!-- Modal Content -->
        <div v-if="selectedTransaction" class="p-4 space-y-4 max-h-96 overflow-y-auto">
          <!-- ID Contract -->
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-purple-50 rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                  <g clip-path="url(#clip0_2_20722)">
                    <path d="M11.043 13.5537H13.9076" stroke="#4B4D50" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M11.043 9.73828H13.9076" stroke="#4B4D50" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M6.09375 9.47806L6.61458 10.5176L7.91667 8.9583" stroke="#4B4D50" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M6.09375 12.6009L7.39583 14.4238" stroke="#4B4D50" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M7.39583 12.6009L6.09375 14.4238" stroke="#4B4D50" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M14.168 3.75448C15.1859 3.82121 15.9909 4.66789 15.9909 5.70304V15.8918C15.9909 16.9706 15.1165 17.845 14.0378 17.845H5.96484C4.88607 17.845 4.01172 16.9706 4.01172 15.8918V5.70304C4.01172 4.66789 4.81673 3.82121 5.83464 3.75448" stroke="#4B4D50" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M6.8125 5.3125H13.1927C13.732 5.3125 14.1693 4.87526 14.1693 4.33594V3.13151C14.1693 2.59219 13.732 2.15495 13.1927 2.15495H6.8125C6.27318 2.15495 5.83594 2.59219 5.83594 3.13151V4.33594C5.83594 4.87526 6.27318 5.3125 6.8125 5.3125Z" stroke="#4B4D50" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
                  </g>
                  <defs>
                    <clipPath id="clip0_2_20722">
                      <rect width="20" height="20" fill="white"/>
                    </clipPath>
                  </defs>
                </svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">ID Contract</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-sm font-medium text-dbd-dark">{{ selectedTransaction.contractId }}</span>
              <!-- Copy Button with Fixed Width to Prevent Jumping -->
              <div class="w-24 flex justify-end pl-2">
                <!-- Default State -->
                <button
                  v-if="!copyState.isShowingCopied"
                  @click="copyToClipboard(selectedTransaction.contractId)"
                  class="copy-btn-default flex items-center gap-2 px-3 py-2 bg-white border border-dbd-blue rounded-full hover:opacity-90 transition-all duration-200"
                >
                  <svg width="16" height="16" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg" class="flex-shrink-0">
                    <path d="M18.0655 0.5H7.60611C6.97596 0.5 6.37161 0.727045 5.92603 1.13119C5.48044 1.53533 5.23011 2.08346 5.23011 2.65501V3.48385H4.04211C3.38111 3.48385 2.74718 3.72201 2.27978 4.14594C1.81239 4.56986 1.5498 5.14483 1.5498 5.74435V19.2395C1.5498 19.839 1.81239 20.414 2.27978 20.8379C2.74718 21.2618 3.38111 21.5 4.04211 21.5H14.2772C14.9382 21.5 15.5721 21.2618 16.0395 20.8379C16.5069 20.414 16.7695 19.839 16.7695 19.2395V18.486H18.0655C18.6907 18.4861 19.291 18.2634 19.7369 17.866C20.1829 17.4685 20.4389 16.9281 20.4498 16.3611V2.65501C20.4476 2.08277 20.1954 1.53465 19.7485 1.13073C19.3016 0.7268 18.6964 0.499997 18.0655 0.5ZM15.108 19.2395C15.108 19.4393 15.0204 19.631 14.8646 19.7723C14.7088 19.9136 14.4975 19.993 14.2772 19.993H4.04211C3.82178 19.993 3.61047 19.9136 3.45467 19.7723C3.29887 19.631 3.21134 19.4393 3.21134 19.2395V5.74435C3.21134 5.54451 3.29887 5.35285 3.45467 5.21154C3.61047 5.07024 3.82178 4.99085 4.04211 4.99085H14.2772C14.4975 4.99085 14.7088 5.07024 14.8646 5.21154C15.0204 5.35285 15.108 5.54451 15.108 5.74435V19.2395ZM18.7883 16.3611C18.7861 16.5337 18.709 16.6985 18.5737 16.8198C18.4383 16.9411 18.2558 17.0092 18.0655 17.0092H16.7695V5.74435C16.7695 5.14483 16.5069 4.56986 16.0395 4.14594C15.5721 3.72201 14.9382 3.48385 14.2772 3.48385H6.89165V2.65501C6.89165 2.48314 6.96693 2.31832 7.10091 2.19679C7.2349 2.07527 7.41663 2.007 7.60611 2.007H18.0655C18.16 2.006 18.2538 2.02203 18.3415 2.05414C18.4291 2.08626 18.5089 2.13384 18.5761 2.19411C18.6433 2.25438 18.6967 2.32616 18.7331 2.40527C18.7695 2.48439 18.7883 2.56927 18.7883 2.65501V16.3611Z" fill="#2019CE"/>
                  </svg>
                  <span class="text-sm font-medium text-dbd-blue">Copy</span>
                </button>

                <!-- Copied State -->
                <div
                  v-if="copyState.isShowingCopied"
                  class="copy-btn-copied flex items-center gap-2 px-3 py-2 bg-green-600 border border-green-500 rounded-full transition-all duration-200"
                >
                  <!-- White circle with green checkmark -->
                  <div class="w-4 h-4 bg-white rounded-full flex items-center justify-center flex-shrink-0">
                    <svg width="10" height="8" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg" class="flex-shrink-0">
                      <path d="M11.3242 0.926106C10.7978 0.642629 10.2106 1.18934 9.86633 1.51331C9.07667 2.28275 8.40848 3.17368 7.65925 3.98362C6.82907 4.87455 6.05963 5.76548 5.20919 6.6362C4.72323 7.12216 4.19677 7.64862 3.8728 8.25607C3.14385 7.54734 2.51615 6.7779 1.70621 6.15023C1.11901 5.70477 0.147086 5.38079 0.167334 6.45396C0.207831 7.85113 1.44299 9.34952 2.35416 10.3012C2.73888 10.7061 3.24509 11.1313 3.8323 11.1516C4.54099 11.1921 5.26994 10.3417 5.69515 9.87594C6.44438 9.06601 7.05183 8.15479 7.74024 7.32464C8.63118 6.23123 9.54236 5.15803 10.413 4.04436C10.9597 3.35592 12.6809 1.65502 11.3242 0.926106ZM1.05823 6.37297C1.03798 6.37297 1.01773 6.37297 0.977238 6.39318C0.896244 6.37297 0.835499 6.35268 0.754505 6.31219C0.815251 6.27169 0.916493 6.29194 1.05823 6.37297Z" fill="#07B80E"/>
                    </svg>
                  </div>
                  <span class="text-sm font-medium text-white">Copied</span>
                </div>
              </div>
            </div>
          </div>

          <div class="h-px bg-gray-200"></div>

          <!-- Date & Time -->
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-dbd-light-orange rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M14.0625 9.1875C14.4077 9.1875 14.6875 8.90768 14.6875 8.5625C14.6875 8.21732 14.4077 7.9375 14.0625 7.9375C13.7173 7.9375 13.4375 8.21732 13.4375 8.5625C13.4375 8.90768 13.7173 9.1875 14.0625 9.1875Z" fill="#4B4D50"/>
                  <path d="M15.5 3.25H14.6875V2.625C14.6875 2.27981 14.4077 2 14.0625 2C13.7173 2 13.4375 2.27981 13.4375 2.625V3.25H10.5938V2.625C10.5938 2.27981 10.3139 2 9.96875 2C9.62356 2 9.34375 2.27981 9.34375 2.625V3.25H6.53125V2.625C6.53125 2.27981 6.25144 2 5.90625 2C5.56106 2 5.28125 2.27981 5.28125 2.625V3.25H4.5C3.1215 3.25 2 4.3715 2 5.75V15.5C2 16.8785 3.1215 18 4.5 18H9.28125C9.62644 18 9.90625 17.7202 9.90625 17.375C9.90625 17.0298 9.62644 16.75 9.28125 16.75H4.5C3.81075 16.75 3.25 16.1892 3.25 15.5V5.75C3.25 5.06075 3.81075 4.5 4.5 4.5H5.28125V5.125C5.28125 5.47019 5.56106 5.75 5.90625 5.75C6.25144 5.75 6.53125 5.47019 6.53125 5.125V4.5H9.34375V5.125C9.34375 5.47019 9.62356 5.75 9.96875 5.75C10.3139 5.75 10.5938 5.47019 10.5938 5.125V4.5H13.4375V5.125C13.4375 5.47019 13.7173 5.75 14.0625 5.75C14.4077 5.75 14.6875 5.47019 14.6875 5.125V4.5H15.5C16.1892 4.5 16.75 5.06075 16.75 5.75V9.3125C16.75 9.65769 17.0298 9.9375 17.375 9.9375C17.7202 9.9375 18 9.65769 18 9.3125V5.75C18 4.3715 16.8785 3.25 15.5 3.25Z" fill="#4B4D50"/>
                  <path d="M14.2188 10.4375C12.1337 10.4375 10.4375 12.1337 10.4375 14.2188C10.4375 16.3038 12.1337 18 14.2188 18C16.3038 18 18 16.3038 18 14.2188C18 12.1337 16.3038 10.4375 14.2188 10.4375ZM14.2188 16.75C12.823 16.75 11.6875 15.6145 11.6875 14.2188C11.6875 12.823 12.823 11.6875 14.2188 11.6875C15.6145 11.6875 16.75 12.823 16.75 14.2188C16.75 15.6145 15.6145 16.75 14.2188 16.75Z" fill="#4B4D50"/>
                  <path d="M15.125 13.5938H14.8438V12.9375C14.8438 12.5923 14.5639 12.3125 14.2188 12.3125C13.8736 12.3125 13.5938 12.5923 13.5938 12.9375V14.2188C13.5938 14.5639 13.8736 14.8438 14.2188 14.8438H15.125C15.4702 14.8438 15.75 14.5639 15.75 14.2188C15.75 13.8736 15.4702 13.5938 15.125 13.5938Z" fill="#4B4D50"/>
                  <path d="M11.3438 9.1875C11.6889 9.1875 11.9688 8.90768 11.9688 8.5625C11.9688 8.21732 11.6889 7.9375 11.3438 7.9375C10.9986 7.9375 10.7188 8.21732 10.7188 8.5625C10.7188 8.90768 10.9986 9.1875 11.3438 9.1875Z" fill="#4B4D50"/>
                  <path d="M8.625 11.9062C8.97018 11.9062 9.25 11.6264 9.25 11.2812C9.25 10.9361 8.97018 10.6562 8.625 10.6562C8.27982 10.6562 8 10.9361 8 11.2812C8 11.6264 8.27982 11.9062 8.625 11.9062Z" fill="#4B4D50"/>
                  <path d="M5.90625 9.1875C6.25143 9.1875 6.53125 8.90768 6.53125 8.5625C6.53125 8.21732 6.25143 7.9375 5.90625 7.9375C5.56107 7.9375 5.28125 8.21732 5.28125 8.5625C5.28125 8.90768 5.56107 9.1875 5.90625 9.1875Z" fill="#4B4D50"/>
                  <path d="M5.90625 11.9062C6.25143 11.9062 6.53125 11.6264 6.53125 11.2812C6.53125 10.9361 6.25143 10.6562 5.90625 10.6562C5.56107 10.6562 5.28125 10.9361 5.28125 11.2812C5.28125 11.6264 5.56107 11.9062 5.90625 11.9062Z" fill="#4B4D50"/>
                  <path d="M5.90625 14.625C6.25143 14.625 6.53125 14.3452 6.53125 14C6.53125 13.6548 6.25143 13.375 5.90625 13.375C5.56107 13.375 5.28125 13.6548 5.28125 14C5.28125 14.3452 5.56107 14.625 5.90625 14.625Z" fill="#4B4D50"/>
                  <path d="M8.625 14.625C8.97018 14.625 9.25 14.3452 9.25 14C9.25 13.6548 8.97018 13.375 8.625 13.375C8.27982 13.375 8 13.6548 8 14C8 14.3452 8.27982 14.625 8.625 14.625Z" fill="#4B4D50"/>
                  <path d="M8.625 9.1875C8.97018 9.1875 9.25 8.90768 9.25 8.5625C9.25 8.21732 8.97018 7.9375 8.625 7.9375C8.27982 7.9375 8 8.21732 8 8.5625C8.625 8.90768 8.97018 9.1875 8.625 9.1875Z" fill="#4B4D50"/>
                </svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Date & Time</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-sm font-medium text-dbd-dark">{{ selectedTransaction.date }}</span>
              <span class="text-sm font-medium text-dbd-gray">{{ selectedTransaction.time }}</span>
            </div>
          </div>

          <div class="h-px bg-gray-200"></div>

          <!-- Amount -->
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-purple-50 rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                  <mask id="mask0_2_20774" style="mask-type:luminance" maskUnits="userSpaceOnUse" x="1" y="1" width="18" height="18">
                    <path d="M1.66797 1.66675H18.3346V18.3334H1.66797V1.66675Z" fill="white"/>
                  </mask>
                  <g mask="url(#mask0_2_20774)">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M1.66797 10.0001C1.66797 5.39771 5.39893 1.66675 10.0013 1.66675C14.6037 1.66675 18.3346 5.39771 18.3346 10.0001C18.3346 14.6025 14.6037 18.3334 10.0013 18.3334C5.39893 18.3334 1.66797 14.6025 1.66797 10.0001ZM10.0013 3.05564C6.166 3.05564 3.05686 6.16478 3.05686 10.0001C3.05686 13.8354 6.166 16.9445 10.0013 16.9445C13.8366 16.9445 16.9457 13.8354 16.9457 10.0001C16.9457 6.16478 13.8366 3.05564 10.0013 3.05564ZM10.6957 5.48362C11.9036 5.62415 13.0909 6.30076 13.4528 7.74825C13.67 8.61712 12.3226 8.95398 12.1054 8.08511C11.9407 7.42662 11.4047 7.00437 10.6957 6.87983V9.2914C14.2044 9.41453 14.1444 13.6943 10.6957 14.4477C10.6957 15.7081 9.30686 15.7737 9.30686 14.5165C8.09901 14.3759 6.91169 13.6993 6.54982 12.2518C6.33259 11.3829 7.68001 11.0461 7.89723 11.9149C8.06186 12.5734 8.59786 12.9957 9.30686 13.1202V10.6606C5.51793 10.5417 6.03766 6.26661 9.30686 5.55244C9.30686 4.34379 10.6957 4.16055 10.6957 5.48362ZM9.30686 9.27017C7.42061 9.20597 7.70982 7.49672 9.30686 6.98585V9.27017ZM10.6957 13.0142V10.682C12.5887 10.7551 12.2913 12.5039 10.6957 13.0142Z" fill="#4B4D50"/>
                  </g>
                </svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Amount</span>
            </div>
            <span class="text-sm font-medium text-dbd-dark">{{ selectedTransaction.amount.toLocaleString() }}</span>
          </div>

          <div class="h-px bg-gray-200"></div>

          <!-- Type -->
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-purple-50 rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                  <path d="M17.2636 3H6.61925C6.15063 3 5.8159 3.33333 5.8159 3.8V7.06667H2.80335C2.33473 7.13333 2 7.46667 2 7.93333C2 8.4 2.33473 8.73333 2.80335 8.73333H5.8159V16.2C5.8159 16.6667 6.15063 17 6.61925 17C7.08787 17 7.42259 16.6667 7.42259 16.2V12.7333H10.8368C11.3054 12.7333 11.6402 12.4 11.6402 11.9333C11.6402 11.4667 11.3054 11.1333 10.8368 11.1333H7.42259V8.66667H13.9163C14.3849 8.66667 14.7197 8.33333 14.7197 7.86667C14.7197 7.4 14.3849 7.06667 13.9163 7.06667H7.42259V4.6H17.1967C17.6653 4.6 18 4.26667 18 3.8C18 3.33333 17.7322 3 17.2636 3Z" fill="#4B4D50"/>
                </svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Type</span>
            </div>
            <div class="flex items-center gap-2">
              <div class="w-6 h-6 rounded-full bg-gray-200 flex items-center justify-center">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                  <path d="M13.7564 1.77783H4.78285C4.38779 1.77783 4.1056 2.06002 4.1056 2.45508V5.22051H1.56592C1.17086 5.27695 0.888672 5.55914 0.888672 5.9542C0.888672 6.34926 1.17086 6.63145 1.56592 6.63145H4.1056V12.9524C4.1056 13.3475 4.38779 13.6297 4.78285 13.6297C5.17791 13.6297 5.4601 13.3475 5.4601 12.9524V10.0177H8.33841C8.73347 10.0177 9.01566 9.7355 9.01566 9.34044C9.01566 8.94538 8.73347 8.66319 8.33841 8.66319H5.4601V6.57501H10.9345C11.3296 6.57501 11.6118 6.29282 11.6118 5.89776C11.6118 5.5027 11.3296 5.22051 10.9345 5.22051H5.4601V3.13233H13.7C14.095 3.13233 14.3772 2.85014 14.3772 2.45508C14.3772 2.06002 14.1515 1.77783 13.7564 1.77783Z" fill="#4B4D50"/>
                </svg>
              </div>
              <span class="text-base font-medium text-dbd-gray">UAE</span>
            </div>
          </div>

          <div class="h-px bg-gray-200"></div>

          <!-- Purchased -->
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-green-50 rounded-full flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <path d="M11.8525 24C11.5497 24 11.2994 23.9056 11.1014 23.7167C10.9035 23.5278 10.8045 23.2889 10.8045 23V21.2C9.68657 21.0222 8.73169 20.6444 7.93984 20.0667C7.14799 19.4889 6.53082 18.7556 6.08831 17.8667C5.97186 17.6222 5.97186 17.3667 6.08831 17.1C6.20476 16.8333 6.40272 16.6444 6.6822 16.5333C6.93839 16.4222 7.20039 16.4222 7.46823 16.5333C7.73606 16.6444 7.93984 16.8222 8.07958 17.0667C8.49879 17.8222 9.0461 18.3889 9.7215 18.7667C10.3969 19.1444 11.1771 19.3333 12.0621 19.3333C13.18 19.3333 14.1 19.0667 14.8219 18.5333C15.5439 18 15.9049 17.2667 15.9049 16.3333C15.9049 15.3556 15.5847 14.6 14.9442 14.0667C14.3037 13.5333 13.0985 12.9889 11.3285 12.4333C9.65163 11.9222 8.39981 11.2444 7.57303 10.4C6.74625 9.55556 6.33285 8.5 6.33285 7.23333C6.33285 6.01111 6.74625 4.98889 7.57303 4.16667C8.39981 3.34444 9.47696 2.87778 10.8045 2.76667V1C10.8045 0.711111 10.9035 0.472222 11.1014 0.283333C11.2994 0.0944446 11.5497 0 11.8525 0C12.1553 0 12.4056 0.0944446 12.6036 0.283333C12.8016 0.472222 12.9005 0.711111 12.9005 1V2.76667C13.739 2.87778 14.4901 3.12222 15.1538 3.5C15.8176 3.87778 16.3707 4.36667 16.8132 4.96667C16.9762 5.18889 17.0112 5.42778 16.918 5.68333C16.8248 5.93889 16.6385 6.12222 16.3591 6.23333C16.1029 6.34444 15.835 6.35556 15.5556 6.26667C15.2761 6.17778 15.0432 6.01111 14.8569 5.76667C14.5308 5.36667 14.1291 5.07222 13.6516 4.88333C13.1742 4.69444 12.5978 4.6 11.9224 4.6C10.851 4.6 10.001 4.83333 9.37216 5.3C8.74333 5.76667 8.42892 6.4 8.42892 7.2C8.42892 8.04444 8.77827 8.72778 9.47696 9.25C10.1756 9.77222 11.4682 10.3111 13.3547 10.8667C14.9384 11.3333 16.1087 12.0056 16.8656 12.8833C17.6225 13.7611 18.001 14.8667 18.001 16.2C18.001 17.6 17.5701 18.7278 16.7084 19.5833C15.8467 20.4389 14.5774 20.9889 12.9005 21.2333V23C12.9005 23.2889 12.8016 23.5278 12.6036 23.7167C12.4056 23.9056 12.1553 24 11.8525 24Z" fill="#07B80E"/>
                </svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Purchased</span>
            </div>
            <span class="text-sm font-medium text-green-600">$ +{{ formatCurrency(selectedTransaction.purchased) }}</span>
          </div>

          <div class="h-px bg-gray-200"></div>

          <!-- Percentage of rent -->
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <div class="w-10 h-10 bg-green-50 rounded-full flex items-center justify-center">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                  <path d="M4 20L19.9351 4M6.53681 8.81929C5.22466 8.81929 4.16095 7.75126 4.16095 6.43376C4.16095 5.11627 5.22466 4.04824 6.53681 4.04824C7.84896 4.04824 8.91267 5.11627 8.91267 6.43376C8.91267 7.75126 7.84896 8.81929 6.53681 8.81929ZM17.6241 19.9518C16.312 19.9518 15.2483 18.8837 15.2483 17.5662C15.2483 16.2487 16.312 15.1807 17.6241 15.1807C18.9363 15.1807 20 16.2487 20 17.5662C20 18.8837 18.9363 19.9518 17.6241 19.9518Z" stroke="#4B4D50" stroke-width="2" stroke-linecap="round" transform="rotate(90 12 12)"/>
                </svg>
              </div>
              <span class="text-sm font-medium text-dbd-gray">Percentage of rent</span>
            </div>
            <span class="text-sm font-medium text-dbd-dark">{{ selectedTransaction.rentPercentage }}%</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import BottomNavigation from '../components/BottomNavigation.vue'

const router = useRouter()
const showExportMenu = ref(false)
const selectedTransactions = ref([])
const showTransactionModal = ref(false)
const selectedTransaction = ref(null)
const copyState = ref({
  isShowingCopied: false
})
const touchStartY = ref(0)
const touchCurrentY = ref(0)
const isDragging = ref(false)

// Sample transaction data
const transactions = ref([
  {
    date: '25.02.2025',
    time: '11:30',
    amount: 2990,
    purchased: 20212.40,
    contractId: 'X5D122C48',
    rentPercentage: 12
  },
  {
    date: '25.02.2025',
    time: '02:30',
    amount: 250,
    purchased: 400.86,
    contractId: 'A3B456C78',
    rentPercentage: 8
  },
  {
    date: '25.02.2025',
    time: '02:30',
    amount: 250,
    purchased: 400.86,
    contractId: 'D9E123F45',
    rentPercentage: 15
  },
  {
    date: '25.02.2025',
    time: '02:30',
    amount: 250,
    purchased: 400.86,
    contractId: 'G7H890I23',
    rentPercentage: 10
  },
  {
    date: '25.02.2025',
    time: '02:30',
    amount: 250,
    purchased: 400.86,
    contractId: 'J4K567L89',
    rentPercentage: 6
  },
  {
    date: '25.02.2025',
    time: '02:30',
    amount: 250,
    purchased: 400.86,
    contractId: 'M1N234O56',
    rentPercentage: 18
  }
])

const goBack = () => {
  router.back()
}

const toggleExportMenu = () => {
  if (selectedTransactions.value.length > 0) {
    showExportMenu.value = !showExportMenu.value
  }
}

const toggleTransactionSelection = (index) => {
  const selectedIndex = selectedTransactions.value.indexOf(index)
  if (selectedIndex > -1) {
    selectedTransactions.value.splice(selectedIndex, 1)
  } else {
    selectedTransactions.value.push(index)
  }
}

const openTransactionDetails = (transaction, index) => {
  selectedTransaction.value = transaction
  showTransactionModal.value = true
}

const closeTransactionModal = () => {
  showTransactionModal.value = false
  selectedTransaction.value = null
}

const copyToClipboard = async (text) => {
  try {
    // Try modern Clipboard API first
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text)
      showCopySuccess()
      return
    }
  } catch (err) {
    console.log('Clipboard API failed, trying fallback method:', err)
  }

  // Fallback method using execCommand
  try {
    const textArea = document.createElement('textarea')
    textArea.value = text
    textArea.style.position = 'fixed'
    textArea.style.left = '-999999px'
    textArea.style.top = '-999999px'
    document.body.appendChild(textArea)
    textArea.focus()
    textArea.select()

    const successful = document.execCommand('copy')
    document.body.removeChild(textArea)

    if (successful) {
      showCopySuccess()
    } else {
      showCopyError()
    }
  } catch (err) {
    console.error('Fallback copy method also failed:', err)
    showCopyError()
  }
}

const showCopySuccess = () => {
  // Show the green "Copied" state
  copyState.value.isShowingCopied = true

  // Reset back to default state after 2 seconds
  setTimeout(() => {
    copyState.value.isShowingCopied = false
  }, 2000)
}

const showCopyError = () => {
  // For error case, briefly show red feedback
  console.error('Copy failed')
  // Could implement error state here if needed
}

// Touch handlers for modal drag-to-close
const handleTouchStart = (event) => {
  touchStartY.value = event.touches[0].clientY
  isDragging.value = true
}

const handleTouchMove = (event) => {
  if (!isDragging.value) return

  touchCurrentY.value = event.touches[0].clientY
  const deltaY = touchCurrentY.value - touchStartY.value

  // Only allow downward dragging
  if (deltaY > 0) {
    event.preventDefault()
    // Add visual feedback here if needed (modal following finger)
  }
}

const handleTouchEnd = (event) => {
  if (!isDragging.value) return

  const deltaY = touchCurrentY.value - touchStartY.value

  // Close modal if dragged down more than 100px
  if (deltaY > 100) {
    closeTransactionModal()
  }

  isDragging.value = false
  touchStartY.value = 0
  touchCurrentY.value = 0
}

const exportData = (format) => {
  const selectedData = selectedTransactions.value.map(index => transactions.value[index])

  if (format === 'csv') {
    exportToCSV(selectedData)
  } else if (format === 'pdf') {
    exportToPDF(selectedData)
  }

  showExportMenu.value = false
}

const exportToCSV = (data) => {
  const headers = ['Date', 'Time', 'Amount', 'Purchased', 'Contract ID', 'Rent Percentage']
  const csvContent = [
    headers.join(','),
    ...data.map(row => [
      row.date,
      row.time,
      row.amount,
      row.purchased,
      row.contractId,
      row.rentPercentage + '%'
    ].join(','))
  ].join('\n')

  const blob = new Blob([csvContent], { type: 'text/csv' })
  const url = window.URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'transactions.csv'
  a.click()
  window.URL.revokeObjectURL(url)
}

const exportToPDF = (data) => {
  // Simple PDF export - in a real app you'd use a library like jsPDF
  console.log('Exporting to PDF:', data)
  alert('PDF export functionality would be implemented here')
}

const formatCurrency = (amount) => {
  return amount.toLocaleString('en-US', { 
    minimumFractionDigits: 2, 
    maximumFractionDigits: 2 
  })
}

// Close export menu when clicking outside
const handleClickOutside = (event) => {
  if (showExportMenu.value && !event.target.closest('.export-btn')) {
    showExportMenu.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style scoped>
.rent-out-transaction-view {
  font-family: 'Montserrat', sans-serif;
}

.transaction-card {
  box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.04);
}

.export-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

/* Mobile first approach for Telegram mini app */
@media (max-width: 430px) {
  .rent-out-transaction-view {
    max-width: 100%;
  }
}

@media (min-width: 431px) and (max-width: 768px) {
  .rent-out-transaction-view {
    max-width: 400px;
  }
}

/* Scrollable content */
.content-container {
  max-height: calc(100vh - 140px);
  overflow-y: auto;
}

/* Custom scrollbar */
.content-container::-webkit-scrollbar {
  display: none;
}

.content-container {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

/* Telegram WebApp optimizations */
@media (max-height: 600px) {
  .content-container {
    max-height: calc(100vh - 120px);
  }

  .empty-state {
    min-height: calc(100vh - 180px) !important;
  }

  .transaction-card {
    padding: 12px;
  }
}

/* Mobile touch optimizations for Telegram */
.rent-out-transaction-view {
  -webkit-overflow-scrolling: touch;
  touch-action: manipulation;
}

/* Export dropdown responsive adjustments */
@media (max-width: 380px) {
  .export-btn {
    width: 120px;
    height: 48px;
  }

  .export-btn span {
    font-size: 0.875rem;
  }
}

/* Transaction modal optimizations for Telegram */
@media (max-height: 700px) {
  .transaction-modal .max-h-96 {
    max-height: 280px;
  }
}

/* Copy button fixed width to prevent layout shifts */
.copy-btn-default,
.copy-btn-copied {
  min-width: 70px;
  justify-content: center;
}

/* Touch-friendly targets for Telegram WebApp */
@media (pointer: coarse) {
  button {
    min-height: 44px;
    min-width: 44px;
  }

  .transaction-card {
    padding: 16px;
  }

  .modal-header-handle {
    padding: 8px;
    margin: -8px;
  }
}

/* Smooth animations */
.transaction-card {
  transition: all 0.2s ease-in-out;
}

.transaction-card:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
}

/* Modal animations */
@keyframes slide-up {
  from {
    transform: translateY(100%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.animate-slide-up {
  animation: slide-up 0.3s ease-out;
}

/* Checkbox animations */
.transition-colors {
  transition: all 0.2s ease-in-out;
}
</style>
