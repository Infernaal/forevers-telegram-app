<template>
  <div class="holders-view">
    <!-- Top Status Bar -->
    <div class="top-status-bar">
      <div class="status-content">
        <!-- Time -->
        <div class="time-section">
          <div class="time">9:41</div>
        </div>
        
        <!-- Telegram Badge -->
        <div class="telegram-badge">
          <div class="telegram-bg"></div>
          <div class="telegram-text">TELEGRAM</div>
        </div>
        
        <!-- Status Icons -->
        <div class="status-icons">
          <!-- Signal bars -->
          <svg width="118" height="14" viewBox="0 0 118 14" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M43.615 2.03295C43.615 1.3999 43.1375 0.886719 42.5484 0.886719H41.4817C40.8926 0.886719 40.415 1.3999 40.415 2.03295V11.9669C40.415 12.5999 40.8926 13.1131 41.4817 13.1131H42.5484C43.1375 13.1131 43.615 12.5999 43.615 11.9669V2.03295ZM36.1809 3.332H37.2476C37.8367 3.332 38.3143 3.8575 38.3143 4.50574V11.9394C38.3143 12.5876 37.8367 13.1131 37.2476 13.1131H36.1809C35.5918 13.1131 35.1143 12.5876 35.1143 11.9394V4.50574C35.1143 3.8575 35.5918 3.332 36.1809 3.332ZM31.8492 5.98105H30.7825C30.1934 5.98105 29.7158 6.51324 29.7158 7.16973V11.9244C29.7158 12.5809 30.1934 13.1131 30.7825 13.1131H31.8492C32.4383 13.1131 32.9158 12.5809 32.9158 11.9244V7.16973C32.9158 6.51324 32.4383 5.98105 31.8492 5.98105ZM26.5484 8.42634H25.4817C24.8926 8.42634 24.415 8.95093 24.415 9.59804V11.9414C24.415 12.5885 24.8926 13.1131 25.4817 13.1131H26.5484C27.1375 13.1131 27.615 12.5885 27.615 11.9414V9.59804C27.615 8.95093 27.1375 8.42634 26.5484 8.42634Z" fill="#02070E"/>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M58.1865 3.30222C60.6736 3.30232 63.0657 4.22441 64.8682 5.87789C65.0039 6.00554 65.2209 6.00393 65.3545 5.87428L66.652 4.61081C66.7197 4.54505 66.7575 4.45597 66.7569 4.36329C66.7563 4.27061 66.7175 4.18197 66.649 4.11697C61.918 -0.257741 54.4543 -0.257741 49.7233 4.11697C49.6548 4.18192 49.6159 4.27054 49.6152 4.36322C49.6146 4.4559 49.6523 4.545 49.7199 4.61081L51.0178 5.87428C51.1514 6.00413 51.3685 6.00574 51.5042 5.87789C53.3069 4.2243 55.6992 3.30221 58.1865 3.30222ZM58.1832 7.5225C59.5405 7.52241 60.8494 8.03415 61.8555 8.95828C61.9916 9.08943 62.2059 9.08659 62.3386 8.95187L63.6259 7.63256C63.6937 7.56336 63.7313 7.46948 63.7303 7.37193C63.7293 7.27438 63.6898 7.1813 63.6207 7.11351C60.5568 4.22266 55.8121 4.22266 52.7483 7.11351C52.6791 7.1813 52.6396 7.27443 52.6387 7.37201C52.6378 7.46959 52.6755 7.56346 52.7435 7.63256L54.0304 8.95187C54.163 9.08659 54.3774 9.08943 54.5135 8.95828C55.5189 8.03476 56.8268 7.52307 58.1832 7.5225ZM60.7076 10.316C60.7095 10.4214 60.6725 10.523 60.6052 10.5968L58.4285 13.0515C58.3647 13.1236 58.2777 13.1642 58.1869 13.1642C58.0962 13.1642 58.0092 13.1236 57.9454 13.0515L55.7683 10.5968C55.7011 10.5229 55.6641 10.4213 55.6661 10.316C55.6681 10.2106 55.7089 10.1108 55.7789 10.0402C57.169 8.72634 59.2049 8.72634 60.595 10.0402C60.6649 10.1109 60.7057 10.2107 60.7076 10.316Z" fill="#02070E"/>
            <rect opacity="0.35" x="73.2568" y="1" width="24" height="12" rx="3.8" stroke="#02070E"/>
            <path opacity="0.4" d="M98.7568 5.28125V9.35672C99.5616 9.01155 100.085 8.20859 100.085 7.31899C100.085 6.42938 99.5616 5.62642 98.7568 5.28125Z" fill="#02070E"/>
            <rect x="74.7568" y="2.5" width="21" height="9" rx="2.5" fill="#02070E"/>
          </svg>
        </div>
      </div>
      
      <!-- DBD Logo -->
      <div class="dbd-logo">
        <svg width="60" height="42" viewBox="0 0 60 42" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g clip-path="url(#clip0_177_9646)">
            <path d="M2.39308 40.809C1.64947 40.4113 1.05458 39.849 0.635451 39.1359C0.202803 38.4228 0 37.6 0 36.6949C0 35.7899 0.216323 34.9808 0.635451 34.254C1.0681 33.5409 1.64947 32.9786 2.39308 32.5809C3.1367 32.1832 3.97495 31.9775 4.92137 31.9775C5.7461 31.9775 6.47619 32.1284 7.13868 32.4164C7.80118 32.7043 8.34199 33.1295 8.77463 33.6917L7.15221 35.1728C6.57084 34.4597 5.86778 34.1031 5.04305 34.1031C4.55632 34.1031 4.12367 34.2128 3.74511 34.4322C3.36654 34.6516 3.06909 34.9533 2.86629 35.351C2.66349 35.7487 2.55532 36.2013 2.55532 36.7087C2.55532 37.2161 2.66349 37.6686 2.86629 38.0663C3.06909 38.464 3.36654 38.7657 3.74511 38.9851C4.12367 39.2045 4.55632 39.3142 5.04305 39.3142C5.86778 39.3142 6.57084 38.9576 7.15221 38.2446L8.76111 39.7256C8.32847 40.2741 7.77414 40.6993 7.12517 41.0009C6.46267 41.2889 5.73258 41.4398 4.90785 41.4398C3.98847 41.4123 3.1367 41.2204 2.39308 40.809Z" fill="#54565A"/>
            <path d="M15.8592 39.465H12.0735L11.3705 41.234H8.78809L12.736 32.1558H15.2237L19.1851 41.234H16.5487L15.8592 39.465ZM15.1156 37.5725L13.9663 34.6653L12.8171 37.5725H15.1156Z" fill="#54565A"/>
            <path d="M26.2428 32.5671C26.8377 32.8413 27.2974 33.2253 27.6219 33.7327C27.9464 34.2401 28.1086 34.8298 28.1086 35.5155C28.1086 36.2011 27.9464 36.7908 27.6219 37.2982C27.2974 37.8056 26.8377 38.1896 26.2428 38.4638C25.6479 38.7381 24.9449 38.8752 24.1337 38.8752H22.5788V41.2477H20.0505V32.1694H24.1472C24.9449 32.1557 25.6479 32.2928 26.2428 32.5671ZM25.1612 36.4891C25.4316 36.256 25.5533 35.9269 25.5533 35.5155C25.5533 35.0903 25.4181 34.7612 25.1612 34.5281C24.9043 34.295 24.4987 34.1715 23.9849 34.1715H22.5788V36.8319H23.9849C24.4987 36.8457 24.8908 36.7222 25.1612 36.4891Z" fill="#54565A"/>
            <path d="M29.366 32.1558H31.8943V41.234H29.366V32.1558Z" fill="#54565A"/>
            <path d="M36.1531 34.199H33.4084V32.1694H41.4259V34.199H38.6949V41.234H36.1666V34.199H36.1531Z" fill="#54565A"/>
            <path d="M47.7264 39.465H43.9407L43.2376 41.234H40.6553L44.6032 32.1558H47.0909L51.0523 41.234H48.4159L47.7264 39.465ZM46.9827 37.5725L45.8335 34.6653L44.6843 37.5725H46.9827Z" fill="#54565A"/>
            <path d="M51.9043 32.1558H54.4326V39.1907H58.705V41.2203H51.9043V32.1558Z" fill="#54565A"/>
            <path d="M58.9213 25.9026H0.270508V28.1927H58.9213V25.9026Z" fill="#FF6800"/>
            <path d="M58.3804 5.66168C57.3799 4.0435 55.9873 2.78187 54.1756 1.8905C52.3639 1.01284 50.2953 0.560303 47.9698 0.560303H37.8972V2.65845C38.6814 3.64581 39.0735 4.83888 39.0735 6.21022C39.0735 7.38957 38.7896 8.4455 38.2082 9.39172C38.1136 9.55628 38.0054 9.70713 37.8972 9.84426V11.3939C38.2758 11.7093 38.6138 12.0521 38.9112 12.4498C39.7089 13.5057 40.101 14.7811 40.101 16.2484C40.101 18.2369 39.3574 19.8413 37.8972 20.9932V22.1726H47.9698C50.3088 22.1726 52.3774 21.7338 54.1756 20.8424C55.9873 19.9647 57.3799 18.7031 58.3804 17.0712C59.3674 15.4393 59.8676 13.5469 59.8676 11.3664C59.8676 9.18602 59.3674 7.29357 58.3804 5.66168ZM52.1205 15.7273C51.0119 16.7832 49.5517 17.3043 47.7264 17.3043H43.9272V5.45598H47.7264C49.5517 5.45598 51.0119 5.97709 52.1205 7.03302C53.2292 8.08895 53.7835 9.52885 53.7835 11.3802C53.7835 13.2315 53.2292 14.6714 52.1205 15.7273ZM20.4832 17.0849C21.4701 15.453 21.9704 13.5606 21.9704 11.3802C21.9704 9.19973 21.4701 7.29357 20.4832 5.67539C19.4827 4.05721 18.0901 2.79558 16.2784 1.90421C14.4667 1.02656 12.3981 0.574015 10.0726 0.574015H0V22.1726H10.0726C12.4116 22.1726 14.4802 21.7338 16.2784 20.8424C18.0901 19.9647 19.4962 18.7031 20.4832 17.0849ZM14.2368 15.7273C13.1281 16.7832 11.668 17.3043 9.84273 17.3043H6.04355V5.45598H9.84273C11.668 5.45598 13.1281 5.97709 14.2368 7.03302C15.3455 8.08895 15.8998 9.52885 15.8998 11.3802C15.8998 13.2315 15.3455 14.6714 14.2368 15.7273ZM38.3028 12.9298C37.6133 12.011 36.6534 11.339 35.4365 10.9139C36.3559 10.4339 37.059 9.80312 37.5457 8.98032C38.0459 8.17123 38.2893 7.25243 38.2893 6.22393C38.2893 4.49604 37.5727 3.1247 36.1531 2.10991C34.7335 1.09512 32.6649 0.587729 29.9473 0.587729H19.05V2.82301C19.8612 3.53611 20.5643 4.3452 21.1321 5.27771C22.2002 7.01931 22.741 9.07631 22.741 11.4076C22.741 13.7389 22.2002 15.7822 21.1321 17.5375C20.5643 18.47 19.8612 19.2791 19.05 19.9922V22.2274H30.5557C33.395 22.2274 35.5717 21.7201 37.0725 20.6778C38.5732 19.6493 39.3304 18.182 39.3304 16.2896C39.3304 14.9456 38.9924 13.8486 38.3028 12.9298ZM25.026 4.97601H29.1632C31.1912 4.97601 32.2052 5.66168 32.2052 7.04673C32.2052 8.4455 31.1912 9.14488 29.1632 9.14488H25.026V4.97601ZM30.0825 17.7569H25.026V13.3686H30.0825C32.1917 13.3686 33.2463 14.0954 33.2463 15.5627C33.2463 17.0301 32.1917 17.7569 30.0825 17.7569Z" fill="#2019CE"/>
          </g>
          <defs>
            <clipPath id="clip0_177_9646">
              <rect width="60" height="42" fill="white"/>
            </clipPath>
          </defs>
        </svg>
      </div>
    </div>

    <!-- Content Container -->
    <div class="content-container">
      <!-- Header Bar -->
      <div class="header-bar">
        <!-- Title -->
        <div class="title">
          <span class="dbd-orange">DBD Capital</span>
          <span class="dbd-blue"> Forevers Bot</span>
        </div>
        <div class="mini-app">mini App</div>
        
        <!-- Close Button -->
        <div class="close-btn">
          <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="16" cy="16" r="15.5" fill="#FAFAFA" stroke="#C7C7C7"/>
          </svg>
          <div class="close-icon">
            <div class="line line-1"></div>
            <div class="line line-2"></div>
          </div>
        </div>
        
        <!-- Options Menu -->
        <div class="options-menu">
          <div class="dots">
            <svg width="4" height="4" viewBox="0 0 4 4" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="2" cy="2" r="2" fill="#02070E"/>
            </svg>
            <svg width="4" height="4" viewBox="0 0 4 4" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="2" cy="2" r="2" fill="#02070E"/>
            </svg>
            <svg width="4" height="4" viewBox="0 0 4 4" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="2" cy="2" r="2" fill="#02070E"/>
            </svg>
          </div>
        </div>
      </div>
      
      <!-- Referral Program Header -->
      <div class="referral-header">
        <h1 class="referral-title">Referral Program</h1>
        <p class="referral-subtitle">Share the QR-code with your friends.</p>
      </div>

      <!-- Scroll Content Container -->
      <div class="scroll-content">
        
        <!-- QR Code Section -->
        <div class="qr-section">
          <!-- Background with gradient -->
          <div class="qr-background">
            <!-- Decorative F Icons -->
            <svg class="f-icon f-icon-1" width="120" height="131" viewBox="0 0 120 131" fill="none" xmlns="http://www.w3.org/2000/svg">
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

            <svg class="f-icon f-icon-2" width="66" height="66" viewBox="0 0 66 66" fill="none" xmlns="http://www.w3.org/2000/svg">
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

            <svg class="f-icon f-icon-3" width="155" height="177" viewBox="0 0 155 177" fill="none" xmlns="http://www.w3.org/2000/svg">
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

            <svg class="f-icon f-icon-4" width="133" height="134" viewBox="0 0 133 134" fill="none" xmlns="http://www.w3.org/2000/svg">
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
          <div class="qr-code-container">
            <div class="qr-code-wrapper">
              <!-- QR Code Image -->
              <img 
                src="https://api.builder.io/api/v1/image/assets/TEMP/d0e1d46df412099f6abe582c7574e9c4a57f8399?width=280" 
                alt="QR Code" 
                class="qr-code-image"
              />
              <!-- QR Code Link -->
              <div class="qr-code-link">vm.dubadu/jjhI1uT4S</div>
            </div>
          </div>
        </div>

        <!-- Terms and Conditions -->
        <div class="terms-container">
          <div class="terms-wrapper">
            <label class="terms-label">
              <input 
                type="checkbox" 
                v-model="termsAccepted" 
                class="terms-checkbox"
              />
              <span class="terms-text">
                I agree that I have read the 
                <a href="#" @click.prevent="openTerms" class="terms-link">Terms and Conditions</a>
              </span>
            </label>
          </div>
        </div>

        <!-- Share Button -->
        <div class="share-button-container">
          <button 
            class="share-button"
            :class="{ 'share-button-disabled': !termsAccepted }"
            :disabled="!termsAccepted"
            @click="shareQRCode"
          >
            Share QR code
          </button>
        </div>

      </div>

      <!-- How to use the Link Section -->
      <div class="how-to-section">
        <!-- Steps Container -->
        <div class="steps-container">
          <!-- Header -->
          <div class="how-to-header">
            <h2 class="how-to-title">How to use the Link</h2>
            <p class="how-to-subtitle">Follow these 3 simple steps</p>
          </div>

          <!-- Step Indicators -->
          <div class="step-indicators">
            <div class="step-indicator-row">
              <div class="step-line step-line-1"></div>
              <div class="step-line step-line-2"></div>
              <div class="step-indicator step-indicator-1"></div>
              <div class="step-indicator step-indicator-2"></div>
              <div class="step-indicator step-indicator-3"></div>
            </div>
          </div>

          <!-- Step Descriptions -->
          <div class="step-descriptions">
            <div class="step-description step-description-1">
              <span class="step-number">1</span>
              <span class="step-text">Share your link</span>
            </div>
            <div class="step-description step-description-2">
              <span class="step-number">2</span>
              <span class="step-text">Wait for joining</span>
            </div>
            <div class="step-description step-description-3">
              <span class="step-number">3</span>
              <span class="step-text">Get rewards</span>
            </div>
          </div>
        </div>

        <!-- Web Referral Link Section -->
        <div class="web-link-section">
          <!-- Background -->
          <div class="web-link-background"></div>
          
          <!-- Content -->
          <div class="web-link-content">
            <div class="web-link-header">
              <h3 class="web-link-title">Web Referral Link</h3>
              <p class="web-link-description">Copy the link bellow and share with your friends.</p>
            </div>
            
            <!-- Copy Link Container -->
            <div class="copy-link-container">
              <div class="copy-link-input-wrapper">
                <span class="copy-link-text">vm.dubadu/jjhI1uT4S</span>
              </div>
              <button 
                class="copy-button"
                :class="{ 'copy-button-copied': linkCopied }"
                @click="copyLink"
              >
                <span class="copy-button-text">Copy</span>
                <div class="copy-icon">
                  <svg v-if="!linkCopied" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M16 4H18C19.1046 4 20 4.89543 20 6V18C20 19.1046 19.1046 20 18 20H6C4.89543 20 4 19.1046 4 18V16M16 4L4 16M16 4V16H4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <div v-else class="copy-tick">✓</div>
                </div>
              </button>
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
import { ref } from 'vue'
import BottomNavigation from '../components/BottomNavigation.vue'

