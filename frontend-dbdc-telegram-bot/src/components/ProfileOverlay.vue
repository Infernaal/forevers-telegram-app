<template>
  <!-- Profile Overlay with backdrop blur -->
  <div v-if="isVisible" 
       class="fixed inset-0 z-[9999] font-montserrat profile-overlay"
       @click="handleBackdropClick">
    
    <!-- Backdrop with blur effect (excludes BottomNavigation area) -->
    <div class="absolute inset-0 bg-black/20 backdrop-blur-md" 
         style="bottom: 88px;"></div>
    
    <!-- Full width modal container -->
    <div class="w-full min-h-full py-8 pt-16"
         style="padding-bottom: 88px;">

      <!-- Main modal content -->
      <div class="relative w-full bg-gradient-to-br from-[#120B81] via-[#120B81] to-[#09074E]
                  rounded-[20px] shadow-2xl border border-white/[0.08] backdrop-blur-[32px]
                  transform transition-all duration-300 ease-out
                  max-h-[calc(100vh-200px)] overflow-hidden flex flex-col ml-4 mr-6"
           @click.stop>

        <!-- Profile Header Section -->
        <div class="flex-shrink-0 px-3 pt-4 pb-2">
          <div class="flex items-center justify-between bg-white/10 border border-white/24 rounded-full px-2 py-2 mb-4">
            <!-- Profile Avatar and Info -->
            <div class="flex items-center gap-3">
              <!-- Avatar -->
              <div class="w-20 h-20 rounded-full border-2 border-[#7E73D6] overflow-hidden bg-gray-200 flex-shrink-0">
                <img 
                  src="https://images.pexels.com/photos/15023413/pexels-photo-15023413.jpeg?auto=compress&cs=tinysrgb&w=400" 
                  alt="Profile" 
                  class="w-full h-full object-cover"
                />
              </div>
              
              <!-- User Info -->
              <div class="flex flex-col min-w-0">
                <!-- Dynamic Rank Badge -->
                <div class="flex items-center gap-1.5 bg-white/20 border border-white/20 rounded-full px-2 py-1 mb-2 w-fit">
                  <div class="w-7 h-7 flex items-center justify-center flex-shrink-0">
                    <div v-html="currentRank.iconSvg" class="w-full h-full"></div>
                  </div>
                  <span class="text-sm font-medium" :style="{ color: currentRank.color }">{{ currentRank.name }}</span>
                </div>
                
                <!-- User Name -->
                <h3 class="text-white text-xl font-bold leading-tight">Jason Williams</h3>
              </div>
            </div>
            
            <!-- Arrow Button -->
            <div class="flex-shrink-0">
              <button class="w-11 h-11 bg-[#EFEEFF] border border-dbd-primary rounded-r-full flex items-center justify-center hover:bg-white/90 transition-colors"
                      @click="emit('close')">
                <svg class="w-6 h-6 text-dbd-light-gray" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M17.2155 11.2862L8.2216 2.29534C7.82696 1.90169 7.18757 1.90169 6.79192 2.29534C6.39728 2.68898 6.39728 3.32838 6.79192 3.72203L15.0724 11.9996L6.79292 20.2771C6.39827 20.6707 6.39827 21.3101 6.79292 21.7048C7.18756 22.0984 7.82795 22.0984 8.2226 21.7048L17.2165 12.7139C17.6051 12.3244 17.6051 11.6749 17.2155 11.2862Z"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Scrollable Menu Items Container -->
        <div class="flex-1 overflow-y-auto px-3 max-h-60">
          <div class="space-y-1">
            
            <!-- Calculator -->
            <div class="flex items-center gap-3 px-3 py-2.5 hover:bg-white/[0.05] rounded-lg transition-colors cursor-pointer"
                 @click="onMenuClick('calculator')">
              <div class="flex-shrink-0">
                <div class="w-10 h-10 rounded-full border border-white/40 bg-white/[0.24] flex items-center justify-center">
                  <svg class="w-5 h-5 text-white" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H9v-2h5v2zm0-3H9v-2h5v2zm0-3H9V9h5v2zm3 3h-2v-2h2v2zm0-3h-2V9h2v2z"/>
                  </svg>
                </div>
              </div>
              <span class="text-white text-base font-semibold">Calculator</span>
            </div>

            <!-- Ambassador -->
            <div class="flex items-center gap-3 px-3 py-2.5 hover:bg-white/[0.05] rounded-lg transition-colors cursor-pointer"
                 @click="onMenuClick('ambassador')">
              <div class="flex-shrink-0">
                <div class="w-10 h-10 rounded-full border border-white/40 bg-white/[0.24] flex items-center justify-center">
                  <svg class="w-4 h-5 text-white" viewBox="0 0 14 20" fill="currentColor">
                    <path d="M7 9.64844C9.76508 9.64858 12.0066 11.9652 12.0068 14.8242C12.0068 17.6826 9.76511 19.9999 7 20C4.23394 20 1.99219 17.6827 1.99219 14.8242C1.99243 11.9651 4.23409 9.64844 7 9.64844ZM6.09668 13.8418L4.07715 14.1465L5.53906 15.6182L5.19434 17.6992L7 16.7168L8.80566 17.6992L8.46191 15.6182L9.92383 14.1465L7.90332 13.8418L7 11.9512L6.09668 13.8418ZM4.60547 0L7 3.30078L9.39453 0H14L7 9.64844L0 0H4.60547Z"/>
                  </svg>
                </div>
              </div>
              <span class="text-white text-base font-semibold">Ambassador</span>
            </div>

            <!-- Verification with red X -->
            <div class="flex items-center gap-3 px-3 py-2.5 hover:bg-white/[0.05] rounded-lg transition-colors cursor-pointer"
                 @click="onMenuClick('verification')">
              <div class="flex-shrink-0">
                <div class="w-10 h-10 rounded-full border border-white/40 bg-white/[0.24] flex items-center justify-center">
                  <svg class="w-[18px] h-[22px] text-white" viewBox="0 0 18 22" fill="currentColor">
                    <path d="M14.2511 12.4974C15.4932 12.4974 16.5 13.5045 16.5 14.7467V15.3222C16.5 16.2166 16.1805 17.0816 15.5989 17.7611C14.0295 19.5949 11.6422 20.5 8.49673 20.5C5.35076 20.5 2.96466 19.5946 1.39831 17.7601C0.818531 17.081 0.5 16.2174 0.5 15.3245V14.7467C0.5 13.5045 1.50689 12.4974 2.74896 12.4974H14.2511ZM14.2511 13.9977H2.74896C2.33534 13.9977 2.00005 14.333 2.00005 14.7467V15.3245C2.00005 15.8602 2.19117 16.3784 2.53904 16.7858C3.79239 18.2538 5.75834 18.9997 8.49673 18.9997C11.2351 18.9997 13.2028 18.2537 14.4593 16.7855C14.8082 16.3779 14.9999 15.8589 14.9999 15.3222V14.7467C14.9999 14.333 14.6647 13.9977 14.2511 13.9977ZM8.49673 0.5C11.2582 0.5 13.4969 2.73897 13.4969 5.50088C13.4969 8.2628 11.2582 10.5017 8.49673 10.5017C5.73521 10.5017 3.49656 8.2628 3.49656 5.50088C3.49656 2.73897 5.73521 0.5 8.49673 0.5ZM8.49673 2.00026C6.56366 2.00026 4.99661 3.56755 4.99661 5.50088C4.99661 7.43422 6.56366 9.00148 8.49673 9.00148C10.4298 9.00148 11.9968 7.43422 11.9968 5.50088C11.9968 3.56755 10.4298 2.00026 8.49673 2.00026Z"/>
                  </svg>
                </div>
              </div>
              <span class="text-white text-base font-semibold">Verification</span>
              <!-- Red X Icon -->
              <div class="ml-auto">
                <div class="w-6 h-6 rounded-full border border-[#FF1919] bg-[#FFF0F3] flex items-center justify-center">
                  <svg class="w-4 h-4 text-[#FF1919]" viewBox="0 0 16 16" fill="currentColor">
                    <path d="M12.854 4.854a.5.5 0 0 0-.708-.708L8 8.293 3.854 4.146a.5.5 0 1 0-.708.708L7.293 9l-4.147 4.146a.5.5 0 0 0 .708.708L8 9.707l4.146 4.147a.5.5 0 0 0 .708-.708L8.707 9l4.147-4.146z"/>
                  </svg>
                </div>
              </div>
            </div>

            <!-- Security -->
            <div class="flex items-center gap-3 px-3 py-2.5 hover:bg-white/[0.05] rounded-lg transition-colors cursor-pointer"
                 @click="onMenuClick('security')">
              <div class="flex-shrink-0">
                <div class="w-10 h-10 rounded-full border border-white/40 bg-white/[0.24] flex items-center justify-center">
                  <svg class="w-[18px] h-5 text-white" viewBox="0 0 18 20" fill="currentColor">
                    <path d="M8.78516 0.0354746C8.92389 -0.0121504 9.07611 -0.0121504 9.21484 0.0354746C10.6561 0.531013 12.1438 0.945188 13.6377 1.26497C14.8838 1.5317 16.1601 1.73823 17.4297 1.87922C17.7546 1.91522 18 2.18263 18 2.50032V8.7386C17.9998 13.165 15.3282 17.2234 11.1943 19.0784L9.26953 19.9427C9.18416 19.9808 9.09193 20.0003 9 20.0003C8.90802 20.0003 8.81583 19.9808 8.73047 19.9427L6.80566 19.0784C2.67178 17.2233 0.000192395 13.165 0 8.7386V2.50032C0 2.18263 0.245411 1.91529 0.570312 1.87922C1.83994 1.73823 3.11627 1.53164 4.3623 1.26497C5.85626 0.945192 7.34396 0.531005 8.78516 0.0354746ZM9 1.28743C7.57623 1.76779 6.10923 2.17074 4.6377 2.48567C3.53526 2.72147 2.41054 2.91243 1.28613 3.05403V8.7386C1.28633 12.6791 3.6638 16.2924 7.34375 17.9437L9 18.6868L10.6562 17.9437C14.3362 16.2924 16.7137 12.6792 16.7139 8.7386V3.05403C15.5895 2.91243 14.4647 2.72154 13.3623 2.48567C11.8908 2.17074 10.4239 1.7678 9 1.28743Z"/>
                  </svg>
                </div>
              </div>
              <span class="text-white text-base font-semibold">Security</span>
            </div>

            <!-- Settings -->
            <div class="flex items-center gap-3 px-3 py-2.5 hover:bg-white/[0.05] rounded-lg transition-colors cursor-pointer"
                 @click="onMenuClick('settings')">
              <div class="flex-shrink-0">
                <div class="w-10 h-10 rounded-full border border-white/40 bg-white/[0.24] flex items-center justify-center">
                  <svg class="w-5 h-5 text-white" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"/>
                  </svg>
                </div>
              </div>
              <span class="text-white text-base font-semibold">Settings</span>
            </div>

            <!-- Support -->
            <div class="flex items-center gap-3 px-3 py-2.5 hover:bg-white/[0.05] rounded-lg transition-colors cursor-pointer"
                 @click="onMenuClick('support')">
              <div class="flex-shrink-0">
                <div class="w-10 h-10 rounded-full border border-white/40 bg-white/[0.24] flex items-center justify-center">
                  <svg class="w-[18px] h-5 text-white" viewBox="0 0 18 20" fill="currentColor">
                    <path d="M8.99902 0C13.9325 0 17.998 3.80872 17.998 8.58691V10.1348C17.9981 10.1411 17.999 10.1479 17.999 10.1543V12.9561C17.9992 12.9624 18 12.9692 18 12.9756V14.543C17.9997 16.724 16.1499 18.4277 13.9502 18.4277H11.2695C10.9422 19.3551 10.0281 19.9951 8.99902 19.9951C7.71066 19.9949 6.59988 18.993 6.59961 17.6777C6.59962 16.3623 7.71051 15.3606 8.99902 15.3604C10.0286 15.3604 10.9435 15.9998 11.2705 16.9277H13.9502C15.1589 16.9277 16.1261 16.1539 16.4111 15.1514C16.155 15.2407 15.8817 15.293 15.5986 15.293C14.3103 15.2927 13.1995 14.2908 13.1992 12.9756V10.1543C13.1992 8.83884 14.3101 7.83714 15.5986 7.83691C15.9032 7.83691 16.1972 7.89422 16.4697 7.99707C16.1535 4.38853 12.9637 1.5 8.99902 1.5C5.03445 1.50011 1.84359 4.38856 1.52734 7.99707C1.80001 7.89396 2.09449 7.83697 2.39941 7.83691C3.6881 7.83691 4.7998 8.83869 4.7998 10.1543V12.9756C4.79953 14.291 3.68794 15.293 2.39941 15.293C1.11107 15.2927 0.000274862 14.2908 0 12.9756V8.58691C4.3009e-05 3.80879 4.0657 0.000121732 8.99902 0Z"/>
                  </svg>
                </div>
              </div>
              <span class="text-white text-base font-semibold">Support</span>
            </div>

            <!-- Help -->
            <div class="flex items-center gap-3 px-3 py-2.5 hover:bg-white/[0.05] rounded-lg transition-colors cursor-pointer"
                 @click="onMenuClick('help')">
              <div class="flex-shrink-0">
                <div class="w-10 h-10 rounded-full border border-white/40 bg-white/[0.24] flex items-center justify-center">
                  <svg class="w-5 h-5 text-white" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z"/>
                  </svg>
                </div>
              </div>
              <span class="text-white text-base font-semibold">Help</span>
            </div>
          </div>
        </div>

        <!-- Bottom Section with Start Card and ID/Language -->
        <div class="flex-shrink-0 px-3 pb-3 space-y-4 sm:space-y-5 md:space-y-6">
          
          <!-- Start Upgrade Card - Figma Design -->
          <div class="relative bg-[#F1E7FF] border border-[#DCCCF1] rounded-2xl overflow-hidden h-[84px] w-full">
            <!-- Purple gradient overlay on left (140px width, opacity 0.4) -->
            <div class="absolute left-0 top-0 h-full bg-gradient-to-r from-[#8C4CD1] to-[#C497FF] opacity-40 rounded-l-2xl"
                 style="width: 140px;"></div>

            <!-- Star icon positioned at left:8px, top:14px equivalent -->
            <div class="absolute" style="left: 8px; top: 14px;">
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clipPath="url(#clip0_2_21309)">
                  <path d="M16 31.0588C24.3167 31.0588 31.0588 24.3167 31.0588 16C31.0588 7.68323 24.3167 0.941162 16 0.941162C7.68323 0.941162 0.941162 7.68323 0.941162 16C0.941162 24.3167 7.68323 31.0588 16 31.0588Z" fill="#8C4CD1"/>
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
                  <g opacity="0.3">
                    <path d="M16.0003 27.5882C20.9059 27.5882 24.8826 27.3442 24.8826 27.0432C24.8826 26.7423 20.9059 26.4983 16.0003 26.4983C11.0947 26.4983 7.11792 26.7423 7.11792 27.0432C7.11792 27.3442 11.0947 27.5882 16.0003 27.5882Z" fill="#20273A"/>
                  </g>
                </g>
                <defs>
                  <clipPath id="clip0_2_21309">
                    <rect width="32" height="32" fill="white"/>
                  </clipPath>
                </defs>
              </svg>
            </div>

            <!-- Start title positioned at left:48px, top:17px equivalent -->
            <div class="absolute font-montserrat font-bold text-[19px] leading-6 text-[#02070E]"
                 style="left: 48px; top: 17px; width: 48px; height: 24px;">
              Start
            </div>

            <!-- Description text positioned at left:8px, top:54px equivalent -->
            <div class="absolute font-montserrat text-sm leading-[22px]"
                 style="left: 8px; top: 54px; width: 299px; height: 22px;">
              <span class="text-[#4B4D50] font-normal">buy </span>
              <span class="text-[#8C4CD1] font-bold">123</span>
              <span class="text-[#4B4D50] font-normal"> more Forevers to upgrade</span>
            </div>

            <!-- Upgrade button positioned at left:195px, top:8px equivalent -->
            <button class="absolute flex items-center justify-center gap-2.5 bg-gradient-to-r from-[#2019CE] to-[#473FFF] text-white font-montserrat font-bold text-base leading-5 rounded-full px-6 py-3 hover:shadow-lg transition-all duration-200 capitalize"
                    style="left: 195px; top: 8px; width: 120px; height: 44px;"
                    @click="onMenuClick('upgrade')">
              Upgrade
            </button>
          </div>

          <!-- Bottom ID and Language Section with Separator -->
          <div class="flex items-center justify-center h-11 relative">

            <!-- ID Section -->
            <div class="relative flex items-center">
              <div class="bg-white/[0.30] backdrop-blur-[32px] border border-white/40 rounded-full h-11 w-36 sm:w-38 md:w-40 flex items-center justify-between pl-3 pr-0">
                <div class="flex items-center min-w-0 overflow-hidden">
                  <span class="text-dbd-light-gray text-sm">ID:</span>
                  <span class="text-white text-sm font-medium ml-1 truncate">515745</span>
                </div>
                <button class="flex-shrink-0 w-6 h-6 sm:w-8 sm:h-10 md:w-10 md:h-10 bg-white border border-[#D8D8D8] rounded-r-full flex items-center justify-center hover:bg-gray-50 transition-colors"
                        @click="copyUserID">
                  <svg class="w-3 h-3 sm:w-5 sm:h-5 md:w-6 md:h-6 text-gray-600" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M18.2806 1.19995H8.98336C8.42322 1.19995 7.88603 1.43348 7.48995 1.84917C7.09387 2.26486 6.87136 2.82866 6.87136 3.41653V4.26906H5.81536C5.2278 4.26906 4.66431 4.51402 4.24885 4.95006C3.83338 5.3861 3.59998 5.97749 3.59998 6.59414V20.4749C3.59998 21.0915 3.83338 21.6829 4.24885 22.119C4.66431 22.555 5.2278 22.8 5.81536 22.8H14.9132C15.5008 22.8 16.0643 22.555 16.4797 22.119C16.8952 21.6829 17.1286 21.0915 17.1286 20.4749V19.6998H18.2806C18.8363 19.6999 19.3699 19.4709 19.7663 19.0621C20.1627 18.6533 20.3903 18.0975 20.4 17.5143V3.41653C20.398 2.82794 20.1739 2.26417 19.7766 1.8487C19.3794 1.43323 18.8414 1.19995 18.2806 1.19995ZM15.6517 20.4749C15.6517 20.6804 15.5739 20.8776 15.4354 21.0229C15.2969 21.1682 15.1091 21.2499 14.9132 21.2499H5.81536C5.61951 21.2499 5.43168 21.1682 5.29319 21.0229C5.1547 20.8776 5.0769 20.6804 5.0769 20.4749V6.59414C5.0769 6.38859 5.1547 6.19146 5.29319 6.04611C5.43168 5.90077 5.61951 5.81911 5.81536 5.81911H14.9132C15.1091 5.81911 15.2969 5.90077 15.4354 6.04611C15.5739 6.19146 15.6517 6.38859 15.6517 6.59414V20.4749ZM18.9231 17.5143C18.9211 17.6918 18.8526 17.8613 18.7323 17.9861C18.612 18.1108 18.4497 18.1808 18.2806 18.1808H17.1286V6.59414C17.1286 5.97749 16.8952 5.3861 16.4797 4.95006C16.0643 4.51402 15.5008 4.26906 14.9132 4.26906H8.34828V3.41653C8.34828 3.23976 8.41519 3.07022 8.53429 2.94523C8.65339 2.82023 8.81493 2.75001 8.98336 2.75001H18.2806C18.3646 2.74898 18.448 2.76546 18.5259 2.7985C18.6038 2.83154 18.6747 2.88047 18.7344 2.94246C18.7942 3.00446 18.8416 3.07828 18.874 3.15966C18.9064 3.24103 18.9231 3.32834 18.9231 3.41653V17.5143Z"/>
                  </svg>
                </button>
              </div>
            </div>

            <!-- Separator Bar -->
            <div class="w-0.5 h-6 bg-white opacity-40 rounded-full mx-4 sm:mx-6 flex-shrink-0"></div>

            <!-- Language Section with Dropdown -->
            <div class="relative flex items-center">
              <div class="bg-white/[0.20] border border-white/24 rounded-full h-11 w-36 sm:w-38 md:w-40 flex items-center px-1.5 cursor-pointer hover:bg-white/25 transition-colors"
                   @click="toggleLanguageDropdown">
                <!-- Selected Country Flag -->
                <div class="w-8 h-8 rounded-full overflow-hidden flex-shrink-0 ml-1 flex items-center justify-center">
                  <CountryFlag :country="selectedLanguage.country" size="small" class="w-full h-full" />
                </div>

                <!-- Language Text -->
                <span class="text-dbd-off-white text-base font-medium flex-1 text-center">{{ selectedLanguage.code }}</span>

                <!-- Dropdown Arrow -->
                <div class="w-5 h-5 rounded-full bg-white/20 flex items-center justify-center mr-1">
                  <svg class="w-3 h-3 text-white transform transition-transform duration-200"
                       :class="{ 'rotate-180': isLanguageDropdownOpen }"
                       viewBox="0 0 20 20" fill="none">
                    <circle opacity="0.2" cx="10" cy="10" r="10" fill="white"/>
                    <path d="M5.71387 8.57146L9.99958 12.8572L14.2853 8.57146" stroke="white" strokeLinecap="round"/>
                  </svg>
                </div>
              </div>

              <!-- Language Dropdown Menu -->
              <Transition
                name="dropdown"
                enter-active-class="transition-all duration-200 ease-out"
                leave-active-class="transition-all duration-150 ease-in"
                enter-from-class="opacity-0 scale-95 translate-y-2"
                enter-to-class="opacity-100 scale-100 translate-y-0"
                leave-from-class="opacity-100 scale-100 translate-y-0"
                leave-to-class="opacity-0 scale-95 translate-y-2">
                <div v-if="isLanguageDropdownOpen"
                     class="absolute bottom-full right-0 mb-2 w-36 sm:w-38 md:w-40 bg-gradient-to-br from-[#120B81] via-[#120B81] to-[#09074E] rounded-xl shadow-xl border border-white/20 py-2 z-50 max-h-32 overflow-y-auto backdrop-blur-[32px]"
                     @click.stop>
                  <div v-for="language in languages"
                       :key="language.code"
                       class="flex items-center gap-2 px-3 py-1.5 hover:bg-white/10 cursor-pointer transition-colors"
                       @click="selectLanguage(language)">
                    <div class="w-5 h-5 rounded-full overflow-hidden flex-shrink-0 flex items-center justify-center">
                      <CountryFlag :country="language.country" size="small" class="w-full h-full" />
                    </div>
                    <span class="text-white text-sm font-medium flex-1 truncate">{{ language.name }}</span>
                  </div>
                </div>
              </Transition>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import CountryFlag from './CountryFlag.vue'

