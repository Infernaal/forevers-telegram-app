<template>
  <div class="min-h-screen bg-gray-100 flex flex-col font-montserrat overflow-hidden">
    <!-- Content -->
    <div class="flex-1 px-2 py-4 sm:px-3 md:px-4 lg:px-6 xl:px-8 sm:py-6 overflow-y-auto scrollbar-hide pb-24" style="-webkit-overflow-scrolling: touch;">

      <!-- Header - Outside the card -->
      <h1 class="text-2xl md:text-3xl font-bold text-black mb-6 w-[95%] mx-auto">Income Calculator</h1>

      <div class="bg-white rounded-3xl border border-gray-200 shadow-sm px-4 sm:px-6 py-6 w-[96%] mx-auto relative">

        <!-- Basic Monthly Income Section -->
        <div class="mb-6">
          <h2 class="text-lg font-semibold text-dbd-dark mb-4">Basic monthly income in USD</h2>
          
          <!-- Input Section -->
          <div class="flex gap-2 mb-6">
            <!-- Amount Input -->
            <div class="flex items-center bg-dbd-off-white border border-gray-200 rounded-full px-3 py-2.5 h-11 flex-[0.5] sm:flex-1">
              <svg class="w-6 h-6 mr-2 text-blue-700 flex-shrink-0" viewBox="0 0 24 24" fill="currentColor">
                <path d="M23 5.536V1H5.347V6.759H1V11.294H5.347V22.581H10.421V17.046H14.712V12.510H10.421V11.294H18.849V6.759H10.421V5.536H23Z"/>
              </svg>
              <input
                v-model="monthlyIncome"
                type="number"
                placeholder="50"
                class="bg-transparent outline-none text-dbd-gray font-medium flex-1 min-w-0 text-sm"
              />
            </div>

            <!-- Currency Selector -->
            <div class="relative flex-shrink-0">
              <button
                @click="toggleCurrencyDropdown"
                class="flex items-center bg-white border border-gray-200 rounded-full px-3 py-2.5 h-11 gap-2 hover:bg-gray-50 transition-colors min-w-fit text-sm"
              >
                <div class="flex items-center gap-1.5">
                  <CountryFlag :country="selectedCurrency.country" size="medium" class="w-6 h-6 flex-shrink-0" />
                  <svg class="w-3.5 h-3.5 text-dbd-dark flex-shrink-0" viewBox="0 0 14 14" fill="currentColor">
                    <path d="M12.8602 1.40015H4.3802C4.00686 1.40015 3.7402 1.66681 3.7402 2.04015V4.65348H1.3402C0.966862 4.70681 0.700195 4.97348 0.700195 5.34681C0.700195 5.72015 0.966862 5.98681 1.3402 5.98681H3.7402V11.9601C3.7402 12.3335 4.00686 12.6001 4.3802 12.6001C4.75353 12.6001 5.0202 12.3335 5.0202 11.9601V9.18681H7.7402C8.11353 9.18681 8.3802 8.92015 8.3802 8.54681C8.3802 8.17348 8.11353 7.90681 7.7402 7.90681H5.0202V5.93348H10.1935C10.5669 5.93348 10.8335 5.66681 10.8335 5.29348C10.8335 4.92015 10.5669 4.65348 10.1935 4.65348H5.0202V2.68015H12.8069C13.1802 2.68015 13.4469 2.41348 13.4469 2.04015C13.4469 1.66681 13.2335 1.40015 12.8602 1.40015Z"/>
                  </svg>
                  <span class="text-sm font-medium text-dbd-dark">{{ selectedCurrency.code }}</span>
                  <span class="text-gray-400 text-sm">/</span>
                  <span class="text-sm font-medium text-dbd-primary">{{ selectedCurrency.rate }} USD</span>
                </div>
                <svg class="w-4 h-4 text-gray-400 ml-1 flex-shrink-0" :class="{ 'rotate-180': showCurrencyDropdown }" viewBox="0 0 16 16" fill="none">
                  <circle cx="8" cy="8" r="7.6" fill="white" stroke="#CFCFCF" stroke-width="0.8"/>
                  <path d="M4.7998 6.4001L7.9998 9.6001L11.1998 6.4001" stroke="#4D4F53" stroke-width="0.8" stroke-linecap="round"/>
                </svg>
              </button>

              <!-- Currency Dropdown -->
              <div v-if="showCurrencyDropdown" class="absolute top-full mt-1 left-0 w-64 bg-gradient-to-r from-purple-800 via-purple-900 to-purple-900 rounded-xl shadow-xl border border-purple-600 z-50 p-2 max-h-80 overflow-y-auto scrollbar-hide">
                <div v-for="currency in currencies" :key="currency.code"
                     @click="selectCurrency(currency)"
                     class="flex items-center justify-between p-2 rounded-lg hover:bg-white/10 cursor-pointer transition-colors">
                  <div class="flex items-center gap-2">
                    <CountryFlag :country="currency.country" size="medium" class="w-6 h-6 flex-shrink-0" />
                    <span class="text-white text-sm font-medium">{{ currency.code }}</span>
                  </div>
                  <span class="text-yellow-400 text-sm font-medium">{{ currency.rate }} USD</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Investment Display -->
          <div class="bg-dbd-light-blue border border-purple-200 rounded-2xl p-4 mb-6">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-white border border-purple-300 rounded-full flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-dbd-primary" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M11.8515 24C11.5488 24 11.2984 23.9056 11.1004 23.7167C10.9025 23.5278 10.8035 23.2889 10.8035 23V21.2C9.68559 21.0222 8.73071 20.6444 7.93886 20.0667C7.14702 19.4889 6.52984 18.7556 6.08734 17.8667C5.97089 17.6222 5.97089 17.3667 6.08734 17.1C6.20378 16.8333 6.40175 16.6444 6.68122 16.5333C6.93741 16.4222 7.19942 16.4222 7.46725 16.5333C7.73508 16.6444 7.93886 16.8222 8.0786 17.0667C8.49782 17.8222 9.04512 18.3889 9.72052 18.7667C10.3959 19.1444 11.1761 19.3333 12.0611 19.3333C13.179 19.3333 14.099 19.0667 14.821 18.5333C15.5429 18 15.9039 17.2667 15.9039 16.3333C15.9039 15.3556 15.5837 14.6 14.9432 14.0667C14.3028 13.5333 13.0975 12.9889 11.3275 12.4333C9.65065 11.9222 8.39883 11.2444 7.57205 10.4C6.74527 9.55556 6.33188 8.5 6.33188 7.23333C6.33188 6.01111 6.74527 4.98889 7.57205 4.16667C8.39883 3.34444 9.47598 2.87778 10.8035 2.76667V1C10.8035 0.711111 10.9025 0.472222 11.1004 0.283333C11.2984 0.0944446 11.5488 0 11.8515 0C12.1543 0 12.4047 0.0944446 12.6026 0.283333C12.8006 0.472222 12.8996 0.711111 12.8996 1V2.76667C13.738 2.87778 14.4891 3.12222 15.1528 3.5C15.8166 3.87778 16.3697 4.36667 16.8122 4.96667C16.9753 5.18889 17.0102 5.42778 16.917 5.68333C16.8239 5.93889 16.6376 6.12222 16.3581 6.23333C16.1019 6.34444 15.8341 6.35556 15.5546 6.26667C15.2751 6.17778 15.0422 6.01111 14.8559 5.76667C14.5298 5.36667 14.1281 5.07222 13.6507 4.88333C13.1732 4.69444 12.5968 4.6 11.9214 4.6C10.8501 4.6 10 4.83333 9.37118 5.3C8.74236 5.76667 8.42795 6.4 8.42795 7.2C8.42795 8.04444 8.77729 8.72778 9.47598 9.25C10.1747 9.77222 11.4672 10.3111 13.3537 10.8667C14.9374 11.3333 16.1077 12.0056 16.8646 12.8833C17.6215 13.7611 18 14.8667 18 16.2C18 17.6 17.5691 18.7278 16.7074 19.5833C15.8457 20.4389 14.5764 20.9889 12.8996 21.2333V23C12.8996 23.2889 12.8006 23.5278 12.6026 23.7167C12.4047 23.9056 12.1543 24 11.8515 24Z"/>
                </svg>
              </div>
              <div class="flex-1">
                <div class="text-sm text-dbd-gray">
                  <span class="text-red-500 font-medium">Invested</span>
                  <span> in Forevers UAE</span>
                </div>
              </div>
              <div class="text-right">
                <div class="text-lg font-semibold text-dbd-dark">{{ calculatedInvestment }} USD</div>
              </div>
            </div>
          </div>

          <!-- Comparison Section -->
          <div class="mb-6">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 bg-white border border-dbd-primary rounded-full flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-dbd-primary" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M15 9.75C15 10.7446 15.3951 11.6984 16.0983 12.4017C16.8016 13.1049 17.7554 13.5 18.75 13.5C19.7446 13.5 20.6984 13.1049 21.4017 12.4017C22.1049 11.6984 22.5 10.7446 22.5 9.75C22.5 9.63355 22.4729 9.51869 22.4209 9.41453L19.4209 3.41453C19.3401 3.25302 19.2038 3.12606 19.037 3.05698C18.8701 2.9879 18.684 2.98133 18.5127 3.03848L13.7646 4.62098C13.5016 4.28658 13.1501 4.03267 12.75 3.88808V1.5H11.25V3.88808C10.8198 4.04023 10.4461 4.31982 10.1788 4.68961C9.91138 5.0594 9.76298 5.50185 9.7533 5.95807L5.0127 7.53832C4.82403 7.60123 4.66808 7.7365 4.57913 7.91437L1.57913 13.9144C1.52704 14.0186 1.49995 14.1335 1.5 14.25C1.5 15.2446 1.89509 16.1984 2.59835 16.9017C3.30161 17.6049 4.25544 18 5.25 18C6.24456 18 7.19839 17.6049 7.90165 16.9017C8.60491 16.1984 9 15.2446 9 14.25C9.00003 14.1335 8.97294 14.0187 8.92087 13.9145L6.3075 8.688L10.2353 7.3788C10.4982 7.71327 10.8498 7.96716 11.25 8.11155V21H4.5V22.5H19.5V21H12.75V8.11192C13.1802 7.95975 13.5538 7.68016 13.8212 7.31037C14.0886 6.94059 14.237 6.49814 14.2467 6.04192L17.2692 5.03408L15.0792 9.41468C15.0271 9.51879 15 9.63359 15 9.75ZM5.25 16.5C4.78629 16.4984 4.33443 16.3534 3.9564 16.0849C3.57838 15.8163 3.29271 15.4374 3.1386 15H7.3611C7.207 15.4373 6.92138 15.8162 6.54342 16.0848C6.16545 16.3533 5.71366 16.4984 5.25 16.5ZM7.03658 13.5H3.46342L5.25 9.92723L7.03658 13.5ZM12 6.75C11.8517 6.75 11.7067 6.70601 11.5833 6.6236C11.46 6.54119 11.3639 6.42406 11.3071 6.28701C11.2503 6.14997 11.2355 5.99917 11.2644 5.85368C11.2933 5.7082 11.3648 5.57456 11.4697 5.46967C11.5746 5.36478 11.7082 5.29335 11.8537 5.26441C11.9992 5.23547 12.15 5.25032 12.287 5.30709C12.4241 5.36386 12.5412 5.45999 12.6236 5.58332C12.706 5.70666 12.75 5.85166 12.75 6C12.7498 6.19886 12.6707 6.38952 12.5301 6.53013C12.3895 6.67075 12.1989 6.74982 12 6.75ZM18.75 12C18.2863 11.9984 17.8344 11.8534 17.4564 11.5848C17.0784 11.3163 16.7927 10.9373 16.6386 10.5H20.8611C20.707 10.9373 20.4214 11.3162 20.0434 11.5848C19.6655 11.8533 19.2137 11.9984 18.75 12ZM18.75 5.42722L20.5366 9H16.9634L18.75 5.42722Z"/>
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-dbd-dark">Compare Forevers annual returns with:</h3>
            </div>

            <!-- Comparison Cards -->
            <div class="space-y-2">
              <!-- Bank Deposit -->
              <div class="bg-dbd-light-blue rounded-2xl p-4 relative">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 bg-white border border-dbd-primary rounded-full flex items-center justify-center flex-shrink-0">
                    <svg class="w-6 h-6 text-dbd-primary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M3.66667 15.125V12.3451M9.22222 15.125V12.3451M14.7778 15.125V12.3451M20.3333 15.125V12.3451M2 18.6667H22V22H2V18.6667ZM2 8.66667V6.44444L11.589 2L22 6.44444V8.66667H2Z"/>
                    </svg>
                  </div>
                  <div class="flex-1">
                    <div class="text-sm text-dbd-gray">Deposit at 3.5% annual Interest Rate</div>
                  </div>
                  <button class="w-6 h-6 bg-transparent rounded-full flex items-center justify-center hover:bg-gray-50 flex-shrink-0">
                    <svg class="w-5 h-5 text-dbd-gray" viewBox="0 0 20 20" fill="currentColor">
                      <path d="M10 2C5.5888 2 2 5.58885 2 10C2 14.4112 5.5888 18 10 18C14.4112 18 18 14.4112 18 10C18 5.58885 14.4112 2 10 2ZM10 16.5455C6.39079 16.5455 3.45455 13.6092 3.45455 10C3.45455 6.39088 6.39079 3.45455 10 3.45455C13.6092 3.45455 16.5455 6.39088 16.5455 10C16.5455 13.6092 13.6092 16.5455 10 16.5455Z"/>
                      <path d="M9.99978 5.39453C9.46518 5.39453 9.03027 5.82973 9.03027 6.36466C9.03027 6.89911 9.46518 7.33393 9.99978 7.33393C10.5344 7.33393 10.9693 6.89911 10.9693 6.36466C10.9693 5.82973 10.5344 5.39453 9.99978 5.39453Z"/>
                      <path d="M9.99973 8.78711C9.59809 8.78711 9.27246 9.11273 9.27246 9.51438V13.878C9.27246 14.2797 9.59809 14.6053 9.99973 14.6053C10.4014 14.6053 10.727 14.2797 10.727 13.878V9.51438C10.727 9.11273 10.4014 8.78711 9.99973 8.78711Z"/>
                    </svg>
                  </button>
                </div>
                <div class="border-t border-white mt-3 pt-3">
                  <div class="text-center text-lg font-semibold text-dbd-dark">{{ bankDepositReturn }} USD</div>
                </div>
              </div>

              <!-- Residential Real Estate -->
              <div class="bg-dbd-light-blue rounded-2xl p-4 relative">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 bg-white border border-dbd-primary rounded-full flex items-center justify-center flex-shrink-0">
                    <svg class="w-6 h-6 text-dbd-primary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M8.66667 22V14.392C8.66667 13.6917 9.26362 13.124 10 13.124H14C14.7364 13.124 15.3333 13.6917 15.3333 14.392V22M11.2273 2.23464L2.56063 8.09559C2.20891 8.33345 2 8.7185 2 9.12895V20.098C2 21.1484 2.89543 22 4 22H20C21.1046 22 22 21.1484 22 20.098V9.12895C22 8.7185 21.7911 8.33345 21.4394 8.09559L12.7727 2.23464C12.3101 1.92179 11.6899 1.92179 11.2273 2.23464Z"/>
                    </svg>
                  </div>
                  <div class="flex-1">
                    <div class="text-sm text-dbd-gray">Investments in Residential Real Estate at 5%</div>
                  </div>
                  <button class="w-6 h-6 bg-transparent rounded-full flex items-center justify-center hover:bg-gray-50 flex-shrink-0">
                    <svg class="w-5 h-5 text-dbd-gray" viewBox="0 0 20 20" fill="currentColor">
                      <path d="M10 2C5.5888 2 2 5.58885 2 10C2 14.4112 5.5888 18 10 18C14.4112 18 18 14.4112 18 10C18 5.58885 14.4112 2 10 2ZM10 16.5455C6.39079 16.5455 3.45455 13.6092 3.45455 10C3.45455 6.39088 6.39079 3.45455 10 3.45455C13.6092 3.45455 16.5455 6.39088 16.5455 10C16.5455 13.6092 13.6092 16.5455 10 16.5455Z"/>
                      <path d="M9.99978 5.39453C9.46518 5.39453 9.03027 5.82973 9.03027 6.36466C9.03027 6.89911 9.46518 7.33393 9.99978 7.33393C10.5344 7.33393 10.9693 6.89911 10.9693 6.36466C10.9693 5.82973 10.5344 5.39453 9.99978 5.39453Z"/>
                      <path d="M9.99973 8.78711C9.59809 8.78711 9.27246 9.11273 9.27246 9.51438V13.878C9.27246 14.2797 9.59809 14.6053 9.99973 14.6053C10.4014 14.6053 10.727 14.2797 10.727 13.878V9.51438C10.727 9.11273 10.4014 8.78711 9.99973 8.78711Z"/>
                    </svg>
                  </button>
                </div>
                <div class="border-t border-white mt-3 pt-3">
                  <div class="text-center text-lg font-semibold text-dbd-dark">{{ residentialReturn }} USD</div>
                </div>
              </div>

              <!-- Commercial Real Estate -->
              <div class="bg-dbd-light-blue rounded-2xl p-4 relative">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 bg-white border border-dbd-primary rounded-full flex items-center justify-center flex-shrink-0">
                    <svg class="w-6 h-6 text-dbd-primary" viewBox="0 0 24 24" fill="currentColor">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M12.479 5.92287C12.6507 6.06536 12.75 6.27689 12.75 6.50001V22C12.75 22.4142 12.4142 22.75 12 22.75H4C3.58579 22.75 3.25 22.4142 3.25 22V8.00001C3.25 7.63909 3.50705 7.32936 3.86178 7.26285L11.8618 5.76285C12.0811 5.72173 12.3073 5.78039 12.479 5.92287ZM4.75 8.62245V21.25H11.25V7.4037L4.75 8.62245Z"/>
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M11.521 1.42287C11.3493 1.56536 11.25 1.77689 11.25 2.00001V22C11.25 22.4142 11.5858 22.75 12 22.75H20C20.4142 22.75 20.75 22.4142 20.75 22V9.05969C20.75 8.64548 20.4142 8.30969 20 8.30969C19.5858 8.30969 19.25 8.64548 19.25 9.05969V21.25H12.75V2.9037L19.25 4.12245V4.98027C19.25 5.39449 19.5858 5.73027 20 5.73027C20.4142 5.73027 20.75 5.39449 20.75 4.98027V3.50001C20.75 3.13909 20.4929 2.82936 20.1382 2.76285L12.1382 1.26285C11.9189 1.22173 11.6927 1.28039 11.521 1.42287Z"/>
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M5.75 16C5.75 15.5858 6.08579 15.25 6.5 15.25H9.5C9.91421 15.25 10.25 15.5858 10.25 16V22C10.25 22.4142 9.91421 22.75 9.5 22.75H6.5C6.08579 22.75 5.75 22.4142 5.75 22V16ZM7.25 16.75V21.25H8.75V16.75H7.25Z"/>
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M5.75 11.5C5.75 11.0858 6.08579 10.75 6.5 10.75H9.5C9.91421 10.75 10.25 11.0858 10.25 11.5C10.25 11.9142 9.91421 12.25 9.5 12.25H6.5C6.08579 12.25 5.75 11.9142 5.75 11.5Z"/>
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M13.75 7C13.75 6.58579 14.0858 6.25 14.5 6.25H17.5C17.9142 6.25 18.25 6.58579 18.25 7C18.25 7.41421 17.9142 7.75 17.5 7.75H14.5C14.0858 7.75 13.75 7.41421 13.75 7Z"/>
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M13.75 11.5C13.75 11.0858 14.0858 10.75 14.5 10.75H17.5C17.9142 10.75 18.25 11.0858 18.25 11.5C18.25 11.9142 17.9142 12.25 17.5 12.25H14.5C14.0858 12.25 13.75 11.9142 13.75 11.5Z"/>
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M1.25 22C1.25 21.5858 1.58579 21.25 2 21.25H22C22.4142 21.25 22.75 21.5858 22.75 22C22.75 22.4142 22.4142 22.75 22 22.75H2C1.58579 22.75 1.25 22.4142 1.25 22Z"/>
                    </svg>
                  </div>
                  <div class="flex-1">
                    <div class="text-sm text-dbd-gray">Investments in Commercial Real Estate at 8%</div>
                  </div>
                  <button class="w-6 h-6 bg-transparent rounded-full flex items-center justify-center hover:bg-gray-50 flex-shrink-0">
                    <svg class="w-5 h-5 text-dbd-gray" viewBox="0 0 20 20" fill="currentColor">
                      <path d="M10 2C5.5888 2 2 5.58885 2 10C2 14.4112 5.5888 18 10 18C14.4112 18 18 14.4112 18 10C18 5.58885 14.4112 2 10 2ZM10 16.5455C6.39079 16.5455 3.45455 13.6092 3.45455 10C3.45455 6.39088 6.39079 3.45455 10 3.45455C13.6092 3.45455 16.5455 6.39088 16.5455 10C16.5455 13.6092 13.6092 16.5455 10 16.5455Z"/>
                      <path d="M9.99978 5.39453C9.46518 5.39453 9.03027 5.82973 9.03027 6.36466C9.03027 6.89911 9.46518 7.33393 9.99978 7.33393C10.5344 7.33393 10.9693 6.89911 10.9693 6.36466C10.9693 5.82973 10.5344 5.39453 9.99978 5.39453Z"/>
                      <path d="M9.99973 8.78711C9.59809 8.78711 9.27246 9.11273 9.27246 9.51438V13.878C9.27246 14.2797 9.59809 14.6053 9.99973 14.6053C10.4014 14.6053 10.727 14.2797 10.727 13.878V9.51438C10.727 9.11273 10.4014 8.78711 9.99973 8.78711Z"/>
                    </svg>
                  </button>
                </div>
                <div class="border-t border-white mt-3 pt-3">
                  <div class="text-center text-lg font-semibold text-dbd-dark">{{ commercialReturn }} USD</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Investment Promotion Section -->
        <div class="bg-dbd-light-blue border border-purple-200 rounded-xl p-4 mt-6">
          <h3 class="text-center text-xl font-bold mb-3 leading-tight">
            <span class="text-dbd-primary">Forevers UAE</span>: A Smarter
            <br><span class="text-red-500">Investment</span> Opportunity
          </h3>
          
          <!-- Placeholder for logo/icon -->
          <div class="w-22 h-22 mx-auto my-4 bg-gray-200 rounded-full"></div>
          
          <p class="text-center text-dbd-dark mb-4 text-base leading-relaxed">
            Forevers UAE offers a unique <span class="text-red-500">investment</span> opportunity with higher earning potential and lower entry thresholds compared to traditional options like bank deposits or real estate.
          </p>
          
          <button class="w-full bg-gradient-to-r from-dbd-primary to-purple-600 text-white font-bold py-3 px-6 rounded-full hover:from-purple-700 hover:to-purple-800 transition-all duration-300">
            <span class="text-red-500">Invested</span> Now
          </button>
        </div>
      </div>
    </div>

    <!-- Bottom Navigation -->
    <div class="mt-auto">
      <BottomNavigation />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import BottomNavigation from '../components/BottomNavigation.vue'
