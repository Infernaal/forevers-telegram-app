<template>
  <!-- Profile Overlay with Blurred Background -->
  <Transition
    name="profile-overlay"
    enter-active-class="transition-all duration-400 ease-out"
    leave-active-class="transition-all duration-300 ease-in"
    enter-from-class="opacity-0 translate-y-full"
    enter-to-class="opacity-100 translate-y-0"
    leave-from-class="opacity-100 translate-y-0"
    leave-to-class="opacity-0 translate-y-full"
  >
    <div
      v-if="isVisible"
      class="overlay-container"
      @click="$emit('close')"
    >
      <!-- Blurred Background Overlay -->
      <div class="overlay-backdrop"></div>

      <!-- Triangular Pointer at Bottom pointing to BottomNavigation -->
      <div class="overlay-pointer"></div>

      <!-- Profile Drop List Container -->
      <div
        class="profile-container"
        @click.stop
      >
        <!-- Profile Header Section -->
        <div class="profile-header">
          <div class="profile-card">
            <div class="profile-content">
              <!-- Large Avatar -->
              <div class="avatar-container">
                <div class="avatar-frame">
                  <img 
                    :src="profileData.avatar" 
                    :alt="profileData.name"
                    class="avatar-image"
                  />
                </div>
              </div>
              
              <!-- User Info -->
              <div class="user-info">
                <!-- Silver Badge -->
                <div class="user-badge">
                  <div class="badge-container">
                    <svg class="badge-icon" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M14.0004 26.2497C7.24592 26.2497 1.75073 20.7545 1.75073 14.0001C1.75073 7.24564 7.24592 1.75085 14.0004 1.75085C20.7548 1.75085 26.25 7.24564 26.25 14.0001C26.25 20.7545 20.7544 26.2497 14.0004 26.2497Z" fill="white"/>
                      <path d="M20.2071 5.37145C20.73 5.37145 21.2468 5.39833 21.7567 5.4472C19.7049 3.58479 16.9828 2.44812 14 2.44812C7.63041 2.44812 2.448 7.63013 2.448 14.0001C2.448 16.2735 3.11102 18.3941 4.24973 20.1832C4.86143 11.9015 11.769 5.37145 20.2071 5.37145Z" fill="#E0E0E0"/>
                      <path d="M14.0006 25.5519C20.3702 25.5519 25.5526 20.3699 25.5526 13.9999C25.5526 10.6131 24.0873 7.56229 21.7577 5.44697C21.2478 5.39809 20.731 5.37122 20.2081 5.37122C11.7704 5.37122 4.86244 11.9017 4.25073 20.1829C6.30211 23.4072 9.90475 25.5519 14.0006 25.5519Z" fill="#B5B5B5"/>
                      <path d="M14.0004 23.1368C19.0464 23.1368 23.1369 19.0463 23.1369 14.0003C23.1369 8.95433 19.0464 4.86377 14.0004 4.86377C8.95445 4.86377 4.86389 8.95433 4.86389 14.0003C4.86389 19.0463 8.95445 23.1368 14.0004 23.1368Z" fill="#9E9E9E"/>
                      <path d="M19.4965 12.7667L15.6984 12.2148L14.0001 8.77307L12.3014 12.2148L8.50366 12.7667L11.2519 15.4452L10.6031 19.2279L14.0001 17.4421L17.397 19.2279L16.7483 15.4452L19.4965 12.7667Z" fill="#F6F6F6"/>
                      <path d="M20.5542 6.30372C20.755 6.5045 21.4074 6.81443 21.7117 6.9529C21.7728 6.98059 21.7728 7.06693 21.7117 7.09462C21.4074 7.23309 20.7554 7.54261 20.5542 7.7438C20.3534 7.94458 20.0435 8.59701 19.905 8.90124C19.8774 8.96233 19.791 8.96233 19.7633 8.90124C19.6249 8.59701 19.3153 7.94499 19.1141 7.7438C18.9134 7.54302 18.2609 7.23309 17.9567 7.09462C17.8956 7.06693 17.8956 6.98059 17.9567 6.9529C18.2609 6.81443 18.913 6.50491 19.1141 6.30372C19.3149 6.10294 19.6249 5.45051 19.7633 5.14628C19.791 5.08519 19.8774 5.08519 19.905 5.14628C20.0431 5.45051 20.353 6.10253 20.5542 6.30372Z" fill="white"/>
                      <path d="M19.4971 12.7667L15.699 12.2144L14.0007 8.77307V17.4421L17.3977 19.2279L16.7489 15.4452L19.4971 12.7667Z" fill="#E0E0E0"/>
                    </svg>
                    <span class="badge-text">Silver</span>
                  </div>
                </div>
                <h1 class="user-name">{{ profileData.name }}</h1>
              </div>
              
              <!-- Right Arrow Button -->
              <button 
                @click="$emit('close')"
                class="close-button"
              >
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                  <path d="M17.2155 11.2862L8.2216 2.29534C7.82696 1.90169 7.18757 1.90169 6.79192 2.29534C6.39728 2.68898 6.39728 3.32838 6.79192 3.72203L15.0724 11.9996L6.79292 20.2771C6.39827 20.6707 6.39827 21.3101 6.79292 21.7048C7.18756 22.0984 7.82795 22.0984 8.2226 21.7048L17.2165 12.7139C17.6051 12.3244 17.6051 11.6749 17.2155 11.2862Z" fill="#B7B7B7"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Menu Items Section with Custom Scrolling -->
        <div class="menu-section">
          <!-- Custom scrollbar indicator -->
          <div class="scrollbar-indicator"></div>

          <div class="menu-items">
            <!-- Calculator -->
            <div @click="handleMenuClick('calculator')" class="menu-item">
              <div class="menu-icon">
                <svg width="16" height="20" viewBox="0 0 16 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M14.1377 0C15.1645 0 16 0.788555 16 1.75781V18.2422C16 19.2114 15.1645 20 14.1377 20H1.8623C0.835502 20 0 19.2114 0 18.2422V1.75781C0 0.788555 0.835502 0 1.8623 0H14.1377ZM1.8623 1.17188C1.52004 1.17188 1.24121 1.43473 1.24121 1.75781V18.2422C1.24121 18.5653 1.52004 18.8281 1.8623 18.8281H14.1377C14.48 18.8281 14.7587 18.5653 14.7588 18.2422V1.75781C14.7588 1.43473 14.48 1.17188 14.1377 1.17188H1.8623ZM5.06445 14.5947C5.40691 14.595 5.68443 14.8573 5.68457 15.1807V16.9668C5.6844 17.2901 5.40693 17.5525 5.06445 17.5527H2.88477C2.54207 17.5527 2.26385 17.2903 2.26367 16.9668V15.1807C2.26381 14.8572 2.54205 14.5947 2.88477 14.5947H5.06445ZM13.1152 14.5947C13.4578 14.5949 13.7353 14.8573 13.7354 15.1807V16.9668C13.7352 17.2901 13.4577 17.5525 13.1152 17.5527H6.91016C6.56746 17.5527 6.28924 17.2903 6.28906 16.9668V15.1807C6.2892 14.8572 6.56744 14.5947 6.91016 14.5947H13.1152ZM3.50488 16.3809H4.44336V15.7666H3.50488V16.3809ZM7.53027 16.3809H12.4941V15.7666H7.53027V16.3809ZM5.06445 11.1709C5.40699 11.1711 5.68457 11.4334 5.68457 11.7568V13.542C5.68457 13.8654 5.40704 14.1277 5.06445 14.1279H2.88477C2.54196 14.1279 2.26367 13.8656 2.26367 13.542V11.7568C2.26367 11.4332 2.54196 11.1709 2.88477 11.1709H5.06445ZM9.08984 11.1709C9.43238 11.1711 9.70996 11.4334 9.70996 11.7568V13.542C9.70996 13.8654 9.43243 14.1277 9.08984 14.1279H6.91016C6.56735 14.1279 6.28906 13.8656 6.28906 13.542V11.7568C6.28906 11.4332 6.56735 11.1709 6.91016 11.1709H9.08984ZM13.1152 11.1709C13.4578 11.1711 13.7354 11.4334 13.7354 11.7568V13.542C13.7354 13.8654 13.4578 14.1277 13.1152 14.1279H10.9355C10.5927 14.1279 10.3145 13.8656 10.3145 13.542V11.7568C10.3145 11.4332 10.5927 11.1709 10.9355 11.1709H13.1152ZM3.50488 12.9561H4.44336V12.3428H3.50488V12.9561ZM7.53027 12.9561H8.46875V12.3428H7.53027V12.9561ZM11.5557 12.9561H12.4941V12.3428H11.5557V12.9561ZM5.06445 7.74609C5.40691 7.74634 5.68443 8.00866 5.68457 8.33203V10.1182C5.6844 10.4415 5.40693 10.7039 5.06445 10.7041H2.88477..." fill="white"/>
                </svg>
              </div>
              <span class="menu-text">Calculator</span>
            </div>

            <!-- Ambassador -->
            <div @click="handleMenuClick('ambassador')" class="menu-item">
              <div class="menu-icon">
                <svg width="14" height="20" viewBox="0 0 14 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M7 9.64844C9.76508 9.64858 12.0066 11.9652 12.0068 14.8242C12.0068 17.6826 9.76511 19.9999 7 20C4.23394 20 1.99219 17.6827 1.99219 14.8242C1.99243 11.9651 4.23409 9.64844 7 9.64844ZM6.09668 13.8418L4.07715 14.1465L5.53906 15.6182L5.19434 17.6992L7 16.7168L8.80566 17.6992L8.46191 15.6182L9.92383 14.1465L7.90332 13.8418L7 11.9512L6.09668 13.8418ZM4.60547 0L7 3.30078L9.39453 0H14L7 9.64844L0 0H4.60547Z" fill="white"/>
                </svg>
              </div>
              <span class="menu-text">Ambassador</span>
            </div>

            <!-- Verification with Badge -->
            <div @click="handleMenuClick('verification')" class="menu-item">
              <div class="menu-icon">
                <svg width="18" height="22" viewBox="0 0 18 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M14.2511 12.4974C15.4932 12.4974 16.5 13.5045 16.5 14.7467V15.3222C16.5 16.2166 16.1805 17.0816 15.5989 17.7611C14.0295 19.5949 11.6422 20.5 8.49673 20.5C5.35076 20.5 2.96466 19.5946 1.39831 17.7601C0.818531 17.081 0.5 16.2174 0.5 15.3245V14.7467C0.5 13.5045 1.50689 12.4974 2.74896 12.4974H14.2511ZM14.2511 13.9977H2.74896C2.33534 13.9977 2.00005 14.333 2.00005 14.7467V15.3245C2.00005 15.8602 2.19117 16.3784 2.53904 16.7858C3.79239 18.2538 5.75834 18.9997 8.49673 18.9997C11.2351 18.9997 13.2028 18.2537 14.4593 16.7855C14.8082 16.3779 14.9999 15.8589 14.9999 15.3222V14.7467C14.9999 14.333 14.6647 13.9977 14.2511 13.9977ZM8.49673 0.5C11.2582 0.5 13.4969 2.73897 13.4969 5.50088C13.4969 8.2628 11.2582 10.5017 8.49673 10.5017C5.73521 10.5017 3.49656 8.2628 3.49656 5.50088C3.49656 2.73897 5.73521 0.5 8.49673 0.5ZM8.49673 2.00026C6.56366 2.00026 4.99661 3.56755 4.99661 5.50088C4.99661 7.43422 6.56366 9.00148 8.49673 9.00148C10.4298 9.00148 11.9968 7.43422 11.9968 5.50088C11.9968 3.56755 10.4298 2.00026 8.49673 2.00026Z" fill="white"/>
                </svg>
              </div>
              <span class="menu-text">Verification</span>
              <!-- Red X Badge -->
              <div class="verification-badge">
                <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M8.5 3.5L3.5 8.5M3.5 3.5L8.5 8.5" stroke="#FF1919" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
            </div>

            <!-- Security -->
            <div @click="handleMenuClick('security')" class="menu-item">
              <div class="menu-icon">
                <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M8.78516 0.0354746C8.92389 -0.0121504 9.07611 -0.0121504 9.21484 0.0354746C10.6561 0.531013 12.1438 0.945188 13.6377 1.26497C14.8838 1.5317 16.1601 1.73823 17.4297 1.87922C17.7546 1.91522 18 2.18263 18 2.50032V8.7386C17.9998 13.165 15.3282 17.2234 11.1943 19.0784L9.26953 19.9427C9.18416 19.9808 9.09193 20.0003 9 20.0003C8.90802 20.0003 8.81583 19.9808 8.73047 19.9427L6.80566 19.0784C2.67178 17.2233 0.000192532 13.165 0 8.7386V2.50032C0 2.18263 0.245411 1.91529 0.570312 1.87922C1.83994 1.73823 3.11627 1.53164 4.3623 1.26497C5.85626 0.945192 7.34396 0.531005 8.78516 0.0354746ZM9 1.28743C7.57623 1.76779 6.10923 2.17074 4.6377 2.48567C3.53526 2.72147 2.41054 2.91243 1.28613 3.05403V8.7386C1.28633 12.6791 3.6638 16.2924 7.34375 17.9437L9 18.6868L10.6562 17.9437C14.3362 16.2924 16.7137 12.6792 16.7139 8.7386V3.05403C15.5895 2.91243 14.4647 2.72154 13.3623 2.48567C11.8907 2.17074 10.4239 1.7678 9 1.28743ZM9 4.37532C10.4179 4.37532 11.5713 5.49682 11.5713 6.87532V7.50032L11.7021 7.50618C12.3499 7.57014 12.8564 8.10392 12.8564 8.75032V13.1253C12.8563 13.8145 12.2802 14.3753 11.5713 14.3753H6.42871C5.71976 14.3753 5.14277 13.8145 5.14258 13.1253V8.75032C5.14258 8.10406 5.64931 7.57034 6.29688 7.50618L6.42871 7.50032V6.87532C6.42871 5.49687 7.58218 4.3754 9 4.37532ZM6.42871 13.1253H11.5723L11.5713 8.75032H6.42871V13.1253ZM9 5.62532C8.29099 5.6254 7.71484 6.18599 7.71484 6.87532V7.50032H10.2861V6.87532C10.2861 6.18594 9.70907 5.62532 9 5.62532Z" fill="white"/>
                </svg>
              </div>
              <span class="menu-text">Security</span>
            </div>

            <!-- Settings -->
            <div @click="handleMenuClick('settings')" class="menu-item">
              <div class="menu-icon">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M12.2222 20L12.3457 19.375L12.8148 17.0913C13.5679 16.8029 14.2469 16.3972 14.8642 15.9135L17.1605 16.6827L17.7778 16.875L18.0988 16.3221L19.679 13.6778L20 13.125L19.5309 12.7163L17.7531 11.2019C17.8179 10.8083 17.9012 10.4147 17.9012 10C17.9012 9.58531 17.8179 9.19169 17.7531 8.79808L19.5309 7.28369L20 6.875L19.679 6.32215L18.0988 3.67785L17.7778 3.125L17.1605 3.31731L14.8642 4.08654C14.2469 3.60277 13.5679 3.19708 12.8148 2.90862L12.3457 0.625L12.2222 0H7.77775L7.65426 0.625L7.18516 2.90862C6.43209 3.19708 5.75306 3.60277 5.13581 4.08654L2.83947 3.31731L2.22215 3.125L1.9012 3.67785L0.32095 6.32215L0 6.875L0.469097 7.28369L2.24688 8.79808C2.18209 9.19169 2.09873 9.58531 2.09873 10C2.09873 10.4147 2.18209 10.8083 2.24688 11.2019L0.469097 12.7163L0 13.125L0.32095 13.6778L1.9012 16.3221L2.22215 16.875L2.83947 16.6827L5.13581 15.9135C5.75306 16.3972 6.43209 16.8029 7.18516 17.0913L7.65426 19.375L7.77775 20H12.2222ZM10.9383 18.4615H9.06171L8.66664 16.4663L8.56788 16.0096L8.12343 15.8654C7.2253 15.5919 6.41044 15.1292 5.72841 14.5192L5.38265 14.2068L4.93828 14.3509L2.93824 15.024L1.99996 13.4615L3.58022 12.0914L3.95062 11.8029L3.82713 11.3462C3.72528 10.9075 3.67898 10.4598 3.67898 10C3.67898 9.54023 3.72528 9.09254 3.82713 8.65385L3.92589 8.19708L3.58022 7.90862L1.99996 6.53846L2.93824 4.976L4.93828 5.64908L5.38265 5.79323L5.72841 5.48077C6.41044 4.87077 7.2253 4.40808 8.12343 4.13461L8.56788 3.99039L8.66664 3.53369L9.06171 1.53846H10.9383L11.3333 3.53369L11.4321 3.99039L11.8765 4.13461C12.7747 4.40808 13.5895 4.87077 14.2716 5.48077L14.6173 5.79323L15.0617 5.64908L17.0617 4.976L18 6.53846L16.4197 7.90862L16.0494 8.19708L16.1728 8.65385C16.2747 9.09254 16.321 9.54023 16.321 10C16.321 10.4598 16.2747 10.9075 16.1728 11.3462L16.0494 11.8029L16.4197 12.0914L18 13.4615L17.0617 15.024L15.0617 14.3509L14.6173 14.2068L14.2716 14.5192C13.5895 15.1292 12.7747 15.5919 11.8765 15.8654L11.4321 16.0096L11.3333 16.4663L10.9383 18.4615ZM9.99998 13.8462C12.17..." fill="white"/>
                </svg>
              </div>
              <span class="menu-text">Settings</span>
            </div>

            <!-- Support -->
            <div @click="handleMenuClick('support')" class="menu-item">
              <div class="menu-icon">
                <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M8.99902 0C13.9325 0 17.998 3.80872 17.998 8.58691V10.1348C17.9981 10.1411 17.999 10.1479 17.999 10.1543V12.9561C17.9992 12.9624 18 12.9692 18 12.9756V14.543C17.9997 16.724 16.1499 18.4277 13.9502 18.4277H11.2695C10.9422 19.3551 10.0281 19.9951 8.99902 19.9951C7.71066 19.9949 6.59988 18.993 6.59961 17.6777C6.59962 16.3623 7.71051 15.3606 8.99902 15.3604C10.0286 15.3604 10.9435 15.9998 11.2705 16.9277H13.9502C15.1589 16.9277 16.1261 16.1539 16.4111 15.1514C16.155 15.2407 15.8817 15.293 15.5986 15.293C14.3103 15.2927 13.1995 14.2908 13.1992 12.9756V10.1543C13.1992 8.83884 14.3101 7.83714 15.5986 7.83691C15.9032 7.83691 16.1972 7.89422 16.4697 7.99707C16.1535 4.38853 12.9637 1.5 8.99902 1.5C5.03445 1.50011 1.84359 4.38856 1.52734 7.99707C1.80001 7.89396 2.09449 7.83697 2.39941 7.83691C3.6881 7.83691 4.7998 8.83869 4.7998 10.1543V12.9756C4.79953 14.291 3.68794 15.293 2.39941 15.293C1.11107 15.2927 0.000274862 14.2908 0 12.9756V8.58691C4.31105e-05 3.80879 4.0657 0.000121624 8.99902 0ZM8.99902 16.8604C8.4656 16.8606 8.09962 17.2622 8.09961 17.6777C8.0999 18.0931 8.4658 18.4949 8.99902 18.4951C9.53249 18.4951 9.89913 18.0932 9.89941 17.6777C9.89941 17.2621 9.53269 16.8604 8.99902 16.8604ZM2.39941 9.33691C1.866 9.33713 1.50001 9.73876 1.5 10.1543V12.9756C1.50029 13.391 1.86621 13.7927 2.39941 13.793C2.93286 13.793 3.29952 13.3911 3.2998 12.9756V10.1543C3.2998 9.73865 2.93306 9.33691 2.39941 9.33691ZM15.5986 9.33691C15.0652 9.33713 14.6992 9.73876 14.6992 10.1543V12.9756C14.6995 13.391 15.0654 13.7927 15.5986 13.793C16.1321 13.793 16.4987 13.3911 16.499 12.9756V10.1729C16.4989 10.1667 16.4981 10.1605 16.498 10.1543V10.1348C16.487 9.72598 16.1241 9.33691 15.5986 9.33691Z" fill="white"/>
                </svg>
              </div>
              <span class="menu-text">Support</span>
            </div>

            <!-- Help -->
            <div @click="handleMenuClick('help')" class="menu-item">
              <div class="menu-icon">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9.69301 13.4082C9.12117 13.4082 8.6582 13.8848 8.6582 14.4566C8.6582 15.0149 9.10754 15.5051 9.69301 15.5051C10.2785 15.5051 10.7414 15.0149 10.7414 14.4566C10.7414 13.8848 10.2649 13.4082 9.69301 13.4082Z" fill="white"/>
                  <path d="M9.86984 5.46875C8.03168 5.46875 7.1875 6.55801 7.1875 7.29328C7.1875 7.82434 7.6368 8.06941 8.00445 8.06941C8.73969 8.06941 8.44016 7.02098 9.82898 7.02098C10.5098 7.02098 11.0545 7.32055 11.0545 7.94687C11.0545 8.68219 10.292 9.10426 9.84262 9.48551C9.44777 9.8259 8.93035 10.3842 8.93035 11.5552C8.93035 12.2632 9.12094 12.4674 9.67922 12.4674C10.3464 12.4674 10.4825 12.1679 10.4825 11.9092C10.4825 11.2011 10.4962 10.7927 11.2451 10.2072C11.6127 9.92125 12.7701 8.99535 12.7701 7.71543C12.7701 6.43551 11.6127 5.46875 9.86984 5.46875Z" fill="white"/>
                  <path d="M10 0C4.47328 0 0 4.47254 0 10V19.2188C0 19.6502 0.349766 20 0.78125 20H10C15.5267 20 20 15.5275 20 10C20 4.47328 15.5275 0 10 0ZM10 18.4375H1.5625V10C1.5625 5.33684 5.33621 1.5625 10 1.5625C14.6632 1.5625 18.4375 5.33621 18.4375 10C18.4375 14.6632 14.6638 18.4375 10 18.4375Z" fill="white"/>
                </svg>
              </div>
              <span class="menu-text">Help</span>
            </div>
          </div>
        </div>

        <!-- Start Level Upgrade Section -->
        <div class="upgrade-section">
          <div class="upgrade-card">
            <!-- Star Icon -->
            <div class="upgrade-star">
              <svg class="star-icon" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
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
            <div class="upgrade-gradient"></div>

            <div class="upgrade-content">
              <div class="upgrade-info">
                <div class="upgrade-title">Start</div>
                <div class="upgrade-subtitle">
                  buy <span class="upgrade-number">123</span> more Forevers to upgrade
                </div>
              </div>
              <button @click="handleUpgrade" class="upgrade-button">
                Upgrade
              </button>
            </div>
          </div>
        </div>

        <!-- Bottom Section - ID and Language -->
        <div class="bottom-section">
          <div class="bottom-controls">
            <!-- ID Container -->
            <div class="id-container">
              <button
                @click="copyUserId"
                class="id-button"
              >
                <div class="id-content">
                  <span class="id-label">ID:</span>
                  <span class="id-value">{{ profileData.id }}</span>
                </div>
                <div class="copy-icon">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M20 9H11C9.9 9 9 9.9 9 11V20C9 21.1 9.9 22 11 22H20C21.1 22 22 21.1 22 20V11C22 9.9 21.1 9 20 9ZM20 20H11V11H20V20ZM17 6H15V4C15 2.9 14.1 2 13 2H4C2.9 2 2 2.9 2 4V13C2 14.1 2.9 15 4 15H6V13H4V4H13V6H15V6Z" fill="#888"/>
                  </svg>
                </div>
              </button>

              <!-- Success Toast -->
              <Transition
                name="copy-toast"
                enter-active-class="transition-all duration-400 ease-out"
                leave-active-class="transition-all duration-300 ease-in"
                enter-from-class="opacity-0 scale-90"
                enter-to-class="opacity-100 scale-100"
                leave-from-class="opacity-100 scale-100"
                leave-to-class="opacity-0 scale-90"
              >
                <div
                  v-if="showCopyMessage"
                  class="copy-toast"
                >
                  <div class="toast-icon">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
                      <polyline points="20,6 9,17 4,12" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>
                  <span class="toast-text">Copied</span>
                </div>
              </Transition>
            </div>

            <!-- Language Container -->
            <div class="language-container">
              <button
                @click="toggleLanguageSelector"
                class="language-button"
              >
                <div class="flag-wrapper">
                  <CountryFlag :country="selectedLanguage.code" size="small" />
                </div>
                <span class="language-text">{{ selectedLanguage.name }}</span>
                <div class="arrow-wrapper">
                  <svg
                    width="16"
                    height="16"
                    viewBox="0 0 16 16"
                    fill="none"
                    class="arrow-icon"
                    :class="{ 'rotate-180': isLanguageDropdownOpen }"
                  >
                    <path d="M4 6L8 10L12 6" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
              </button>

              <!-- Language Dropdown -->
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
                  v-if="isLanguageDropdownOpen"
                  class="language-dropdown"
                >
                  <div class="dropdown-content">
                    <button
                      v-for="language in availableLanguages"
                      :key="language.code"
                      @click="selectLanguage(language)"
                      class="dropdown-item"
                      :class="{
                        'dropdown-item-active': selectedLanguage.code === language.code,
                        'dropdown-item-inactive': selectedLanguage.code !== language.code
                      }"
                    >
                      <div class="dropdown-flag">
                        <CountryFlag :country="language.code" size="small" />
                      </div>
                      <span class="dropdown-text">{{ language.name }}</span>
                      <div
                        v-if="selectedLanguage.code === language.code"
                        class="dropdown-indicator"
                      ></div>
                    </button>
                  </div>
                </div>
              </Transition>
            </div>
          </div>
        </div>

      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted } from 'vue'
