<template>
  <div class="w-full min-h-screen bg-white font-montserrat overflow-hidden flex flex-col" style="padding-bottom: max(var(--tg-content-safe-area-inset-bottom, 0px), 1rem);">
    <!-- Main Content -->
    <div class="flex-1 flex items-center justify-center p-4 sm:p-6 md:p-8">
      <div class="w-full max-w-[375px] mx-auto">
        <!-- Main Registration Card -->
        <div class="w-full rounded-3xl bg-gradient-to-r from-dbd-primary to-[#473FFF] relative overflow-hidden">
          <!-- Gradient overlay -->
          <div class="absolute inset-0 bg-black bg-opacity-25"></div>
          
          <!-- Content -->
          <div class="relative p-4 pb-8">
            <!-- Header Text -->
            <div class="text-center pt-5 pb-6">
              <h1 class="text-white text-lg sm:text-xl font-bold leading-6 mb-6">
                We require additional information to continue with your registration.
              </h1>
              <p class="text-white text-sm font-medium leading-6 opacity-90">
                Please enter additional details about yourself below.
              </p>
            </div>

            <!-- Registration Form -->
            <div class="space-y-6">
              <!-- Section Title -->
              <h2 class="text-white text-base font-medium">Complete Registration</h2>

              <!-- Email Field -->
              <div class="relative">
                <div :class="[
                  'w-full h-[52px] rounded-lg border bg-white flex items-center px-3 focus-within:border-dbd-primary focus-within:ring-1 focus-within:ring-dbd-primary/20 transition-all duration-200',
                  showEmailFilled ? 'border-dbd-dark' : 'border-[#B7B7B7]'
                ]">
                  <div v-if="!showEmailFilled" class="flex items-center flex-1">
                    <svg class="w-6 h-6 mr-2 flex-shrink-0" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                      <path d="M21.4037 13.3072C21.8438 13.3072 22.2005 12.9775 22.2005 12.5706V7.7461C22.2005 6.12151 20.7706 4.7998 19.013 4.7998H4.98804C3.23045 4.7998 1.80054 6.12151 1.80054 7.7461V16.2535C1.80054 17.8781 3.23045 19.1998 4.98804 19.1998H19.013C20.7706 19.1998 22.2005 17.8781 22.2005 16.2535C22.2005 15.8467 21.8438 15.5169 21.4037 15.5169C20.9635 15.5169 20.6068 15.8467 20.6068 16.2535C20.6068 17.0658 19.8918 17.7267 19.013 17.7267H4.98804C4.10924 17.7267 3.39429 17.0658 3.39429 16.2535V7.90218L10.3173 11.8813C10.8365 12.1797 11.4185 12.3289 12.0005 12.3289C12.5826 12.3289 13.1646 12.1797 13.6837 11.8813L20.6068 7.90218V12.5706C20.6068 12.9775 20.9635 13.3072 21.4037 13.3072ZM12.8421 10.6303C12.323 10.9286 11.678 10.9287 11.159 10.6303L4.05924 6.54961C4.32093 6.37556 4.64176 6.27295 4.98804 6.27295H19.013C19.3593 6.27295 19.6801 6.37559 19.9418 6.54964L12.8421 10.6303Z" fill="#4B4D50"/>
                    </svg>
                    <input
                      v-model="formData.email"
                      type="email"
                      placeholder="Email"
                      required
                      @blur="handleFieldBlur('email')"
                      class="flex-1 text-sm font-medium text-dbd-gray placeholder-dbd-light-gray bg-transparent border-none outline-none focus:ring-0"
                    />
                    <span v-if="!showEmailError" class="text-red-500 text-sm font-medium ml-1"> *</span>
                  </div>
                  <div v-else class="flex flex-col items-start justify-center flex-1 cursor-pointer" @click="editField('email')">
                    <div class="text-xs text-dbd-gray font-medium leading-none">
                      <span>Email </span><span class="text-red-500">*</span>
                    </div>
                    <div class="text-base font-medium text-dbd-dark mt-1">{{ formData.email }}</div>
                  </div>
                  <!-- Success checkmark -->
                  <div v-if="showEmailFilled" class="w-5 h-5 rounded-full border border-[#88EF8C] bg-[#B3FFB6] flex items-center justify-center">
                    <svg class="w-2 h-2" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8">
                      <path d="M7.65064 0.0612768C7.28964 -0.158776 6.88699 0.265611 6.65095 0.5171C6.10947 1.11439 5.65128 1.80598 5.13753 2.4347C4.56826 3.1263 4.04064 3.81789 3.45749 4.49379C3.12425 4.87103 2.76325 5.27969 2.5411 5.75124C2.04125 5.20108 1.61083 4.60379 1.05545 4.11656C0.652791 3.77076 -0.0136711 3.51927 0.000213534 4.35233C0.0279828 5.4369 0.874945 6.60004 1.49975 7.33876C1.76356 7.65312 2.11068 7.9832 2.51333 7.99892C2.99929 8.03035 3.49914 7.37019 3.79072 7.00868C4.30447 6.37996 4.72101 5.67262 5.19306 5.02821C5.80399 4.17943 6.4288 3.34635 7.02584 2.48186C7.40072 1.94744 8.58091 0.627101 7.65064 0.0612768ZM0.611114 4.28946C0.59723 4.28946 0.583345 4.28946 0.555576 4.30515C0.500037 4.28946 0.458384 4.27371 0.402845 4.24228C0.444499 4.21084 0.513922 4.22656 0.611114 4.28946Z" fill="#07B80E"/>
                    </svg>
                  </div>
                  <!-- Error cross -->
                  <div v-else-if="showEmailError" class="w-5 h-5 rounded-full border border-[#EF8888] bg-[#FFB3B3] flex items-center justify-center">
                    <svg class="w-2 h-2" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8">
                      <path d="M6.5 1.5L1.5 6.5M1.5 1.5L6.5 6.5" stroke="#DC2626" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>
                </div>
              </div>

              <!-- First Name Field -->
              <div class="relative">
                <div :class="[
                  'w-full h-[52px] rounded-lg border bg-white flex items-center px-3 focus-within:border-dbd-primary focus-within:ring-1 focus-within:ring-dbd-primary/20 transition-all duration-200',
                  showFirstNameFilled ? 'border-dbd-dark' : 'border-[#B7B7B7]'
                ]">
                  <div v-if="!showFirstNameFilled" class="flex items-center flex-1">
                    <svg class="w-6 h-6 mr-2 flex-shrink-0" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                      <path d="M12 12C15.3137 12 18 9.31371 18 6C18 2.68629 15.3137 0 12 0C8.68629 0 6 2.68629 6 6C6 9.31371 8.68629 12 12 12ZM12 15C5.37258 15 0 17.6863 0 21V24H24V21C24 17.6863 18.6274 15 12 15Z" fill="#4B4D50"/>
                    </svg>
                    <input
                      v-model="formData.firstName"
                      type="text"
                      placeholder="First name"
                      required
                      @blur="handleFieldBlur('firstName')"
                      class="flex-1 text-sm font-medium text-dbd-gray placeholder-dbd-light-gray bg-transparent border-none outline-none focus:ring-0"
                    />
                    <span v-if="!showFirstNameError" class="text-red-500 text-sm font-medium ml-1"> *</span>
                  </div>
                  <div v-else class="flex flex-col items-start justify-center flex-1 cursor-pointer" @click="editField('firstName')">
                    <div class="text-xs text-dbd-gray font-medium leading-none">
                      <span>First name</span><span class="text-red-500">*</span>
                    </div>
                    <div class="text-base font-medium text-dbd-dark mt-1">{{ formData.firstName }}</div>
                  </div>
                  <!-- Success checkmark -->
                  <div v-if="showFirstNameFilled" class="w-5 h-5 rounded-full border border-[#88EF8C] bg-[#B3FFB6] flex items-center justify-center">
                    <svg class="w-2 h-2" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8">
                      <path d="M7.65064 0.0612768C7.28964 -0.158776 6.88699 0.265611 6.65095 0.5171C6.10947 1.11439 5.65128 1.80598 5.13753 2.4347C4.56826 3.1263 4.04064 3.81789 3.45749 4.49379C3.12425 4.87103 2.76325 5.27969 2.5411 5.75124C2.04125 5.20108 1.61083 4.60379 1.05545 4.11656C0.652791 3.77076 -0.0136711 3.51927 0.000213534 4.35233C0.0279828 5.4369 0.874945 6.60004 1.49975 7.33876C1.76356 7.65312 2.11068 7.9832 2.51333 7.99892C2.99929 8.03035 3.49914 7.37019 3.79072 7.00868C4.30447 6.37996 4.72101 5.67262 5.19306 5.02821C5.80399 4.17943 6.4288 3.34635 7.02584 2.48186C7.40072 1.94744 8.58091 0.627101 7.65064 0.0612768ZM0.611114 4.28946C0.59723 4.28946 0.583345 4.28946 0.555576 4.30515C0.500037 4.28946 0.458384 4.27371 0.402845 4.24228C0.444499 4.21084 0.513922 4.22656 0.611114 4.28946Z" fill="#07B80E"/>
                    </svg>
                  </div>
                  <!-- Error cross -->
                  <div v-else-if="showFirstNameError" class="w-5 h-5 rounded-full border border-[#EF8888] bg-[#FFB3B3] flex items-center justify-center">
                    <svg class="w-2 h-2" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8">
                      <path d="M6.5 1.5L1.5 6.5M1.5 1.5L6.5 6.5" stroke="#DC2626" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>
                </div>
              </div>

              <!-- Last Name Field -->
              <div class="relative">
                <div :class="[
                  'w-full h-[52px] rounded-lg border bg-white flex items-center px-3 focus-within:border-dbd-primary focus-within:ring-1 focus-within:ring-dbd-primary/20 transition-all duration-200',
                  showLastNameFilled ? 'border-dbd-dark' : 'border-[#B7B7B7]'
                ]">
                  <div v-if="!showLastNameFilled" class="flex items-center flex-1">
                    <svg class="w-6 h-6 mr-2 flex-shrink-0" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                      <path d="M12 12C15.3137 12 18 9.31371 18 6C18 2.68629 15.3137 0 12 0C8.68629 0 6 2.68629 6 6C6 9.31371 8.68629 12 12 12ZM12 15C5.37258 15 0 17.6863 0 21V24H24V21C24 17.6863 18.6274 15 12 15Z" fill="#4B4D50"/>
                    </svg>
                    <input
                      v-model="formData.lastName"
                      type="text"
                      placeholder="Last name"
                      required
                      @blur="handleFieldBlur('lastName')"
                      class="flex-1 text-sm font-medium text-dbd-gray placeholder-dbd-light-gray bg-transparent border-none outline-none focus:ring-0"
                    />
                    <span v-if="!showLastNameError" class="text-red-500 text-sm font-medium ml-1"> *</span>
                  </div>
                  <div v-else class="flex flex-col items-start justify-center flex-1 cursor-pointer" @click="editField('lastName')">
                    <div class="text-xs text-dbd-gray font-medium leading-none">
                      <span>Last name</span><span class="text-red-500">*</span>
                    </div>
                    <div class="text-base font-medium text-dbd-dark mt-1">{{ formData.lastName }}</div>
                  </div>
                  <!-- Success checkmark -->
                  <div v-if="showLastNameFilled" class="w-5 h-5 rounded-full border border-[#88EF8C] bg-[#B3FFB6] flex items-center justify-center">
                    <svg class="w-2 h-2" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8">
                      <path d="M7.65064 0.0612768C7.28964 -0.158776 6.88699 0.265611 6.65095 0.5171C6.10947 1.11439 5.65128 1.80598 5.13753 2.4347C4.56826 3.1263 4.04064 3.81789 3.45749 4.49379C3.12425 4.87103 2.76325 5.27969 2.5411 5.75124C2.04125 5.20108 1.61083 4.60379 1.05545 4.11656C0.652791 3.77076 -0.0136711 3.51927 0.000213534 4.35233C0.0279828 5.4369 0.874945 6.60004 1.49975 7.33876C1.76356 7.65312 2.11068 7.9832 2.51333 7.99892C2.99929 8.03035 3.49914 7.37019 3.79072 7.00868C4.30447 6.37996 4.72101 5.67262 5.19306 5.02821C5.80399 4.17943 6.4288 3.34635 7.02584 2.48186C7.40072 1.94744 8.58091 0.627101 7.65064 0.0612768ZM0.611114 4.28946C0.59723 4.28946 0.583345 4.28946 0.555576 4.30515C0.500037 4.28946 0.458384 4.27371 0.402845 4.24228C0.444499 4.21084 0.513922 4.22656 0.611114 4.28946Z" fill="#07B80E"/>
                    </svg>
                  </div>
                  <!-- Error cross -->
                  <div v-else-if="showLastNameError" class="w-5 h-5 rounded-full border border-[#EF8888] bg-[#FFB3B3] flex items-center justify-center">
                    <svg class="w-2 h-2" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8">
                      <path d="M6.5 1.5L1.5 6.5M1.5 1.5L6.5 6.5" stroke="#DC2626" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>
                </div>
              </div>

              <!-- Divider Line -->
              <div class="w-full h-px bg-dbd-off-white opacity-50"></div>

              <!-- Country Selector -->
              <div class="relative">
                <div :class="[
                  'w-full h-[52px] rounded-lg border bg-white flex items-center px-3 cursor-pointer focus-within:border-dbd-primary focus-within:ring-1 focus-within:ring-dbd-primary/20 transition-all duration-200',
                  showCountryFilled ? 'border-dbd-dark' : 'border-[#B7B7B7]'
                ]" @click="toggleCountryDropdown">
                  <div v-if="!showCountryFilled" class="flex items-center flex-1">
                    <svg class="w-6 h-6 mr-2 flex-shrink-0" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                      <path d="M20.4375 12.75C20.8517 12.75 21.1875 12.4142 21.1875 12C21.1875 11.5858 20.8517 11.25 20.4375 11.25L20.4375 12L20.4375 12.75ZM21 12H20.25C20.25 16.5563 16.5563 20.25 12 20.25V21V21.75C17.3848 21.75 21.75 17.3848 21.75 12H21ZM12 21V20.25C7.44365 20.25 3.75 16.5563 3.75 12H3H2.25C2.25 17.3848 6.61522 21.75 12 21.75V21ZM3 12H3.75C3.75 7.44365 7.44365 3.75 12 3.75V3V2.25C6.61522 2.25 2.25 6.61522 2.25 12H3ZM12 3V3.75C16.5563 3.75 20.25 7.44365 20.25 12H21H21.75C21.75 6.61522 17.3848 2.25 12 2.25V3ZM12 21V20.25C11.7045 20.25 11.3639 20.1163 10.9886 19.7535C10.6098 19.3873 10.2344 18.8211 9.90289 18.0633C9.24079 16.55 8.8125 14.4069 8.8125 12H8.0625H7.3125C7.3125 14.5637 7.76565 16.9206 8.52865 18.6646C8.90966 19.5355 9.38272 20.2873 9.94605 20.8319C10.513 21.3801 11.2082 21.75 12 21.75V21ZM8.0625 12H8.8125C8.8125 9.59314 9.24079 7.45001 9.90289 5.93665C10.2344 5.17886 10.6098 4.61271 10.9886 4.24648C11.3639 3.88373 11.7045 3.75 12 3.75V3V2.25C11.2082 2.25 10.513 2.61995 9.94605 3.16805C9.38272 3.71267 8.90966 4.46454 8.52865 5.33542C7.76565 7.07943 7.3125 9.4363 7.3125 12H8.0625ZM12 21V21.75C12.7918 21.75 13.487 21.3801 14.054 20.8319C14.6173 20.2873 15.0903 19.5355 15.4714 18.6646C16.2344 16.9206 16.6875 14.5637 16.6875 12H15.9375H15.1875C15.1875 14.4069 14.7592 16.55 14.0971 18.0633C13.7656 18.8211 13.3902 19.3873 13.0114 19.7535C12.6361 20.1163 12.2955 20.25 12 20.25V21ZM15.9375 12H16.6875C16.6875 9.4363 16.2344 7.07943 15.4714 5.33542C15.0903 4.46454 14.6173 3.71267 14.054 3.16805C13.487 2.61995 12.7918 2.25 12 2.25V3V3.75C12.2955 3.75 12.6361 3.88373 13.0114 4.24648C13.3902 4.61271 13.7656 5.17886 14.0971 5.93665C14.7592 7.45001 15.1875 9.59314 15.1875 12H15.9375ZM3 12L3 12.75L20.4375 12.75L20.4375 12L20.4375 11.25L3 11.25L3 12Z" fill="#4B4D50"/>
                    </svg>
                    <span class="flex-1 text-sm font-medium text-dbd-light-gray">
                      Country<span class="text-red-500"> *</span>
                    </span>
                    <div class="w-5 h-5 rounded-full border border-[#CFCFCF] bg-white flex items-center justify-center">
                      <svg class="w-3 h-3" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M8 14L12 10L8 6" stroke="#4B4D50" stroke-linecap="round"/>
                      </svg>
                    </div>
                  </div>
                  <div v-else class="flex items-center flex-1 cursor-pointer" @click="editField('country')">
                    <!-- Country Flag -->
                    <CountryFlag :country="selectedCountry.code" size="small" class="mr-2" />
                    <div class="flex flex-col items-start justify-center flex-1">
                      <div class="text-xs text-dbd-gray font-medium leading-none">Country</div>
                      <div class="text-base font-medium text-dbd-dark mt-1">{{ selectedCountry.name }}</div>
                    </div>
                    <div v-if="showCountryFilled" class="w-5 h-5 rounded-full border border-[#88EF8C] bg-[#B3FFB6] flex items-center justify-center mr-2">
                      <svg class="w-2 h-2" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8">
                        <path d="M7.65064 0.0612768C7.28964 -0.158776 6.88699 0.265611 6.65095 0.5171C6.10947 1.11439 5.65128 1.80598 5.13753 2.4347C4.56826 3.1263 4.04064 3.81789 3.45749 4.49379C3.12425 4.87103 2.76325 5.27969 2.5411 5.75124C2.04125 5.20108 1.61083 4.60379 1.05545 4.11656C0.652791 3.77076 -0.0136711 3.51927 0.000213534 4.35233C0.0279828 5.4369 0.874945 6.60004 1.49975 7.33876C1.76356 7.65312 2.11068 7.9832 2.51333 7.99892C2.99929 8.03035 3.49914 7.37019 3.79072 7.00868C4.30447 6.37996 4.72101 5.67262 5.19306 5.02821C5.80399 4.17943 6.4288 3.34635 7.02584 2.48186C7.40072 1.94744 8.58091 0.627101 7.65064 0.0612768ZM0.611114 4.28946C0.59723 4.28946 0.583345 4.28946 0.555576 4.30515C0.500037 4.28946 0.458384 4.27371 0.402845 4.24228C0.444499 4.21084 0.513922 4.22656 0.611114 4.28946Z" fill="#07B80E"/>
                      </svg>
                    </div>
                    <div class="w-5 h-5 rounded-full border border-[#CFCFCF] bg-white flex items-center justify-center">
                      <svg class="w-3 h-3" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M8 14L12 10L8 6" stroke="#4B4D50" stroke-linecap="round"/>
                      </svg>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Phone Number Field -->
              <div class="relative">
                <div :class="[
                  'w-full h-[52px] rounded-lg border bg-white flex items-center px-3 focus-within:border-dbd-primary focus-within:ring-1 focus-within:ring-dbd-primary/20 transition-all duration-200',
                  showPhoneFilled ? 'border-dbd-dark' : 'border-[#B7B7B7]'
                ]">
                  <div v-if="!showPhoneFilled" class="flex items-center flex-1">
                    <svg class="w-6 h-6 mr-2 flex-shrink-0" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                      <path d="M22.4979 18.4211C22.4686 17.6088 22.1303 16.8508 21.5452 16.2866C20.3996 15.1819 19.4397 14.5442 18.5245 14.2797C17.2635 13.9153 16.0954 14.2467 15.0529 15.2648C15.0513 15.2663 15.0498 15.2678 15.0482 15.2694L13.9392 16.3702C13.246 15.9795 11.8983 15.1216 10.4421 13.6654L10.3342 13.5576C8.8778 12.1012 8.01995 10.7532 7.62961 10.0608L8.73047 8.95173C8.73203 8.95018 8.73358 8.94862 8.73514 8.94702C9.75319 7.90464 10.0846 6.73659 9.72017 5.4754C9.45566 4.56021 8.81799 3.60036 7.71328 2.45475C7.14915 1.86974 6.39114 1.53136 5.57883 1.50207C4.76602 1.47274 3.98607 1.75567 3.38117 2.29864L3.35763 2.3198C3.34672 2.32961 3.33605 2.33974 3.32564 2.35011C2.12146 3.5543 1.49023 5.24009 1.50011 7.2253C1.51697 10.5977 3.37043 14.4543 6.45804 17.5419C7.04026 18.1241 7.70196 18.7003 8.42474 19.2545C8.78424 19.5302 9.29915 19.4622 9.57481 19.1027C9.85052 18.7432 9.78252 18.2282 9.42297 17.9526C8.75709 17.442 8.14985 16.9135 7.61812 16.3819C4.82923 13.593 3.15542 10.167 3.1407 7.21713C3.13311 5.68823 3.59302 4.4121 4.47087 3.52509L4.47715 3.51943C5.07339 2.98422 5.97611 3.01679 6.53236 3.59359C8.65611 5.79606 8.50234 6.83585 7.5639 7.79816L6.04329 9.33019C5.80482 9.57046 5.73842 9.93255 5.87611 10.2418C5.91471 10.3285 6.84859 12.3921 9.17438 14.7179L9.28237 14.8258C11.6079 17.1513 13.6715 18.0852 13.7582 18.1238C14.0674 18.2615 14.4296 18.1951 14.6698 17.9566L16.2019 16.436C17.1643 15.4975 18.2041 15.3438 20.4064 17.4676C20.9832 18.0237 21.0158 18.9265 20.4807 19.5227L20.4749 19.5291C19.5951 20.3998 18.3326 20.8594 16.8203 20.8594C16.8079 20.8594 16.7954 20.8594 16.7829 20.8593C15.5741 20.8533 14.1744 20.5219 12.7351 19.9011C12.3192 19.7216 11.8364 19.9134 11.657 20.3294C11.4776 20.7454 11.6693 21.2281 12.0853 21.4075C13.749 22.1252 15.3267 22.4927 16.7747 22.4999C16.7901 22.5 16.8054 22.5 16.8208 22.5C18.786 22.5 20.455 21.8692 21.6499 20.6744C21.6603 20.664 21.6704 20.6533 21.6802 20.6424L21.7014 20.6187C22.2444 20.0139 22.5273 19.2334 22.4979 18.421..." fill="#4B4D50"/>
                    </svg>
                    <div class="flex flex-col items-start justify-center flex-1 min-w-0">
                      <div class="flex items-center">
                        <span class="text-xs text-dbd-gray font-medium leading-none whitespace-nowrap">Your Phone #</span>
                        <span v-if="!showPhoneError" class="text-red-500 text-xs font-medium ml-1">*</span>
                      </div>
                      <div class="w-full mt-1">
                        <VueTelInput
                          v-model="formData.phone"
                          @update:model-value="onPhoneInput"
                          @blur="onPhoneBlur"
                          :inputOptions="{
                            placeholder: 'Enter phone number',
                            styleClasses: 'vue-tel-input-custom'
                          }"
                          :dropdownOptions="{
                            showDialCodeInSelection: true,
                            showFlags: true,
                            showSearchBox: true
                          }"
                          mode="international"
                          :autoDefaultCountry="false"
                          :validCharactersOnly="true"
                          styleClasses="vue-tel-input-wrapper"
                        />
                      </div>
                    </div>
                    <div class="w-5 h-5 rounded-full border border-[#CFCFCF] bg-white flex items-center justify-center flex-shrink-0">
                      <svg class="w-3 h-3" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M8 14L12 10L8 6" stroke="#4B4D50" stroke-linecap="round"/>
                      </svg>
                    </div>
                  </div>
                  <div v-else class="flex items-center flex-1">
                    <svg class="w-6 h-6 mr-2 flex-shrink-0" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                      <path d="M22.4979 18.4211C22.4686 17.6088 22.1303 16.8508 21.5452 16.2866C20.3996 15.1819 19.4397 14.5442 18.5245 14.2797C17.2635 13.9153 16.0954 14.2467 15.0529 15.2648C15.0513 15.2663 15.0498 15.2678 15.0482 15.2694L13.9392 16.3702C13.246 15.9795 11.8983 15.1216 10.4421 13.6654L10.3342 13.5576C8.8778 12.1012 8.01995 10.7532 7.62961 10.0608L8.73047 8.95173C8.73203 8.95018 8.73358 8.94862 8.73514 8.94702C9.75319 7.90464 10.0846 6.73659 9.72017 5.4754C9.45566 4.56021 8.81799 3.60036 7.71328 2.45475C7.14915 1.86974 6.39114 1.53136 5.57883 1.50207C4.76602 1.47274 3.98607 1.75567 3.38117 2.29864L3.35763 2.3198C3.34672 2.32961 3.33605 2.33974 3.32564 2.35011C2.12146 3.5543 1.49023 5.24009 1.50011 7.2253C1.51697 10.5977 3.37043 14.4543 6.45804 17.5419C7.04026 18.1241 7.70196 18.7003 8.42474 19.2545C8.78424 19.5302 9.29915 19.4622 9.57481 19.1027C9.85052 18.7432 9.78252 18.2282 9.42297 17.9526C8.75709 17.442 8.14985 16.9135 7.61812 16.3819C4.82923 13.593 3.15542 10.167 3.1407 7.21713C3.13311 5.68823 3.59302 4.4121 4.47087 3.52509L4.47715 3.51943C5.07339 2.98422 5.97611 3.01679 6.53236 3.59359C8.65611 5.79606 8.50234 6.83585 7.5639 7.79816L6.04329 9.33019C5.80482 9.57046 5.73842 9.93255 5.87611 10.2418C5.91471 10.3285 6.84859 12.3921 9.17438 14.7179L9.28237 14.8258C11.6079 17.1513 13.6715 18.0852 13.7582 18.1238C14.0674 18.2615 14.4296 18.1951 14.6698 17.9566L16.2019 16.436C17.1643 15.4975 18.2041 15.3438 20.4064 17.4676C20.9832 18.0237 21.0158 18.9265 20.4807 19.5227L20.4749 19.5291C19.5951 20.3998 18.3326 20.8594 16.8203 20.8594C16.8079 20.8594 16.7954 20.8594 16.7829 20.8593C15.5741 20.8533 14.1744 20.5219 12.7351 19.9011C12.3192 19.7216 11.8364 19.9134 11.657 20.3294C11.4776 20.7454 11.6693 21.2281 12.0853 21.4075C13.749 22.1252 15.3267 22.4927 16.7747 22.4999C16.7901 22.5 16.8054 22.5 16.8208 22.5C18.786 22.5 20.455 21.8692 21.6499 20.6744C21.6603 20.664 21.6704 20.6533 21.6802 20.6424L21.7014 20.6187C22.2444 20.0139 22.5273 19.2334 22.4979 18.421..." fill="#4B4D50"/>
                    </svg>
                    <div class="flex flex-col items-start justify-center flex-1 cursor-pointer" @click="editField('phone')">
                      <div class="text-xs text-dbd-gray font-medium leading-none">Your Phone #</div>
                      <div class="text-base font-medium text-dbd-dark mt-1">{{ formData.phone }}</div>
                    </div>
                    <!-- Success checkmark -->
                    <div v-if="showPhoneFilled" class="w-5 h-5 rounded-full border border-[#88EF8C] bg-[#B3FFB6] flex items-center justify-center mr-2">
                      <svg class="w-2 h-2" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8">
                        <path d="M7.65064 0.0612768C7.28964 -0.158776 6.88699 0.265611 6.65095 0.5171C6.10947 1.11439 5.65128 1.80598 5.13753 2.4347C4.56826 3.1263 4.04064 3.81789 3.45749 4.49379C3.12425 4.87103 2.76325 5.27969 2.5411 5.75124C2.04125 5.20108 1.61083 4.60379 1.05545 4.11656C0.652791 3.77076 -0.0136711 3.51927 0.000213534 4.35233C0.0279828 5.4369 0.874945 6.60004 1.49975 7.33876C1.76356 7.65312 2.11068 7.9832 2.51333 7.99892C2.99929 8.03035 3.49914 7.37019 3.79072 7.00868C4.30447 6.37996 4.72101 5.67262 5.19306 5.02821C5.80399 4.17943 6.4288 3.34635 7.02584 2.48186C7.40072 1.94744 8.58091 0.627101 7.65064 0.0612768ZM0.611114 4.28946C0.59723 4.28946 0.583345 4.28946 0.555576 4.30515C0.500037 4.28946 0.458384 4.27371 0.402845 4.24228C0.444499 4.21084 0.513922 4.22656 0.611114 4.28946Z" fill="#07B80E"/>
                      </svg>
                    </div>
                    <!-- Error cross -->
                    <div v-else-if="showPhoneError" class="w-5 h-5 rounded-full border border-[#EF8888] bg-[#FFB3B3] flex items-center justify-center mr-2">
                      <svg class="w-2 h-2" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8">
                        <path d="M6.5 1.5L1.5 6.5M1.5 1.5L6.5 6.5" stroke="#DC2626" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                    </div>
                    <div class="w-5 h-5 rounded-full border border-[#CFCFCF] bg-white flex items-center justify-center">
                      <svg class="w-3 h-3" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M8 14L12 10L8 6" stroke="#4B4D50" stroke-linecap="round"/>
                      </svg>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Register Button -->
              <div class="pt-4">
                <button
                  @click="handleRegister"
                  :disabled="!isFormValid"
                  :class="[
                    'w-full h-[52px] rounded-full font-bold text-base flex items-center justify-center gap-2',
                    'border transition-all duration-200',
                    isFormValid
                      ? 'bg-dbd-orange text-white border-dbd-orange active:scale-[0.98]'
                      : 'bg-[#E2E2E2] text-[#989898] border-[#C7C7C7] cursor-not-allowed'
                  ]"
                >
                  Register
                  <svg class="w-6 h-6" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M1.03895 13.0391L20.4531 13.0391L15.8206 17.6718C15.4147 18.0774 15.4147 18.7354 15.8206 19.1409C16.2264 19.5468 16.8844 19.5468 17.2896 19.1409L23.6956 12.7348C24.1015 12.3292 24.1015 11.6712 23.6956 11.2657L17.2896 4.85927C17.0867 4.6563 16.8209 4.55496 16.5551 4.55496C16.2893 4.55496 16.0234 4.6563 15.8206 4.85927C15.4147 5.26487 15.4147 5.92282 15.8206 6.3283L20.4531 10.9613L1.03895 10.9613C0.465234 10.9613 -1.69986e-06 11.4265 -1.75002e-06 12.0002C-1.80017e-06 12.5739 0.465174 13.0391 1.03895 13.0391Z"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import CountryFlag from '@/components/CountryFlag.vue'