import CountryFlag from '../components/CountryFlag.vue'

// Reactive data
const monthlyIncome = ref(50)
const showCurrencyDropdown = ref(false)
const selectedCurrency = ref({
  code: 'UAE',
  name: 'United Arab Emirates',
  country: 'uae',
  rate: '9'
})

// Currency options
const currencies = ref([
  { code: 'UAE', name: 'United Arab Emirates', country: 'uae', rate: '9' },
  { code: 'KZ', name: 'Kazakhstan', country: 'kz', rate: '8' },
  { code: 'DE', name: 'Germany', country: 'germany', rate: '4' },
  { code: 'PL', name: 'Poland', country: 'poland', rate: '4' },
  { code: 'UA', name: 'Ukraine', country: 'ukraine', rate: '4' },
  { code: 'PL2', name: 'Poland', country: 'poland', rate: '1' }
])

// Computed values
const calculatedInvestment = computed(() => {
  const investment = monthlyIncome.value * parseFloat(selectedCurrency.value.rate) * 12
  return investment.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })
})

const bankDepositReturn = computed(() => {
  const annualIncome = monthlyIncome.value * 12
  const return5Years = annualIncome * 5 * 1.035
  return return5Years.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })
})

const residentialReturn = computed(() => {
  const annualIncome = monthlyIncome.value * 12
  const return5Years = annualIncome * 5 * 1.05
  return return5Years.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })
})

