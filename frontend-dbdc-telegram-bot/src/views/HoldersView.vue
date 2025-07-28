<template>
  <div class="w-full min-h-screen bg-gray-100 font-montserrat overflow-y-auto overflow-x-hidden">
    <!-- Content Container -->
    <div class="w-full min-h-screen bg-gray-100 relative px-4 pt-5 pb-32 sm:pb-36 md:pb-40 lg:pb-44">
      
      <!-- Referral Program Header -->
      <div class="flex flex-col items-start gap-1 mb-5">
        <h1 class="text-dbd-dark text-xl font-bold leading-6 m-0">Referral Program</h1>
        <p class="text-dbd-gray text-base font-medium leading-6 m-0">Share the QR-code with your friends.</p>
      </div>

      <!-- QR Code Section -->
      <div class="relative w-full h-96 mb-5">
        <!-- Background with gradient -->
        <div class="absolute inset-0 rounded-3xl bg-gradient-to-r from-blue-900 via-indigo-900 to-blue-800 backdrop-blur-lg overflow-hidden">
          <!-- Decorative F Icons behind QR code -->
          <!-- F_Icon 1 - Top left -->
          <svg class="absolute w-16 h-16 sm:w-20 sm:h-20 md:w-24 md:h-24 opacity-10 transform rotate-[46.8deg] -left-2 -top-1 sm:-left-4 sm:-top-1.5" viewBox="0 0 120 131" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g opacity="0.1">
              <g clip-path="url(#clip0_f_icon_1)">
                <path d="M107.496 65.3312L67.7265 22.9094C65.9756 21.0418 63.3909 20.9584 61.5233 22.7093L51.9517 31.6826C50.0177 33.4957 46.9801 33.3977 45.167 31.4637L37.4276 23.2082C37.2722 23.0425 37.1069 22.8853 36.9223 22.7529C34.9485 21.338 32.509 21.3362 30.7243 23.0093C28.8567 24.7602 28.7733 27.3448 30.5242 29.2125L38.497 37.7168C40.3101 39.6508 40.2121 42.6884 38.2781 44.5015L11.8979 69.2327C10.0303 70.9836 9.94687 73.5682 11.6978 75.4359C13.4486 77.3035 16.0333 77.3869 17.9009 75.636L28.2729 65.9123C30.2069 64.0992 33.2445 64.1973 35.0576 66.1312L44.5311 76.2364C46.282 78.104 48.8666 78.1874 50.7342 76.4365C52.6019 74.6857 52.6853 72.101 50.9344 70.2334L41.4609 60.1282C39.6478 58.1942 39.7458 55.1566 41.6797 53.3435L44.5479 50.6547C46.4819 48.8416 49.5195 48.9396 51.3326 50.8736L72.3119 73.2517C74.0628 75.1193 76.6474 75.2027 78.515 73.4518C80.3827 71.7009 80.466 69.1163 78.7152 67.2487L57.7359 44.8705C55.9228 42.9366 56.0208 39.8989 57.9548 38.0858L60.8229 35.397C62.7569 33.5839 65.7945 33.6819 67.6076 35.6159L100.843 71.0674C102.594 72.935 105.179 73.0184 107.046 71.2675C108.914 69.5166 109.247 67.1988 107.496 65.3312Z" fill="#FAFAFA"/>
              </g>
            </g>
            <defs>
              <clipPath id="clip0_f_icon_1">
                <rect x="54.1885" y="-5.56738" width="96" height="96" rx="4.8" transform="rotate(46.8479 54.1885 -5.56738)" fill="white"/>
              </clipPath>
            </defs>
          </svg>

          <!-- F_Icon 5 - Top right -->
          <svg class="absolute w-16 h-16 sm:w-20 sm:h-20 md:w-24 md:h-24 opacity-10 transform rotate-[121.978deg] right-16 sm:right-12 md:right-14 top-5 sm:top-3 md:top-5" viewBox="0 0 133 134" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g opacity="0.1">
              <g clip-path="url(#clip0_f_icon_5)">
                <path d="M80.6837 123.072L111.479 73.7471C112.834 71.5756 112.252 69.0561 110.08 67.7003L98.9511 60.7521C96.7024 59.3482 96.0176 56.3872 97.4215 54.1385L103.414 44.5396C103.535 44.3469 103.644 44.1467 103.725 43.9344C104.586 41.6636 103.961 39.3054 101.886 38.0098C99.7148 36.6541 97.1954 37.2368 95.8396 39.4083L89.6661 49.2965C88.2622 51.5452 85.3011 52.23 83.0524 50.8261L52.3796 31.6761C50.2081 30.3203 47.6886 30.903 46.3328 33.0746C44.9771 35.2461 45.5598 37.7656 47.7313 39.1213L59.791 46.6506C62.0397 48.0545 62.7245 51.0155 61.3206 53.2642L53.985 65.0138C52.6293 67.1853 53.212 69.7048 55.3835 71.0605C57.555 72.4163 60.0745 71.8336 61.4303 69.662L68.7659 57.9125C70.1698 55.6638 73.1308 54.979 75.3795 56.3829L78.7144 58.465C80.9631 59.8689 81.6479 62.83 80.2439 65.0786L63.9991 91.0982C62.6434 93.2697 63.2261 95.7892 65.3976 97.145C67.5691 98.5007 70.0886 97.918 71.4444 95.7465L87.6892 69.7269C89.0931 67.4783 92.0541 66.7934 94.3028 68.1974L97.6377 70.2794C99.8864 71.6833 100.571 74.6444 99.1673 76.8931L73.4322 118.113C72.0764 120.285 72.6591 122.804 74.8307 124.16C77.0022 125.516 79.328 125.243 80.6837 123.072Z" fill="#1E5DFF"/>
              </g>
            </g>
            <defs>
              <clipPath id="clip0_f_icon_5">
                <rect x="132.813" y="51.6599" width="96" height="96" rx="4.8" transform="rotate(121.978 132.813 51.6599)" fill="white"/>
              </clipPath>
            </defs>
          </svg>

          <!-- F_Icon 2 - Bottom left -->
          <svg class="absolute w-20 h-24 sm:w-24 sm:h-28 md:w-32 md:h-36 opacity-10 transform rotate-[-31.597deg] -left-5 sm:-left-6 md:-left-7 bottom-44 sm:bottom-48 md:bottom-44" viewBox="0 0 155 177" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g opacity="0.1">
              <g clip-path="url(#clip0_f_icon_2)">
                <path d="M85.163 16.9519L19.125 57.5734C16.2177 59.3618 15.4184 62.7159 17.2068 65.6232L26.3722 80.5233C28.2241 83.5339 27.2848 87.4758 24.2742 89.3277L11.4228 97.2329C11.1649 97.3916 10.9153 97.5656 10.6932 97.7714C8.31768 99.9719 7.66372 103.158 9.37267 105.936C11.161 108.844 14.5151 109.643 17.4224 107.855L30.6612 99.7111C33.6718 97.8591 37.6137 98.7985 39.4656 101.809L64.7264 142.875C66.5147 145.782 69.8688 146.582 72.7761 144.793C75.6835 143.005 76.4827 139.651 74.6944 136.744L64.7625 120.598C62.9106 117.587 63.8499 113.645 66.8606 111.793L82.5913 102.117C85.4986 100.328 86.2979 96.9743 84.5095 94.067C82.7212 91.1596 79.3671 90.3604 76.4598 92.1487L60.729 101.825C57.7184 103.677 53.7765 102.738 51.9246 99.7271L49.1781 95.2622C47.3262 92.2516 48.2656 88.3097 51.2762 86.4578L86.1123 65.0293C89.0196 63.2409 89.8189 59.8868 88.0305 56.9795C86.2421 54.0721 82.888 53.2729 79.9807 55.0613L45.1446 76.4898C42.134 78.3417 38.1921 77.4024 36.3402 74.3917L33.5938 69.9269C31.7419 66.9163 32.6812 62.9744 35.6918 61.1225L90.8792 27.1753C93.7865 25.387 94.5858 22.0329 92.7974 19.1256C91.009 16.2182 88.0703 15.1635 85.163 16.9519Z" fill="#FAFAFA"/>
              </g>
            </g>
            <defs>
              <clipPath id="clip0_f_icon_2">
                <rect x="-21.6904" y="67.6526" width="128" height="128" rx="6.4" transform="rotate(-31.5967 -21.6904 67.6526)" fill="white"/>
              </clipPath>
            </defs>
          </svg>

          <!-- F_Icon 3 - Right side -->
          <svg class="absolute w-10 h-10 sm:w-12 sm:h-12 md:w-16 md:h-16 opacity-10 transform rotate-[150.638deg] right-16 sm:right-20 md:right-20 top-44 sm:top-48 md:top-44" viewBox="0 0 66 66" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g opacity="0.1">
              <g clip-path="url(#clip0_f_icon_3)">
                <path d="M25.6898 61.2584L51.0293 47.0026C52.1448 46.375 52.4934 45.1299 51.8658 44.0143L48.6493 38.297C47.9993 37.1418 48.409 35.6784 49.5642 35.0285L54.4954 32.2543C54.5944 32.1986 54.6904 32.137 54.7767 32.0632C55.699 31.2733 55.9906 30.089 55.3909 29.023C54.7633 27.9074 53.5181 27.5588 52.4026 28.1865L47.3227 31.0443C46.1675 31.6943 44.7042 31.2846 44.0542 30.1294L35.1892 14.3719C34.5616 13.2564 33.3165 12.9078 32.2009 13.5354C31.0853 14.1631 30.7368 15.4082 31.3644 16.5238L34.8499 22.7192C35.4998 23.8744 35.0902 25.3377 33.935 25.9876L27.8989 29.3835C26.7833 30.0111 26.4348 31.2562 27.0624 32.3718C27.69 33.4874 28.9352 33.8359 30.0507 33.2083L36.0868 29.8125C37.242 29.1626 38.7053 29.5722 39.3552 30.7274L40.3191 32.4406C40.969 33.5958 40.5594 35.0592 39.4042 35.7091L26.0372 43.2292C24.9216 43.8568 24.5731 45.102 25.2007 46.2175C25.8283 47.3331 27.0734 47.6816 28.189 47.054L41.556 39.5339C42.7112 38.884 44.1745 39.2936 44.8244 40.4488L45.7883 42.162C46.4382 43.3172 46.0286 44.7806 44.8733 45.4305L23.6974 57.3439C22.5818 57.9715 22.2333 59.2167 22.8609 60.3322C23.4885 61.4478 24.5743 61.886 25.6898 61.2584Z" fill="#1E5DFF"/>
              </g>
            </g>
            <defs>
              <clipPath id="clip0_f_icon_3">
                <rect x="65.6865" y="42.4282" width="48" height="48" rx="2.4" transform="rotate(150.638 65.6865 42.4282)" fill="white"/>
              </clipPath>
            </defs>
          </svg>


      <svg class="absolute right-4 top-20 w-20 h-20 opacity-25 -rotate-12" viewBox="0 0 120 131" fill="none" xmlns="http://www.w3.org/2000/svg">
        <use href="#clip0" />
      </svg>

      <svg class="absolute left-10 bottom-10 w-28 h-28 opacity-15 rotate-45" viewBox="0 0 120 131" fill="none" xmlns="http://www.w3.org/2000/svg">
        <use href="#clip0" />
      </svg>

      <svg class="absolute right-2 bottom-4 w-24 h-24 opacity-15 rotate-[-30deg]" viewBox="0 0 120 131" fill="none" xmlns="http://www.w3.org/2000/svg">
        <use href="#clip0" />
      </svg>

          <svg class="absolute right-20 top-44 w-16 h-16 opacity-10 transform rotate-150" viewBox="0 0 66 66" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g opacity="0.1">
              <g clip-path="url(#clip0_2_20038)">
                <path d="M25.6898 61.2584L51.0293 47.0026C52.1448 46.375 52.4934 45.1299 51.8658 44.0143L48.6493 38.297C47.9993 37.1418 48.409 35.6784 49.5642 35.0285L54.4954 32.2543C54.5944 32.1986 54.6904 32.137 54.7767 32.0632C55.699 31.2733 55.9906 30.089 55.3909 29.023C54.7633 27.9074 53.5181 27.5588 52.4026 28.1865L47.3227 31.0443C46.1675 31.6943 44.7042 31.2846 44.0542 30.1294L35.1892 14.3719C34.5616 13.2564 33.3165 12.9078 32.2009 13.5354C31.0853 14.1631 30.7368 15.4082 31.3644 16.5238L34.8499 22.7192C35.4998 23.8744 35.0902 25.3377 33.935 25.9876L27.8989 29.3835C26.7833 30.0111 26.4348 31.2562 27.0624 32.3718C27.69 33.4874 28.9352 33.8359 30.0507 33.2083L36.0868 29.8125C37.242 29.1626 38.7053 29.5722 39.3552 30.7274L40.3191 32.4406C40.969 33.5958 40.5594 35.0592 39.4042 35.7091L26.0372 43.2292C24.9216 43.8568 24.5731 45.102 25.2007 46.2175C25.8283 47.3331 27.0734 47.6816 28.189 47.054L41.556 39.5339C42.7112 38.884 44.1745 39.2936 44.8244 40.4488L45.7883 42.162C46.4382 43.3172 46.0286 44.7806 44.8733 45.4305L23.6974 57.3439C22.5818 57.9715 22.2333 59.2167 22.8609 60.3322C23.4885 61.4478 24.5743 61.886 25.6898 61.2584Z" fill="#1E5DFF"/>
              </g>
            </g>
            <defs>
              <clipPath id="clip0_2_20038">
                <rect x="65.6865" y="42.4282" width="48" height="48" rx="2.4" transform="rotate(150.638 65.6865 42.4282)" fill="white"/>
              </clipPath>
            </defs>
          </svg>

          <svg class="absolute -left-7 top-44 w-36 h-44 opacity-10 transform -rotate-12" viewBox="0 0 155 177" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g opacity="0.1">
              <g clip-path="url(#clip0_2_20040)">
                <path d="M85.163 16.9519L19.125 57.5734C16.2177 59.3618 15.4184 62.7159 17.2068 65.6232L26.3722 80.5233C28.2241 83.5339 27.2848 87.4758 24.2742 89.3277L11.4228 97.2329C11.1649 97.3916 10.9153 97.5656 10.6932 97.7714C8.31768 99.9719 7.66372 103.158 9.37267 105.936C11.161 108.844 14.5151 109.643 17.4224 107.855L30.6612 99.7111C33.6718 97.8591 37.6137 98.7985 39.4656 101.809L64.7264 142.875C66.5147 145.782 69.8688 146.582 72.7761 144.793C75.6835 143.005 76.4827 139.651 74.6944 136.744L64.7625 120.598C62.9106 117.587 63.8499 113.645 66.8606 111.793L82.5913 102.117C85.4986 100.328 86.2979 96.9743 84.5095 94.067C82.7212 91.1596 79.3671 90.3604 76.4598 92.1487L60.729 101.825C57.7184 103.677 53.7765 102.738 51.9246 99.7271L49.1781 95.2622C47.3262 92.2516 48.2656 88.3097 51.2762 86.4578L86.1123 65.0293C89.0196 63.2409 89.8189 59.8868 88.0305 56.9795C86.2421 54.0721 82.888 53.2729 79.9807 55.0613L45.1446 76.4898C42.134 78.3417 38.1921 77.4024 36.3402 74.3917L33.5938 69.9269C31.7419 66.9163 32.6812 62.9744 35.6918 61.1225L90.8792 27.1753C93.7865 25.387 94.5858 22.0329 92.7974 19.1256C91.009 16.2182 88.0703 15.1635 85.163 16.9519Z" fill="#FAFAFA"/>
              </g>
            </g>
            <defs>
              <clipPath id="clip0_2_20040">
                <rect x="-21.6904" y="67.6526" width="128" height="128" rx="6.4" transform="rotate(-31.5967 -21.6904 67.6526)" fill="white"/>
              </clipPath>
            </defs>
          </svg>

          <svg class="absolute right-12 top-4 w-32 h-32 opacity-10 transform rotate-120" viewBox="0 0 133 134" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g opacity="0.1">
              <g clip-path="url(#clip0_2_20042)">
                <path d="M80.6837 123.072L111.479 73.7471C112.834 71.5756 112.252 69.0561 110.08 67.7003L98.9511 60.7521C96.7024 59.3482 96.0176 56.3872 97.4215 54.1385L103.414 44.5396C103.535 44.3469 103.644 44.1467 103.725 43.9344C104.586 41.6636 103.961 39.3054 101.886 38.0098C99.7148 36.6541 97.1954 37.2368 95.8396 39.4083L89.6661 49.2965C88.2622 51.5452 85.3011 52.23 83.0524 50.8261L52.3796 31.6761C50.2081 30.3203 47.6886 30.903 46.3328 33.0746C44.9771 35.2461 45.5598 37.7656 47.7313 39.1213L59.791 46.6506C62.0397 48.0545 62.7245 51.0155 61.3206 53.2642L53.985 65.0138C52.6293 67.1853 53.212 69.7048 55.3835 71.0605C57.555 72.4163 60.0745 71.8336 61.4303 69.662L68.7659 57.9125C70.1698 55.6638 73.1308 54.979 75.3795 56.3829L78.7144 58.465C80.9631 59.8689 81.6479 62.83 80.2439 65.0786L63.9991 91.0982C62.6434 93.2697 63.2261 95.7892 65.3976 97.145C67.5691 98.5007 70.0886 97.918 71.4444 95.7465L87.6892 69.7269C89.0931 67.4783 92.0541 66.7934 94.3028 68.1974L97.6377 70.2794C99.8864 71.6833 100.571 74.6444 99.1673 76.8931L73.4322 118.113C72.0764 120.285 72.6591 122.804 74.8307 124.16C77.0022 125.516 79.328 125.243 80.6837 123.072Z" fill="#1E5DFF"/>
              </g>
            </g>
            <defs>
              <clipPath id="clip0_2_20042">
                <rect x="132.813" y="51.6599" width="96" height="96" rx="4.8" transform="rotate(121.978 132.813 51.6599)" fill="white"/>
              </clipPath>
            </defs>
          </svg>
        </div>

        <!-- QR Code Container -->
        <div class="absolute left-1/2 top-6 transform -translate-x-1/2 w-56 h-56 z-10">
          <div class="w-full h-full rounded-2xl border border-gray-200 bg-dbd-off-white shadow-lg relative">
            <!-- QR Code Image -->
            <img 
              src="https://api.builder.io/api/v1/image/assets/TEMP/d0e1d46df412099f6abe582c7574e9c4a57f8399?width=280" 
              alt="QR Code" 
              class="absolute left-1/2 top-5 transform -translate-x-1/2 w-36 h-36 aspect-square object-contain"
            />
            <!-- QR Code Link -->
            <div class="absolute left-1/2 bottom-5 transform -translate-x-1/2 text-dbd-primary text-lg font-semibold leading-6 text-center">
              vm.dubadu/jjhI1uT4S
            </div>
          </div>
        </div>

        <!-- Terms and Conditions -->
        <div class="absolute left-1/2 bottom-16 transform -translate-x-1/2 z-20">
          <TermsCheckbox
            v-model="termsAccepted"
            @open-terms="openTerms"
          />
        </div>

        <!-- Share Button -->
        <div class="absolute left-0 right-0 bottom-2 px-4 z-20">
          <button
            class="w-full max-w-xs sm:max-w-sm md:max-w-md lg:max-w-lg xl:max-w-xl mx-auto
                  flex justify-center items-center
                  px-5 sm:px-6 py-2.5 sm:py-3
                  rounded-full
                  bg-gradient-to-r from-dbd-primary to-blue-500
                  text-white font-semibold text-sm sm:text-base leading-6
                  transition-all duration-200 ease-in-out
                  hover:-translate-y-0.5 hover:shadow-lg
                  disabled:bg-gray-300 disabled:text-white disabled:cursor-not-allowed h-11 sm:h-12"
            :class="{
              '!bg-gray-300 !cursor-not-allowed': !termsAccepted,
              '!bg-gradient-to-r !from-blue-700 !to-indigo-700 !cursor-wait': isSharing
            }"
            :disabled="!termsAccepted || isSharing"
            @click="shareQRCode"
          >
            <span v-if="!isSharing">Share QR code</span>
            <span v-else class="flex items-center gap-2">
              <svg class="animate-spin h-4 w-4" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10"
                        stroke="currentColor" stroke-width="4" fill="none" />
                <path class="opacity-75" fill="currentColor"
                      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
              </svg>
              Sharing...
            </span>
          </button>
        </div>
      </div>

      <!-- How to use the Link Section -->
      <div class="relative w-full mt-12">
        <!-- Header -->
        <div class="flex flex-col items-start gap-3 mb-8">
          <h2 class="text-dbd-dark text-xl font-bold leading-6 m-0">How to use the Link</h2>
          <p class="text-dbd-gray text-base font-medium leading-6 m-0">Follow these 3 simple steps</p>
        </div>

      <!-- Unified Step Section -->
      <div class="w-full max-w-2xl mx-auto px-4 mb-12">
        <!-- Step Indicators -->
        <div class="grid grid-cols-5 gap-0 items-center text-center mb-4">
          <!-- D1 -->
          <div class="flex justify-center">
            <div class="w-8 h-8 sm:w-10 sm:h-10 md:w-12 md:h-12 bg-dbd-primary rounded-r-full"></div>
          </div>

          <!-- Line between D1 and D2 -->
          <div class="flex justify-center">
            <div class="w-full max-w-[60px] h-px bg-dbd-light-gray"></div>
          </div>

          <!-- D2 -->
          <div class="flex justify-center">
            <div class="w-8 h-8 sm:w-10 sm:h-10 md:w-12 md:h-12 bg-dbd-primary rounded-r-full"></div>
          </div>

          <!-- Line between D2 and D3 -->
          <div class="flex justify-center">
            <div class="w-full max-w-[60px] h-px bg-dbd-light-gray"></div>
          </div>

          <!-- D3 -->
          <div class="flex justify-center">
            <div class="w-8 h-8 sm:w-10 sm:h-10 md:w-12 md:h-12 bg-dbd-primary rounded-r-full"></div>
          </div>
        </div>

        <!-- Step Descriptions -->
        <div class="grid grid-cols-5 gap-0 text-center">
          <!-- Description under D1 -->
          <div class="flex flex-col items-center gap-1">
            <div class="flex items-center gap-1.5 justify-center">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                <path d="M18 16.08C17.24 16.08 16.56 16.38 16.04 16.85L8.91 12.7C8.96 12.47 9 12.24 9 12C9 11.76 8.96 11.53 8.91 11.3L15.96 7.19C16.5 7.69 17.21 8 18 8C19.66 8 21 6.66 21 5C21 3.34 19.66 2 18 2C16.34 2 15 3.34 15 5C15 5.24 15.04 5.47 15.09 5.7L8.04 9.81C7.5 9.31 6.79 9 6 9C4.34 9 3 10.34 3 12C3 13.66 4.34 15 6 15C6.79 15 7.5 14.69 8.04 14.19L15.16 18.34C15.11 18.55 15.08 18.77 15.08 19C15.08 20.61 16.39 21.92 18 21.92C19.61 21.92 20.92 20.61 20.92 19C20.92 17.39 19.61 16.08 18 16.08Z" fill="#7E7E7E"/>
              </svg>
              <span class="text-dbd-gray text-base font-medium leading-6">1</span>
            </div>
            <span class="text-dbd-gray text-xs font-medium leading-4">Share your link</span>
          </div>

          <!-- Empty under Line 1 -->
          <div></div>

          <!-- Description under D2 -->
          <div class="flex flex-col items-center gap-1">
            <div class="flex items-center gap-1.5 justify-center">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
                <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM17 13H11V7H13V11H17V13Z" fill="#7E7E7E"/>
              </svg>
              <span class="text-dbd-gray text-sm font-medium leading-6">2</span>
            </div>
            <span class="text-dbd-gray text-xs font-medium leading-4">Wait for joining</span>
          </div>

          <!-- Empty under Line 2 -->
          <div></div>

          <!-- Description under D3 -->
          <div class="flex flex-col items-center gap-1">
            <div class="flex items-center gap-1.5 justify-center">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
                <path d="M12 2L15.09 8.26L22 9L17 13.74L18.18 20.74L12 17.77L5.82 20.74L7 13.74L2 9L8.91 8.26L12 2Z" fill="#7E7E7E"/>
              </svg>
              <span class="text-dbd-gray text-sm font-medium leading-6">3</span>
            </div>
            <span class="text-dbd-gray text-xs font-medium leading-4">Get rewards</span>
          </div>
        </div>
      </div>

        <!-- Web Referral Link Section -->
        <div class="relative w-full h-52">
          <!-- Background -->
          <div class="absolute inset-0 rounded-3xl bg-gradient-to-r from-blue-900 via-indigo-900 to-blue-800 backdrop-blur-lg"></div>
          
          <!-- Content -->
          <div class="relative z-10 p-5">
            <div class="mb-7">
              <h3 class="text-white text-2xl font-bold leading-7 m-0 mb-3">Web Referral Link</h3>
              <p class="text-white text-base font-medium leading-6 m-0">Copy the link bellow and share with your friends.</p>
            </div>
            
            <!-- Copy Link Container -->
            <div class="relative w-full max-w-sm h-13 sm:h-14 md:h-16 rounded-full border border-blue-600 border-opacity-60 bg-white bg-opacity-10 flex items-center transition-all duration-400 ease-out overflow-hidden"
                :class="{ 'border-green-500 bg-green-700 transform scale-105': linkCopied }">

              <!-- URL text -->
              <div v-if="!linkCopied" class="flex-1 px-4 sm:px-6 py-3.5 overflow-hidden">
                <span class="text-dbd-off-white text-xs sm:text-sm font-semibold leading-5 underline truncate block max-w-full">
                  vm.dubadu/jjhI1uT4S
                </span>
              </div>

              <!-- Copied State -->
              <div v-if="linkCopied" class="w-full h-full flex items-center justify-center gap-3 px-6 py-3.5 animate-pulse">
                <span class="text-white text-sm font-semibold leading-5 text-center">Copied</span>
                <div class="relative w-7 h-7 flex items-center justify-center">
                  <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="14" cy="14" r="14" fill="white"/>
                  </svg>
                  <svg class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M11.3242 0.926106C10.7978 0.642629 10.2106 1.18934 9.86633 1.51331C9.07667 2.28275 8.40848 3.17368 7.65925 3.98362C6.82907 4.87455 6.05963 5.76548 5.20919 6.6362C4.72323 7.12216 4.19677 7.64862 3.8728 8.25607C3.14385 7.54734 2.51615 6.7779 1.70621 6.15023C1.11901 5.70477 0.147086 5.38079 0.167334 6.45396C0.207831 7.85113 1.44299 9.34952 2.35416 10.3012C2.73888 10.7061 3.24509 11.1313 3.8323 11.1516C4.54099 11.1921 5.26994 10.3417 5.69515 9.87594C6.44438 9.06601 7.05183 8.15479 7.74024 7.32464C8.63118 6.23123 9.54236 5.15803 10.413 4.04436C10.9597 3.35592 12.6809 1.65502 11.3242 0.926106ZM1.05823 6.37297C1.03798 6.37297 1.01773 6.37297 0.977238 6.39318C0.896244 6.37297 0.835499 6.35268 0.754505 6.31219C0.815251 6.27169 0.916493 6.29194 1.05823 6.37297Z" fill="#07B80E"/>
                  </svg>
                </div>
              </div>

              <!-- Copy Button -->
              <button
                v-if="!linkCopied"
                class="absolute right-0 top-0 bottom-0 flex items-center justify-center px-4 sm:px-5 md:px-6 bg-dbd-off-white border-l border-indigo-700 rounded-r-full cursor-pointer transition-all duration-300 ease-out hover:bg-blue-50 hover:-translate-y-0.5 hover:scale-105 active:translate-y-0 active:scale-95"
                @click="copyWebLink"
              >
                <svg class="w-5 h-5 sm:w-6 sm:h-6 md:w-7 md:h-7 text-indigo-700" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M18.0655 0.5H7.60611C6.97596 0.5 6.37161 0.727045 5.92603 1.13119C5.48044 1.53533 5.23011 2.08346 5.23011 2.65501V3.48385H4.04211C3.38111 3.48385 2.74718 3.72201 2.27978 4.14594C1.81239 4.56986 1.5498 5.14483 1.5498 5.74435V19.2395C1.5498 19.839 1.81239 20.414 2.27978 20.8379C2.74718 21.2618 3.38111 21.5 4.04211 21.5H14.2772C14.9382 21.5 15.5721 21.2618 16.0395 20.8379C16.5069 20.414 16.7695 19.839 16.7695 19.2395V18.486H18.0655C18.6907 18.4861 19.291 18.2634 19.7369 17.866C20.1829 17.4685 20.4389 16.9281 20.4498 16.3611V2.65501C20.4476 2.08277 20.1954 1.53465 19.7485 1.13073C19.3016 0.7268 18.6964 0.499997 18.0655 0.5ZM15.108 19.2395C15.108 19.4393 15.0204 19.631 14.8646 19.7723C14.7088 19.9136 14.4975 19.993 14.2772 19.993H4.04211C3.82178 19.993 3.61047 19.9136 3.45467 19.7723C3.29887 19.631 3.21134 19.4393 3.21134 19.2395V5.74435C3.21134 5.54451 3.29887 5.35285 3.45467 5.21154C3.61047 5.07024 3.82178 4.99085 4.04211 4.99085H14.2772C14.4975 4.99085 14.7088 5.07024 14.8646 5.21154C15.0204 5.35285 15.108 5.54451 15.108 5.74435V19.2395ZM18.7883 16.3611C18.7861 16.5337 18.709 16.6985 18.5737 16.8198C18.4383 16.9411 18.2558 17.0092 18.0655 17.0092H16.7695V5.74435C16.7695 5.14483 16.5069 4.56986 16.0395 4.14594C15.5721 3.72201 14.9382 3.48385 14.2772 3.48385H6.89165V2.65501C6.89165 2.48314 6.96693 2.31832 7.10091 2.19679C7.2349 2.07527 7.41663 2.007 7.60611 2.007H18.0655C18.16 2.006 18.2538 2.02203 18.3415 2.05414C18.4291 2.08626 18.5089 2.13384 18.5761 2.19411C18.6433 2.25438 18.6967 2.32616 18.7331 2.40527C18.7695 2.48439 18.7883 2.56927 18.7883 2.65501V16.3611Z" fill="#2019CE"/>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Navigation Component -->
    <BottomNavigation />

    <!-- Terms and Conditions Modal -->
    <TermsAndConditionsModal
      :isVisible="showTermsModal"
      @close="closeTermsModal"
      @agree="agreeToTerms"
    />

    <!-- Success Notification -->
    <SuccessNotification
      :is-visible="showSuccessNotification"
      :class="{ 'blur-notification': isAnyModalOpen }"
      :message="successMessage"
      @close="hideSuccessNotification"
    />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import BottomNavigation from '../components/BottomNavigation.vue'