const router = useRouter()
const route = useRoute()

// Form data
const formData = ref({
  email: '',
  firstName: '',
  lastName: '',
  country: '',
  phone: ''
})

// Country dropdown state
const showCountryDropdown = ref(false)
const selectedCountry = ref({ name: '', code: '' })

// Available countries list with phone codes
const countries = ref([
  { name: 'United States', code: 'USA', phoneCode: '+1', minDigits: 10, maxDigits: 10, placeholder: '(555) 123-4567' },
  { name: 'Canada', code: 'CA', phoneCode: '+1', minDigits: 10, maxDigits: 10, placeholder: '(555) 123-4567' },
  { name: 'United Kingdom', code: 'GB', phoneCode: '+44', minDigits: 10, maxDigits: 11, placeholder: '7911 123456' },
  { name: 'Australia', code: 'AU', phoneCode: '+61', minDigits: 9, maxDigits: 9, placeholder: '412 345 678' },
  { name: 'Germany', code: 'DE', phoneCode: '+49', minDigits: 10, maxDigits: 12, placeholder: '1512 3456789' },
  { name: 'France', code: 'FR', phoneCode: '+33', minDigits: 9, maxDigits: 9, placeholder: '6 12 34 56 78' },
  { name: 'Spain', code: 'ES', phoneCode: '+34', minDigits: 9, maxDigits: 9, placeholder: '612 34 56 78' },
  { name: 'Italy', code: 'IT', phoneCode: '+39', minDigits: 9, maxDigits: 11, placeholder: '312 345 6789' },
  { name: 'Netherlands', code: 'NL', phoneCode: '+31', minDigits: 9, maxDigits: 9, placeholder: '6 12345678' },
  { name: 'Norway', code: 'NO', phoneCode: '+47', minDigits: 8, maxDigits: 8, placeholder: '12 34 56 78' },
  { name: 'Ireland', code: 'IE', phoneCode: '+353', minDigits: 9, maxDigits: 9, placeholder: '85 123 4567' },
  { name: 'New Zealand', code: 'NZ', phoneCode: '+64', minDigits: 8, maxDigits: 10, placeholder: '21 123 4567' },
  { name: 'Japan', code: 'JP', phoneCode: '+81', minDigits: 10, maxDigits: 11, placeholder: '90 1234 5678' },
  { name: 'South Korea', code: 'KR', phoneCode: '+82', minDigits: 9, maxDigits: 11, placeholder: '10 1234 5678' },
  { name: 'Singapore', code: 'SG', phoneCode: '+65', minDigits: 8, maxDigits: 8, placeholder: '9123 4567' },
  { name: 'China', code: 'CN', phoneCode: '+86', minDigits: 11, maxDigits: 11, placeholder: '138 0013 8000' },
  { name: 'India', code: 'IN', phoneCode: '+91', minDigits: 10, maxDigits: 10, placeholder: '98765 43210' },
  { name: 'UAE', code: 'UAE', phoneCode: '+971', minDigits: 9, maxDigits: 9, placeholder: '50 123 4567' },
  { name: 'Kazakhstan', code: 'KZ', phoneCode: '+7', minDigits: 10, maxDigits: 10, placeholder: '701 123 4567' },
  { name: 'Poland', code: 'PL', phoneCode: '+48', minDigits: 9, maxDigits: 9, placeholder: '512 345 678' },
  { name: 'Ukraine', code: 'UA', phoneCode: '+380', minDigits: 9, maxDigits: 9, placeholder: '67 123 4567' },
  { name: 'Russia', code: 'RU', phoneCode: '+7', minDigits: 10, maxDigits: 10, placeholder: '912 345 6789' },
  { name: 'Portugal', code: 'PT', phoneCode: '+351', minDigits: 9, maxDigits: 9, placeholder: '912 345 678' },
  { name: 'Malta', code: 'MT', phoneCode: '+356', minDigits: 8, maxDigits: 8, placeholder: '9696 1234' }
])

