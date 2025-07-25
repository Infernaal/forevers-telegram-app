<template>
  <div class="holders-view w-full min-h-screen bg-gray-100 font-montserrat">
    <!-- Main Content -->
    <div class="w-full max-w-md mx-auto bg-gray-100 min-h-screen relative overflow-x-hidden">
      <!-- Content Container -->
      <div class="bg-gray-100 rounded-t-2xl relative">
        <!-- Title Section -->
        <div class="px-4 pt-4 pb-1">
          <div class="flex flex-col gap-1">
            <h1 class="text-dbd-dark text-xl font-bold leading-6">
              Referral Program
            </h1>
            <p class="text-dbd-gray text-base font-medium leading-6">
              Share the QR-code with your friends.
            </p>
          </div>
        </div>

        <!-- Scroll Content -->
        <div class="px-4 pt-6 pb-20 space-y-5">
          <!-- QR Code Section -->
          <div class="relative w-full h-80 sm:h-96 rounded-3xl overflow-hidden"
               style="background: linear-gradient(93deg, #000482 33.15%, rgba(3, 0, 155, 0.84) 76.97%);">
            
            <!-- Background Icons -->
            <div class="absolute inset-0 overflow-hidden">
              <!-- F Icon 1 -->
              <svg class="absolute -left-4 -top-2 w-24 h-24 transform rotate-45 opacity-10"
                   width="120" height="131" viewBox="0 0 120 131" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g opacity="0.1">
                  <g clip-path="url(#clip0_2_20036)">
                    <path d="M107.496 65.3312L67.7265 22.9094C65.9756 21.0418 63.3909 20.9584 61.5233 22.7093L51.9517 31.6826C50.0177 33.4957 46.9801 33.3977 45.167 31.4637L37.4276 23.2082C37.2722 23.0425 37.1069 22.8853 36.9223 22.7529C34.9485 21.338 32.509 21.3362 30.7243 23.0093C28.8567 24.7602 28.7733 27.3448 30.5242 29.2125L38.497 37.7168C40.3101 39.6508 40.2121 42.6884 38.2781 44.5015L11.8979 69.2327C10.0303 70.9836 9.94687 73.5682 11.6978 75.4359C13.4486 77.3035 16.0333 77.3869 17.9009 75.636L28.2729 65.9123C30.2069 64.0992 33.2445 64.1973 35.0576 66.1312L44.5311 76.2364C46.282 78.104 48.8666 78.1874 50.7342 76.4365C52.6019 74.6857 52.6853 72.101 50.9344 70.2334L41.4609 60.1282C39.6478 58.1942 39.7458 55.1566 41.6797 53.3435L44.5479 50.6547C46.4819 48.8416 49.5195 48.9396 51.3326 50.8736L72.3119 73.2517C74.0628 75.1193 76.6474 75.2027 78.515 73.4518C80.3827 71.7009 80.466 69.1163 78.7152 67.2487L57.7359 44.8705C55.9228 42.9366 56.0208 39.8989 57.9548 38.0858L60.8229 35.397C62.7569 33.5839 65.7945 33.6819 67.6076 35.6159L100.843 71.0674C102.594 72.935 105.179 73.0184 107.046 71.2675C108.914 69.5166 109.247 67.1988 107.496 65.3312Z" fill="#FAFAFA"/>
                  </g>
                </g>
                <defs>
                  <clipPath id="clip0_2_20036">
                    <rect x="54.1885" y="-5.56738" width="96" height="96" rx="4.8" transform="rotate(46.8479 54.1885 -5.56738)" fill="white"/>
                  </clipPath>
                </defs>
              </svg>

              <!-- F Icon 2 -->
              <svg class="absolute right-16 top-48 w-12 h-12 transform rotate-150 opacity-10"
                   width="66" height="66" viewBox="0 0 66 66" fill="none" xmlns="http://www.w3.org/2000/svg">
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

              <!-- F Icon 3 -->
              <svg class="absolute -left-6 bottom-12 w-32 h-32 transform -rotate-32 opacity-10"
                   width="155" height="177" viewBox="0 0 155 177" fill="none" xmlns="http://www.w3.org/2000/svg">
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

              <!-- F Icon 4 -->
              <svg class="absolute top-5 right-12 w-24 h-24 transform rotate-122 opacity-10"
                   width="133" height="134" viewBox="0 0 133 134" fill="none" xmlns="http://www.w3.org/2000/svg">
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
            <div class="absolute left-1/2 top-4 sm:top-6 transform -translate-x-1/2 w-48 h-48 sm:w-56 sm:h-56 bg-white rounded-2xl border border-gray-200 shadow-lg flex flex-col items-center justify-center">
              <!-- QR Code Placeholder -->
              <div class="w-28 h-28 sm:w-36 sm:h-36 bg-gray-800 rounded-lg flex items-center justify-center mb-2 sm:mb-4">
                <div class="grid grid-cols-8 gap-1">
                  <!-- QR Pattern Mock -->
                  <div v-for="i in 64" :key="i" 
                       :class="qrPattern[i] ? 'bg-black' : 'bg-white'"
                       class="w-2 h-2 rounded-sm">
                  </div>
                </div>
              </div>
              
              <!-- Link Text -->
              <div class="text-dbd-primary text-sm sm:text-lg font-semibold px-2 text-center">
                {{ referralLink }}
              </div>
            </div>

            <!-- Terms Checkbox -->
            <div class="absolute bottom-12 sm:bottom-16 left-4 right-4 flex items-start gap-2">
              <div class="flex-shrink-0">
                <label class="flex items-center cursor-pointer">
                  <input 
                    v-model="agreedToTerms" 
                    type="checkbox" 
                    class="sr-only"
                  />
                  <div class="w-6 h-6 border-2 border-gray-300 rounded bg-white flex items-center justify-center">
                    <svg v-if="agreedToTerms" class="w-4 h-4 text-dbd-primary" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                    </svg>
                  </div>
                </label>
              </div>
              <div class="text-white text-sm sm:text-base font-medium leading-relaxed">
                I agree that I have read the
                <span class="text-dbd-orange underline cursor-pointer">Terms and Conditions</span>
              </div>
            </div>

            <!-- Share Button -->
            <div class="absolute bottom-2 sm:bottom-4 left-4 sm:left-6 right-4 sm:right-6">
              <button
                :disabled="!agreedToTerms"
                :class="[
                  'w-full py-2 sm:py-3 px-8 sm:px-12 rounded-full font-semibold text-sm sm:text-base transition-all duration-200',
                  agreedToTerms
                    ? 'bg-dbd-primary text-white hover:bg-blue-700'
                    : 'bg-gray-300 text-gray-500 cursor-not-allowed'
                ]"
                @click="shareQRCode"
              >
                Share QR code
              </button>
            </div>
          </div>

          <!-- How to use section -->
          <div class="space-y-5">
            <!-- Title -->
            <div class="space-y-3">
              <h2 class="text-dbd-dark text-xl font-bold leading-6">
                How to use the Link
              </h2>
              <p class="text-dbd-gray text-base font-medium leading-6">
                Follow these 3 simple steps
              </p>
            </div>

            <!-- Steps -->
            <div class="flex items-center justify-center gap-4 sm:gap-6 py-4 sm:py-6">
              <!-- Progress Line -->
              <div class="absolute flex items-center justify-between w-60 sm:w-72 mx-auto">
                <div class="flex-1 h-px bg-dbd-light-gray mx-8 sm:mx-11"></div>
                <div class="flex-1 h-px bg-dbd-light-gray mx-8 sm:mx-11"></div>
              </div>

              <!-- Step circles -->
              <div class="relative flex items-center justify-between w-60 sm:w-72 mx-auto">
                <!-- Step 1 -->
                <div class="w-8 h-8 sm:w-10 sm:h-10 bg-dbd-primary rounded-r-full flex items-center justify-center">
                  <span class="text-white text-xs sm:text-sm font-semibold">1</span>
                </div>

                <!-- Step 2 -->
                <div class="w-8 h-8 sm:w-10 sm:h-10 bg-dbd-primary rounded-r-full flex items-center justify-center">
                  <span class="text-white text-xs sm:text-sm font-semibold">2</span>
                </div>

                <!-- Step 3 -->
                <div class="w-8 h-8 sm:w-10 sm:h-10 bg-dbd-primary rounded-r-full flex items-center justify-center">
                  <span class="text-white text-xs sm:text-sm font-semibold">3</span>
                </div>
              </div>
            </div>

            <!-- Step descriptions -->
            <div class="flex justify-between items-start gap-4 px-2">
              <div class="flex flex-col items-center text-center flex-1">
                <div class="flex items-center gap-1 mb-1">
                  <svg class="w-4 h-4 text-dbd-gray" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.367 2.684 3 3 0 00-5.367-2.684z"></path>
                  </svg>
                  <span class="text-dbd-gray text-base font-medium">1</span>
                </div>
                <span class="text-dbd-gray text-xs font-medium leading-4">Share your link</span>
              </div>
              <div class="flex flex-col items-center text-center flex-1">
                <div class="flex items-center gap-1 mb-1">
                  <svg class="w-4 h-4 text-dbd-gray" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                  <span class="text-dbd-gray text-sm font-medium">2</span>
                </div>
                <span class="text-dbd-gray text-xs font-medium leading-4">Wait for joining</span>
              </div>
              <div class="flex flex-col items-center text-center flex-1">
                <div class="flex items-center gap-1 mb-1">
                  <svg class="w-4 h-4 text-dbd-gray" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"></path>
                  </svg>
                  <span class="text-dbd-gray text-sm font-medium">3</span>
                </div>
                <span class="text-dbd-gray text-xs font-medium leading-4">Get rewards</span>
              </div>
            </div>

            <!-- Web Referral Link Section -->
            <div class="relative w-full h-44 sm:h-52 rounded-3xl overflow-hidden"
                 style="background: linear-gradient(93deg, #000482 33.15%, rgba(3, 0, 155, 0.84) 76.97%);">
              
              <!-- Content -->
              <div class="p-4 sm:p-5 space-y-3 sm:space-y-4">
                <div class="space-y-1 sm:space-y-2">
                  <h3 class="text-white text-xl sm:text-2xl font-bold leading-6 sm:leading-8">
                    Web Referral Link
                  </h3>
                  <p class="text-white text-sm sm:text-base font-medium leading-5 sm:leading-6 max-w-48 sm:max-w-52">
                    Copy the link bellow and share with your friends.
                  </p>
                </div>

                <!-- Copy Link Container -->
                <div class="relative w-full h-10 sm:h-12 rounded-full border border-dbd-primary/60 bg-white/10 flex items-center">
                  <div class="flex-1 px-4 sm:px-6 py-2 sm:py-3">
                    <span class="text-white text-base sm:text-lg font-semibold underline truncate block">
                      {{ referralLink }}
                    </span>
                  </div>

                  <!-- Copy Button -->
                  <button
                    @click="copyReferralLink"
                    class="absolute right-0 top-0 h-10 sm:h-12 px-3 sm:px-4 bg-white rounded-r-full border border-dbd-primary flex items-center justify-center gap-1 sm:gap-2 transition-all duration-200 hover:bg-gray-50"
                  >
                    <svg class="w-4 h-4 sm:w-5 sm:h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path>
                    </svg>
                    <span class="text-gray-700 text-xs sm:text-sm font-semibold hidden sm:inline">Copy</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Navigation Component -->
    <BottomNavigation />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import BottomNavigation from '../components/BottomNavigation.vue'