// Reactive data
const termsAccepted = ref(false)
const linkCopied = ref(false)
const referralLink = ref('vm.dubadu/jjhI1uT4S')

// Methods
const shareQRCode = () => {
  if (!termsAccepted.value) return
  
  console.log('Sharing QR code...')
  
  if (navigator.share) {
    navigator.share({
      title: 'DBD Capital Forevers Bot',
      text: 'Join me on DBD Capital Forevers Bot!',
      url: referralLink.value
    }).catch(console.error)
  } else {
    copyLink()
  }
}

const copyLink = async () => {
  try {
    await navigator.clipboard.writeText(referralLink.value)
    linkCopied.value = true
    setTimeout(() => {
      linkCopied.value = false
    }, 2000)
  } catch (err) {
    console.error('Failed to copy link:', err)
  }
}

const openTerms = () => {
  console.log('Opening terms and conditions...')
}
</script>

<style scoped>
.holders-view {
  font-family: 'Montserrat', sans-serif;
  width: 375px;
  height: 812px;
  background: #fff;
  position: relative;
  margin: 0 auto;
  max-width: 375px;
}

/* Top Status Bar */
.top-status-bar {
  width: 375px;
  height: 68px;
  background: linear-gradient(0deg, rgba(255, 255, 255, 0.00) 0%, #FFF 100%);
  position: absolute;
  left: 0;
  top: 0;
}

.status-content {
  display: flex;
  width: 375px;
  justify-content: space-between;
  align-items: center;
  position: absolute;
  left: 0;
  top: 16px;
  height: 36px;
}

.time-section {
  display: flex;
  padding-right: 6px;
  justify-content: center;
  align-items: center;
  gap: 10px;
  flex: 1 0 0;
}

.time {
  color: #02070E;
  text-align: center;
  font-family: 'SF Pro', -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 17px;
  font-weight: 590;
  line-height: 22px;
}

.telegram-badge {
  width: 140px;
  height: 36px;
  position: relative;
}

.telegram-bg {
  width: 140px;
  height: 36px;
  border-radius: 30px;
  background: #027BFD;
  position: absolute;
  left: 0;
  top: 0;
}

.telegram-text {
  color: #FFF;
  text-align: center;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 16px;
  font-weight: 500;
  line-height: 20px;
  position: absolute;
  left: 36px;
  top: 8px;
  width: 92px;
  height: 20px;
}

.status-icons {
  display: flex;
  padding-left: 6px;
  justify-content: center;
  align-items: center;
  gap: 6px;
  flex: 1 0 0;
}

/* DBD Logo */
.dbd-logo {
  width: 60px;
  height: 42px;
  position: absolute;
  left: 157px;
  top: 13px;
}

/* Content Container */
.content-container {
  width: 375px;
  height: 737px;
  background: #F0F0F0;
  border-radius: 16px 16px 0 0;
  position: absolute;
  left: 0;
  top: 76px;
  padding: 0;
}

/* Header Bar */
.header-bar {
  width: 375px;
  height: 44px;
  position: absolute;
  left: 0;
  top: 8px;
}

.title {
  text-align: center;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 18px;
  font-weight: 500;
  line-height: 20px;
  position: absolute;
  left: 71px;
  top: 4px;
  width: 233px;
  height: 20px;
}

.dbd-orange {
  color: #FF6800;
}

.dbd-blue {
  color: #2019CE;
}

.mini-app {
  color: #7E7E7E;
  text-align: center;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 12px;
  font-weight: 500;
  line-height: 16px;
  position: absolute;
  left: 159px;
  top: 24px;
  width: 56px;
  height: 16px;
}

.close-btn {
  width: 44px;
  height: 44px;
  position: absolute;
  left: 8px;
  top: 0;
}

.close-btn svg {
  position: absolute;
  left: 6px;
  top: 6px;
}

.close-icon {
  width: 20px;
  height: 20px;
  position: absolute;
  left: 12px;
  top: 12px;
}

.line {
  width: 18px;
  height: 2px;
  border-radius: 10px;
  background: #02070E;
  position: absolute;
  left: 1px;
  top: 9px;
}

.line-1 {
  transform: rotate(45deg);
}

.line-2 {
  transform: rotate(-45deg);
}

.options-menu {
  width: 44px;
  height: 44px;
  position: absolute;
  left: 331px;
  top: 0;
}

.dots {
  display: flex;
  flex-direction: column;
  gap: 3px;
  position: absolute;
  left: 20px;
  top: 13px;
}

/* Referral Program Header */
.referral-header {
  display: flex;
  width: 299px;
  flex-direction: column;
  align-items: flex-start;
  gap: 4px;
  position: absolute;
  left: 14px;
  top: 66px;
  height: 52px;
}

.referral-title {
  color: #02070E;
  font-family: Montserrat;
  font-size: 20px;
  font-weight: 700;
  line-height: 24px;
  margin: 0;
  align-self: stretch;
}

.referral-subtitle {
  color: #4B4D50;
  font-family: Montserrat;
  font-size: 16px;
  font-weight: 500;
  line-height: 24px;
  margin: 0;
  align-self: stretch;
}

/* Scroll Content */
.scroll-content {
  display: flex;
  width: 347px;
  flex-direction: column;
  justify-content: flex-end;
  align-items: flex-start;
  gap: 20px;
  position: absolute;
  left: 14px;
  top: 138px;
  height: 507px;
}

/* QR Section */
.qr-section {
  width: 347px;
  height: 396px;
  position: absolute;
  left: 0;
  top: 0;
}

.qr-background {
  width: 347px;
  height: 396px;
  border-radius: 24px;
  background: linear-gradient(93deg, #000482 33.15%, rgba(3, 0, 155, 0.84) 76.97%);
  backdrop-filter: blur(32px);
  position: absolute;
  top: 0;
  left: 0;
}

/* Decorative F Icons */
.f-icon {
  position: absolute;
  opacity: 0.1;
}

.f-icon-1 {
  width: 96px;
  height: 96px;
  transform: rotate(46.848deg);
  left: -16px;
  top: -6px;
}

.f-icon-2 {
  width: 48px;
  height: 48px;
  transform: rotate(150.638deg);
  left: 280px;
  top: 189px;
}

.f-icon-3 {
  width: 128px;
  height: 128px;
  transform: rotate(-31.597deg);
  left: -22px;
  top: 194px;
}

.f-icon-4 {
  width: 96px;
  height: 96px;
  transform: rotate(121.978deg);
  left: 211px;
  top: 21px;
}

/* QR Code Container */
.qr-code-container {
  width: 222px;
  height: 220px;
  position: absolute;
  left: 63px;
  top: 24px;
  z-index: 10;
}

.qr-code-wrapper {
  width: 222px;
  height: 220px;
  border-radius: 20px;
  border: 1px solid #F2F2F2;
  background: #FAFAFA;
  box-shadow: 2px 4px 12px 0 rgba(0, 0, 0, 0.04);
  position: relative;
}

.qr-code-image {
  width: 140px;
  height: 140px;
  aspect-ratio: 1/1;
  position: absolute;
  left: 41px;
  top: 20px;
}

.qr-code-link {
  color: #2019CE;
  font-family: Montserrat;
  font-size: 17px;
  font-weight: 600;
  line-height: 24px;
  position: absolute;
  left: 20px;
  top: 176px;
  width: 182px;
  height: 24px;
}

/* Terms Section */
.terms-container {
  position: absolute;
  left: 0;
  top: 256px;
  width: 319px;
  height: 44px;
  z-index: 20;
}

.terms-wrapper {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  width: 100%;
  height: 100%;
}

.terms-label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.terms-checkbox {
  width: 24px;
  height: 24px;
  border-radius: 4px;
  border: 1px solid #7E7E7E;
  background: #FAFAFA;
  cursor: pointer;
}

.terms-text {
  width: 287px;
  color: #4B4D50;
  font-family: Montserrat;
  font-size: 16px;
  font-weight: 500;
  line-height: 22px;
}

.terms-link {
  color: #FF6800;
  text-decoration: underline;
}

/* Share Button */
.share-button-container {
  position: absolute;
  left: 23px;
  top: 322px;
  z-index: 20;
}

.share-button {
  display: flex;
  width: 300px;
  padding: 12px 48px;
  justify-content: center;
  align-items: center;
  gap: 10px;
  border-radius: 1000px;
  background: linear-gradient(90deg, #2019CE 0%, #473FFF 100%);
  border: none;
  cursor: pointer;
  height: 50px;
  color: #FFF;
  text-align: center;
  font-family: Montserrat;
  font-size: 16px;
  font-weight: 600;
  line-height: 26px;
  transition: all 0.2s ease;
}

.share-button:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(32, 25, 206, 0.3);
}

.share-button-disabled {
  background: #E2E2E2 !important;
  color: #989898 !important;
  cursor: not-allowed;
}

/* How to Section */
.how-to-section {
  position: absolute;
  left: 0;
  top: 416px;
  width: 347px;
  height: 410px;
}

.steps-container {
  position: relative;
  width: 100%;
  height: 100%;
}

/* How to Header */
.how-to-header {
  position: absolute;
  left: 0;
  top: 0;
  width: 229px;
  height: 60px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
}

.how-to-title {
  color: #02070E;
  font-family: Montserrat;
  font-size: 20px;
  font-weight: 700;
  line-height: 24px;
  margin: 0;
}

.how-to-subtitle {
  color: #4B4D50;
  font-family: Montserrat;
  font-size: 16px;
  font-weight: 500;
  line-height: 24px;
  margin: 0;
  align-self: stretch;
}

/* Step Indicators */
.step-indicators {
  position: absolute;
  left: 27px;
  top: 88px;
  width: 298px;
  height: 40px;
}

.step-indicator-row {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
  width: 100%;
  height: 100%;
  position: relative;
}

.step-line {
  width: 44px;
  height: 1px;
  background: #7E7E7E;
}

.step-line-1 {
  position: absolute;
  left: 62px;
  top: 20px;
}

.step-line-2 {
  position: absolute;
  left: 192px;
  top: 19px;
}

.step-indicator {
  width: 38px;
  height: 40px;
  border-radius: 0 100px 100px 0;
  background: #2019CE;
}

.step-indicator-1 {
  position: absolute;
  left: 0;
  top: 0;
}

.step-indicator-2 {
  position: absolute;
  left: 130px;
  top: 0;
}

.step-indicator-3 {
  position: absolute;
  left: 260px;
  top: 0;
}

/* Step Descriptions */
.step-descriptions {
  position: absolute;
  left: 0;
  top: 144px;
  width: 100%;
  height: 44px;
  display: flex;
  justify-content: space-between;
}

.step-description {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  text-align: center;
}

.step-description-1 {
  width: 92px;
}

.step-description-2 {
  width: 96px;
  justify-content: center;
}

.step-description-3 {
  width: 74px;
  justify-content: center;
}

.step-number {
  color: #4B4D50;
  font-family: Montserrat;
  font-size: 16px;
  font-weight: 500;
  line-height: 24px;
}

.step-description-2 .step-number,
.step-description-3 .step-number {
  font-size: 14px;
}

.step-text {
  color: #4B4D50;
  font-family: Montserrat;
  font-size: 12px;
  font-weight: 500;
  line-height: 16px;
}

/* Web Referral Link Section */
.web-link-section {
  position: absolute;
  left: 0;
  top: 202px;
  width: 347px;
  height: 208px;
}

.web-link-background {
  width: 347px;
  height: 206px;
  border-radius: 24px;
  background: linear-gradient(93deg, #000482 33.15%, rgba(3, 0, 155, 0.84) 76.97%);
  backdrop-filter: blur(32px);
  position: absolute;
  left: 0;
  top: 2px;
}

.web-link-content {
  position: relative;
  z-index: 10;
  padding: 20px;
}

.web-link-header {
  width: 204px;
  height: 86px;
  margin-bottom: 28px;
}

.web-link-title {
  color: #FFF;
  font-family: Montserrat;
  font-size: 26px;
  font-weight: 700;
  line-height: 30px;
  margin: 0 0 12px 0;
  width: 244px;
  height: 30px;
}

.web-link-description {
  color: #FFF;
  font-family: Montserrat;
  font-size: 16px;
  font-weight: 500;
  line-height: 24px;
  margin: 0;
  width: 204px;
  height: 48px;
}

/* Copy Link Container */
.copy-link-container {
  width: 307px;
  height: 52px;
  position: relative;
  border-radius: 100px;
  border: 1px solid rgba(32, 25, 206, 0.60);
  background: rgba(255, 255, 255, 0.10);
  display: flex;
  align-items: center;
}

.copy-link-input-wrapper {
  flex: 1;
  padding: 14px 24px;
}

.copy-link-text {
  color: #FAFAFA;
  font-family: Montserrat;
  font-size: 17px;
  font-weight: 600;
  line-height: 24px;
  text-decoration: underline;
  width: 182px;
  height: 24px;
}

.copy-button {
  width: 50px;
  height: 52px;
  border-radius: 0 100px 100px 0;
  border: 1px solid #443FCC;
  background: #FAFAFA;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
}

.copy-button:hover {
  background: #e8e8ff;
}

.copy-button-copied {
  background: #4caf50 !important;
}

.copy-button-text {
  color: #FFF;
  font-family: Montserrat;
  font-size: 14px;
  font-weight: 600;
  line-height: 22px;
  position: absolute;
  left: -18px;
  white-space: nowrap;
  width: 37px;
  height: 22px;
}

.copy-icon {
  display: flex;
  width: 24px;
  height: 24px;
  padding: 1.5px;
  justify-content: center;
  align-items: center;
  color: #443FCC;
}

.copy-tick {
  color: white;
  font-weight: bold;
}

/* Responsive Design */
@media (max-width: 375px) {
  .holders-view {
    width: 100vw;
    max-width: 375px;
  }
  
  .content-container {
    width: 100vw;
    max-width: 375px;
  }
  
  .top-status-bar {
    width: 100vw;
    max-width: 375px;
  }
  
  .status-content {
    width: 100vw;
    max-width: 375px;
  }
}

@media (min-width: 376px) {
  .holders-view {
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  }
}

/* Touch-friendly optimizations */
.holders-view {
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

button {
  touch-action: manipulation;
  -webkit-user-select: none;
  user-select: none;
}

button:active {
  transform: scale(0.98);
  transition: transform 0.1s ease;
}
</style>