// Props
const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  }
})

// Emits
const emit = defineEmits(['close'])

// Current user rank (this would come from user data in real app)
const userRank = ref('silver') // Can be: norank, bronze, silver, gold, diamond, doublediam ond, ambassador, royalambassador

// Rank definitions with SVG icons and colors
const rankDefinitions = {
  norank: {
    name: 'No Rank',
    color: '#FAFAFA',
    iconSvg: `<svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M10.4819 13.9291C10.793 13.9291 11.0747 13.8034 11.2797 13.6003C11.4873 13.3946 11.616 13.1093 11.616 12.7939C11.616 12.167 11.1082 11.6588 10.4819 11.6588C9.85553 11.6588 9.34771 12.167 9.34771 12.7939C9.34771 12.9414 9.3767 13.0819 9.42788 13.2112C9.59418 13.6314 10.0029 13.9291 10.4819 13.9291Z" fill="#FAFAFA"/>
      <path d="M18.5536 13.2112C18.6048 13.0819 18.6338 12.9414 18.6338 12.7939C18.6338 12.167 18.126 11.6588 17.4996 11.6588C16.8733 11.6588 16.3655 12.167 16.3655 12.7939C16.3655 13.1093 16.4942 13.3946 16.7018 13.6004C16.9067 13.8034 17.1884 13.9291 17.4996 13.9291C17.9786 13.9291 18.3873 13.6314 18.5536 13.2112Z" fill="#FAFAFA"/>
      <path d="M16.3063 18.1152H11.6279V19.2504H16.3063V18.1152Z" fill="#FAFAFA"/>
      <path d="M24.5 8.90182C24.5 8.22591 24.0784 7.38079 23.211 6.31822C22.6145 5.58747 22.0257 5.02699 22.001 5.00351L21.6109 4.63338L21.2208 5.00344C21.2028 5.02046 20.8878 5.32064 20.4888 5.76257C18.7006 4.34654 16.4427 3.5 13.9908 3.5C8.20617 3.5 3.5 8.21023 3.5 14C3.5 19.7897 8.20617 24.5 13.9908 24.5C19.7754 24.5 24.4816 19.7897 24.4816 14C24.4816 12.8213 24.2864 11.6872 23.9269 10.6286C24.2867 10.1464 24.5 9.54858 24.5 8.90182ZM23.3474 14C23.3474 19.1638 19.1501 23.3648 13.9908 23.3648C11.4208 23.3648 9.08961 22.3222 7.39695 20.6376C6.721 19.9649 6.14719 19.1896 5.7004 18.3375C5.01991 17.04 4.63415 15.5644 4.63415 14C4.63415 8.8362 8.83152 4.63515 13.9908 4.63515C16.1665 4.63515 18.1712 5.38229 19.7621 6.63365C19.73 6.67594 19.6983 6.71787 19.6677 6.7593C19.0326 7.6179 18.7216 8.32226 18.7216 8.90175C18.7216 10.4963 20.0178 11.7935 21.6109 11.7935C21.9899 11.7935 22.3517 11.7193 22.6837 11.586C22.7897 11.5433 22.8929 11.4953 22.9923 11.4408C23.2236 12.2546 23.3474 13.1131 23.3474 14ZM21.6109 10.6584C20.6432 10.6584 19.8558 9.87039 19.8558 8.90175C19.8558 8.28643 20.7844 7.08026 21.6111 6.21663C22.4375 7.07941 23.3658 8.28494 23.3658 8.90175C23.3658 9.87039 22.5785 10.6584 21.6109 10.6584Z" fill="#FAFAFA"/>
    </svg>`
  },
  bronze: {
    name: 'Bronze',
    color: '#FAB44D',
    iconSvg: `<svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.0006 25.5516C20.3702 25.5516 25.5526 20.3696 25.5526 13.9996C25.5526 7.62964 20.3702 2.44764 14.0006 2.44764C7.63102 2.44764 2.44861 7.62964 2.44861 13.9996C2.44861 20.3696 7.63102 25.5516 14.0006 25.5516Z" fill="#CD7F32"/>
      <path d="M14.0004 23.1368C19.0464 23.1368 23.1369 19.0463 23.1369 14.0003C23.1369 8.95433 19.0464 4.86377 14.0004 4.86377C8.95445 4.86377 4.86389 8.95433 4.86389 14.0003C4.86389 19.0463 8.95445 23.1368 14.0004 23.1368Z" fill="#B8860B"/>
      <path d="M19.4965 12.7669L15.6984 12.2151L14.0001 8.77332L12.3014 12.2151L8.50366 12.7669L11.2519 15.4455L10.6031 19.2281L14.0001 17.4423L17.397 19.2281L16.7483 15.4455L19.4965 12.7669Z" fill="#FFD700"/>
    </svg>`
  },
  silver: {
    name: 'Silver',
    color: '#FAFAFA',
    iconSvg: `<svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.0004 26.2497C7.24592 26.2497 1.75073 20.7545 1.75073 14.0001C1.75073 7.24564 7.24592 1.75085 14.0004 1.75085C20.7548 1.75085 26.25 7.24564 26.25 14.0001C26.25 20.7545 20.7544 26.2497 14.0004 26.2497Z" fill="white"/>
      <path d="M14.0004 23.1368C19.0464 23.1368 23.1369 19.0463 23.1369 14.0003C23.1369 8.95433 19.0464 4.86377 14.0004 4.86377C8.95445 4.86377 4.86389 8.95433 4.86389 14.0003C4.86389 19.0463 8.95445 23.1368 14.0004 23.1368Z" fill="#9E9E9E"/>
      <path d="M19.4965 12.7669L15.6984 12.2151L14.0001 8.77332L12.3014 12.2151L8.50366 12.7669L11.2519 15.4455L10.6031 19.2281L14.0001 17.4423L17.397 19.2281L16.7483 15.4455L19.4965 12.7669Z" fill="#F6F6F6"/>
    </svg>`
  },
  gold: {
    name: 'Gold',
    color: '#FFD475',
    iconSvg: `<svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M26.1333 13.6111C26.5222 13.8445 26.5222 14.1556 26.1333 14.3889L11.1222 23.1778C10.7333 23.4111 10.1889 23.4111 9.79998 23.1778L1.86665 18.5111C1.47776 18.2778 1.47776 17.9667 1.86665 17.7334L16.9555 8.94447C17.3444 8.71114 17.8889 8.71114 18.2778 8.94447L26.1333 13.6111Z" fill="#F9A83D"/>
      <path d="M25.0448 9.02223C25.3559 9.17779 25.3559 9.4889 25.0448 9.72223L11.3559 17.6556C11.0448 17.8111 10.5003 17.8111 10.1892 17.6556L2.95587 13.4556C2.64476 13.3 2.64476 12.9889 2.95587 12.7556L16.6448 4.82223C16.9559 4.66668 17.5003 4.66668 17.8114 4.82223L25.0448 9.02223Z" fill="#FFD475"/>
      <path d="M11.6666 18.0445C11.5111 18.0445 11.4333 18.2 11.5111 18.3556C12.6778 19.7556 12.6778 19.9111 11.3555 18.5111C11.2778 18.4334 11.0444 18.4334 11.0444 18.5889C10.8889 20.1445 10.7333 21.5445 10.6555 21.5445C10.5778 21.5445 10.5778 20.1445 10.5778 18.5889C10.5778 18.4334 10.4222 18.3556 10.2666 18.4334C8.78887 19.6 8.78887 19.6 10.1111 18.2778C10.1889 18.2 10.1889 17.9667 10.0333 17.9667C8.47776 17.8111 7.07776 17.6556 7.07776 17.5778C7.07776 17.5 8.47776 17.5 10.0333 17.5C10.1889 17.5 10.2666 17.3445 10.1889 17.1889C9.7222 16.5667 9.25554 16.1 9.33331 16.0222C9.41109 16.0222 9.79998 16.4111 10.3444 16.9556C10.4222 17.0334 10.6555 17.0334 10.6555 16.8778C10.8111 15.3222 10.9666 13.9222 11.0444 13.9222C11.1222 13.9222 11.1222 15.3222 11.1222 16.8778C11.1222 17.0334 11.2778 17.1111 11.4333 17.0334C12.9111 15.7889 12.9111 15.9445 11.5889 17.1889C11.5111 17.2667 11.5111 17.5 11.6666 17.5C15.6333 17.8889 15.6333 18.0445 11.6666 18.0445Z" fill="white"/>
    </svg>`
  },
  diamond: {
    name: 'Diamond',
    color: '#FF8187',
    iconSvg: `<svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M13.873 4.61237H8.88559C8.70619 4.61237 8.53388 4.69833 8.40558 4.8519L3.70629 10.4758C3.55613 10.6555 3.48903 10.8967 3.50145 11.132L12.1851 14.2475L13.873 4.61237Z" fill="#FF5F66"/>
      <path d="M24.289 10.4863L19.7316 5.12968L19.4911 4.84675C19.3631 4.6963 19.1927 4.6123 19.0154 4.6123H13.9377L16.331 13.1732L24.4993 11.132C24.508 10.8993 24.4388 10.6624 24.289 10.4863Z" fill="#FA184B"/>
      <path d="M17.854 11.132L13.9061 9.74603L10.1181 11.132L13.8304 23.3804C13.8905 23.3903 13.9514 23.3903 14.0116 23.3806L17.8604 11.1427L17.854 11.132Z" fill="#FF5F66"/>
      <path d="M13.9062 11.1318V23.3871C13.9415 23.3881 13.9767 23.3861 14.0117 23.3805L17.8606 11.1425L17.8542 11.1318H13.9062Z" fill="#FA184B"/>
    </svg>`
  },
  doublediamond: {
    name: 'Double Diamond',
    color: '#DABEFF',
    iconSvg: `<svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M18.9956 7.59085H18.9952C17.2559 7.27931 15.7828 7.7167 14.5754 8.90267C13.9831 9.74196 13.9887 10.6024 14.4693 11.4798C15.7329 11.7951 17.0352 11.7832 18.3735 11.4668L18.9756 9.74807C19.222 9.04414 19.225 8.28587 18.9956 7.59085Z" fill="#00C8FB"/>
      <path d="M23.8482 20.4671C23.1781 19.2775 22.1167 18.7702 20.7534 18.7891C19.2763 19.0742 18.1879 19.9798 17.6617 21.4776C17.2758 22.3369 17.4895 23.1141 18.4645 23.6458L22.6728 21.6213C23.1859 21.3745 23.5967 20.9662 23.8482 20.4671Z" fill="#AC77F2"/>
      <path d="M24.3206 16.8202C23.5012 18.2808 22.2879 18.8845 20.7531 18.7888C19.7598 17.2797 19.73 15.6817 20.4047 14.0186L23.1622 15.5135C23.7047 15.8079 24.1057 16.2765 24.3206 16.8202Z" fill="#BE96F2"/>
    </svg>`
  },
  ambassador: {
    name: 'Ambassador',
    color: '#FFD064',
    iconSvg: `<svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M9.61692 22.8661L12.7871 15.2127L10.2413 14.1582L6.58877 22.9759C6.4349 23.3474 6.78304 23.7303 7.16743 23.6123L9.23853 22.9768C9.29998 22.9579 9.35912 22.9522 9.41999 22.9581L9.61692 22.8661Z" fill="#FFE07D"/>
      <path d="M14.9172 2.94466C15.2992 3.24774 15.8063 3.34251 16.272 3.19793C16.9269 2.99455 17.6355 3.26911 17.9824 3.86057C18.2292 4.28117 18.6677 4.55275 19.1542 4.58612C19.8383 4.63304 20.3999 5.14505 20.5098 5.82191C20.5879 6.30326 20.8988 6.71489 21.3404 6.92177C21.9614 7.21268 22.3001 7.89296 22.1581 8.56377C22.057 9.04081 22.1982 9.537 22.5352 9.88941C23.0091 10.385 23.0792 11.1417 22.7045 11.7159C22.4379 12.1242 22.3903 12.6379 22.5773 13.0883C22.8402 13.7216 22.6322 14.4525 22.0753 14.8526C21.6793 15.137 21.4493 15.5988 21.461 16.0863C21.4774 16.7718 21.0194 17.3782 20.3556 17.5501C19.8835 17.6723 19.5023 18.0199 19.337 18.4786C19.1047 19.1238 18.4585 19.5239 17.7774 19.4443C17.2931 19.3877 16.8121 19.574 16.4922 19.9422C16.0425 20.4598 15.2955 20.5994 14.6892 20.2792C14.258 20.0515 13.7421 20.0515 13.3109 20.2792C12.7046 20.5995 11.9576 20.4598 11.5078 19.9422C11.188 19.574 10.707 19.3877 10.2226 19.4443C9.54157 19.5239 8.89546 19.1238 8.66307 18.4786C8.49782 18.0199 8.11663 17.6723 7.64452 17.5501C6.98068 17.3783 6.52271 16.7718 6.5391 16.0863C6.55074 15.5988 6.3208 15.137 5.92476 14.8526C5.36783 14.4525 5.15988 13.7216 5.4228 13.0883C5.60977 12.6379 5.56218 12.1242 5.29563 11.7159C4.92083 11.1417 4.99095 10.385 5.46487 9.88941C5.8019 9.537 5.94307 9.04081 5.84207 8.56377C5.70002 7.89296 6.03873 7.21264 6.65969 6.92177C7.10128 6.71489 7.41213 6.30326 7.49029 5.82191C7.60013 5.14505 8.16177 4.63309 8.84587 4.58612C9.33238 4.55275 9.77094 4.28117 10.0177 3.86057C10.3646 3.26911 11.0733 2.9946 11.7281 3.19793C12.1938 3.34256 12.7009 3.24774 13.0829 2.94466C13.6201 2.51845 14.3801 2.51845 14.9172 2.94466Z" fill="#E8AE4D"/>
      <path d="M14.1797 14.0364L16.4266 15.5488C16.5149 15.6083 16.6125 15.617 16.698 15.5907C16.7774 15.4828 16.8537 15.3725 16.9269 15.2599C16.9251 15.2384 16.9212 15.2165 16.9148 15.1942L16.1707 12.5899C16.1348 12.4642 16.1787 12.3293 16.2816 12.2488L17.9975 10.9055C17.9691 10.5944 17.9197 10.2894 17.851 9.9918L15.5211 9.90822C15.3905 9.90355 15.2757 9.82015 15.2309 9.69738L14.3021 7.15307C14.1994 6.87167 13.8014 6.87167 13.6986 7.15307L12.7698 9.69729C12.725 9.82006 12.6103 9.90346 12.4796 9.90813L9.77293 10.0052C9.47353 10.016 9.35059 10.3945 9.58644 10.5791L11.7192 12.2487C11.8221 12.3292 11.8659 12.4641 11.83 12.5898L11.0859 15.1941C11.0036 15.4821 11.3256 15.716 11.5741 15.5488L13.821 14.0364C13.9295 13.9634 14.0713 13.9634 14.1797 14.0364Z" fill="#AA7926"/>
    </svg>`
  },
  royalambassador: {
    name: 'Royal Ambassador',
    color: '#ECA72C',
    iconSvg: `<svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M14 26.25C20.9037 26.25 26.5 20.6537 26.5 13.75C26.5 6.84625 20.9037 1.25 14 1.25C7.09625 1.25 1.5 6.84625 1.5 13.75C1.5 20.6537 7.09625 26.25 14 26.25Z" fill="#194E57"/>
      <path d="M17.8439 18.5624H10.1558C9.82642 18.5624 9.53931 18.3382 9.45945 18.0187L7.92183 11.8682C7.85388 11.5963 7.9504 11.3097 8.16908 11.1343C8.38772 10.9588 8.68846 10.9268 8.93921 11.0522L11.4199 12.2925L13.3844 9.01838C13.5142 8.80218 13.7478 8.66992 13.9999 8.66992C14.252 8.66992 14.4856 8.80223 14.6154 9.01838L16.5799 12.2925L19.0606 11.0522C19.3112 10.9268 19.612 10.9588 19.8307 11.1343C20.0494 11.3097 20.1459 11.5963 20.0779 11.8682L18.5403 18.0187C18.4604 18.3382 18.1733 18.5624 17.8439 18.5624Z" fill="#FFE66F"/>
    </svg>`
  }
}

