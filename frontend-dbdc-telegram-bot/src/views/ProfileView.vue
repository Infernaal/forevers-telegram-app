<template>
  <div class="min-h-screen bg-gradient-to-br from-[#120B81] via-[#1A1086] to-[#09074E] relative overflow-hidden">
    <!-- Profile Header Section -->
    <div class="px-4 pt-12 pb-6">
      <div class="bg-[#605F87]/24 border border-[#D8D8D8]/30 backdrop-blur-sm rounded-[50px_20px_20px_50px] p-5">
        <div class="flex items-center gap-4">
          <!-- Large Avatar -->
          <div class="relative flex-shrink-0">
            <div class="w-20 h-20 rounded-full border border-[#7E73D6] overflow-hidden">
              <img 
                :src="profileData.avatar" 
                :alt="profileData.name"
                class="w-full h-full object-cover"
              />
            </div>
          </div>
          
          <!-- User Info -->
          <div class="flex-1 min-w-0">
            <!-- Silver Badge -->
            <div class="flex items-center gap-2 mb-3">
              <div class="flex items-center gap-2 px-4 py-1.5 bg-[#6E6BA9]/90 border border-[#2019CE] rounded-3xl backdrop-blur-sm">
                <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M14.0004 26.2497C7.24592 26.2497 1.75073 20.7545 1.75073 14.0001C1.75073 7.24564 7.24592 1.75085 14.0004 1.75085C20.7548 1.75085 26.25 7.24564 26.25 14.0001C26.25 20.7545 20.7544 26.2497 14.0004 26.2497Z" fill="white"/>
                  <path d="M20.2071 5.37145C20.73 5.37145 21.2468 5.39833 21.7567 5.4472C19.7049 3.58479 16.9828 2.44812 14 2.44812C7.63041 2.44812 2.448 7.63013 2.448 14.0001C2.448 16.2735 3.11102 18.3941 4.24973 20.1832C4.86143 11.9015 11.769 5.37145 20.2071 5.37145Z" fill="#E0E0E0"/>
                  <path d="M14.0006 25.5519C20.3702 25.5519 25.5526 20.3699 25.5526 13.9999C25.5526 10.6131 24.0873 7.56229 21.7577 5.44697C21.2478 5.39809 20.731 5.37122 20.2081 5.37122C11.7704 5.37122 4.86244 11.9017 4.25073 20.1829C6.30211 23.4072 9.90475 25.5519 14.0006 25.5519Z" fill="#B5B5B5"/>
                  <path d="M14.0004 23.1368C19.0464 23.1368 23.1369 19.0463 23.1369 14.0003C23.1369 8.95433 19.0464 4.86377 14.0004 4.86377C8.95445 4.86377 4.86389 8.95433 4.86389 14.0003C4.86389 19.0463 8.95445 23.1368 14.0004 23.1368Z" fill="#9E9E9E"/>
                  <path d="M19.4965 12.7667L15.6984 12.2148L14.0001 8.77307L12.3014 12.2148L8.50366 12.7667L11.2519 15.4452L10.6031 19.2279L14.0001 17.4421L17.397 19.2279L16.7483 15.4452L19.4965 12.7667Z" fill="#F6F6F6"/>
                  <path d="M19.4971 12.7667L15.699 12.2144L14.0007 8.77307V17.4421L17.3977 19.2279L16.7489 15.4452L19.4971 12.7667Z" fill="#E0E0E0"/>
                </svg>
                <span class="text-[#FAFAFA] text-sm font-medium">Silver</span>
              </div>
            </div>
            <h1 class="text-white text-xl font-bold leading-tight">{{ profileData.name }}</h1>
          </div>
        </div>
      </div>
    </div>

    <!-- Menu Items Section with invisible scroll -->
    <div class="px-6 relative">
      <!-- Gradient fade at bottom -->
      <div class="absolute bottom-0 left-0 right-0 h-12 bg-gradient-to-t from-[#120B81] via-[#120B81]/90 to-transparent pointer-events-none z-10"></div>
      
      <div 
        class="space-y-1 overflow-y-auto scroll-smooth touch-scroll"
        style="height: calc(100vh - 360px);"
      >
        <!-- Calculator -->
        <div @click="handleMenuClick('calculator')" class="flex items-center gap-3 px-3 py-3 hover:bg-white/10 rounded-lg cursor-pointer transition-all active:scale-95 touch-target">
          <div class="w-10 h-10 bg-[#404040]/24 border border-white rounded-full flex items-center justify-center flex-shrink-0">
            <svg width="18" height="18" viewBox="0 0 16 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M14.1377 0C15.1645 0 16 0.788555 16 1.75781V18.2422C16 19.2114 15.1645 20 14.1377 20H1.8623C0.835502 20 0 19.2114 0 18.2422V1.75781C0 0.788555 0.835502 0 1.8623 0H14.1377ZM1.8623 1.17188C1.52004 1.17188 1.24121 1.43473 1.24121 1.75781V18.2422C1.24121 18.5653 1.52004 18.8281 1.8623 18.8281H14.1377C14.48 18.8281 14.7587 18.5653 14.7588 18.2422V1.75781C14.7588 1.43473 14.48 1.17188 14.1377 1.17188H1.8623Z" fill="white"/>
            </svg>
          </div>
          <span class="text-white font-medium text-base">Calculator</span>
        </div>

        <!-- Ambassador -->
        <div @click="handleMenuClick('ambassador')" class="flex items-center gap-3 px-3 py-3 hover:bg-white/10 rounded-lg cursor-pointer transition-all active:scale-95 touch-target">
          <div class="w-10 h-10 bg-[#404040]/24 border border-white rounded-full flex items-center justify-center flex-shrink-0">
            <svg width="16" height="16" viewBox="0 0 14 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M7 9.64844C9.76508 9.64858 12.0066 11.9652 12.0068 14.8242C12.0068 17.6826 9.76511 19.9999 7 20C4.23394 20 1.99219 17.6827 1.99219 14.8242C1.99243 11.9651 4.23409 9.64844 7 9.64844ZM6.09668 13.8418L4.07715 14.1465L5.53906 15.6182L5.19434 17.6992L7 16.7168L8.80566 17.6992L8.46191 15.6182L9.92383 14.1465L7.90332 13.8418L7 11.9512L6.09668 13.8418ZM4.60547 0L7 3.30078L9.39453 0H14L7 9.64844L0 0H4.60547Z" fill="white"/>
            </svg>
          </div>
          <span class="text-white font-medium text-base">Ambassador</span>
        </div>

        <!-- Verification with Badge -->
        <div @click="handleMenuClick('verification')" class="flex items-center gap-3 px-3 py-3 hover:bg-white/10 rounded-lg cursor-pointer transition-all active:scale-95 touch-target">
          <div class="w-10 h-10 bg-[#404040]/24 border border-white rounded-full flex items-center justify-center flex-shrink-0">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M9 12.75L11.25 15L15 9.75M21 12C21 16.5563 16.5563 21 12 21C7.44365 21 3 16.5563 3 12C3 7.44365 7.44365 3 12 3C16.5563 3 21 7.44365 21 12Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <span class="text-white font-medium text-base flex-1">Verification</span>
          <!-- Red X Badge -->
          <div class="w-5 h-5 bg-red-500 rounded-full flex items-center justify-center flex-shrink-0">
            <svg width="10" height="10" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M9 3L3 9M3 3L9 9" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
        </div>

        <!-- Security -->
        <div @click="handleMenuClick('security')" class="flex items-center gap-3 px-3 py-3 hover:bg-white/10 rounded-lg cursor-pointer transition-all active:scale-95 touch-target">
          <div class="w-10 h-10 bg-[#404040]/24 border border-white rounded-full flex items-center justify-center flex-shrink-0">
            <svg width="16" height="16" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M8.78516 0.0354746C8.92389 -0.0121504 9.07611 -0.0121504 9.21484 0.0354746C10.6561 0.531013 12.1438 0.945188 13.6377 1.26497C14.8838 1.5317 16.1601 1.73823 17.4297 1.87922C17.7546 1.91522 18 2.18263 18 2.50032V8.7386C17.9998 13.165 15.3282 17.2234 11.1943 19.0784L9.26953 19.9427C9.18416 19.9808 9.09193 20.0003 9 20.0003C8.90802 20.0003 8.81583 19.9808 8.73047 19.9427L6.80566 19.0784C2.67178 17.2233 0.000192532 13.165 0 8.7386V2.50032C0 2.18263 0.245411 1.91529 0.570312 1.87922C1.83994 1.73823 3.11627 1.53164 4.3623 1.26497C5.85626 0.945192 7.34396 0.531005 8.78516 0.0354746Z" fill="white"/>
            </svg>
          </div>
          <span class="text-white font-medium text-base">Security</span>
        </div>

        <!-- Settings -->
        <div @click="handleMenuClick('settings')" class="flex items-center gap-3 px-3 py-3 hover:bg-white/10 rounded-lg cursor-pointer transition-all active:scale-95 touch-target">
          <div class="w-10 h-10 bg-[#404040]/24 border border-white rounded-full flex items-center justify-center flex-shrink-0">
            <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12.2222 20L12.3457 19.375L12.8148 17.0913C13.5679 16.8029 14.2469 16.3972 14.8642 15.9135L17.1605 16.6827L17.7778 16.875L18.0988 16.3221L19.679 13.6778L20 13.125L19.5309 12.7163L17.7531 11.2019C17.8179 10.8083 17.9012 10.4147 17.9012 10C17.9012 9.58531 17.8179 9.19169 17.7531 8.79808L19.5309 7.28369L20 6.875L19.679 6.32215L18.0988 3.67785L17.7778 3.125L17.1605 3.31731L14.8642 4.08654C14.2469 3.60277 13.5679 3.19708 12.8148 2.90862L12.3457 0.625L12.2222 0H7.77775L7.65426 0.625L7.18516 2.90862C6.43209 3.19708 5.75306 3.60277 5.13581 4.08654L2.83947 3.31731L2.22215 3.125L1.9012 3.67785L0.32095 6.32215L0 6.875L0.469097 7.28369L2.24688 8.79808C2.18209 9.19169 2.09873 9.58531 2.09873 10C2.09873 10.4147 2.18209 10.8083 2.24688 11.2019L0.469097 12.7163L0 13.125L0.32095 13.6778L1.9012 16.3221L2.22215 16.875L2.83947 16.6827L5.13581 15.9135C5.75306 16.3972 6.43209 16.8029 7.18516 17.0913L7.65426 19.375L7.77775 20H12.2222Z" fill="white"/>
            </svg>
          </div>
          <span class="text-white font-medium text-base">Settings</span>
        </div>

        <!-- Support -->
        <div @click="handleMenuClick('support')" class="flex items-center gap-3 px-3 py-3 hover:bg-white/10 rounded-lg cursor-pointer transition-all active:scale-95 touch-target">
          <div class="w-10 h-10 bg-[#404040]/24 border border-white rounded-full flex items-center justify-center flex-shrink-0">
            <svg width="16" height="16" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M8.99902 0C13.9325 0 17.998 3.80872 17.998 8.58691V10.1348C17.9981 10.1411 17.999 10.1479 17.999 10.1543V12.9561C17.9992 12.9624 18 12.9692 18 12.9756V14.543C17.9997 16.724 16.1499 18.4277 13.9502 18.4277H11.2695C10.9422 19.3551 10.0281 19.9951 8.99902 19.9951C7.71066 19.9949 6.59988 18.993 6.59961 17.6777C6.59962 16.3623 7.71051 15.3606 8.99902 15.3604C10.0286 15.3604 10.9435 15.9998 11.2705 16.9277H13.9502C15.1589 16.9277 16.1261 16.1539 16.4111 15.1514C16.155 15.2407 15.8817 15.293 15.5986 15.293C14.3103 15.2927 13.1995 14.2908 13.1992 12.9756V10.1543C13.1992 8.83884 14.3101 7.83714 15.5986 7.83691C15.9032 7.83691 16.1972 7.89422 16.4697 7.99707C16.1535 4.38853 12.9637 1.5 8.99902 1.5C5.03445 1.50011 1.84359 4.38856 1.52734 7.99707C1.80001 7.89396 2.09449 7.83697 2.39941 7.83691C3.6881 7.83691 4.7998 8.83869 4.7998 10.1543V12.9756C4.79953 14.291 3.68794 15.293 2.39941 15.293C1.11107 15.2927 0.000274862 14.2908 0 12.9756V8.58691C4.31105e-05 3.80879 4.0657 0.000121624 8.99902 0Z" fill="white"/>
            </svg>
          </div>
          <span class="text-white font-medium text-base">Support</span>
        </div>

        <!-- Help -->
        <div @click="handleMenuClick('help')" class="flex items-center gap-3 px-3 py-3 hover:bg-white/10 rounded-lg cursor-pointer transition-all active:scale-95 touch-target">
          <div class="w-10 h-10 bg-[#404040]/24 border border-white rounded-full flex items-center justify-center flex-shrink-0">
            <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M9.69301 13.4082C9.12117 13.4082 8.6582 13.8848 8.6582 14.4566C8.6582 15.0149 9.10754 15.5051 9.69301 15.5051C10.2785 15.5051 10.7414 15.0149 10.7414 14.4566C10.7414 13.8848 10.2649 13.4082 9.69301 13.4082Z" fill="white"/>
              <path d="M9.86984 5.46875C8.03168 5.46875 7.1875 6.55801 7.1875 7.29328C7.1875 7.82434 7.6368 8.06941 8.00445 8.06941C8.73969 8.06941 8.44016 7.02098 9.82898 7.02098C10.5098 7.02098 11.0545 7.32055 11.0545 7.94687C11.0545 8.68219 10.292 9.10426 9.84262 9.48551C9.44777 9.8259 8.93035 10.3842 8.93035 11.5552C8.93035 12.2632 9.12094 12.4674 9.67922 12.4674C10.3464 12.4674 10.4825 12.1679 10.4825 11.9092C10.4825 11.2011 10.4962 10.7927 11.2451 10.2072C11.6127 9.92125 12.7701 8.99535 12.7701 7.71543C12.7701 6.43551 11.6127 5.46875 9.86984 5.46875Z" fill="white"/>
              <path d="M10 0C4.47328 0 0 4.47254 0 10V19.2188C0 19.6502 0.349766 20 0.78125 20H10C15.5267 20 20 15.5275 20 10C20 4.47328 15.5275 0 10 0ZM10 18.4375H1.5625V10C1.5625 5.33684 5.33621 1.5625 10 1.5625C14.6632 1.5625 18.4375 5.33621 18.4375 10C18.4375 14.6632 14.6638 18.4375 10 18.4375Z" fill="white"/>
            </svg>
          </div>
          <span class="text-white font-medium text-base">Help</span>
        </div>
      </div>
    </div>

    <!-- Beautiful Bottom Section -->
    <div class="px-6 pb-6 mt-auto">
      <div class="flex items-center gap-4">
        <!-- Elegant ID Card with Copy -->
        <div class="flex-1 relative">
          <!-- Base Card -->
          <div
            class="bg-gradient-to-r from-white/95 to-white/85 backdrop-blur-xl border border-white/50 rounded-2xl px-5 py-3.5 shadow-2xl cursor-pointer group transition-all duration-300 hover:shadow-3xl hover:scale-[1.02] active:scale-[0.98]"
            @click="copyUserId"
          >
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="flex items-center gap-1">
                  <span class="text-gray-500 text-sm font-medium">ID</span>
                  <div class="w-1 h-1 bg-gray-400 rounded-full"></div>
                </div>
                <span class="text-gray-900 text-base font-bold tracking-wide">{{ profileData.id }}</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-8 h-8 bg-[#2019CE]/10 rounded-full flex items-center justify-center group-hover:bg-[#2019CE]/20 transition-colors">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" class="text-[#2019CE]">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2" stroke="currentColor" stroke-width="2" fill="none"/>
                    <path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1" stroke="currentColor" stroke-width="2" fill="none"/>
                  </svg>
                </div>
              </div>
            </div>
          </div>

          <!-- Success Toast Overlay -->
          <Transition
            name="copy-success"
            enter-active-class="transition-all duration-500 ease-out"
            leave-active-class="transition-all duration-300 ease-in"
            enter-from-class="opacity-0 scale-95 translate-y-2"
            enter-to-class="opacity-100 scale-100 translate-y-0"
            leave-from-class="opacity-100 scale-100 translate-y-0"
            leave-to-class="opacity-0 scale-95 -translate-y-2"
          >
            <div
              v-if="isCopied"
              class="absolute inset-0 bg-gradient-to-r from-emerald-500 to-green-500 rounded-2xl px-5 py-3.5 shadow-2xl flex items-center justify-center gap-3 z-10"
            >
              <div class="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center backdrop-blur-sm">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" class="text-white">
                  <polyline points="20,6 9,17 4,12" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                </svg>
              </div>
              <span class="text-white font-bold text-base">ID Copied!</span>
            </div>
          </Transition>
        </div>

        <!-- Sophisticated Language Selector -->
        <div class="relative">
          <button
            @click="toggleLanguageSelector"
            class="bg-gradient-to-r from-white/95 to-white/85 backdrop-blur-xl border border-white/50 rounded-2xl px-4 py-3.5 shadow-2xl transition-all duration-300 hover:shadow-3xl hover:scale-105 active:scale-95 flex items-center gap-3 min-w-[100px]"
          >
            <!-- Current Language Flag -->
            <div class="w-6 h-6 rounded-full overflow-hidden shadow-md border border-white/30">
              <component :is="getCurrentLanguageFlag()" />
            </div>
            <span class="text-gray-900 font-bold text-sm">{{ selectedLanguage }}</span>
            <svg
              width="12"
              height="12"
              viewBox="0 0 24 24"
              fill="none"
              class="text-gray-500 transition-transform duration-300"
              :class="{ 'rotate-180': showLanguageDropdown }"
            >
              <polyline points="6,9 12,15 18,9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>

          <!-- Beautiful Dropdown -->
          <Transition
            name="dropdown"
            enter-active-class="transition-all duration-300 ease-out"
            leave-active-class="transition-all duration-200 ease-in"
            enter-from-class="opacity-0 scale-95 translate-y-2"
            enter-to-class="opacity-100 scale-100 translate-y-0"
            leave-from-class="opacity-100 scale-100 translate-y-0"
            leave-to-class="opacity-0 scale-95 translate-y-2"
          >
            <div
              v-if="showLanguageDropdown"
              class="absolute bottom-full right-0 mb-3 bg-white/95 backdrop-blur-xl border border-white/50 rounded-2xl shadow-3xl overflow-hidden z-50 min-w-[160px]"
            >
              <div class="p-2 space-y-1">
                <button
                  v-for="language in languages"
                  :key="language.code"
                  @click="selectLanguage(language)"
                  class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition-all duration-200 hover:bg-gradient-to-r hover:from-[#2019CE]/10 hover:to-purple-500/10 text-left group"
                  :class="{
                    'bg-gradient-to-r from-[#2019CE]/20 to-purple-500/20 text-[#2019CE]': selectedLanguage === language.code,
                    'text-gray-700 hover:text-gray-900': selectedLanguage !== language.code
                  }"
                >
                  <div class="w-5 h-5 rounded-full overflow-hidden shadow-sm border border-white/50">
                    <component :is="language.flag" />
                  </div>
                  <span class="text-sm font-medium transition-colors">{{ language.name }}</span>
                  <div
                    v-if="selectedLanguage === language.code"
                    class="ml-auto w-2 h-2 bg-[#2019CE] rounded-full"
                  ></div>
                </button>
              </div>
            </div>
          </Transition>
        </div>
      </div>
    </div>

    <!-- Start Level Upgrade Section -->
    <div class="px-4 pb-8">
      <div class="bg-[#F1E7FF] border border-[#DCCCF1] rounded-xl p-4 relative overflow-hidden">
        <!-- Star Icon -->
        <div class="absolute left-2 top-3">
          <svg width="24" height="24" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="16" cy="16" r="15.06" fill="#8C4CD1"/>
            <path d="M28.998 8.39055C26.1133 12.4471 21.365 15.0918 16.0003 15.0918C10.6356 15.0918 5.88739 12.4471 3.00269 8.39055C5.61916 3.9341 10.4615 0.941162 16.0003 0.941162C21.5392 0.941162 26.3815 3.9341 28.998 8.39055Z" fill="#9C68E1"/>
            <path d="M15.9997 5.11792V15.4117L19.3443 11.8949L15.9997 5.11792Z" fill="#FF9F00"/>
            <path d="M15.9996 5.11792V15.4117L12.655 11.8949L15.9996 5.11792Z" fill="#FED110"/>
            <path d="M26.8232 12.982L19.3443 11.8953L15.9997 15.412L26.8232 12.982Z" fill="#FED110"/>
            <path d="M26.8232 12.9825L21.4115 18.2577L15.9997 15.4126L26.8232 12.9825Z" fill="#FF9F00"/>
            <path d="M5.17645 12.982L12.6553 11.8953L16 15.412L5.17645 12.982Z" fill="#FF9F00"/>
            <path d="M5.17645 12.9825L10.5882 18.2577L16 15.4126L5.17645 12.9825Z" fill="#FED110"/>
            <path d="M15.9997 15.4124L21.4115 18.2575L22.689 25.7061L15.9997 15.4124Z" fill="#FED110"/>
            <path d="M22.689 25.7061L15.9997 22.1894V15.4124L22.689 25.7061Z" fill="#FF9F00"/>
            <path d="M15.9996 15.4124L10.5878 18.2575L9.31024 25.7061L15.9996 15.4124Z" fill="#FF9F00"/>
            <path d="M9.31024 25.7061L15.9996 22.1894V15.4124L9.31024 25.7061Z" fill="#FED110"/>
            <ellipse opacity="0.3" cx="16.0003" cy="27.5882" rx="8.88235" ry="0.545" fill="#20273A"/>
          </svg>
        </div>

        <!-- Background gradient -->
        <div class="absolute left-0 top-0 w-28 h-full bg-gradient-to-r from-[#8C4CD1]/30 to-transparent rounded-l-xl"></div>

        <div class="flex items-center justify-between relative z-10">
          <div class="ml-8">
            <div class="text-[#02070E] font-bold text-base">Start</div>
            <div class="text-sm text-[#4B4D50]">
              buy <span class="font-bold text-[#8C4CD1]">123</span> more to upgrade
            </div>
          </div>
          <button @click="handleUpgrade" class="px-4 py-2 bg-gradient-to-r from-[#2019CE] to-[#473FFF] text-white font-medium rounded-full text-sm hover:shadow-lg transition-all duration-200 flex-shrink-0 active:scale-95">
            Upgrade
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, h } from 'vue'
import { useRouter } from 'vue-router'

