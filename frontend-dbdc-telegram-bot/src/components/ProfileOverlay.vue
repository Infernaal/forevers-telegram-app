<template>
  <div v-if="isVisible" class="profile-overlay">
    <!-- Triangle Pointer -->
    <div class="triangle-pointer">
      <div class="triangle-shape"></div>
    </div>

    <!-- Profile Dropdown Menu -->
    <div class="profile-dropdown" @click.stop>
      <!-- Background -->
      <div class="dropdown-background"></div>

      <!-- Profile Header Section -->
      <div class="profile-header-section">
        <div class="profile-header-container">
          <!-- Avatar -->
          <div class="profile-avatar">
            <img src="https://images.pexels.com/photos/15023413/pexels-photo-15023413.jpeg?auto=compress&cs=tinysrgb&w=400" alt="Jason Williams" class="avatar-img" />
          </div>

          <!-- User Info -->
          <div class="profile-user-info">
            <!-- Silver Badge -->
            <div class="silver-badge-container">
              <div class="silver-badge-icon">
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
              <span class="silver-badge-text">Silver</span>
            </div>

            <!-- User Name -->
            <h2 class="profile-user-name">Jason Williams</h2>
          </div>

          <!-- Arrow Button -->
          <button class="profile-arrow-btn" @click="$emit('close')">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path d="M17.2155 11.2862L8.2216 2.29534C7.82696 1.90169 7.18757 1.90169 6.79192 2.29534C6.39728 2.68898 6.39728 3.32838 6.79192 3.72203L15.0724 11.9996L6.79292 20.2771C6.39827 20.6707 6.39827 21.3101 6.79292 21.7048C7.18756 22.0984 7.82795 22.0984 8.2226 21.7048L17.2165 12.7139C17.6051 12.3244 17.6051 11.6749 17.2155 11.2862Z" fill="#B7B7B7"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- Menu Items -->
      <div class="menu-container">
        <!-- Calculator -->
        <div class="menu-item" @click="handleMenuClick('calculator')">
          <div class="menu-icon-circle">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 16 20" fill="none">
                <path d="M14.1377 0C15.1645 0 16 0.788555 16 1.75781V18.2422C16 19.2114 15.1645 20 14.1377 20H1.8623C0.835502 20 0 19.2114 0 18.2422V1.75781C0 0.788555 0.835502 0 1.8623 0H14.1377ZM1.8623 1.17188C1.52004 1.17188 1.24121 1.43473 1.24121 1.75781V18.2422C1.24121 18.5653 1.52004 18.8281 1.8623 18.8281H14.1377C14.48 18.8281 14.7587 18.5653 14.7588 18.2422V1.75781C14.7588 1.43473 14.48 1.17188 14.1377 1.17188H1.8623ZM5.06445 14.5947C5.40691 14.595 5.68443 14.8573 5.68457 15.1807V16.9668C5.6844 17.2901 5.40693 17.5525 5.06445 17.5527H2.88477C2.54207 17.5527 2.26385 17.2903 2.26367 16.9668V15.1807C2.26381 14.8572 2.54205 14.5947 2.88477 14.5947H5.06445ZM13.1152 14.5947C13.4578 14.5949 13.7353 14.8573 13.7354 15.1807V16.9668C13.7352 17.2901 13.4577 17.5525 13.1152 17.5527H6.91016C6.56746 17.5527 6.28924 17.2903 6.28906 16.9668V15.1807C6.2892 14.8572 6.56744 14.5947 6.91016 14.5947H13.1152ZM3.50488 16.3809H4.44336V15.7666H3.50488V16.3809ZM7.53027 16.3809H12.4941V15.7666H7.53027V16.3809ZM5.06445 11.1709C5.40699 11.1711 5.68457 11.4334 5.68457 11.7568V13.542C5.68457 13.8654 5.40704 14.1277 5.06445 14.1279H2.88477C2.54196 14.1279 2.26367 13.8656 2.26367 13.542V11.7568C2.26367 11.4332 2.54196 11.1709 2.88477 11.1709H5.06445ZM9.08984 11.1709C9.43238 11.1711 9.70996 11.4334 9.70996 11.7568V13.542C9.70996 13.8654 9.43243 14.1277 9.08984 14.1279H6.91016C6.56735 14.1279 6.28906 13.8656 6.28906 13.542V11.7568C6.28906 11.4332 6.56735 11.1709 6.91016 11.1709H9.08984ZM13.1152 11.1709C13.4578 11.1711 13.7354 11.4334 13.7354 11.7568V13.542C13.7354 13.8654 13.4578 14.1277 13.1152 14.1279H10.9355C10.5927 14.1279 10.3145 13.8656 10.3145 13.542V11.7568C10.3145 11.4332 10.5927 11.1709 10.9355 11.1709H13.1152ZM3.50488 12.9561H4.44336V12.3428H3.50488V12.9561ZM7.53027 12.9561H8.46875V12.3428H7.53027V12.9561ZM11.5557 12.9561H12.4941V12.3428H11.5557V12.9561ZM5.06445 7.74609C5.40691 7.74634 5.68443 8.00866 5.68457 8.33203V10.1182C5.6844 10.4415 5.40693 10.7039 5.06445 10.7041H2.88477C2.54207 10.7041 2.26385 10.4416 2.26367 10.1182V8.33203C2.26381 8.00855 2.54205 7.74609 2.88477 7.74609H5.06445ZM9.08984 7.74609C9.4323 7.74634 9.70982 8.0087 9.70996 8.33203V10.1182C9.70979 10.4415 9.43232 10.7039 9.08984 10.7041H6.91016C6.56746 10.7041 6.28924 10.4416 6.28906 10.1182V8.33203C6.2892 8.00855 6.56744 7.74609 6.91016 7.74609H9.08984ZM13.1152 7.74609C13.4577 7.74634 13.7352 8.00866 13.7354 8.33203V10.1182C13.7352 10.4415 13.4577 10.7039 13.1152 10.7041H10.9355C10.5928 10.7041 10.3146 10.4416 10.3145 10.1182V8.33203C10.3146 8.00855 10.5928 7.74609 10.9355 7.74609H13.1152ZM3.50488 9.53223H4.44336V8.91797H3.50488V9.53223ZM7.53027 9.53223H8.46875V8.91797H7.53027V9.53223ZM11.5557 9.53223H12.4941V8.91797H11.5557V9.53223ZM13.1416 2.39648C13.7575 2.39666 14.2588 2.86972 14.2588 3.45117V5.23828C14.2588 5.81971 13.7575 6.29278 13.1416 6.29297H3.02441C2.40839 6.29291 1.90725 5.81979 1.90723 5.23828V3.45117C1.90723 2.86965 2.40838 2.39654 3.02441 2.39648H13.1416ZM3.14844 3.56836V5.12109H13.0166V3.56836H3.14844Z" fill="white"/>
              </svg>
            </div>
          </div>
          <span class="menu-label">Calculator</span>
        </div>

        <!-- Ambassador -->
        <div class="menu-item" @click="handleMenuClick('ambassador')">
          <div class="menu-icon-circle">
            <div class="menu-icon">
              <svg width="14" height="20" viewBox="0 0 14 20" fill="none">
                <path d="M7 9.64844C9.76508 9.64858 12.0066 11.9652 12.0068 14.8242C12.0068 17.6826 9.76511 19.9999 7 20C4.23394 20 1.99219 17.6827 1.99219 14.8242C1.99243 11.9651 4.23409 9.64844 7 9.64844ZM6.09668 13.8418L4.07715 14.1465L5.53906 15.6182L5.19434 17.6992L7 16.7168L8.80566 17.6992L8.46191 15.6182L9.92383 14.1465L7.90332 13.8418L7 11.9512L6.09668 13.8418ZM4.60547 0L7 3.30078L9.39453 0H14L7 9.64844L0 0H4.60547Z" fill="white"/>
              </svg>
            </div>
          </div>
          <span class="menu-label">Ambassador</span>
        </div>

        <!-- Verification -->
        <div class="menu-item" @click="handleMenuClick('verification')">
          <div class="menu-icon-circle">
            <div class="menu-icon">
              <svg width="18" height="22" viewBox="0 0 18 22" fill="none">
                <path d="M14.2511 12.4974C15.4932 12.4974 16.5 13.5045 16.5 14.7467V15.3222C16.5 16.2166 16.1805 17.0816 15.5989 17.7611C14.0295 19.5949 11.6422 20.5 8.49673 20.5C5.35076 20.5 2.96466 19.5946 1.39831 17.7601C0.818531 17.081 0.5 16.2174 0.5 15.3245V14.7467C0.5 13.5045 1.50689 12.4974 2.74896 12.4974H14.2511ZM14.2511 13.9977H2.74896C2.33534 13.9977 2.00005 14.333 2.00005 14.7467V15.3245C2.00005 15.8602 2.19117 16.3784 2.53904 16.7858C3.79239 18.2538 5.75834 18.9997 8.49673 18.9997C11.2351 18.9997 13.2028 18.2537 14.4593 16.7855C14.8082 16.3779 14.9999 15.8589 14.9999 15.3222V14.7467C14.9999 14.333 14.6647 13.9977 14.2511 13.9977ZM8.49673 0.5C11.2582 0.5 13.4969 2.73897 13.4969 5.50088C13.4969 8.2628 11.2582 10.5017 8.49673 10.5017C5.73521 10.5017 3.49656 8.2628 3.49656 5.50088C3.49656 2.73897 5.73521 0.5 8.49673 0.5ZM8.49673 2.00026C6.56366 2.00026 4.99661 3.56755 4.99661 5.50088C4.99661 7.43422 6.56366 9.00148 8.49673 9.00148C10.4298 9.00148 11.9968 7.43422 11.9968 5.50088C11.9968 3.56755 10.4298 2.00026 8.49673 2.00026Z" fill="white"/>
              </svg>
            </div>
          </div>
          <span class="menu-label">Verification</span>
          <!-- Error Badge -->
          <div class="error-badge">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
              <path d="M14.9228 7.16821C14.7585 6.94745 14.6305 6.70193 14.5436 6.4409C14.5201 6.18054 14.5379 5.91813 14.5962 5.66333C14.7477 5.12283 14.7046 4.54628 14.4744 4.0341C14.1456 3.57863 13.6671 3.25299 13.1226 3.11407C12.8728 3.03698 12.6365 2.92116 12.4226 2.77084C12.2398 2.5653 12.0911 2.33194 11.9819 2.07958C11.7892 1.56689 11.4246 1.13678 10.9502 0.862631C10.4256 0.692048 9.8579 0.709823 9.34519 0.912887C9.08843 0.99967 8.81951 1.04525 8.54844 1.04795C8.28733 0.989378 8.03727 0.889426 7.80776 0.751882C7.34444 0.444166 6.78837 0.307359 6.23518 0.364993C5.72041 0.534107 5.28002 0.875815 4.98858 1.33226C4.82575 1.56079 4.62746 1.76187 4.40119 1.92794C4.14391 2.04102 3.87014 2.11219 3.5903 2.13875C3.04904 2.16266 2.53279 2.37289 2.12909 2.73379C1.80194 3.18287 1.64241 3.73224 1.67814 4.28669C1.68201 4.55398 1.64344 4.82018 1.56385 5.07536C1.42625 5.30891 1.25231 5.51905 1.04854 5.6979C0.616901 6.04079 0.317739 6.52274 0.202076 7.06155C0.203417 7.60886 0.394039 8.13897 0.741655 8.56208C0.905939 8.78283 1.03392 9.02836 1.12078 9.28939C1.14429 9.54974 1.12656 9.81216 1.06823 10.067C0.916691 10.6074 0.959774 11.184 1.18997 11.6962C1.51892 12.1515 1.99733 12.4771 2.54179 12.6162C2.79166 12.6933 3.02788 12.8091 3.24182 12.9594C3.42458 13.165 3.57336 13.3983 3.68254 13.6507C3.87516 14.1634 4.23981 14.5935 4.71426 14.8676C4.77988 14.8969 4.84771 14.9209 4.91712 14.9394C5.38717 15.022 5.87062 14.9799 6.31921 14.8174C6.57597 14.7306 6.84489 14.685 7.11596 14.6823C7.37691 14.7414 7.62688 14.8413 7.85663 14.9784C8.32008 15.2858 8.87605 15.4226 9.42921 15.3653C9.94398 15.1962 10.3844 14.8545 10.6758 14.398C10.8386 14.1695 11.0369 13.9684 11.2632 13.8023C11.5205 13.6892 11.7943 13.6181 12.0741 13.5915C12.6154 13.5676 13.1316 13.3574 13.5353 12.9965C13.8625 12.5474 14.022 11.998 13.9863 11.4436C13.9824 11.1763 14.021 10.9101 14.1005 10.6549C14.2381 10.4214 14.4121 10.2112 14.6158 10.0324C15.0475 9.6895 15.3466 9.20755 15.4623 8.66874C15.461 8.12143 15.2704 7.59133 14.9228 7.16821Z" fill="#FF1919"/>
              <path d="M15.1261 9.67421L9.56268 15.2377C9.28451 15.5158 8.91361 15.5158 8.63544 15.2377C8.35726 14.9595 8.35726 14.5886 8.63544 14.3104L14.1989 8.74697C14.4771 8.46879 14.848 8.46879 15.1261 8.74697C15.4043 9.02514 15.4043 9.39604 15.1261 9.67421Z" fill="white"/>
              <path d="M15.1262 15.2377C14.848 15.5158 14.4771 15.5158 14.199 15.2377L8.6355 9.67419C8.35732 9.39602 8.35732 9.02512 8.6355 8.74695C8.91367 8.46878 9.28457 8.46878 9.56274 8.74695L15.1262 14.3104C15.4044 14.5886 15.4044 14.9595 15.1262 15.2377Z" fill="white"/>
            </svg>
          </div>
        </div>

        <!-- Security -->
        <div class="menu-item" @click="handleMenuClick('security')">
          <div class="menu-icon-circle">
            <div class="menu-icon">
              <svg width="18" height="20" viewBox="0 0 18 20" fill="none">
                <path d="M8.78516 0.0354746C8.92389 -0.0121504 9.07611 -0.0121504 9.21484 0.0354746C10.6561 0.531013 12.1438 0.945188 13.6377 1.26497C14.8838 1.5317 16.1601 1.73823 17.4297 1.87922C17.7546 1.91522 18 2.18263 18 2.50032V8.7386C17.9998 13.165 15.3282 17.2234 11.1943 19.0784L9.26953 19.9427C9.18416 19.9808 9.09193 20.0003 9 20.0003C8.90802 20.0003 8.81583 19.9808 8.73047 19.9427L6.80566 19.0784C2.67178 17.2233 0.000192532 13.165 0 8.7386V2.50032C0 2.18263 0.245411 1.91529 0.570312 1.87922C1.83994 1.73823 3.11627 1.53164 4.3623 1.26497C5.85626 0.945192 7.34396 0.531005 8.78516 0.0354746ZM9 1.28743C7.57623 1.76779 6.10923 2.17074 4.6377 2.48567C3.53526 2.72147 2.41054 2.91243 1.28613 3.05403V8.7386C1.28633 12.6791 3.6638 16.2924 7.34375 17.9437L9 18.6868L10.6562 17.9437C14.3362 16.2924 16.7137 12.6792 16.7139 8.7386V3.05403C15.5895 2.91243 14.4647 2.72154 13.3623 2.48567C11.8907 2.17074 10.4239 1.7678 9 1.28743ZM9 4.37532C10.4179 4.37532 11.5713 5.49682 11.5713 6.87532V7.50032L11.7021 7.50618C12.3499 7.57014 12.8564 8.10392 12.8564 8.75032V13.1253C12.8563 13.8145 12.2802 14.3753 11.5713 14.3753H6.42871C5.71976 14.3753 5.14277 13.8145 5.14258 13.1253V8.75032C5.14258 8.10406 5.64931 7.57034 6.29688 7.50618L6.42871 7.50032V6.87532C6.42871 5.49687 7.58218 4.3754 9 4.37532ZM6.42871 13.1253H11.5723L11.5713 8.75032H6.42871V13.1253ZM9 5.62532C8.29099 5.6254 7.71484 6.18599 7.71484 6.87532V7.50032H10.2861V6.87532C10.2861 6.18594 9.70907 5.62532 9 5.62532Z" fill="white"/>
              </svg>
            </div>
          </div>
          <span class="menu-label">Security</span>
        </div>

        <!-- Settings -->
        <div class="menu-item" @click="handleMenuClick('settings')">
          <div class="menu-icon-circle">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M12.2222 20L12.3457 19.375L12.8148 17.0913C13.5679 16.8029 14.2469 16.3972 14.8642 15.9135L17.1605 16.6827L17.7778 16.875L18.0988 16.3221L19.679 13.6778L20 13.125L19.5309 12.7163L17.7531 11.2019C17.8179 10.8083 17.9012 10.4147 17.9012 10C17.9012 9.58531 17.8179 9.19169 17.7531 8.79808L19.5309 7.28369L20 6.875L19.679 6.32215L18.0988 3.67785L17.7778 3.125L17.1605 3.31731L14.8642 4.08654C14.2469 3.60277 13.5679 3.19708 12.8148 2.90862L12.3457 0.625L12.2222 0H7.77775L7.65426 0.625L7.18516 2.90862C6.43209 3.19708 5.75306 3.60277 5.13581 4.08654L2.83947 3.31731L2.22215 3.125L1.9012 3.67785L0.32095 6.32215L0 6.875L0.469097 7.28369L2.24688 8.79808C2.18209 9.19169 2.09873 9.58531 2.09873 10C2.09873 10.4147 2.18209 10.8083 2.24688 11.2019L0.469097 12.7163L0 13.125L0.32095 13.6778L1.9012 16.3221L2.22215 16.875L2.83947 16.6827L5.13581 15.9135C5.75306 16.3972 6.43209 16.8029 7.18516 17.0913L7.65426 19.375L7.77775 20H12.2222ZM10.9383 18.4615H9.06171L8.66664 16.4663L8.56788 16.0096L8.12343 15.8654C7.2253 15.5919 6.41044 15.1292 5.72841 14.5192L5.38265 14.2068L4.93828 14.3509L2.93824 15.024L1.99996 13.4615L3.58022 12.0914L3.95062 11.8029L3.82713 11.3462C3.72528 10.9075 3.67898 10.4598 3.67898 10C3.67898 9.54023 3.72528 9.09254 3.82713 8.65385L3.92589 8.19708L3.58022 7.90862L1.99996 6.53846L2.93824 4.976L4.93828 5.64908L5.38265 5.79323L5.72841 5.48077C6.41044 4.87077 7.2253 4.40808 8.12343 4.13461L8.56788 3.99039L8.66664 3.53369L9.06171 1.53846H10.9383L11.3333 3.53369L11.4321 3.99039L11.8765 4.13461C12.7747 4.40808 13.5895 4.87077 14.2716 5.48077L14.6173 5.79323L15.0617 5.64908L17.0617 4.976L18 6.53846L16.4197 7.90862L16.0494 8.19708L16.1728 8.65385C16.2747 9.09254 16.321 9.54023 16.321 10C16.321 10.4598 16.2747 10.9075 16.1728 11.3462L16.0494 11.8029L16.4197 12.0914L18 13.4615L17.0617 15.024L15.0617 14.3509L14.6173 14.2068L14.2716 14.5192C13.5895 15.1292 12.7747 15.5919 11.8765 15.8654L11.4321 16.0096L11.3333 16.4663L10.9383 18.4615ZM9.99998 13.8462C12.1728 13.8462 13.9506 12.1154 13.9506 10C13.9506 7.88461 12.1728 6.15385 9.99998 6.15385C7.82714 6.15385 6.04936 7.88461 6.04936 10C6.04936 12.1154 7.82714 13.8462 9.99998 13.8462ZM9.99998 12.3077C8.68205 12.3077 7.62961 11.2831 7.62961 10C7.62961 8.71692 8.68205 7.69231 9.99998 7.69231C11.3179 7.69231 12.3704 8.71692 12.3704 10C12.3704 11.2831 11.3179 12.3077 9.99998 12.3077Z" fill="white"/>
              </svg>
            </div>
          </div>
          <span class="menu-label">Settings</span>
        </div>

        <!-- Support -->
        <div class="menu-item" @click="handleMenuClick('support')">
          <div class="menu-icon-circle">
            <div class="menu-icon">
              <svg width="18" height="20" viewBox="0 0 18 20" fill="none">
                <path d="M8.99902 0C13.9325 0 17.998 3.80872 17.998 8.58691V10.1348C17.9981 10.1411 17.999 10.1479 17.999 10.1543V12.9561C17.9992 12.9624 18 12.9692 18 12.9756V14.543C17.9997 16.724 16.1499 18.4277 13.9502 18.4277H11.2695C10.9422 19.3551 10.0281 19.9951 8.99902 19.9951C7.71066 19.9949 6.59988 18.993 6.59961 17.6777C6.59962 16.3623 7.71051 15.3606 8.99902 15.3604C10.0286 15.3604 10.9435 15.9998 11.2705 16.9277H13.9502C15.1589 16.9277 16.1261 16.1539 16.4111 15.1514C16.155 15.2407 15.8817 15.293 15.5986 15.293C14.3103 15.2927 13.1995 14.2908 13.1992 12.9756V10.1543C13.1992 8.83884 14.3101 7.83714 15.5986 7.83691C15.9032 7.83691 16.1972 7.89422 16.4697 7.99707C16.1535 4.38853 12.9637 1.5 8.99902 1.5C5.03445 1.50011 1.84359 4.38856 1.52734 7.99707C1.80001 7.89396 2.09449 7.83697 2.39941 7.83691C3.6881 7.83691 4.7998 8.83869 4.7998 10.1543V12.9756C4.79953 14.291 3.68794 15.293 2.39941 15.293C1.11107 15.2927 0.000274862 14.2908 0 12.9756V8.58691C4.31105e-05 3.80879 4.0657 0.000121624 8.99902 0ZM8.99902 16.8604C8.4656 16.8606 8.09962 17.2622 8.09961 17.6777C8.0999 18.0931 8.4658 18.4949 8.99902 18.4951C9.53249 18.4951 9.89913 18.0932 9.89941 17.6777C9.89941 17.2621 9.53269 16.8604 8.99902 16.8604ZM2.39941 9.33691C1.866 9.33713 1.50001 9.73876 1.5 10.1543V12.9756C1.50029 13.391 1.86621 13.7927 2.39941 13.793C2.93286 13.793 3.29952 13.3911 3.2998 12.9756V10.1543C3.2998 9.73865 2.93306 9.33691 2.39941 9.33691ZM15.5986 9.33691C15.0652 9.33713 14.6992 9.73876 14.6992 10.1543V12.9756C14.6995 13.391 15.0654 13.7927 15.5986 13.793C16.1321 13.793 16.4987 13.3911 16.499 12.9756V10.1729C16.4989 10.1667 16.4981 10.1605 16.498 10.1543V10.1348C16.487 9.72598 16.1241 9.33691 15.5986 9.33691Z" fill="white"/>
              </svg>
            </div>
          </div>
          <span class="menu-label">Support</span>
        </div>

        <!-- Help -->
        <div class="menu-item" @click="handleMenuClick('help')">
          <div class="menu-icon-circle">
            <div class="menu-icon">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M9.69301 13.4082C9.12117 13.4082 8.6582 13.8848 8.6582 14.4566C8.6582 15.0149 9.10754 15.5051 9.69301 15.5051C10.2785 15.5051 10.7414 15.0149 10.7414 14.4566C10.7414 13.8848 10.2649 13.4082 9.69301 13.4082Z" fill="white"/>
                <path d="M9.86984 5.46875C8.03168 5.46875 7.1875 6.55801 7.1875 7.29328C7.1875 7.82434 7.6368 8.06941 8.00445 8.06941C8.73969 8.06941 8.44016 7.02098 9.82898 7.02098C10.5098 7.02098 11.0545 7.32055 11.0545 7.94687C11.0545 8.68219 10.292 9.10426 9.84262 9.48551C9.44777 9.8259 8.93035 10.3842 8.93035 11.5552C8.93035 12.2632 9.12094 12.4674 9.67922 12.4674C10.3464 12.4674 10.4825 12.1679 10.4825 11.9092C10.4825 11.2011 10.4962 10.7927 11.2451 10.2072C11.6127 9.92125 12.7701 8.99535 12.7701 7.71543C12.7701 6.43551 11.6127 5.46875 9.86984 5.46875Z" fill="white"/>
                <path d="M10 0C4.47328 0 0 4.47254 0 10V19.2188C0 19.6502 0.349766 20 0.78125 20H10C15.5267 20 20 15.5275 20 10C20 4.47328 15.5275 0 10 0ZM10 18.4375H1.5625V10C1.5625 5.33684 5.33621 1.5625 10 1.5625C14.6632 1.5625 18.4375 5.33621 18.4375 10C18.4375 14.6632 14.6638 18.4375 10 18.4375Z" fill="white"/>
              </svg>
            </div>
          </div>
          <span class="menu-label">Help</span>
        </div>
      </div>

      <!-- Start Section -->
      <div class="start-section">
        <div class="start-card">
          <div class="start-icon">
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
          <div class="start-content">
            <div class="start-title">Start</div>
            <div class="start-description">
              buy <span class="start-number">123</span> more Forevers to upgrade
            </div>
          </div>
          <button class="upgrade-button" @click="handleUpgrade">
            Upgrade
          </button>
        </div>
      </div>

      <!-- Bottom Controls -->
      <div class="bottom-controls">
        <!-- ID Section -->
        <div class="id-section" :class="{ 'id-section-copied': showCopySuccess }">
          <div v-if="!showCopySuccess" class="id-content">
            <span class="id-label">ID: </span>
            <span class="id-value">515745</span>
          </div>
          <div v-if="showCopySuccess" class="id-copied-content">
            <span class="id-copied-text">Copied</span>
            <div class="id-copied-icon">
              <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="14" cy="14" r="14" fill="white"/>
              </svg>
              <svg class="id-tick-svg" width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
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
          <button
            v-if="!showCopySuccess"
            class="copy-button"
            @click="copyUserID"
          >
            <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M18.0655 0.5H7.60611C6.97596 0.5 6.37161 0.727045 5.92603 1.13119C5.48044 1.53533 5.23011 2.08346 5.23011 2.65501V3.48385H4.04211C3.38111 3.48385 2.74718 3.72201 2.27978 4.14594C1.81239 4.56986 1.5498 5.14483 1.5498 5.74435V19.2395C1.5498 19.839 1.81239 20.414 2.27978 20.8379C2.74718 21.2618 3.38111 21.5 4.04211 21.5H14.2772C14.9382 21.5 15.5721 21.2618 16.0395 20.8379C16.5069 20.414 16.7695 19.839 16.7695 19.2395V18.486H18.0655C18.6907 18.4861 19.291 18.2634 19.7369 17.866C20.1829 17.4685 20.4389 16.9281 20.4498 16.3611V2.65501C20.4476 2.08277 20.1954 1.53465 19.7485 1.13073C19.3016 0.7268 18.6964 0.499997 18.0655 0.5ZM15.108 19.2395C15.108 19.4393 15.0204 19.631 14.8646 19.7723C14.7088 19.9136 14.4975 19.993 14.2772 19.993H4.04211C3.82178 19.993 3.61047 19.9136 3.45467 19.7723C3.29887 19.631 3.21134 19.4393 3.21134 19.2395V5.74435C3.21134 5.54451 3.29887 5.35285 3.45467 5.21154C3.61047 5.07024 3.82178 4.99085 4.04211 4.99085H14.2772C14.4975 4.99085 14.7088 5.07024 14.8646 5.21154C15.0204 5.35285 15.108 5.54451 15.108 5.74435V19.2395ZM18.7883 16.3611C18.7861 16.5337 18.709 16.6985 18.5737 16.8198C18.4383 16.9411 18.2558 17.0092 18.0655 17.0092H16.7695V5.74435C16.7695 5.14483 16.5069 4.56986 16.0395 4.14594C15.5721 3.72201 14.9382 3.48385 14.2772 3.48385H6.89165V2.65501C6.89165 2.48314 6.96693 2.31832 7.10091 2.19679C7.2349 2.07527 7.41663 2.007 7.60611 2.007H18.0655C18.16 2.006 18.2538 2.02203 18.3415 2.05414C18.4291 2.08626 18.5089 2.13384 18.5761 2.19411C18.6433 2.25438 18.6967 2.32616 18.7331 2.40527C18.7695 2.48439 18.7883 2.56927 18.7883 2.65501V16.3611Z" fill="#2019CE"/>
            </svg>
          </button>
        </div>

        <!-- Language Section -->
        <div class="language-section">
          <div class="language-content">
            <div class="flag-wrapper">
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                <circle cx="16" cy="16" r="16" fill="#D4D4D4"/>
                <g clip-path="url(#clip0_flag)">
                  <path d="M15.9993 31.0591C24.316 31.0591 31.0581 24.317 31.0581 16.0002C31.0581 7.68347 24.316 0.941406 15.9993 0.941406C7.68249 0.941406 0.94043 7.68347 0.94043 16.0002C0.94043 24.317 7.68249 31.0591 15.9993 31.0591Z" fill="#F0F0F0"/>
                  <path d="M15.3438 16.0025H31.0573C31.0573 14.6433 30.8761 13.3266 30.5385 12.0741H15.3438V16.0025Z" fill="#D80027"/>
                  <path d="M15.3438 8.14179H28.847C27.9252 6.63756 26.7466 5.30797 25.3723 4.21338H15.3438V8.14179Z" fill="#D80027"/>
                  <path d="M16.0038 31.06C19.5478 31.06 22.8053 29.8351 25.3776 27.7864H6.62988C9.20224 29.8351 12.4597 31.06 16.0038 31.06Z" fill="#D80027"/>
                  <path d="M3.15241 23.855H28.8496C29.5896 22.6475 30.1636 21.3275 30.5411 19.9266H1.46094C1.83841 21.3275 2.41235 22.6475 3.15241 23.855Z" fill="#D80027"/>
                  <path d="M7.91596 3.29305H9.28825L8.01178 4.22041L8.49937 5.72094L7.22296 4.79358L5.94655 5.72094L6.36772 4.42464C5.24384 5.36082 4.25878 6.45764 3.44702 7.67976H3.88672L3.07419 8.27005C2.94761 8.48123 2.82619 8.69576 2.70984 8.91346L3.09784 10.1076L2.37396 9.5817C2.19402 9.96294 2.02943 10.3528 1.88149 10.7507L2.30896 12.0665H3.88672L2.61025 12.9938L3.09784 14.4943L1.82143 13.567L1.05684 14.1225C0.980312 14.7377 0.94043 15.3643 0.94043 16.0002H15.9993C15.9993 7.68352 15.9993 6.70305 15.9993 0.941406C13.0244 0.941406 10.2513 1.80435 7.91596 3.29305ZM8.49937 14.4943L7.22296 13.567L5.94655 14.4943L6.43414 12.9938L5.15767 12.0665H6.73543L7.22296 10.5659L7.71049 12.0665H9.28825L8.01178 12.9938L8.49937 14.4943ZM8.01178 8.60711L8.49937 10.1076L7.22296 9.18029L5.94655 10.1076L6.43414 8.60711L5.15767 7.67976H6.73543L7.22296 6.17923L7.71049 7.67976H9.28825L8.01178 8.60711ZM13.9009 14.4943L12.6245 13.567L11.3481 14.4943L11.8357 12.9938L10.5592 12.0665H12.137L12.6245 10.5659L13.112 12.0665H14.6898L13.4133 12.9938L13.9009 14.4943ZM13.4133 8.60711L13.9009 10.1076L12.6245 9.18029L11.3481 10.1076L11.8357 8.60711L10.5592 7.67976H12.137L12.6245 6.17923L13.112 7.67976H14.6898L13.4133 8.60711ZM13.4133 4.22041L13.9009 5.72094L12.6245 4.79358L11.3481 5.72094L11.8357 4.22041L10.5592 3.29305H12.137L12.6245 1.79252L13.112 3.29305H14.6898L13.4133 4.22041Z" fill="#0052B4"/>
                </g>
                <defs>
                  <clipPath id="clip0_flag">
                    <rect width="30.1176" height="30.1176" fill="white" transform="translate(0.94043 0.941406)"/>
                  </clipPath>
                </defs>
              </svg>
            </div>
            <span class="language-text">ENG</span>
          </div>
          <div class="dropdown-arrow">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <circle opacity="0.2" cx="10" cy="10" r="10" fill="white"/>
              <path d="M5.71387 8.57146L9.99958 12.8572L14.2853 8.57146" stroke="white" stroke-linecap="round"/>
            </svg>
          </div>
        </div>
      </div>


    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

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
</script>