// Current rank computed property
const currentRank = computed(() => {
  return rankDefinitions[userRank.value] || rankDefinitions.norank
})

// Language dropdown state
const isLanguageDropdownOpen = ref(false)
const selectedLanguage = ref({
  code: 'ENG',
  name: 'English',
  country: 'us'
})

// Available languages
const languages = [
  { code: 'ENG', name: 'English', country: 'us' },
  { code: 'ESP', name: 'Spanish', country: 'spain' },
  { code: 'FRA', name: 'French', country: 'france' },
  { code: 'DEU', name: 'German', country: 'germany' },
  { code: 'ITA', name: 'Italian', country: 'italy' },
  { code: 'JPN', name: 'Japanese', country: 'japan' },
  { code: 'KOR', name: 'Korean', country: 'korea' },
  { code: 'CHN', name: 'Chinese', country: 'china' },
  { code: 'RUS', name: 'Russian', country: 'russia' },
  { code: 'ARA', name: 'Arabic', country: 'uae' }
]

// Methods
const handleBackdropClick = (event) => {
  // Close language dropdown if open
  if (isLanguageDropdownOpen.value) {
    isLanguageDropdownOpen.value = false
  }

  // Only close if clicking the backdrop itself, not the modal content
  if (event.target === event.currentTarget) {
    emit('close')
  }
}