// Track which fields have been touched (user moved away from them)
const touchedFields = ref({
  email: false,
  firstName: false,
  lastName: false,
  country: false,
  phone: false
})

// Computed properties for individual field validation
const isEmailValid = computed(() => {
  const email = formData.value.email.trim()
  // Require at least 2 characters for domain extension (like .com, .ru, etc.)
  return email && /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)
})

const isFirstNameValid = computed(() => {
  return formData.value.firstName.trim().length >= 2
})

const isLastNameValid = computed(() => {
  return formData.value.lastName.trim().length >= 2
})

const isCountryValid = computed(() => {
  return selectedCountry.value.name.length > 0
})

const isPhoneValid = computed(() => {
  if (!selectedCountry.value.name || !formData.value.phone.trim()) {
    return false
  }

  // Remove spaces and formatting for digit counting
  const phoneDigits = formData.value.phone.replace(/\D/g, '')
  const country = countries.value.find(c => c.name === selectedCountry.value.name)

  if (!country) return false

  return phoneDigits.length >= country.minDigits && phoneDigits.length <= country.maxDigits
})

// Show filled state only if field is touched, valid, and has meaningful content
const showEmailFilled = computed(() => {
  return touchedFields.value.email && isEmailValid.value && formData.value.email.trim().length > 5
})