<style scoped>
.profile-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 50;
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: rgba(89, 89, 89, 0.10);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

/* Triangle Pointer */
.triangle-pointer {
  position: absolute;
  left: 34px;
  bottom: 100px;
  z-index: 65;
}

.triangle-shape {
  width: 0;
  height: 0;
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  border-top: 15px solid rgba(18, 11, 129, 0.95);
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.1));
}

/* Profile Dropdown */
.profile-dropdown {
  position: absolute;
  left: 8px;
  right: 8px;
  bottom: 110px;
  height: 580px;
  border-radius: 20px;
  overflow: hidden;
  z-index: 55;
}

.dropdown-background {
  position: absolute;
  inset: 0;
  background: linear-gradient(94deg, #120B81 33.64%, #09074E 76.52%);
  border: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(32px);
  -webkit-backdrop-filter: blur(32px);
}

/* Profile Header Section */
.profile-header-section {
  position: absolute;
  top: 12px;
  left: 12px;
  right: 12px;
  z-index: 2;
}

.profile-header-container {
  width: 100%;
  height: 96px;
  background: rgba(96, 95, 135, 0.24);
  border: 1px solid #D8D8D8;
  border-radius: 1000px 20px 20px 1000px;
  display: flex;
  align-items: center;
  padding: 8px;
  gap: 12px;
  overflow: hidden;
}

.profile-avatar {
  flex-shrink: 0;
}

.avatar-img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  border: 0.727px solid #7E73D6;
}