// Router
const router = useRouter()

// Profile data
const profileData = ref({
  name: 'Jason Williams',
  id: '515745',
  avatar: 'https://cdn.builder.io/api/v1/image/assets%2Fcd0d81f444984dacbac377cc9f78a1aa%2F572074b5aefa4337aec163bd9a21aec3?format=webp&width=800'
})

// Copy button state
const isCopied = ref(false)

// Language selector state
const showLanguageDropdown = ref(false)
const selectedLanguage = ref('ENG')

// Enhanced language options with better flag components
const languages = ref([
  {
    code: 'ENG',
    name: 'English',
    flag: () => h('svg', {
      width: 20,
      height: 20,
      viewBox: '0 0 32 32',
      class: 'rounded-full'
    }, [
      h('circle', { cx: 16, cy: 16, r: 16, fill: '#F0F0F0' }),
      h('path', { d: 'M15.3438 16.0025H31.0573C31.0573 14.6433 30.8761 13.3266 30.5385 12.0741H15.3438V16.0025Z', fill: '#D80027' }),
      h('path', { d: 'M15.3438 8.14179H28.847C27.9252 6.63756 26.7466 5.30797 25.3723 4.21338H15.3438V8.14179Z', fill: '#D80027' }),
      h('path', { d: 'M16.0038 31.06C19.5478 31.06 22.8053 29.8351 25.3776 27.7864H6.62988C9.20224 29.8351 12.4597 31.06 16.0038 31.06Z', fill: '#D80027' }),
      h('path', { d: 'M3.15241 23.855H28.8496C29.5896 22.6475 30.1636 21.3275 30.5411 19.9266H1.46094C1.83841 21.3275 2.41235 22.6475 3.15241 23.855Z', fill: '#D80027' }),
      h('path', { d: 'M7.91596 3.29305H9.28825L8.01178 4.22041L8.49937 5.72094L7.22296 4.79358L5.94655 5.72094L6.36772 4.42464C5.24384 5.36082 4.25878 6.45764 3.44702 7.67976H3.88672L3.07419 8.27005C2.94761 8.48123 2.82619 8.69576 2.70984 8.91346L3.09784 10.1076L2.37396 9.5817C2.19402 9.96294 2.02943 10.3528 1.88149 10.7507L2.30896 12.0665H3.88672L2.61025 12.9938L3.09784 14.4943L1.82143 13.567L1.05684 14.1225C0.980312 14.7377 0.94043 15.3643 0.94043 16.0002H15.9993C15.9993 7.68352 15.9993 6.70305 15.9993 0.941406C13.0244 0.941406 10.2513 1.80435 7.91596 3.29305ZM8.49937 14.4943L7.22296 13.567L5.94655 14.4943L6.43414 12.9938L5.15767 12.0665H6.73543L7.22296 10.5659L7.71049 12.0665H9.28825L8.01178 12.9938L8.49937 14.4943ZM8.01178 8.60711L8.49937 10.1076L7.22296 9.18029L5.94655 10.1076L6.43414 8.60711L5.15767 7.67976H6.73543L7.22296 6.17923L7.71049 7.67976H9.28825L8.01178 8.60711ZM13.9009 14.4943L12.6245 13.567L11.3481 14.4943L11.8357 12.9938L10.5592 12.0665H12.137L12.6245 10.5659L13.112 12.0665H14.6898L13.4133 12.9938L13.9009 14.4943ZM13.4133 8.60711L13.9009 10.1076L12.6245 9.18029L11.3481 10.1076L11.8357 8.60711L10.5592 7.67976H12.137L12.6245 6.17923L13.112 7.67976H14.6898L13.4133 8.60711ZM13.4133 4.22041L13.9009 5.72094L12.6245 4.79358L11.3481 5.72094L11.8357 4.22041L10.5592 3.29305H12.137L12.6245 1.79252L13.112 3.29305H14.6898L13.4133 4.22041Z', fill: '#0052B4' })
    ])
  },
  {
    code: 'RUS',
    name: 'Ру��ский',
    flag: () => h('svg', {
      width: 20,
      height: 20,
      viewBox: '0 0 32 32',
      class: 'rounded-full'
    }, [
      h('circle', { cx: 16, cy: 16, r: 16, fill: '#F0F0F0' }),
      h('path', { d: 'M30.1062 15.5233C30.1062 12.2598 29.0925 9.24863 27.359 6.83691H3.68767C1.95408 9.24863 0.94043 12.2598 0.94043 15.5233H30.1062Z', fill: '#0052B4' }),
      h('path', { d: 'M15.5233 30.1062C20.4067 30.1062 24.7598 27.8462 27.359 24.21H3.68767C6.28686 27.8462 10.6399 30.1062 15.5233 30.1062Z', fill: '#D80027' })
    ])
  },
  {
    code: 'DE',
    name: 'Deutsch',
    flag: () => h('svg', {
      width: 20,
      height: 20,
      viewBox: '0 0 32 32',
      class: 'rounded-full'
    }, [
      h('circle', { cx: 16, cy: 16, r: 16, fill: '#000' }),
      h('path', { d: 'M16 0C21.5228 0 26.3137 3.15596 28.6274 7.7778H3.37258C5.68626 3.15596 10.4772 0 16 0Z', fill: '#000' }),
      h('path', { d: 'M16 32C10.4772 32 5.68626 28.844 3.37258 24.2222H28.6274C26.3137 28.844 21.5228 32 16 32Z', fill: '#FFDA44' }),
      h('path', { d: 'M3.37258 7.7778H28.6274C30.0693 10.3137 30.8889 13.1563 30.8889 16.1111C30.8889 19.0659 30.0693 21.9085 28.6274 24.4444H3.37258C1.93069 21.9085 1.11111 19.0659 1.11111 16.1111C1.11111 13.1563 1.93069 10.3137 3.37258 7.7778Z', fill: '#D80027' })
    ])
  },
  {
    code: 'FR',
    name: 'Français',
    flag: () => h('svg', {
      width: 20,
      height: 20,
      viewBox: '0 0 32 32',
      class: 'rounded-full'
    }, [
      h('circle', { cx: 16, cy: 16, r: 16, fill: '#F0F0F0' }),
      h('path', { d: 'M16 0C21.5228 0 26.3137 3.15596 28.6274 7.7778V24.2222C26.3137 28.844 21.5228 32 16 32V0Z', fill: '#D80027' }),
      h('path', { d: 'M16 0C10.4772 0 5.68626 3.15596 3.37258 7.7778V24.2222C5.68626 28.844 10.4772 32 16 32V0Z', fill: '#0052B4' })
    ])
  }
])