const showFirstNameFilled = computed(() => {
  return touchedFields.value.firstName && isFirstNameValid.value && formData.value.firstName.trim().length > 2
})

const showLastNameFilled = computed(() => {
  return touchedFields.value.lastName && isLastNameValid.value && formData.value.lastName.trim().length > 2
})

const showCountryFilled = computed(() => {
  return touchedFields.value.country && isCountryValid.value
})

const showPhoneFilled = computed(() => {
  return touchedFields.value.phone && isPhoneValid.value
})

// Show error state for invalid fields that are touched and have content
const showEmailError = computed(() => {
  const hasContent = formData.value.email.trim().length > 3
  return touchedFields.value.email && !isEmailValid.value && hasContent
})

const showFirstNameError = computed(() => {
  const hasContent = formData.value.firstName.trim().length > 0 && formData.value.firstName.trim().length < 2
  return touchedFields.value.firstName && hasContent
})

const showLastNameError = computed(() => {
  const hasContent = formData.value.lastName.trim().length > 0 && formData.value.lastName.trim().length < 2
  return touchedFields.value.lastName && hasContent
})

const showCountryError = computed(() => {
  return false // Country field doesn't need error state since it's a dropdown
})

const showPhoneError = computed(() => {
  if (!touchedFields.value.phone || !formData.value.phone.trim() || !selectedCountry.value.name) {
    return false
  }

  const phoneDigits = formData.value.phone.replace(/\D/g, '')
  const country = countries.value.find(c => c.name === selectedCountry.value.name)

  if (!country) return false

  const hasContent = phoneDigits.length > 0
  const isInvalid = phoneDigits.length > 0 && (phoneDigits.length < country.minDigits || phoneDigits.length > country.maxDigits)

  return hasContent && isInvalid
})