import CountryFlag from './CountryFlag.vue'

// Props
const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  }
})

// Emits
defineEmits(['close'])

// Profile data
const profileData = ref({
  name: 'Jason Williams',
  id: '515745',
  avatar: 'https://images.pexels.com/photos/15023413/pexels-photo-15023413.jpeg?auto=compress&cs=tinysrgb&w=400'
})

// Language selector state
const isLanguageDropdownOpen = ref(false)
const selectedLanguage = ref({ code: 'us', name: 'ENG' })
const showCopyMessage = ref(false)

// Available languages
const availableLanguages = ref([
  { code: 'us', name: 'ENG' },
  { code: 'ru', name: 'RUS' },
  { code: 'de', name: 'DEU' },
  { code: 'fr', name: 'FRA' },
  { code: 'es', name: 'ESP' },
  { code: 'it', name: 'ITA' },
  { code: 'pl', name: 'POL' },
  { code: 'ua', name: 'UKR' },
  { code: 'kz', name: 'KAZ' },
  { code: 'uae', name: 'UAE' }
])

// Prevent body scroll when overlay is open
watch(() => props.isVisible, (isVisible) => {
  if (isVisible) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = ''
    isLanguageDropdownOpen.value = false
  }
})

// Close dropdown when clicking outside
const handleClickOutside = (event) => {
  if (!event.target.closest('.language-container')) {
    isLanguageDropdownOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})