// Reactive data
const agreedToTerms = ref(false)
const referralLink = ref('vm.dubadu/jjhI1uT4S')

// QR Code pattern mock (placeholder)
const qrPattern = computed(() => {
  const pattern = {}
  for (let i = 0; i < 64; i++) {
    // Create a simple random pattern for QR code mock
    pattern[i] = Math.random() > 0.5
  }
  return pattern
})

// Methods
const shareQRCode = () => {
  if (!agreedToTerms.value) return
  
  // Mock share functionality
  if (navigator.share) {
    navigator.share({
      title: 'DBD Capital Referral',
      text: 'Join DBD Capital using my referral link!',
      url: `https://${referralLink.value}`
    }).catch(console.error)
  } else {
    // Fallback for platforms without Web Share API
    copyReferralLink()
  }
}

const copyReferralLink = async () => {
  try {
    if (navigator.clipboard) {
      await navigator.clipboard.writeText(`https://${referralLink.value}`)
    } else {
      // Fallback for older browsers
      const textArea = document.createElement('textarea')
      textArea.value = `https://${referralLink.value}`
      textArea.style.position = 'fixed'
      textArea.style.left = '-999999px'
      textArea.style.top = '-999999px'
      document.body.appendChild(textArea)
      textArea.focus()
      textArea.select()
      document.execCommand('copy')
      document.body.removeChild(textArea)
    }
    
    // Could add a toast notification here
    console.log('Link copied to clipboard!')
  } catch (err) {
    console.error('Failed to copy link:', err)
  }
}
</script>