const isFormValid = computed(() => {
  return isEmailValid.value &&
         isFirstNameValid.value &&
         isLastNameValid.value &&
         isCountryValid.value &&
         isPhoneValid.value
})

// Helper functions for phone field
const getCountryPhoneCode = () => {
  if (!selectedCountry.value.name) return ''
  const country = countries.value.find(c => c.name === selectedCountry.value.name)
  return country ? country.phoneCode : ''
}

const getPhonePlaceholder = () => {
  if (!selectedCountry.value.name) return '__ - ___ - ___'
  const country = countries.value.find(c => c.name === selectedCountry.value.name)
  return country ? country.placeholder : '__ - ___ - ___'
}

// Methods
const handleFieldBlur = (fieldName) => {
  // Only mark as touched if the field has some meaningful content
  const fieldValue = formData.value[fieldName]
  if (fieldValue && fieldValue.trim().length > 0) {
    touchedFields.value[fieldName] = true
  }
}

const toggleCountryDropdown = () => {
  // Save current form data before navigation
  saveFormData()

  // Pass current selected country to CountrySelectView if any
  if (selectedCountry.value && selectedCountry.value.name) {
    sessionStorage.setItem('currentCountry', JSON.stringify(selectedCountry.value))
  }
  // Navigate to country selection view instead of showing dropdown
  router.push('/country-select')
}

