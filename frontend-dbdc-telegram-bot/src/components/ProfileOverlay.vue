<template>
  <div v-if="isVisible" class="fixed inset-0 z-50 font-montserrat bg-black bg-opacity-10 backdrop-blur-xl">
    <!-- Triangle Pointer -->
    <div class="absolute left-8 lg:left-9 bottom-[110px] sm:bottom-[105px] md:bottom-[200px] lg:bottom-[180px] xl:bottom-[170px] z-[65]
                transition-all duration-300 safe-area-inset-bottom-calc">
      <div class="w-0 h-0 border-l-[12px] border-r-[12px] border-t-[15px] 
                  border-l-transparent border-r-transparent 
                  border-t-[rgba(18,11,129,0.95)] 
                  drop-shadow-md"></div>
    </div>

    <!-- Profile Dropdown Menu -->
    <div class="absolute left-2 right-2 bottom-[110px] sm:bottom-[115px] md:bottom-[210px] lg:bottom-[190px] xl:bottom-[180px]
                h-[580px] sm:h-[560px] md:h-[580px] lg:h-[500px] xl:h-[450px]
                max-h-[calc(100vh-130px)] sm:max-h-[calc(100vh-120px)] md:max-h-[calc(100vh-215px)] lg:max-h-[calc(100vh-210px)] xl:max-h-[calc(100vh-200px)]
                rounded-[20px] overflow-hidden z-[55] transition-all duration-300 safe-area-inset-calc" 
         @click.stop>
      
      <!-- Background -->
      <div class="absolute inset-0 bg-gradient-to-r from-[#120B81] via-[#09074E] to-[#09074E] 
                  border border-white border-opacity-8 backdrop-blur-[32px]"></div>

      <!-- Profile Header Section -->
      <div class="absolute top-3 left-3 right-3 z-[2]">
        <div class="w-full h-24 bg-[rgba(96,95,135,0.24)] border border-[#D8D8D8] 
                    rounded-[1000px_20px_20px_1000px] 
                    flex items-center p-2 gap-3 overflow-hidden">
          
          <!-- Avatar -->
          <div class="flex-shrink-0">
            <img src="https://images.pexels.com/photos/15023413/pexels-photo-15023413.jpeg?auto=compress&cs=tinysrgb&w=400" 
                 alt="Jason Williams" 
                 class="w-20 h-20 rounded-full object-cover border border-[#7E73D6]" />
          </div>

          <!-- User Info -->
          <div class="flex-1 flex flex-col gap-1.5 px-1 min-w-0 overflow-hidden">
            <!-- Silver Badge -->
            <div class="flex items-center gap-1.5 px-4 py-0.5 pr-4 pl-0.5 
                        bg-[rgba(110,107,169,0.90)] border border-[#D8D8D8] 
                        rounded-3xl w-fit">
              <div class="w-7 h-7 flex-shrink-0">
                <svg width="28" height="28" viewBox="0 0 28 28" fill="none">
                  <path d="M14.0004 26.2497C7.24592 26.2497 1.75073 20.7545 1.75073 14.0001C1.75073 7.24564 7.24592 1.75085 14.0004 1.75085C20.7548 1.75085 26.25 7.24564 26.25 14.0001C26.25 20.7545 20.7544 26.2497 14.0004 26.2497Z" fill="white"/>
                  <path d="M20.2071 5.37145C20.73 5.37145 21.2468 5.39833 21.7567 5.4472C19.7049 3.58479 16.9828 2.44812 14 2.44812C7.63041 2.44812 2.448 7.63013 2.448 14.0001C2.448 16.2735 3.11102 18.3941 4.24973 20.1832C4.86143 11.9015 11.769 5.37145 20.2071 5.37145Z" fill="#E0E0E0"/>
                  <path d="M14.0006 25.5519C20.3702 25.5519 25.5526 20.3699 25.5526 13.9999C25.5526 10.6131 24.0873 7.56229 21.7577 5.44697C21.2478 5.39809 20.731 5.37122 20.2081 5.37122C11.7704 5.37122 4.86244 11.9017 4.25073 20.1829C6.30211 23.4072 9.90475 25.5519 14.0006 25.5519Z" fill="#B5B5B5"/>
                  <path d="M14.0004 23.1368C19.0464 23.1368 23.1369 19.0463 23.1369 14.0003C23.1369 8.95433 19.0464 4.86377 14.0004 4.86377C8.95445 4.86377 4.86389 8.95433 4.86389 14.0003C4.86389 19.0463 8.95445 23.1368 14.0004 23.1368Z" fill="#9E9E9E"/>
                  <path d="M19.4965 12.7667L15.6984 12.2148L14.0001 8.77307L12.3014 12.2148L8.50366 12.7667L11.2519 15.4452L10.6031 19.2279L14.0001 17.4421L17.397 19.2279L16.7483 15.4452L19.4965 12.7667Z" fill="#F6F6F6"/>
                  <path d="M20.5542 6.30372C20.755 6.5045 21.4074 6.81443 21.7117 6.9529C21.7728 6.98059 21.7728 7.06693 21.7117 7.09462C21.4074 7.23309 20.7554 7.54261 20.5542 7.7438C20.3534 7.94458 20.0435 8.59701 19.905 8.90124C19.8774 8.96233 19.791 8.96233 19.7633 8.90124C19.6249 8.59701 19.3153 7.94499 19.1141 7.7438C18.9134 7.54302 18.2609 7.23309 17.9567 7.09462C17.8956 7.06693 17.8956 6.98059 17.9567 6.9529C18.2609 6.81443 18.913 6.50491 19.1141 6.30372C19.3149 6.10294 19.6249 5.45051 19.7633 5.14628C19.791 5.08519 19.8774 5.08519 19.905 5.14628C20.0431 5.45051 20.353 6.10253 20.5542 6.30372Z" fill="white"/>
                  <path d="M19.4971 12.7667L15.699 12.2144L14.0007 8.77307V17.4421L17.3977 19.2279L16.7489 15.4452L19.4971 12.7667Z" fill="#E0E0E0"/>
                </svg>
              </div>
              <span class="text-dbd-off-white text-sm font-medium leading-5">Silver</span>
            </div>

            <!-- User Name -->
            <h2 class="text-white text-lg font-bold leading-5 m-0 whitespace-nowrap overflow-hidden text-ellipsis">
              Jason Williams
            </h2>
          </div>

          <!-- Arrow Button -->
          <button class="w-11 h-11 bg-dbd-light-blue border border-dbd-primary 
                         rounded-r-[1000px] flex items-center justify-center 
                         cursor-pointer transition-all duration-200 hover:bg-[#E0D9FF] hover:scale-105
                         flex-shrink-0" 
                  @click="$emit('close')">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path d="M17.2155 11.2862L8.2216 2.29534C7.82696 1.90169 7.18757 1.90169 6.79192 2.29534C6.39728 2.68898 6.39728 3.32838 6.79192 3.72203L15.0724 11.9996L6.79292 20.2771C6.39827 20.6707 6.39827 21.3101 6.79292 21.7048C7.18756 22.0984 7.82795 22.0984 8.2226 21.7048L17.2165 12.7139C17.6051 12.3244 17.6051 11.6749 17.2155 11.2862Z" fill="#B7B7B7"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- Menu Items -->
      <div class="absolute top-[130px] bottom-[178px] left-3 right-3 z-[1] 
                  overflow-y-auto overflow-x-hidden scrollbar-none
                  [-webkit-overflow-scrolling:touch] [scroll-behavior:smooth] 
                  [overscroll-behavior:contain] [overscroll-behavior-y:contain]">
        
        <!-- Calculator -->
        <div class="flex items-center gap-2 px-3 py-1.5 h-13 cursor-pointer 
                    transition-all duration-200 rounded-lg mb-2 mt-3
                    hover:bg-white hover:bg-opacity-10 hover:translate-x-1 relative" 
             @click="handleMenuClick('calculator')">
          <div class="w-10 h-10 bg-gray-600 bg-opacity-24 border border-white border-opacity-24 
                      rounded-full flex items-center justify-center flex-shrink-0 opacity-24">
            <div class="flex items-center justify-center">
              <svg width="20" height="20" viewBox="0 0 16 20" fill="none">
                <path d="M14.1377 0C15.1645 0 16 0.788555 16 1.75781V18.2422C16 19.2114 15.1645 20 14.1377 20H1.8623C0.835502 20 0 19.2114 0 18.2422V1.75781C0 0.788555 0.835502 0 1.8623 0H14.1377ZM1.8623 1.17188C1.52004 1.17188 1.24121 1.43473 1.24121 1.75781V18.2422C1.24121 18.5653 1.52004 18.8281 1.8623 18.8281H14.1377C14.48 18.8281 14.7587 18.5653 14.7588 18.2422V1.75781C14.7588 1.43473 14.48 1.17188 14.1377 1.17188H1.8623Z..." fill="white"/>
              </svg>
            </div>
          </div>
          <span class="text-white text-base font-bold leading-7 flex-1">Calculator</span>
        </div>

        <!-- Ambassador -->
        <div class="flex items-center gap-2 px-3 py-1.5 h-13 cursor-pointer 
                    transition-all duration-200 rounded-lg mb-2
                    hover:bg-white hover:bg-opacity-10 hover:translate-x-1 relative" 
             @click="handleMenuClick('ambassador')">
          <div class="w-10 h-10 bg-gray-600 bg-opacity-24 border border-white border-opacity-24 
                      rounded-full flex items-center justify-center flex-shrink-0 opacity-24">
            <div class="flex items-center justify-center">
              <svg width="14" height="20" viewBox="0 0 14 20" fill="none">
                <path d="M7 9.64844C9.76508 9.64858 12.0066 11.9652 12.0068 14.8242C12.0068 17.6826 9.76511 19.9999 7 20C4.23394 20 1.99219 17.6827 1.99219 14.8242C1.99243 11.9651 4.23409 9.64844 7 9.64844ZM6.09668 13.8418L4.07715 14.1465L5.53906 15.6182L5.19434 17.6992L7 16.7168L8.80566 17.6992L8.46191 15.6182L9.92383 14.1465L7.90332 13.8418L7 11.9512L6.09668 13.8418ZM4.60547 0L7 3.30078L9.39453 0H14L7 9.64844L0 0H4.60547Z" fill="white"/>
              </svg>
            </div>
          </div>
          <span class="text-white text-base font-bold leading-7 flex-1">Ambassador</span>
        </div>

        <!-- Verification -->
        <div class="flex items-center gap-2 px-3 py-1.5 h-13 cursor-pointer 
                    transition-all duration-200 rounded-lg mb-2
                    hover:bg-white hover:bg-opacity-10 hover:translate-x-1 relative" 
             @click="handleMenuClick('verification')">
          <div class="w-10 h-10 bg-gray-600 bg-opacity-24 border border-white border-opacity-24 
                      rounded-full flex items-center justify-center flex-shrink-0 opacity-24">
            <div class="flex items-center justify-center">
              <svg width="18" height="22" viewBox="0 0 18 22" fill="none">
                <path d="M14.2511 12.4974C15.4932 12.4974 16.5 13.5045 16.5 14.7467V15.3222C16.5 16.2166 16.1805 17.0816 15.5989 17.7611C14.0295 19.5949 11.6422 20.5 8.49673 20.5C5.35076 20.5 2.96466 19.5946 1.39831 17.7601C0.818531 17.081 0.5 16.2174 0.5 15.3245V14.7467C0.5 13.5045 1.50689 12.4974 2.74896 12.4974H14.2511Z..." fill="white"/>
              </svg>
            </div>
          </div>
          <span class="text-white text-base font-bold leading-7 flex-1">Verification</span>
          <!-- Error Badge -->
          <div class="absolute right-4 top-1/2 transform -translate-y-1/2 w-6 h-6 
                      rounded-full bg-[#FFF0F3] border-[0.667px] border-[#FF1919] 
                      flex items-center justify-center flex-shrink-0">
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
              <path d="M7 0C10.866 0 14 3.134 14 7C14 10.866 10.866 14 7 14C3.134 14 0 10.866 0 7C0 3.134 3.134 0 7 0Z" fill="#FF1919"/>
              <path d="M10.5 4.5L4.5 10.5M4.5 4.5L10.5 10.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
        </div>

        <!-- Security -->
        <div class="flex items-center gap-2 px-3 py-1.5 h-13 cursor-pointer 
                    transition-all duration-200 rounded-lg mb-2
                    hover:bg-white hover:bg-opacity-10 hover:translate-x-1 relative" 
             @click="handleMenuClick('security')">
          <div class="w-10 h-10 bg-gray-600 bg-opacity-24 border border-white border-opacity-24 
                      rounded-full flex items-center justify-center flex-shrink-0 opacity-24">
            <div class="flex items-center justify-center">
              <svg width="18" height="20" viewBox="0 0 18 20" fill="none">
                <path d="M8.78516 0.0354746C8.92389 -0.0121504 9.07611 -0.0121504 9.21484 0.0354746C10.6561 0.531013 12.1438 0.945188 13.6377 1.26497C14.8838 1.5317 16.1601 1.73823 17.4297 1.87922C17.7546 1.91522 18 2.18263 18 2.50032V8.7386C17.9998 13.165 15.3282 17.2234 11.1943 19.0784L9.26953 19.9427C9.18416 19.9808 9.09193 20.0003 9 20.0003C8.90802 20.0003 8.81583 19.9808 8.73047 19.9427L6.80566 19.0784C2.67178 17.2233 0.000192532 13.165 0 8.7386V2.50032C0 2.18263 0.245411 1.91529 0.570312 1.87922C1.83994 1.73823 3.11627 1.53164 4.3623 1.26497C5.85626 0.945192 7.34396 0.531005 8.78516 0.0354746Z..." fill="white"/>
              </svg>
            </div>
          </div>
          <span class="text-white text-base font-bold leading-7 flex-1">Security</span>
        </div>

        <!-- Settings -->
        <div class="flex items-center gap-2 px-3 py-1.5 h-13 cursor-pointer 
                    transition-all duration-200 rounded-lg mb-2
                    hover:bg-white hover:bg-opacity-10 hover:translate-x-1 relative" 
             @click="handleMenuClick('settings')">
          <div class="w-10 h-10 bg-gray-600 bg-opacity-24 border border-white border-opacity-24 
                      rounded-full flex items-center justify-center flex-shrink-0 opacity-24">
            <div class="flex items-center justify-center">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M12.2222 20L12.3457 19.375L12.8148 17.0913C13.5679 16.8029 14.2469 16.3972 14.8642 15.9135L17.1605 16.6827L17.7778 16.875L18.0988 16.3221L19.679 13.6778L20 13.125L19.5309 12.7163L17.7531 11.2019C17.8179 10.8083 17.9012 10.4147 17.9012 10C17.9012 9.58531 17.8179 9.19169 17.7531 8.79808L19.5309 7.28369L20 6.875L19.679 6.32215L18.0988 3.67785L17.7778 3.125L17.1605 3.31731L14.8642 4.08654C14.2469 3.60277 13.5679 3.19708 12.8148 2.90862L12.3457 0.625L12.2222 0H7.77775L7.65426 0.625L7.18516 2.90862C6.43209 3.19708 5.75306 3.60277 5.13581 4.08654L2.83947 3.31731L2.22215 3.125L1.9012 3.67785L0.32095 6.32215L0 6.875L0.469097 7.28369L2.24688 8.79808C2.18209 9.19169 2.09873 9.58531 2.09873 10C2.09873 10.4147 2.18209 10.8083 2.24688 11.2019L0.469097 12.7163L0 13.125L0.32095 13.6778L1.9012 16.3221L2.22215 16.875L2.83947 16.6827L5.13581 15.9135C5.75306 16.3972 6.43209 16.8029 7.18516 17.0913L7.65426 19.375L7.77775 20H12.2222Z..." fill="white"/>
              </svg>
            </div>
          </div>
          <span class="text-white text-base font-bold leading-7 flex-1">Settings</span>
        </div>

        <!-- Support -->
        <div class="flex items-center gap-2 px-3 py-1.5 h-13 cursor-pointer 
                    transition-all duration-200 rounded-lg mb-2
                    hover:bg-white hover:bg-opacity-10 hover:translate-x-1 relative" 
             @click="handleMenuClick('support')">
          <div class="w-10 h-10 bg-gray-600 bg-opacity-24 border border-white border-opacity-24 
                      rounded-full flex items-center justify-center flex-shrink-0 opacity-24">
            <div class="flex items-center justify-center">
              <svg width="18" height="20" viewBox="0 0 18 20" fill="none">
                <path d="M8.99902 0C13.9325 0 17.998 3.80872 17.998 8.58691V10.1348C17.9981 10.1411 17.999 10.1479 17.999 10.1543V12.9561C17.9992 12.9624 18 12.9692 18 12.9756V14.543C17.9997 16.724 16.1499 18.4277 13.9502 18.4277H11.2695C10.9422 19.3551 10.0281 19.9951 8.99902 19.9951C7.71066 19.9949 6.59988 18.993 6.59961 17.6777C6.59962 16.3623 7.71051 15.3606 8.99902 15.3604C10.0286 15.3604 10.9435 15.9998 11.2705 16.9277H13.9502C15.1589 16.9277 16.1261 16.1539 16.4111 15.1514C16.155 15.2407 15.8817 15.293 15.5986 15.293C14.3103 15.2927 13.1995 14.2908 13.1992 12.9756V10.1543C13.1992 8.83884 14.3101 7.83714 15.5986 7.83691C15.9032 7.83691 16.1972 7.89422 16.4697 7.99707C16.1535 4.38853 12.9637 1.5 8.99902 1.5C5.03445 1.50011 1.84359 4.38856 1.52734 7.99707C1.80001 7.89396 2.09449 7.83697 2.39941 7.83691C3.6881 7.83691 4.7998 8.83869 4.7998 10.1543V12.9756C4.79953 14.291 3.68794 15.293 2.39941 15.293C1.11107 15.2927 0.000274862 14.2908 0 12.9756V8.58691C4.31105e-05 3.80879 4.0657 0.000121624 8.99902 0Z..." fill="white"/>
              </svg>
            </div>
          </div>
          <span class="text-white text-base font-bold leading-7 flex-1">Support</span>
        </div>

        <!-- Help -->
        <div class="flex items-center gap-2 px-3 py-1.5 h-13 cursor-pointer 
                    transition-all duration-200 rounded-lg mb-3
                    hover:bg-white hover:bg-opacity-10 hover:translate-x-1 relative" 
             @click="handleMenuClick('help')">
          <div class="w-10 h-10 bg-gray-600 bg-opacity-24 border border-white border-opacity-24 
                      rounded-full flex items-center justify-center flex-shrink-0 opacity-24">
            <div class="flex items-center justify-center">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M9.69301 13.4082C9.12117 13.4082 8.6582 13.8848 8.6582 14.4566C8.6582 15.0149 9.10754 15.5051 9.69301 15.5051C10.2785 15.5051 10.7414 15.0149 10.7414 14.4566C10.7414 13.8848 10.2649 13.4082 9.69301 13.4082Z" fill="white"/>
                <path d="M9.86984 5.46875C8.03168 5.46875 7.1875 6.55801 7.1875 7.29328C7.1875 7.82434 7.6368 8.06941 8.00445 8.06941C8.73969 8.06941 8.44016 7.02098 9.82898 7.02098C10.5098 7.02098 11.0545 7.32055 11.0545 7.94687C11.0545 8.68219 10.292 9.10426 9.84262 9.48551C9.44777 9.8259 8.93035 10.3842 8.93035 11.5552C8.93035 12.2632 9.12094 12.4674 9.67922 12.4674C10.3464 12.4674 10.4825 12.1679 10.4825 11.9092C10.4825 11.2011 10.4962 10.7927 11.2451 10.2072C11.6127 9.92125 12.7701 8.99535 12.7701 7.71543C12.7701 6.43551 11.6127 5.46875 9.86984 5.46875Z" fill="white"/>
                <path d="M10 0C4.47328 0 0 4.47254 0 10V19.2188C0 19.6502 0.349766 20 0.78125 20H10C15.5267 20 20 15.5275 20 10C20 4.47328 15.5275 0 10 0ZM10 18.4375H1.5625V10C1.5625 5.33684 5.33621 1.5625 10 1.5625C14.6632 1.5625 18.4375 5.33621 18.4375 10C18.4375 14.6632 14.6638 18.4375 10 18.4375Z" fill="white"/>
              </svg>
            </div>
          </div>
          <span class="text-white text-base font-bold leading-7 flex-1">Help</span>
        </div>
      </div>

      <!-- Start Section -->
      <div class="absolute bottom-[86px] sm:bottom-[84px] left-3 right-3 z-[1]">
        <div class="w-full h-21 bg-[#F1E7FF] border border-[#DCCCF1] rounded-2xl 
                    flex flex-col justify-center p-2 relative overflow-hidden">
          <!-- Background gradient -->
          <div class="absolute left-0 top-0 w-[140px] h-full 
                      bg-gradient-to-r from-[#8C4CD1] to-[#C497FF] 
                      opacity-40 rounded-l-2xl"></div>
          
          <div class="flex items-center justify-between mb-1 relative z-[1]">
            <div class="flex items-center gap-3 flex-1">
              <div class="flex-shrink-0">
                <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                  <g clip-path="url(#clip0_2_21309)">
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
              <div class="text-dbd-dark text-lg font-bold leading-6 mb-1">Start</div>
            </div>
            <button class="relative z-[1] w-[120px] h-11 
                           bg-gradient-to-r from-dbd-primary to-[#473FFF] 
                           border-none rounded-full text-white text-base font-bold leading-5 
                           capitalize cursor-pointer transition-all duration-200 
                           hover:-translate-y-0.5 hover:shadow-lg flex-shrink-0" 
                    @click="handleUpgrade">
              Upgrade
            </button>
          </div>
          <div class="relative z-[1]">
            <div class="text-dbd-gray text-sm font-normal leading-6">
              buy <span class="text-[#8C4CD1] font-bold">123</span> more Forevers to upgrade
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom Controls -->
      <div class="absolute bottom-3 sm:bottom-2 left-3 right-3 z-[1] 
                  flex justify-center items-center gap-5 h-11">
        
        <!-- ID Section -->
        <div class="w-[145px] h-11 bg-white bg-opacity-30 border border-white border-opacity-40 
                    rounded-full backdrop-blur-[32px] flex items-center justify-between p-1.5 
                    relative transition-all duration-[400ms] ease-[cubic-bezier(0.4,0,0.2,1)]"
             :class="{ 'border-[#07B80E] bg-[#129E0F] scale-[1.02]': showCopySuccess }">
          
          <div v-if="!showCopySuccess" class="flex items-center gap-0.5 pl-3 pr-10 flex-1">
            <span class="text-[#B7B7B7] text-sm font-normal leading-6">ID: </span>
            <span class="text-white text-sm font-normal leading-6">515745</span>
          </div>
          
          <div v-if="showCopySuccess" class="w-full h-full flex items-center justify-center gap-2 p-1.5 box-border animate-[fadeInScale_0.4s_cubic-bezier(0.4,0,0.2,1)]">
            <span class="text-white text-sm font-semibold leading-6 text-center animate-[slideInLeft_0.3s_ease-out_0.1s_both]">Copied</span>
            <div class="relative w-7 h-7 flex items-center justify-center animate-[bounceIn_0.5s_ease-out_0.2s_both]">
              <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="14" cy="14" r="14" fill="white"/>
              </svg>
              <svg class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_2_22327)">
                  <path d="M11.3242 0.926106C10.7978 0.642629 10.2106 1.18934 9.86633 1.51331C9.07667 2.28275 8.40848 3.17368 7.65925 3.98362C6.82907 4.87455 6.05963 5.76548 5.20919 6.6362C4.72323 7.12216 4.19677 7.64862 3.8728 8.25607C3.14385 7.54734 2.51615 6.7779 1.70621 6.15023C1.11901 5.70477 0.147086 5.38079 0.167334 6.45396C0.207831 7.85113 1.44299 9.34952 2.35416 10.3012C2.73888 10.7061 3.24509 11.1313 3.8323 11.1516C4.54099 11.1921 5.26994 10.3417 5.69515 9.87594C6.44438 9.06601 7.05183 8.15479 7.74024 7.32464C8.63118 6.23123 9.54236 5.15803 10.413 4.04436C10.9597 3.35592 12.6809 1.65502 11.3242 0.926106ZM1.05823 6.37297C1.03798 6.37297 1.01773 6.37297 0.977238 6.39318C0.896244 6.37297 0.835499 6.35268 0.754505 6.31219C0.815251 6.27169 0.916493 6.29194 1.05823 6.37297Z" fill="#07B80E"/>
                </g>
                <defs>
                  <clipPath id="clip0_2_22327">
                    <rect width="11.6667" height="11.6667" fill="white" transform="translate(0.166992 0.166504)"/>
                  </clipPath>
                </defs>
              </svg>
            </div>
          </div>
          
          <button v-if="!showCopySuccess"
                  class="w-8 h-8 bg-white border-[1.2px] border-[#D8D8D8] 
                         rounded-r-full border-l-0 flex items-center justify-center 
                         cursor-pointer transition-all duration-200 flex-shrink-0 
                         absolute right-0 top-1/2 transform -translate-y-1/2
                         hover:bg-gray-100 hover:scale-105 hover:shadow-lg
                         active:scale-98" 
                  @click="copyUserID">
            <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M18.0655 0.5H7.60611C6.97596 0.5 6.37161 0.727045 5.92603 1.13119C5.48044 1.53533 5.23011 2.08346 5.23011 2.65501V3.48385H4.04211C3.38111 3.48385 2.74718 3.72201 2.27978 4.14594C1.81239 4.56986 1.5498 5.14483 1.5498 5.74435V19.2395C1.5498 19.839 1.81239 20.414 2.27978 20.8379C2.74718 21.2618 3.38111 21.5 4.04211 21.5H14.2772C14.9382 21.5 15.5721 21.2618 16.0395 20.8379C16.5069 20.414 16.7695 19.839 16.7695 19.2395V18.486H18.0655C18.6907 18.4861 19.291 18.2634 19.7369 17.866C20.1829 17.4685 20.4389 16.9281 20.4498 16.3611V2.65501C20.4476 2.08277 20.1954 1.53465 19.7485 1.13073C19.3016 0.7268 18.6964 0.499997 18.0655 0.5ZM15.108 19.2395C15.108 19.4393 15.0204 19.631 14.8646 19.7723C14.7088 19.9136 14.4975 19.993 14.2772 19.993H4.04211C3.82178 19.993 3.61047 19.9136 3.45467 19.7723C3.29887 19.631 3.21134 19.4393 3.21134 19.2395V5.74435C3.21134 5.54451 3.29887 5.35285 3.45467 5.21154C3.61047 5.07024 3.82178 4.99085 4.04211 4.99085H14.2772C14.4975 4.99085 14.7088 5.07024 14.8646 5.21154C15.0204 5.35285 15.108 5.54451 15.108 5.74435V19.2395ZM18.7883 16.3611C18.7861 16.5337 18.709 16.6985 18.5737 16.8198C18.4383 16.9411 18.2558 17.0092 18.0655 17.0092H16.7695V5.74435C16.7695 5.14483 16.5069 4.56986 16.0395 4.14594C15.5721 3.72201 14.9382 3.48385 14.2772 3.48385H6.89165V2.65501C6.89165 2.48314 6.96693 2.31832 7.10091 2.19679C7.2349 2.07527 7.41663 2.007 7.60611 2.007H18.0655C18.16 2.006 18.2538 2.02203 18.3415 2.05414C18.4291 2.08626 18.5089 2.13384 18.5761 2.19411C18.6433 2.25438 18.6967 2.32616 18.7331 2.40527C18.7695 2.48439 18.7883 2.56927 18.7883 2.65501V16.3611Z" fill="#2019CE"/>
            </svg>
          </button>
        </div>

        <!-- Vertical Divider -->
        <div class="w-0.5 h-6 bg-[#E2E2E2] border border-[#B7B7B7] rounded-[30px] opacity-40 flex-shrink-0"></div>

        <!-- Language Section -->
        <div class="w-[131px] h-11 bg-white bg-opacity-20 border border-white border-opacity-24 
                    rounded-full flex items-center p-1.5 cursor-pointer transition-all duration-200 
                    relative overflow-visible hover:bg-white hover:bg-opacity-30" 
             @click="toggleLanguageDropdown">
          
          <div class="flex items-center gap-1.5 flex-1 min-w-0 pr-6">
            <CountryFlag :country="selectedLanguage.country" size="medium" class="flex-shrink-0 !w-8 !h-8 !min-w-8 !min-h-8" />
            <span class="text-dbd-off-white text-base font-normal leading-7 flex-shrink-0 whitespace-nowrap w-10 text-left">
              {{ selectedLanguage.code }}
            </span>
          </div>
          
          <div class="w-5 h-5 flex items-center justify-center flex-shrink-0 
                      transition-transform duration-200 absolute right-1.5 top-1/2 
                      transform -translate-y-1/2"
               :class="{ 'rotate-180': showLanguageDropdown }">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <circle opacity="0.2" cx="10" cy="10" r="10" fill="white"/>
              <path d="M5.71387 8.57146L9.99958 12.8572L14.2853 8.57146" stroke="white" stroke-linecap="round"/>
            </svg>
          </div>

          <!-- Language Dropdown -->
          <div v-if="showLanguageDropdown" 
               class="absolute bottom-[50px] left-0 right-0 z-[1000] animate-[dropdownSlideUp_0.2s_ease-out]">
            <div class="bg-gradient-to-r from-[#120B81] via-[#09074E] to-[#09074E] 
                        border border-white border-opacity-8 rounded-2xl 
                        backdrop-blur-[32px] p-2 max-h-[140px] overflow-y-auto 
                        scrollbar-none shadow-[0_8px_32px_rgba(0,0,0,0.3)]">
              <div v-for="(language, index) in languages"
                   :key="language.code"
                   class="flex items-center gap-2.5 px-3 py-1.5 rounded-lg cursor-pointer 
                          transition-all duration-200 min-h-9 relative
                          hover:bg-white hover:bg-opacity-10"
                   :class="{ 'bg-white bg-opacity-15': language.code === selectedLanguage.code }"
                   @click.stop="selectLanguage(language)">
                <CountryFlag :country="language.country" size="small" class="flex-shrink-0 !w-6 !h-6 !min-w-6 !min-h-6" />
                <span class="text-dbd-off-white text-sm font-medium leading-5 flex-1 mr-6">
                  {{ language.code }}
                </span>
                <svg v-if="language.code === selectedLanguage.code" 
                     class="absolute right-3 top-1/2 transform -translate-y-1/2 flex-shrink-0" 
                     width="16" height="16" viewBox="0 0 16 16" fill="none">
                  <path d="M13.5 4.5L6 12L2.5 8.5" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CountryFlag from './CountryFlag.vue'

// Props
defineProps({
  isVisible: {
    type: Boolean,
    default: false
  }
})

// Emits
const emit = defineEmits(['close'])

// State
const showCopySuccess = ref(false)
const showLanguageDropdown = ref(false)

// Language state
const languages = ref([
  { code: 'ENG', name: 'English', country: 'uk' },
  { code: 'ESP', name: 'Español', country: 'spain' },
  { code: 'FRA', name: 'Français', country: 'france' },
  { code: 'DEU', name: 'Deutsch', country: 'germany' },
  { code: 'ITA', name: 'Italiano', country: 'italy' },
  { code: 'RUS', name: 'Русский', country: 'ukraine' },
  { code: 'CHN', name: '中文', country: 'china' },
  { code: 'JPN', name: '日本語', country: 'japan' },
  { code: 'KOR', name: '한국어', country: 'new zealand' },
  { code: 'ARA', name: 'العربية', country: 'uae' },
  { code: 'POR', name: 'Português', country: 'spain' },
  { code: 'NLD', name: 'Nederlands', country: 'norway' }
])

const selectedLanguage = ref(languages.value[0])

// Methods
const handleMenuClick = (menuItem) => {
  console.log(`Menu clicked: ${menuItem}`)
  // Handle menu navigation
}

const handleUpgrade = () => {
  console.log('Upgrade clicked')
  // Handle upgrade
}

const copyUserID = async () => {
  let copySuccess = false

  // Try modern clipboard API first
  if (navigator.clipboard) {
    try {
      await navigator.clipboard.writeText('515745')
      copySuccess = true
    } catch (clipboardErr) {
      console.log('Clipboard API failed, trying fallback method')
    }
  }

  // If clipboard API failed or is not available, use fallback
  if (!copySuccess) {
    try {
      const textArea = document.createElement('textarea')
      textArea.value = '515745'
      textArea.style.position = 'fixed'
      textArea.style.left = '-999999px'
      textArea.style.top = '-999999px'
      textArea.style.opacity = '0'
      document.body.appendChild(textArea)
      textArea.focus()
      textArea.select()

      const successful = document.execCommand('copy')
      document.body.removeChild(textArea)

      if (!successful) {
        console.log('Fallback copy method also failed')
      }
    } catch (fallbackErr) {
      console.error('Fallback copy failed:', fallbackErr)
    }
  }

  // Show copied state for user feedback
  showCopySuccess.value = true
  setTimeout(() => {
    showCopySuccess.value = false
  }, 2500)
}

const toggleLanguageDropdown = () => {
  showLanguageDropdown.value = !showLanguageDropdown.value
}

const selectLanguage = (language) => {
  selectedLanguage.value = language
  showLanguageDropdown.value = false
  console.log('Language selected:', language)
}
</script>

<style scoped>
/* Custom animations */
@keyframes fadeInScale {
  0% {
    opacity: 0;
    transform: scale(0.9);
  }
  50% {
    opacity: 0.8;
    transform: scale(1.05);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes bounceIn {
  0% {
    opacity: 0;
    transform: scale(0.3) rotate(-10deg);
  }
  50% {
    opacity: 0.9;
    transform: scale(1.1) rotate(5deg);
  }
  80% {
    transform: scale(0.95) rotate(-2deg);
  }
  100% {
    opacity: 1;
    transform: scale(1) rotate(0deg);
  }
}

@keyframes dropdownSlideUp {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Custom utilities */
.scrollbar-none {
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.scrollbar-none::-webkit-scrollbar {
  display: none;
}

/* Safe area utilities */
.safe-area-inset-bottom-calc {
  bottom: calc(110px + env(safe-area-inset-bottom, 0px));
}

@media (min-width: 768px) {
  .safe-area-inset-bottom-calc {
    bottom: calc(200px + env(safe-area-inset-bottom, 0px));
  }
}

@media (min-width: 1024px) {
  .safe-area-inset-bottom-calc {
    bottom: calc(180px + env(safe-area-inset-bottom, 0px));
  }
}

@media (min-width: 1280px) {
  .safe-area-inset-bottom-calc {
    bottom: calc(170px + env(safe-area-inset-bottom, 0px));
  }
}

.safe-area-inset-calc {
  bottom: calc(110px + env(safe-area-inset-bottom, 0px));
  height: calc(580px - env(safe-area-inset-bottom, 0px));
  max-height: calc(100vh - 130px - env(safe-area-inset-bottom, 0px));
}

@media (min-width: 768px) {
  .safe-area-inset-calc {
    bottom: calc(210px + env(safe-area-inset-bottom, 0px));
    height: calc(580px - env(safe-area-inset-bottom, 0px));
    max-height: calc(100vh - 215px - env(safe-area-inset-bottom, 0px));
  }
}

@media (min-width: 1024px) {
  .safe-area-inset-calc {
    bottom: calc(190px + env(safe-area-inset-bottom, 0px));
    height: calc(500px - env(safe-area-inset-bottom, 0px));
    max-height: calc(100vh - 210px - env(safe-area-inset-bottom, 0px));
  }
}

@media (min-width: 1280px) {
  .safe-area-inset-calc {
    bottom: calc(180px + env(safe-area-inset-bottom, 0px));
    height: calc(450px - env(safe-area-inset-bottom, 0px));
    max-height: calc(100vh - 200px - env(safe-area-inset-bottom, 0px));
  }
}

/* Height utilities */
.h-13 {
  height: 3.25rem;
}

.h-21 {
  height: 5.25rem;
}

/* Touch optimizations */
@media (pointer: coarse) {
  button {
    min-height: 44px;
    min-width: 44px;
  }
}

/* Responsive adaptations for different screen heights */
@media (max-height: 667px) {
  .safe-area-inset-bottom-calc {
    bottom: calc(100px + env(safe-area-inset-bottom, 0px));
  }
  
  .safe-area-inset-calc {
    bottom: calc(110px + env(safe-area-inset-bottom, 0px));
    height: calc(500px - env(safe-area-inset-bottom, 0px));
  }
}

@media (max-height: 568px) {
  .safe-area-inset-bottom-calc {
    bottom: calc(95px + env(safe-area-inset-bottom, 0px));
  }
  
  .safe-area-inset-calc {
    bottom: calc(105px + env(safe-area-inset-bottom, 0px));
    height: calc(450px - env(safe-area-inset-bottom, 0px));
  }
}

@media (orientation: landscape) and (max-height: 500px) {
  .safe-area-inset-bottom-calc {
    bottom: calc(85px + env(safe-area-inset-bottom, 0px));
  }
  
  .safe-area-inset-calc {
    bottom: calc(95px + env(safe-area-inset-bottom, 0px));
    height: calc(350px - env(safe-area-inset-bottom, 0px));
  }
}

/* Fine-tune small screens */
@media (max-width: 375px) {
  .safe-area-inset-bottom-calc {
    bottom: calc(105px + env(safe-area-inset-bottom, 0px));
    left: 7.5rem;
  }
  
  .safe-area-inset-calc {
    left: 1rem;
    right: 1rem;
    bottom: calc(115px + env(safe-area-inset-bottom, 0px));
    height: calc(560px - env(safe-area-inset-bottom, 0px));
    max-height: calc(100vh - 120px - env(safe-area-inset-bottom, 0px));
  }
}

/* Fade in animation for overlay */
.fixed.inset-0.z-50 {
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