import TermsAndConditionsModal from '../components/TermsAndConditionsModal.vue'
import SuccessNotification from '../components/SuccessNotification.vue'
import TermsCheckbox from '../components/TermsCheckbox.vue'

// Reactive data
const termsAccepted = ref(false)
const linkCopied = ref(false)
const referralLink = ref('vm.dubadu/jjhI1uT4S')
const showTermsModal = ref(false)

// Check if any modal is open for blur effect
const isAnyModalOpen = computed(() => {
  return showTermsModal.value
})

// Success notification
const showSuccessNotification = ref(false)
const successMessage = ref('')
const isSharing = ref(false)
let successTimeout = null

// Methods
const shareQRCode = () => {
  if (!termsAccepted.value || isSharing.value) return

  console.log('Sharing QR code...')
  isSharing.value = true

  // Safety timeout to prevent spinner from getting stuck
  const safetyTimeout = setTimeout(() => {
    if (isSharing.value) {
      console.log('Safety timeout triggered - stopping spinner')
      isSharing.value = false
    }
  }, 15000) // 15 seconds safety timeout

  // Add haptic feedback
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'light')
  }

  // Try standard Web Share API first (works on most platforms including Telegram, Viber, etc.)
  if (navigator.share) {
    navigator.share({
      title: 'DBD Capital Forevers Bot',
      text: 'Join me on DBD Capital Forevers Bot! 🚀',
      url: referralLink.value
    }).then(() => {
      // Sharing was successful
      clearTimeout(safetyTimeout)
      isSharing.value = false
      showSuccessMessage('Referral QR-code sent successfully')
    }).catch((error) => {
      console.log('Web Share API failed or cancelled:', error)
      clearTimeout(safetyTimeout)
      isSharing.value = false

      // If user didn't cancel (AbortError), try Telegram-specific sharing
      if (error.name !== 'AbortError') {
        telegramFallback(safetyTimeout)
      }
    })
  } else {
    // Web Share API not available, try Telegram-specific sharing
    telegramFallback(safetyTimeout)
  }
}