const onMenuClick = (item) => {
  console.log('Menu item clicked:', item)
  
  // Handle different menu actions
  switch(item) {
    case 'calculator':
      // Navigate to calculator
      break
    case 'ambassador':
      // Navigate to ambassador program
      break
    case 'verification':
      // Navigate to verification
      break
    case 'security':
      // Navigate to security settings
      break
    case 'settings':
      // Navigate to settings
      break
    case 'support':
      // Navigate to support
      break
    case 'help':
      // Navigate to help
      break
    case 'upgrade':
      // Handle upgrade action
      break
    case 'language':
      // Handle language selection
      break
    default:
      console.log('Unknown menu item:', item)
  }
  
  // Telegram WebApp haptic feedback
  if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {
    window.Telegram.WebApp.HapticFeedback.impactOccurred('light')
  }
}

const copyUserID = () => {
  const userID = '515745'
  navigator.clipboard.writeText(userID).then(() => {
    console.log('User ID copied to clipboard')

    // Telegram WebApp haptic feedback
    if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {
      window.Telegram.WebApp.HapticFeedback.notificationOccurred('success')
    }
  }).catch(err => {
    console.error('Failed to copy user ID: ', err)
  })
}

const toggleLanguageDropdown = () => {
  isLanguageDropdownOpen.value = !isLanguageDropdownOpen.value

  // Telegram WebApp haptic feedback
  if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {
    window.Telegram.WebApp.HapticFeedback.impactOccurred('light')
  }
}