const selectCountry = (country) => {
  selectedCountry.value = country
  formData.value.country = country.name
  showCountryDropdown.value = false
  touchedFields.value.country = true
}

// Close dropdown when clicking outside
const handleClickOutside = (event) => {
  if (!event.target.closest('.country-dropdown-container')) {
    showCountryDropdown.value = false
  }
}

// Save form data to prevent loss during navigation
const saveFormData = () => {
  const formState = {
    formData: formData.value,
    touchedFields: touchedFields.value,
    selectedCountry: selectedCountry.value
  }
  sessionStorage.setItem('registrationFormState', JSON.stringify(formState))
}

// Restore form data after navigation
const restoreFormData = () => {
  const storedState = sessionStorage.getItem('registrationFormState')
  if (storedState) {
    try {
      const formState = JSON.parse(storedState)

      // Restore only if the current form is relatively empty
      if (!formData.value.email && !formData.value.firstName && !formData.value.lastName) {
        formData.value = { ...formData.value, ...formState.formData }
        touchedFields.value = { ...touchedFields.value, ...formState.touchedFields }

        // Don't restore selectedCountry here - it will be handled by handleCountrySelection
        if (!selectedCountry.value.name && formState.selectedCountry?.name) {
          selectedCountry.value = formState.selectedCountry
        }
      }
    } catch (error) {
      console.error('Error restoring form data:', error)
    }
  }
}