// Methods
const handleMenuClick = (section) => {
  console.log(`Navigate to ${section}`)
  // TODO: Add navigation logic for each menu item
}

const handleUpgrade = () => {
  console.log('Upgrade clicked')
  // TODO: Add upgrade logic
}

const copyUserId = async () => {
  try {
    await navigator.clipboard.writeText(profileData.value.id)
    isCopied.value = true

    // Hide the copied state after 2 seconds
    setTimeout(() => {
      isCopied.value = false
    }, 2000)

    console.log('User ID copied to clipboard')
  } catch (err) {
    console.error('Failed to copy user ID:', err)
  }
}

const toggleLanguageSelector = () => {
  showLanguageDropdown.value = !showLanguageDropdown.value
}

const selectLanguage = (language) => {
  selectedLanguage.value = language.code
  showLanguageDropdown.value = false
  console.log('Language selected:', language.name)
}

const getCurrentLanguageFlag = () => {
  const current = languages.value.find(lang => lang.code === selectedLanguage.value)
  return current?.flag || languages.value[0].flag
}

// Close dropdown when clicking outside
const handleClickOutside = (event) => {
  if (!event.target.closest('.relative')) {
    showLanguageDropdown.value = false
  }
}

// Add event listener for clicking outside
if (typeof window !== 'undefined') {
  document.addEventListener('click', handleClickOutside)
}
</script>