const selectLanguage = (language) => {
  selectedLanguage.value = language
  isLanguageDropdownOpen.value = false
  console.log('Language selected:', language)

  // Telegram WebApp haptic feedback
  if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {
    window.Telegram.WebApp.HapticFeedback.selectionChanged()
  }
}

console.log('ProfileOverlay loaded with corrected design')
</script>

<style scoped>
.profile-overlay {
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from { 
    opacity: 0; 
    transform: scale(0.95);
  }
  to { 
    opacity: 1; 
    transform: scale(1);
  }
}

/* Prevent touch highlighting */
* {
  -webkit-tap-highlight-color: transparent;
}

/* Responsive adjustments - Full width on all screens */
@media (max-width: 375px) {
  .ml-4 {
    margin-left: 0.75rem;
  }
  .mr-6 {
    margin-right: 1rem;
  }
}

/* Ensure proper backdrop blur on iOS Safari */
.backdrop-blur-md {
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
}

/* Smooth hover effects */
.hover\:bg-white\/\[0\.05\]:hover {
  transition: background-color 0.2s ease-in-out;
}

/* Custom scrollbar for webkit browsers */
.overflow-y-auto::-webkit-scrollbar {
  width: 2px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  background: transparent;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  background: rgba(183, 183, 183, 0.4);
  border-radius: 30px;
}