// Handle country selection from CountrySelectView
const handleCountrySelection = () => {
  const storedCountry = sessionStorage.getItem('selectedCountry')
  if (storedCountry) {
    try {
      const country = JSON.parse(storedCountry)

      // Add a small delay for smooth transition
      setTimeout(() => {
        selectedCountry.value = country
        formData.value.country = country.name
        touchedFields.value.country = true

        // Add haptic feedback when country is updated
        if (window.triggerHaptic) {
          window.triggerHaptic('impact', 'light')
        }
      }, 100)

      // Clear the stored data after using it
      sessionStorage.removeItem('selectedCountry')
      sessionStorage.removeItem('registrationFormState')
    } catch (error) {
      console.error('Error parsing stored country:', error)
    }
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  window.addEventListener('focus', handleCountrySelection)

  // Restore form data first
  restoreFormData()

  // Check if a country was selected from CountrySelectView
  handleCountrySelection()
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
  window.removeEventListener('focus', handleCountrySelection)
})

// Watch for route changes to detect return from country selection
watch(() => route.name, (newRouteName) => {
  if (newRouteName === 'registration') {
    restoreFormData()
    handleCountrySelection()
  }
}, { immediate: false })

const editField = (fieldName) => {
  if (fieldName === 'country') {
    // Save current form data before navigation
    saveFormData()

    // Pass current selected country to CountrySelectView for editing
    if (selectedCountry.value && selectedCountry.value.name) {
      sessionStorage.setItem('currentCountry', JSON.stringify(selectedCountry.value))
    }
    // Navigate to country select view for editing
    router.push('/country-select')
    return
  }

  // Reset the touched state for other fields to show the input again
  touchedFields.value[fieldName] = false

  // Add haptic feedback if available
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'light')
  }
}