// Methods
const handleMenuClick = (section) => {
  console.log(`Navigate to ${section}`)
  // TODO: Add navigation logic
}

const handleUpgrade = () => {
  console.log('Upgrade clicked')
  // TODO: Add upgrade logic
}

const copyUserId = async () => {
  const showSuccessMessage = () => {
    showCopyMessage.value = true
    setTimeout(() => {
      showCopyMessage.value = false
    }, 2000)
  }

  // Check if modern clipboard API is available and allowed
  if (navigator.clipboard && window.isSecureContext) {
    try {
      await navigator.clipboard.writeText(profileData.value.id)
      showSuccessMessage()
      return
    } catch (err) {
      console.log('Clipboard API failed, using fallback:', err.message)
    }
  }

  // Fallback method for older browsers or when clipboard API is blocked
  try {
    const textArea = document.createElement('textarea')
    textArea.value = profileData.value.id
    textArea.style.position = 'fixed'
    textArea.style.left = '-999999px'
    textArea.style.top = '-999999px'
    document.body.appendChild(textArea)
    textArea.focus()
    textArea.select()
    const successful = document.execCommand('copy')
    document.body.removeChild(textArea)

    if (successful) {
      showSuccessMessage()
    } else {
      console.error('Fallback copy method failed')
    }
  } catch (err) {
    console.error('All copy methods failed:', err)
  }
}