.profile-user-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 0 4px;
  min-width: 0;
  overflow: hidden;
}

.silver-badge-container {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 2px 16px 2px 2px;
  background: rgba(110, 107, 169, 0.90);
  border: 1px solid #D8D8D8;
  border-radius: 24px;
  width: fit-content;
}

.silver-badge-icon {
  width: 28px;
  height: 28px;
  flex-shrink: 0;
}

.silver-badge-text {
  color: #FAFAFA;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
}

.profile-user-name {
  color: white;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 18px;
  font-weight: 700;
  line-height: 22px;
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.profile-arrow-btn {
  width: 44px;
  height: 44px;
  background: #EFEEFF;
  border: 1px solid #2019CE;
  border-radius: 0 1000px 1000px 0;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  flex-shrink: 0;
}

.profile-arrow-btn:hover {
  background: #E0D9FF;
  transform: scale(1.05);
}

/* Menu Container */
.menu-container {
  position: absolute;
  top: 130px;
  bottom: 190px;
  left: 12px;
  right: 12px;
  z-index: 1;
  padding: 0;
  overflow-y: auto;
  overflow-x: hidden;
  scrollbar-width: none;
  -ms-overflow-style: none;
  -webkit-overflow-scrolling: touch;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
  overscroll-behavior-y: contain;
}

.menu-container::-webkit-scrollbar {
  display: none;
  width: 0;
  height: 0;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 12px;
  height: 52px;
  cursor: pointer;
  transition: all 0.2s ease;
  border-radius: 8px;
  margin-bottom: 8px;
  position: relative;
}

.menu-item:first-child {
  margin-top: 12px;
}

.menu-item:last-child {
  margin-bottom: 12px;
}

.menu-item:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateX(4px);
}