/* Responsive height adjustments */
@media (max-height: 800px) {
  .max-h-60 {
    max-height: 12rem; /* 192px */
  }
}

@media (max-height: 700px) {
  .max-h-60 {
    max-height: 10rem; /* 160px */
  }

  .max-h-\[calc\(100vh-176px\)\] {
    max-height: calc(100vh - 140px);
  }
}

@media (max-height: 600px) {
  .max-h-60 {
    max-height: 8rem; /* 128px */
  }

  .max-h-\[calc\(100vh-176px\)\] {
    max-height: calc(100vh - 120px);
  }
}

@media (max-height: 500px) {
  .max-h-60 {
    max-height: 6rem; /* 96px */
  }

  .max-h-\[calc\(100vh-176px\)\] {
    max-height: calc(100vh - 100px);
  }
}

/* Mobile width adjustments */
@media (max-width: 320px) {
  .mx-4 {
    margin-left: 0.5rem;
    margin-right: 0.5rem;
  }
}

/* Ensure proper gap spacing on smaller screens */
@media (max-width: 375px) {
  .mx-4 {
    margin-left: 0.75rem;
    margin-right: 0.75rem;
  }
}

/* Dropdown animation styles */
.dropdown-enter-active,
.dropdown-leave-active {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  transform-origin: bottom center;
}