const toggleLanguageSelector = () => {
  isLanguageDropdownOpen.value = !isLanguageDropdownOpen.value
}

const selectLanguage = (language) => {
  selectedLanguage.value = language
  isLanguageDropdownOpen.value = false
  console.log(`Language selected: ${language.name}`)
}
</script>

<style scoped>
/* Overlay Container */
.overlay-container {
  position: fixed;
  inset: 0;
  z-index: 50;
  overflow: hidden;
}

.overlay-backdrop {
  position: absolute;
  inset: 0;
  background: rgba(107, 114, 128, 0.1);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

.overlay-pointer {
  position: absolute;
  bottom: calc(180px + env(safe-area-inset-bottom, 0));
  left: 32px;
  width: 0;
  height: 0;
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  border-top: 12px solid #120B81;
  z-index: 60;
}

/* Profile Container */
.profile-container {
  position: absolute;
  left: 16px;
  right: 16px;
  top: 40px;
  bottom: calc(180px + env(safe-area-inset-bottom, 0));
  background: linear-gradient(135deg, #120B81 0%, #1A1086 50%, #09074E 100%);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(8px);
  display: flex;
  flex-direction: column;
  max-height: calc(100vh - 220px - env(safe-area-inset-bottom, 0));
}

/* Profile Header */
.profile-header {
  padding: 12px;
  flex-shrink: 0;
}

.profile-card {
  background: rgba(96, 95, 135, 0.24);
  border: 1px solid rgba(216, 216, 216, 0.24);
  backdrop-filter: blur(12px);
  border-radius: 50px 20px 20px 50px;
  padding: 16px;
}

.profile-content {
  display: flex;
  align-items: center;
  gap: 16px;
}

.avatar-container {
  position: relative;
  flex-shrink: 0;
}

.avatar-frame {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 1px solid #7E73D6;
  overflow: hidden;
}

.avatar-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.user-info {
  flex: 1;
  min-width: 0;
}

.user-badge {
  margin-bottom: 12px;
}

.badge-container {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 16px;
  background: rgba(110, 107, 169, 0.9);
  border: 1px solid #D8D8D8;
  border-radius: 24px;
  backdrop-filter: blur(4px);
  width: fit-content;
}

.badge-icon {
  width: 28px;
  height: 28px;
}

.badge-text {
  color: #FAFAFA;
  font-size: 14px;
  font-weight: 500;
}

.user-name {
  color: white;
  font-size: 20px;
  font-weight: 700;
  line-height: 1.2;
  margin: 0;
}

.close-button {
  width: 44px;
  height: 44px;
  background: #EFEEFF;
  border: 1px solid #2019CE;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  cursor: pointer;
  transition: all 0.2s ease;
  outline: none;
  -webkit-tap-highlight-color: transparent;
}

.close-button:hover {
  background: #E5E7EB;
}

.close-button:active {
  transform: scale(0.95);
}

/* Menu Section */
.menu-section {
  position: relative;
  flex: 1;
  overflow: hidden;
  padding: 0 12px;
  min-height: 80px;
  max-height: calc(100vh - 280px);
}

.scrollbar-indicator {
  position: absolute;
  right: 4px;
  top: 8px;
  width: 2px;
  height: 60px;
  background: rgba(183, 183, 183, 0.4);
  border-radius: 2px;
  opacity: 0.4;
  z-index: 10;
}

.menu-items {
  height: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  padding-right: 8px;
  padding-bottom: 8px;
  -webkit-overflow-scrolling: touch;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
  touch-action: pan-y;
  scrollbar-width: none;
  -ms-overflow-style: none;
  scroll-snap-type: y proximity;
}

.menu-items::-webkit-scrollbar {
  display: none;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 6px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
  outline: none;
  -webkit-tap-highlight-color: transparent;
  scroll-snap-align: start;
}

.menu-item:hover {
  background: rgba(255, 255, 255, 0.1);
}

.menu-item:active {
  background: rgba(255, 255, 255, 0.15);
  transform: scale(0.98);
}

.menu-icon {
  width: 40px;
  height: 40px;
  background: rgba(64, 64, 64, 0.24);
  border: 1px solid rgba(255, 255, 255, 0.24);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.menu-text {
  color: white;
  font-weight: 600;
  font-size: 16px;
  flex: 1;
}

.verification-badge {
  width: 24px;
  height: 24px;
  background: #FFF0F3;
  border: 1px solid #FF1919;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

/* Upgrade Section */
.upgrade-section {
  padding: 8px 12px;
  flex-shrink: 0;
}

.upgrade-card {
  background: #F1E7FF;
  border: 1px solid #DCCCF1;
  border-radius: 16px;
  padding: 16px;
  position: relative;
  overflow: hidden;
}

.upgrade-star {
  position: absolute;
  left: 12px;
  top: 16px;
}

.star-icon {
  width: 32px;
  height: 32px;
}

.upgrade-gradient {
  position: absolute;
  left: 0;
  top: 0;
  width: 160px;
  height: 100%;
  background: linear-gradient(90deg, rgba(140, 76, 209, 0.4) 0%, transparent 100%);
  border-radius: 16px 0 0 16px;
}

.upgrade-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  z-index: 10;
}

.upgrade-info {
  margin-left: 44px;
}

.upgrade-title {
  color: #02070E;
  font-weight: 700;
  font-size: 18px;
  margin-bottom: 2px;
}

.upgrade-subtitle {
  font-size: 13px;
  color: #4B4D50;
  line-height: 1.3;
}

.upgrade-number {
  font-weight: 700;
  color: #8C4CD1;
}

.upgrade-button {
  padding: 10px 20px;
  background: linear-gradient(90deg, #2019CE 0%, #473FFF 100%);
  color: white;
  font-weight: 600;
  border-radius: 20px;
  font-size: 14px;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(32, 25, 206, 0.25);
  flex-shrink: 0;
  outline: none;
  -webkit-tap-highlight-color: transparent;
}

.upgrade-button:hover {
  box-shadow: 0 6px 16px rgba(32, 25, 206, 0.35);
  transform: translateY(-1px);
}

.upgrade-button:active {
  transform: translateY(0) scale(0.98);
}

/* Bottom Section */
.bottom-section {
  padding: 8px 12px;
  flex-shrink: 0;
  background: rgba(255, 255, 255, 0.05);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  min-height: 56px;
}

.bottom-controls {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  max-width: 300px;
  margin: 0 auto;
}

/* ID Container */
.id-container {
  position: relative;
  flex: 1;
}

.id-button {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 14px;
  transition: all 0.25s ease;
  width: 100%;
  height: 36px;
  cursor: pointer;
  outline: none;
  -webkit-tap-highlight-color: transparent;
}

.id-button:hover {
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.3);
}

.id-button:active {
  transform: scale(0.97);
}

.id-content {
  display: flex;
  align-items: center;
  gap: 4px;
  flex: 1;
  min-width: 0;
}

.id-label {
  color: #B7B7B7;
  font-size: 14px;
  font-weight: 500;
  white-space: nowrap;
}

.id-value {
  color: white;
  font-size: 14px;
  font-weight: 600;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}

.copy-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 18px;
  height: 18px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 5px;
  flex-shrink: 0;
  transition: all 0.2s ease;
}

.id-button:hover .copy-icon {
  background: rgba(255, 255, 255, 0.3);
}

.copy-toast {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border-radius: 16px;
  padding: 10px 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  z-index: 20;
  box-shadow: 0 8px 20px rgba(16, 185, 129, 0.4);
}

.toast-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 18px;
  height: 18px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  flex-shrink: 0;
}

.toast-text {
  color: white;
  font-weight: 600;
  font-size: 14px;
}

/* Language Container */
.language-container {
  position: relative;
  flex: 1;
}

.language-button {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 14px;
  transition: all 0.25s ease;
  width: 100%;
  height: 36px;
  cursor: pointer;
  outline: none;
  -webkit-tap-highlight-color: transparent;
}

.language-button:hover {
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.3);
}