<style scoped>
/* Telegram WebApp optimizations */
* {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
}

/* Allow text selection for specific elements */
span, h1 {
  -webkit-user-select: text;
  -moz-user-select: text;
  -ms-user-select: text;
  user-select: text;
}

/* Touch-optimized scrolling for Telegram WebApp */
.touch-scroll {
  -webkit-overflow-scrolling: touch;
  overscroll-behavior: contain;
  scroll-behavior: smooth;
  touch-action: pan-y;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.touch-scroll::-webkit-scrollbar {
  display: none;
  width: 0;
  height: 0;
}

/* Enhanced touch targets */
.touch-target {
  min-height: 56px;
  min-width: 44px;
  touch-action: manipulation;
}

/* Active state for touch feedback */
.active\:scale-95:active {
  transform: scale(0.95);
  transition: transform 0.1s ease-in-out;
}

/* Hover effects only for desktop */
@media (hover: hover) {
  .hover\:bg-white\/10:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }
  
  .hover\:bg-white\/90:hover {
    background-color: rgba(255, 255, 255, 0.9);
  }
  
  .hover\:shadow-lg:hover {
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  }
}

/* Safe area support for iOS */
@supports (padding: max(0px)) {
  .pb-8 {
    padding-bottom: max(32px, env(safe-area-inset-bottom));
  }
  
  .pt-12 {
    padding-top: max(48px, env(safe-area-inset-top));
  }
}