.menu-icon-circle {
  width: 40px;
  height: 40px;
  background: rgba(64, 64, 64, 0.24);
  border: 1px solid rgba(255, 255, 255, 0.24);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  opacity: 0.24;
}

.menu-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.menu-icon svg {
  fill: white;
}

.menu-label {
  color: white;
  font-size: 16px;
  font-weight: 700;
  line-height: 26px;
  flex: 1;
}

.error-badge {
  position: absolute;
  right: 16px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #FFF0F3;
  border: 0.667px solid #FF1919;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Start Section */
.start-section {
  position: absolute;
  bottom: 96px;
  left: 12px;
  right: 12px;
  z-index: 1;
}

.start-card {
  width: 100%;
  height: 84px;
  background: #F1E7FF;
  border: 1px solid #DCCCF1;
  border-radius: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px;
  position: relative;
  overflow: hidden;
}

.start-card::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 140px;
  height: 100%;
  background: linear-gradient(90deg, #8C4CD1 0%, #C497FF 100%);
  opacity: 0.4;
  border-radius: 16px 0 0 16px;
}

.start-icon {
  position: relative;
  z-index: 1;
  flex-shrink: 0;
}

.start-content {
  position: relative;
  z-index: 1;
  flex: 1;
}

.start-title {
  color: #02070E;
  font-size: 19px;
  font-weight: 700;
  line-height: 24px;
  margin-bottom: 4px;
}

.start-description {
  color: #4B4D50;
  font-size: 14px;
  font-weight: 400;
  line-height: 22px;
}

.start-number {
  color: #8C4CD1;
  font-weight: 700;
}

.upgrade-button {
  position: relative;
  z-index: 1;
  width: 120px;
  height: 44px;
  background: linear-gradient(90deg, #2019CE 0%, #473FFF 100%);
  border: none;
  border-radius: 1000px;
  color: white;
  font-size: 16px;
  font-weight: 700;
  line-height: 20px;
  text-transform: capitalize;
  cursor: pointer;
  transition: all 0.2s ease;
  flex-shrink: 0;
}

.upgrade-button:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(32, 25, 206, 0.3);
}

/* Bottom Controls */
.bottom-controls {
  position: absolute;
  bottom: 12px;
  left: 12px;
  right: 12px;
  z-index: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 33px;
  height: 44px;
}

/* ID Section */
.id-section {
  width: 131px;
  height: 44px;
  background: rgba(255, 255, 255, 0.30);
  border: 1px solid rgba(255, 255, 255, 0.40);
  border-radius: 100px;
  backdrop-filter: blur(32px);
  -webkit-backdrop-filter: blur(32px);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 6px;
  position: relative;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.id-section-copied {
  border: 1px solid #07B80E;
  background: #129E0F;
  transform: scale(1.02);
}

.id-content {
  display: flex;
  align-items: center;
  gap: 2px;
  padding-left: 8px;
  flex: 1;
}

.id-label {
  color: #B7B7B7;
  font-size: 14px;
  font-weight: 400;
  line-height: 22px;
}

.id-value {
  color: white;
  font-size: 14px;
  font-weight: 400;
  line-height: 22px;
}

.copy-button {
  width: 32px;
  height: 32px;
  background: white;
  border: 1.2px solid #D8D8D8;
  border-radius: 0 100px 100px 0;
  border-left: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  flex-shrink: 0;
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
}

.copy-button:hover {
  background: #f3f4f6;
  transform: translateY(-50%) scale(1.05);
  box-shadow: 0 4px 12px rgba(32, 25, 206, 0.3);
}

.copy-button:active {
  transform: translateY(-50%) scale(0.98);
}

/* ID Copied Content */
.id-copied-content {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 6px;
  box-sizing: border-box;
  animation: fadeInScale 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.id-copied-text {
  color: #FFF;
  font-family: Montserrat, -apple-system, Roboto, Helvetica, sans-serif;
  font-size: 14px;
  font-weight: 600;
  line-height: 22px;
  text-align: center;
  animation: slideInLeft 0.3s ease-out 0.1s both;
}

.id-copied-icon {
  position: relative;
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: bounceIn 0.5s ease-out 0.2s both;
}

.id-tick-svg {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

/* Animations */
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

/* Language Section */
.language-section {
  width: 131px;
  height: 44px;
  background: rgba(255, 255, 255, 0.20);
  border: 1px solid rgba(255, 255, 255, 0.24);
  border-radius: 1000px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.language-section:hover {
  background: rgba(255, 255, 255, 0.3);
}

.language-content {
  display: flex;
  align-items: center;
  gap: 12px;
  flex: 1;
}

.flag-wrapper {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
}

.language-text {
  color: #FAFAFA;
  font-size: 16px;
  font-weight: 400;
  line-height: 26px;
}

.dropdown-arrow {
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}



/* Responsive */
@media (max-width: 375px) {
  .profile-dropdown {
    left: 4px;
    right: 4px;
  }
  
  .triangle-pointer {
    bottom: 105px;
  }
  
  .start-section {
    bottom: 107px;
  }
  
  .bottom-controls {
    gap: 20px;
    bottom: 8px;
  }
}

/* Animations */
.profile-overlay {
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

.menu-item {
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}
</style>