.language-button:active {
  transform: scale(0.97);
}

.flag-wrapper {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  flex-shrink: 0;
}

.language-text {
  color: white;
  font-size: 14px;
  font-weight: 600;
  flex: 1;
  text-align: left;
}

.arrow-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 18px;
  height: 18px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 5px;
  flex-shrink: 0;
  transition: all 0.2s ease;
}

.language-button:hover .arrow-wrapper {
  background: rgba(255, 255, 255, 0.3);
}

.arrow-icon {
  transition: transform 0.3s ease;
}

/* Language Dropdown */
.language-dropdown {
  position: absolute;
  bottom: 100%;
  left: 0;
  right: 0;
  margin-bottom: 8px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 12px;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  z-index: 50;
  max-height: 150px;
}

.dropdown-content {
  padding: 8px;
  max-height: 134px;
  overflow-y: auto;
  overflow-x: hidden;
  scrollbar-width: thin;
  scrollbar-color: rgba(32, 25, 206, 0.3) transparent;
}

.dropdown-content::-webkit-scrollbar {
  width: 4px;
}

.dropdown-content::-webkit-scrollbar-track {
  background: transparent;
}

.dropdown-content::-webkit-scrollbar-thumb {
  background: rgba(32, 25, 206, 0.3);
  border-radius: 2px;
}