const handleRegister = () => {
  if (!isFormValid.value) return

  // Add haptic feedback if available
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'medium')
  }

  console.log('Registration submitted:', formData.value)
  // Handle registration logic here
}
</script>

<style scoped>
/* Mobile-first responsive design */
@media (min-width: 768px) {
  .w-full.max-w-\[375px\] {
    max-width: 500px;
  }
}

@media (min-width: 1024px) {
  .w-full.max-w-\[375px\] {
    max-width: 600px;
  }
}

/* Remove default focus outline and blue square */
input {
  outline: none !important;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}

input:focus {
  outline: none !important;
  box-shadow: none !important;
  border-color: inherit;
}

/* Prevent zoom on mobile inputs */
@media (max-width: 768px) {
  input, button, select, textarea {
    font-size: 16px;
  }
}

/* Button hover states for touch devices */
@media (hover: none) and (pointer: coarse) {
  button:hover {
    transform: none;
  }
  
  button:active {
    opacity: 0.8;
  }
}

/* Style asterisks in placeholders to be red */
input::placeholder {
  color: #7E7E7E;
}

/* Custom styling for required fields with asterisks */
.required-field::placeholder {
  color: #7E7E7E;
}

/* Performance optimizations */
* {
  will-change: auto;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Vue Tel Input Custom Styling */
:deep(.vue-tel-input-wrapper) {
  width: 100%;
}

:deep(.vue-tel-input) {
  border: none !important;
  background: transparent !important;
  width: 100%;
}

:deep(.vue-tel-input .vti__dropdown) {
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
}

:deep(.vue-tel-input .vti__selection) {
  background: transparent !important;
  border: none !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  color: #4B4D50 !important;
  padding: 0 8px 0 0 !important;
}

:deep(.vue-tel-input .vti__input) {
  background: transparent !important;
  border: none !important;
  outline: none !important;
  font-size: 16px !important;
  font-weight: 500 !important;
  color: #4B4D50 !important;
  padding: 0 !important;
  margin-left: 8px !important;
}

:deep(.vue-tel-input .vti__input::placeholder) {
  color: #7E7E7E !important;
}

:deep(.vue-tel-input .vti__dropdown-list) {
  border-radius: 8px !important;
  box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1) !important;
  max-height: 200px !important;
  z-index: 1000 !important;
}

:deep(.vue-tel-input .vti__dropdown-item) {
  padding: 8px 12px !important;
  font-size: 14px !important;
}

:deep(.vue-tel-input .vti__dropdown-item:hover) {
  background-color: #F3F4F6 !important;
}
</style>