const commercialReturn = computed(() => {
  const annualIncome = monthlyIncome.value * 12
  const return5Years = annualIncome * 5 * 1.08
  return return5Years.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })
})

// Methods
const toggleCurrencyDropdown = () => {
  showCurrencyDropdown.value = !showCurrencyDropdown.value
}

const selectCurrency = (currency) => {
  selectedCurrency.value = currency
  showCurrencyDropdown.value = false
}

// Close dropdown when clicking outside
const handleClickOutside = (event) => {
  if (!event.target.closest('.relative')) {
    showCurrencyDropdown.value = false
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
/* Custom width for containers */
.w-22 {
  width: 5.5rem;
}

.h-22 {
  height: 5.5rem;
}

/* Hide scrollbar while maintaining scroll functionality */
.scrollbar-hide {
  -ms-overflow-style: none;  /* Internet Explorer 10+ */
  scrollbar-width: none;  /* Firefox */
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;  /* Safari and Chrome */
}

/* Touch scrolling for mobile */
.scrollbar-hide {
  -webkit-overflow-scrolling: touch;
}

/* Ensure proper responsive design */
@media (max-width: 640px) {
  .max-w-sm {
    max-width: 24rem;
  }

  .px-3\.5 {
    padding-left: 0.875rem;
    padding-right: 0.875rem;
  }
}

@media (max-width: 480px) {
  .max-w-sm {
    max-width: calc(100vw - 1.75rem);
  }

  .text-xl {
    font-size: 1.125rem;
    line-height: 1.75rem;
  }

  .text-lg {
    font-size: 1rem;
    line-height: 1.5rem;
  }
}

/* Tablet and desktop responsive adjustments */
@media (min-width: 768px) {
  .max-w-sm {
    max-width: 42rem;
  }
}

@media (min-width: 1024px) {
  .max-w-sm {
    max-width: 56rem;
  }
}

@media (min-width: 1280px) {
  .max-w-sm {
    max-width: 72rem;
  }
}

/* Custom scrollbar for dropdown */
.overflow-y-auto::-webkit-scrollbar {
  width: 4px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.3);
  border-radius: 4px;
}

.overflow-y-auto::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.5);
}

/* Smooth transitions */
.transition-all {
  transition: all 0.3s ease;
}

/* Responsive text adjustments */
@media (max-width: 375px) {
  .text-sm {
    font-size: 0.8rem;
    line-height: 1.25rem;
  }

  .gap-3 {
    gap: 0.5rem;
  }

  .p-4 {
    padding: 0.75rem;
  }
}

/* Input focus styles */
input:focus {
  outline: none;
}

/* Button hover effects */
button:hover {
  transform: translateY(-1px);
}

button:active {
  transform: translateY(0);
}
</style>