.dropdown-content::-webkit-scrollbar-thumb:hover {
  background: rgba(32, 25, 206, 0.5);
}

.dropdown-item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px;
  border-radius: 12px;
  transition: all 0.2s ease;
  text-align: left;
  border: none;
  background: none;
  cursor: pointer;
  outline: none;
  -webkit-tap-highlight-color: transparent;
}

.dropdown-item-active {
  background: linear-gradient(90deg, rgba(32, 25, 206, 0.2) 0%, rgba(147, 51, 234, 0.2) 100%);
  color: #2019CE;
}

.dropdown-item-inactive {
  color: #374151;
}

.dropdown-item-inactive:hover {
  background: linear-gradient(90deg, rgba(32, 25, 206, 0.1) 0%, rgba(147, 51, 234, 0.1) 100%);
  color: #1F2937;
}

.dropdown-flag {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.dropdown-text {
  font-size: 14px;
  font-weight: 500;
  transition: color 0.2s ease;
}

.dropdown-indicator {
  margin-left: auto;
  width: 8px;
  height: 8px;
  background: #2019CE;
  border-radius: 50%;
}

/* Unified responsive design - one design scaled for all screens */

/* Base/Mobile First - 320px+ */
.profile-container {
  left: 16px;
  right: 16px;
  top: 40px;
  bottom: calc(180px + env(safe-area-inset-bottom, 0));
  border-radius: 24px;
  max-height: calc(100vh - 220px - env(safe-area-inset-bottom, 0));
}

.overlay-pointer {
  bottom: calc(170px + env(safe-area-inset-bottom, 0));
  left: 32px;
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  border-top: 12px solid #120B81;
}

.profile-header {
  padding: 12px;
}

.profile-card {
  padding: 16px;
  border-radius: 50px 20px 20px 50px;
}

.profile-content {
  gap: 16px;
}

.avatar-frame {
  width: 80px;
  height: 80px;
}

.badge-container {
  padding: 6px 16px;
}

.badge-icon {
  width: 28px;
  height: 28px;
}

.badge-text {
  font-size: 14px;
}

.user-name {
  font-size: 20px;
}

.close-button {
  width: 44px;
  height: 44px;
}

.menu-section {
  padding: 0 12px;
  min-height: 200px;
  max-height: calc(100vh - 400px);
}

.menu-item {
  padding: 12px 6px;
  gap: 12px;
}

.menu-icon {
  width: 40px;
  height: 40px;
}

.menu-text {
  font-size: 16px;
}

.verification-badge {
  width: 24px;
  height: 24px;
}

.upgrade-section {
  padding: 8px 12px;
}

.upgrade-card {
  padding: 16px;
  border-radius: 16px;
}

.upgrade-star {
  left: 12px;
  top: 16px;
}

.star-icon {
  width: 32px;
  height: 32px;
}

.upgrade-info {
  margin-left: 44px;
}

.upgrade-title {
  font-size: 18px;
  margin-bottom: 2px;
}

.upgrade-subtitle {
  font-size: 13px;
}

.upgrade-button {
  padding: 10px 20px;
  font-size: 14px;
  border-radius: 20px;
}

.bottom-section {
  padding: 8px 12px;
  min-height: 56px;
}

.bottom-controls {
  gap: 12px;
  max-width: 300px;
}

.id-button,
.language-button {
  height: 36px;
  padding: 8px 12px;
  border-radius: 14px;
}

.id-label,
.id-value,
.language-text {
  font-size: 14px;
}

.copy-icon {
  width: 18px;
  height: 18px;
}

.flag-wrapper {
  width: 22px;
  height: 22px;
}

.arrow-wrapper {
  width: 18px;
  height: 18px;
}

/* Small screens scale down */
@media (max-width: 360px) {
  .profile-container {
    left: 12px;
    right: 12px;
    top: 30px;
    border-radius: 20px;
  }

  .overlay-pointer {
    left: 24px;
    border-left-width: 10px;
    border-right-width: 10px;
    border-top-width: 10px;
  }

  .profile-header { padding: 10px; }
  .profile-card { padding: 14px; border-radius: 45px 18px 18px 45px; }
  .profile-content { gap: 14px; }
  .avatar-frame { width: 70px; height: 70px; }
  .badge-container { padding: 5px 14px; }
  .badge-icon { width: 26px; height: 26px; }
  .badge-text { font-size: 13px; }
  .user-name { font-size: 18px; }
  .close-button { width: 40px; height: 40px; }
  .menu-section { padding: 0 10px; min-height: 180px; max-height: calc(100vh - 380px); }
  .menu-item { padding: 10px 5px; gap: 10px; }
  .menu-icon { width: 36px; height: 36px; }
  .menu-text { font-size: 15px; }
  .verification-badge { width: 22px; height: 22px; }
  .upgrade-section { padding: 7px 10px; }
  .upgrade-card { padding: 14px; border-radius: 14px; }
  .upgrade-star { left: 10px; top: 14px; }
  .star-icon { width: 28px; height: 28px; }
  .upgrade-info { margin-left: 38px; }
  .upgrade-title { font-size: 16px; }
  .upgrade-subtitle { font-size: 12px; }
  .upgrade-button { padding: 9px 18px; font-size: 13px; border-radius: 18px; }
  .bottom-section { padding: 7px 10px; }
  .bottom-controls { gap: 10px; max-width: 270px; }
  .id-button, .language-button { height: 32px; padding: 6px 10px; border-radius: 12px; }
  .id-label, .id-value, .language-text { font-size: 13px; }
  .copy-icon { width: 16px; height: 16px; }
  .flag-wrapper { width: 20px; height: 20px; }
  .arrow-wrapper { width: 16px; height: 16px; }
}

/* Large screens scale up */
@media (min-width: 480px) {
  .profile-container {
    left: 20px;
    right: 20px;
    top: 50px;
    border-radius: 28px;
    max-width: 400px;
    margin: 0 auto;
  }

  .overlay-pointer {
    left: 50%;
    transform: translateX(-50%);
    border-left-width: 14px;
    border-right-width: 14px;
    border-top-width: 14px;
  }

  .profile-header { padding: 16px; }
  .profile-card { padding: 20px; border-radius: 55px 22px 22px 55px; }
  .profile-content { gap: 20px; }
  .avatar-frame { width: 90px; height: 90px; }
  .badge-container { padding: 8px 18px; }
  .badge-icon { width: 30px; height: 30px; }
  .badge-text { font-size: 15px; }
  .user-name { font-size: 22px; }
  .close-button { width: 48px; height: 48px; }
  .menu-section { padding: 0 16px; min-height: 220px; max-height: calc(100vh - 440px); }
  .menu-item { padding: 14px 8px; gap: 14px; }
  .menu-icon { width: 44px; height: 44px; }
  .menu-text { font-size: 17px; }
  .verification-badge { width: 26px; height: 26px; }
  .upgrade-section { padding: 10px 16px; }
  .upgrade-card { padding: 18px; border-radius: 18px; }
  .upgrade-star { left: 16px; top: 18px; }
  .star-icon { width: 34px; height: 34px; }
  .upgrade-info { margin-left: 50px; }
  .upgrade-title { font-size: 20px; margin-bottom: 3px; }
  .upgrade-subtitle { font-size: 14px; }
  .upgrade-button { padding: 12px 24px; font-size: 15px; border-radius: 22px; }
  .bottom-section { padding: 10px 16px; }
  .bottom-controls { gap: 14px; max-width: 320px; }
  .id-button, .language-button { height: 40px; padding: 10px 14px; border-radius: 16px; }
  .id-label, .id-value, .language-text { font-size: 15px; }
  .copy-icon { width: 20px; height: 20px; }
  .flag-wrapper { width: 26px; height: 26px; }
  .arrow-wrapper { width: 20px; height: 20px; }
}

/* Landscape mode - compact everything */
@media (max-height: 500px) and (orientation: landscape) {
  .profile-container {
    top: 20px;
    bottom: calc(140px + env(safe-area-inset-bottom, 0));
    border-radius: 18px;
    max-height: calc(100vh - 160px - env(safe-area-inset-bottom, 0));
  }

  .overlay-pointer {
    bottom: calc(130px + env(safe-area-inset-bottom, 0));
    border-left-width: 8px;
    border-right-width: 8px;
    border-top-width: 8px;
  }

  .profile-header { padding: 8px; }
  .profile-card { padding: 10px; border-radius: 35px 14px 14px 35px; }
  .profile-content { gap: 10px; }
  .avatar-frame { width: 50px; height: 50px; }
  .badge-container { padding: 3px 8px; }
  .badge-icon { width: 20px; height: 20px; }
  .badge-text { font-size: 11px; }
  .user-name { font-size: 15px; }
  .close-button { width: 32px; height: 32px; }
  .menu-section { padding: 0 8px; min-height: 80px; max-height: calc(100vh - 220px); }
  .menu-item { padding: 6px 4px; gap: 8px; }
  .menu-icon { width: 28px; height: 28px; }
  .menu-text { font-size: 12px; }
  .verification-badge { width: 18px; height: 18px; }
  .upgrade-section { padding: 5px 8px; }
  .upgrade-card { padding: 10px; border-radius: 12px; }
  .upgrade-star { left: 8px; top: 10px; }
  .star-icon { width: 22px; height: 22px; }
  .upgrade-info { margin-left: 30px; }
  .upgrade-title { font-size: 14px; margin-bottom: 1px; }
  .upgrade-subtitle { font-size: 10px; }
  .upgrade-button { padding: 6px 12px; font-size: 11px; border-radius: 14px; }
  .bottom-section { padding: 5px 8px; }
  .bottom-controls { gap: 8px; max-width: 250px; }
  .id-button, .language-button { height: 28px; padding: 5px 8px; border-radius: 10px; }
  .id-label, .id-value, .language-text { font-size: 11px; }
  .copy-icon { width: 14px; height: 14px; }
  .flag-wrapper { width: 18px; height: 18px; }
  .arrow-wrapper { width: 14px; height: 14px; }
}

/* Touch optimizations */
@media (hover: none) and (pointer: coarse) {
  .menu-item:hover {
    background: rgba(255, 255, 255, 0.05);
  }

  .close-button:hover,
  .id-button:hover,
  .language-button:hover,
  .upgrade-button:hover {
    transform: none;
  }

  .close-button:active,
  .id-button:active,
  .language-button:active,
  .upgrade-button:active {
    transform: scale(0.96);
  }
}



/* iPhone 14 Pro Max and similar with large safe areas */
@media (min-width: 428px) and (min-height: 926px) {
  .profile-container {
    bottom: calc(82px + env(safe-area-inset-bottom, 0));
    max-height: calc(100vh - 142px - env(safe-area-inset-bottom, 0));
  }

  .overlay-pointer {
    bottom: calc(72px + env(safe-area-inset-bottom, 0));
  }
}

/* Very small screens with safe areas */
@media (max-width: 320px) {
  .profile-container {
    left: 4px;
    right: 4px;
    top: 16px;
    bottom: calc(60px + env(safe-area-inset-bottom, 0));
    max-height: calc(100vh - 76px - env(safe-area-inset-bottom, 0));
  }

  .overlay-pointer {
    bottom: calc(50px + env(safe-area-inset-bottom, 0));
    left: 20px;
  }
}

/* Performance optimizations */
.profile-container,
.close-button,
.menu-item,
.id-button,
.language-button,
.upgrade-button {
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Telegram WebApp specific optimizations */
* {
  -webkit-tap-highlight-color: transparent;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Allow text selection for specific elements */
.user-name,
.id-value {
  -webkit-user-select: text;
  -moz-user-select: text;
  -ms-user-select: text;
  user-select: text;
}

/* Overlay animations */
.profile-overlay-enter-active {
  transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.profile-overlay-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.6, 1);
}

.profile-overlay-enter-from {
  opacity: 0;
  transform: translateY(100%);
}

.profile-overlay-enter-to {
  opacity: 1;
  transform: translateY(0);
}

.profile-overlay-leave-from {
  opacity: 1;
  transform: translateY(0);
}

.profile-overlay-leave-to {
  opacity: 0;
  transform: translateY(100%);
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
</style>