/* Backdrop blur support */
@supports (backdrop-filter: blur(10px)) {
  .backdrop-blur-sm {
    backdrop-filter: blur(4px);
  }
}

/* Mobile optimizations */
@media (max-width: 375px) {
  .text-xl {
    font-size: 1.125rem;
    line-height: 1.5rem;
  }
  
  .text-base {
    font-size: 0.875rem;
    line-height: 1.25rem;
  }
  
  .text-sm {
    font-size: 0.8125rem;
    line-height: 1.125rem;
  }
  
  .px-4 {
    padding-left: 1rem;
    padding-right: 1rem;
  }
  
  .px-6 {
    padding-left: 1.25rem;
    padding-right: 1.25rem;
  }
}

/* Improved scrolling performance */
.touch-scroll {
  transform: translateZ(0);
  will-change: scroll-position;
}

/* Better button sizing for mobile */
@media (max-width: 768px) {
  button {
    min-height: 44px;
    min-width: 44px;
  }
}

/* Gradient fade performance optimization */
.bg-gradient-to-t {
  background-image: linear-gradient(to top, var(--tw-gradient-stops));
}

.bg-gradient-to-br {
  background-image: linear-gradient(to bottom right, var(--tw-gradient-stops));
}

.bg-gradient-to-r {
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}

/* Copy button animations */
/* Enhanced shadow and blur effects */
.shadow-3xl {
  box-shadow: 0 35px 60px -12px rgba(0, 0, 0, 0.25), 0 0 0 1px rgba(255, 255, 255, 0.5);
}

/* Copy success animation */
.copy-success-enter-active {
  transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.copy-success-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.6, 1);
}

/* Dropdown animation */
.dropdown-enter-active {
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.dropdown-leave-active {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.6, 1);
}

/* Backdrop blur enhancement */
@supports (backdrop-filter: blur(20px)) {
  .backdrop-blur-xl {
    backdrop-filter: blur(20px) saturate(180%);
  }
}

/* Language dropdown positioning */
.relative {
  position: relative;
}

/* Dropdown shadow */
.shadow-xl {
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

/* Smooth transitions */
.transition-transform {
  transition: transform 0.2s ease-in-out;
}

.rotate-180 {
  transform: rotate(180deg);
}
</style>