.dropdown-enter-from,
.dropdown-leave-to {
  opacity: 0;
  transform: scale(0.95) translateY(8px);
}

.dropdown-enter-to,
.dropdown-leave-from {
  opacity: 1;
  transform: scale(1) translateY(0);
}

/* Custom scrollbar for language dropdown */
.max-h-32::-webkit-scrollbar {
  width: 3px;
}

.max-h-32::-webkit-scrollbar-track {
  background: transparent;
}

.max-h-32::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.3);
  border-radius: 2px;
}

.max-h-32::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.5);
}

/* Responsive margin adjustments for all screens */
@media (min-width: 769px) {
  .ml-4 {
    margin-left: 1.5rem; /* 24px */
  }
  .mr-6 {
    margin-right: 2rem; /* 32px */
  }
}

@media (min-width: 641px) and (max-width: 768px) {
  .ml-4 {
    margin-left: 1.25rem; /* 20px */
  }
  .mr-6 {
    margin-right: 1.75rem; /* 28px */
  }
}

/* Responsive ID/ENG block adjustments */
@media (max-width: 640px) {
  .w-36 {
    width: 9.5rem; /* 152px - увеличиваем на мобиле */
  }
  .ml-4 {
    margin-left: 1rem; /* 16px */
  }
  .mr-6 {
    margin-right: 1.5rem; /* 24px */
  }
}

@media (max-width: 480px) {
  .w-36 {
    width: 10rem; /* 160px - еще больше для лучшей видимости */
  }
  .ml-4 {
    margin-left: 0.875rem; /* 14px */
  }
  .mr-6 {
    margin-right: 1.25rem; /* 20px */
  }
}

@media (max-width: 375px) {
  .w-36 {
    width: 9.75rem; /* 156px */
  }

  .ml-4 {
    margin-left: 0.75rem;
  }
  .mr-6 {
    margin-right: 1rem;
  }
}

/* Fix flag container to prevent distortion */
.country-flag {
  min-width: 100%;
  min-height: 100%;
  object-fit: cover;
}
</style>