const telegramFallback = (safetyTimeout = null) => {
  // Use Telegram WebApp sharing if available
  if (window.Telegram && window.Telegram.WebApp) {
    const tg = window.Telegram.WebApp

    try {
      // Use Telegram's openTelegramLink for sharing (compatible with version 6.0)
      const shareUrl = `https://t.me/share/url?url=${encodeURIComponent(referralLink.value)}&text=${encodeURIComponent('Join me on DBD Capital Forevers Bot! 🚀')}`
      tg.openTelegramLink(shareUrl)

      // Set up event listener for when user returns to app
      const handleVisibilityChange = () => {
        if (!document.hidden) {
          // User returned to the app, likely after sharing
          if (safetyTimeout) clearTimeout(safetyTimeout)
          isSharing.value = false
          setTimeout(() => {
            showSuccessMessage('Referral QR-code sent successfully')
          }, 500)
          document.removeEventListener('visibilitychange', handleVisibilityChange)
        }
      }

      document.addEventListener('visibilitychange', handleVisibilityChange)

      // Cleanup listener after 30 seconds if user doesn't return
      setTimeout(() => {
        document.removeEventListener('visibilitychange', handleVisibilityChange)
        if (safetyTimeout) clearTimeout(safetyTimeout)
        isSharing.value = false
      }, 30000)

    } catch (error) {
      console.error('Telegram share failed:', error)
      if (safetyTimeout) clearTimeout(safetyTimeout)
      isSharing.value = false
      // Final fallback to clipboard
      copyLink()
    }
  } else {
    // Not in Telegram environment, copy to clipboard
    if (safetyTimeout) clearTimeout(safetyTimeout)
    isSharing.value = false
    copyLink()
  }
}