<style scoped>
.holders-view {
  font-family: 'Montserrat', sans-serif;
}

/* Mobile first approach for Telegram mini app */
@media (max-width: 430px) {
  .holders-view {
    max-width: 100%;
    padding-bottom: env(safe-area-inset-bottom, 80px);
  }

  /* Ensure QR section fits on small screens */
  .qr-section {
    min-height: 320px;
  }

  /* Better touch targets */
  button {
    min-height: 44px;
  }
}

@media (min-width: 431px) and (max-width: 768px) {
  .holders-view {
    max-width: 430px;
    margin: 0 auto;
  }

  /* Tablet optimizations */
  .qr-section {
    min-height: 384px;
  }
}

/* Landscape phone optimizations */
@media (max-height: 600px) and (orientation: landscape) {
  .holders-view {
    font-size: 14px;
  }

  .qr-section {
    height: 280px !important;
  }

  .referral-section {
    height: 160px !important;
  }
}

/* Very small screens */
@media (max-width: 350px) {
  .px-4 {
    padding-left: 12px;
    padding-right: 12px;
  }

  .text-xl {
    font-size: 18px;
  }

  .text-lg {
    font-size: 16px;
  }
}

/* Smooth animations */
button {
  transition: all 0.2s ease;
  -webkit-tap-highlight-color: transparent;
}

button:active {
  transform: scale(0.98);
}

/* Touch-friendly interactions */
@media (hover: none) and (pointer: coarse) {
  button:hover {
    transform: none;
  }

  button:active {
    transform: scale(0.95);
    transition: transform 0.1s ease;
  }
}

/* Prevent text selection on mobile */
* {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* Allow text selection for specific elements */
input, textarea, [contenteditable] {
  -webkit-user-select: text;
  -moz-user-select: text;
  -ms-user-select: text;
  user-select: text;
}

/* Improve scrolling on iOS */
.overflow-y-auto {
  -webkit-overflow-scrolling: touch;
  overscroll-behavior: contain;
}

/* Custom checkbox styling */
input[type="checkbox"]:checked + div {
  background-color: white;
  border-color: #2019CE;
}

/* Ensure proper gradient backgrounds on mobile */
@supports (-webkit-backdrop-filter: blur(32px)) {
  .backdrop-blur {
    -webkit-backdrop-filter: blur(32px);
    backdrop-filter: blur(32px);
  }
}
</style>