const fallbackShare = () => {
  // This function is no longer used, but keeping for backwards compatibility
  telegramFallback()
}

const copyLink = async () => {
  let copySuccess = false

  // Try modern clipboard API first
  if (navigator.clipboard) {
    try {
      await navigator.clipboard.writeText(referralLink.value)
      copySuccess = true
    } catch (clipboardErr) {
      console.log('Clipboard API failed, trying fallback method')
    }
  }

  // If clipboard API failed or is not available, use fallback
  if (!copySuccess) {
    try {
      const textArea = document.createElement('textarea')
      textArea.value = referralLink.value
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

  // Show success notification when called from share button
  showSuccessMessage('Link copied to clipboard')

  // Also show copied state for user feedback
  linkCopied.value = true
  setTimeout(() => {
    linkCopied.value = false
  }, 2000)
}

const copyWebLink = async () => {
  let copySuccess = false

  // Try modern clipboard API first
  if (navigator.clipboard) {
    try {
      await navigator.clipboard.writeText(referralLink.value)
      copySuccess = true
    } catch (clipboardErr) {
      console.log('Clipboard API failed, trying fallback method')
    }
  }

  // If clipboard API failed or is not available, use fallback
  if (!copySuccess) {
    try {
      const textArea = document.createElement('textarea')
      textArea.value = referralLink.value
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

  // Always show copied state for user feedback
  linkCopied.value = true
  setTimeout(() => {
    linkCopied.value = false
  }, 2500)
}

const openTerms = () => {
  showTermsModal.value = true
}

const closeTermsModal = () => {
  showTermsModal.value = false
}

const agreeToTerms = () => {
  termsAccepted.value = true
  showTermsModal.value = false
}

const showSuccessMessage = (message) => {
  successMessage.value = message
  showSuccessNotification.value = true

  // Add haptic feedback for success
  if (window.triggerHaptic) {
    window.triggerHaptic('notification', 'success')
  }

  // Clear existing timeout
  if (successTimeout) {
    clearTimeout(successTimeout)
  }

  // Auto-hide after 3 seconds
  successTimeout = setTimeout(() => {
    showSuccessNotification.value = false
  }, 3000)
}

const hideSuccessNotification = () => {
  showSuccessNotification.value = false
  if (successTimeout) {
    clearTimeout(successTimeout)
    successTimeout = null
  }
}
</script>

<style scoped>
/* Hide scrollbar for WebKit browsers (Chrome, Safari, Edge) */
::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for Firefox */
* {
  scrollbar-width: none;
}

/* Hide scrollbar for Internet Explorer and Edge Legacy */
* {
  -ms-overflow-style: none;
}

/* Ensure smooth scrolling on touch devices */
.overflow-y-auto {
  -webkit-overflow-scrolling: touch;
  overscroll-behavior: contain;
}

/* Apply hidden scrollbar to main container */
.w-full.min-h-screen.bg-gray-100.font-montserrat.overflow-y-auto.overflow-x-hidden {
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.w-full.min-h-screen.bg-gray-100.font-montserrat.overflow-y-auto.overflow-x-hidden::-webkit-scrollbar {
  display: none;
}
</style>
