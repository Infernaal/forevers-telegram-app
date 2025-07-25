<template>
  <div :class="[
    'country-flag rounded-full overflow-hidden flex items-center justify-center relative',
    'shadow-sm transition-all duration-300 hover:shadow-md',
    size === 'small' ? 'w-6 h-6' : size === 'large' ? 'w-10 h-10' : 'w-8 h-8'
  ]">
    <!-- US Flag -->
    <svg v-if="country.toLowerCase() === 'us'" 
         :width="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         :height="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         viewBox="0 0 32 32" class="rounded-full">
      <circle cx="16" cy="16" r="16" fill="#F0F0F0"/>
      <path d="M16 0C10.8 0 6.3 2.9 3.8 7.3H28.2C25.7 2.9 21.2 0 16 0Z" fill="#D80027"/>
      <path d="M16 32C21.2 32 25.7 29.1 28.2 24.7H3.8C6.3 29.1 10.8 32 16 32Z" fill="#D80027"/>
      <path d="M3.8 7.3C1.5 10.4 0 13.9 0 16S1.5 21.6 3.8 24.7H28.2C30.5 21.6 32 18.1 32 16S30.5 10.4 28.2 7.3H3.8Z" fill="#F0F0F0"/>
      <path d="M3.8 12.3H28.2C29.0 13.4 29.7 14.7 30.1 16H1.9C2.3 14.7 3.0 13.4 3.8 12.3Z" fill="#D80027"/>
      <path d="M3.8 19.7H28.2C29.7 18.1 30.5 16.1 30.5 16H1.5C1.5 16.1 2.3 18.1 3.8 19.7Z" fill="#D80027"/>
      <rect x="0" y="0" width="17" height="18" fill="#0052B4"/>
      <g fill="white">
        <circle cx="4" cy="3" r="0.5"/>
        <circle cx="8" cy="3" r="0.5"/>
        <circle cx="12" cy="3" r="0.5"/>
        <circle cx="6" cy="6" r="0.5"/>
        <circle cx="10" cy="6" r="0.5"/>
        <circle cx="14" cy="6" r="0.5"/>
        <circle cx="4" cy="9" r="0.5"/>
        <circle cx="8" cy="9" r="0.5"/>
        <circle cx="12" cy="9" r="0.5"/>
        <circle cx="6" cy="12" r="0.5"/>
        <circle cx="10" cy="12" r="0.5"/>
        <circle cx="14" cy="12" r="0.5"/>
        <circle cx="4" cy="15" r="0.5"/>
        <circle cx="8" cy="15" r="0.5"/>
        <circle cx="12" cy="15" r="0.5"/>
      </g>
    </svg>

    <!-- Russian Flag -->
    <svg v-else-if="country.toLowerCase() === 'ru'" 
         :width="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         :height="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         viewBox="0 0 32 32" class="rounded-full">
      <circle cx="16" cy="16" r="16" fill="#F0F0F0"/>
      <path d="M16 0C7.2 0 0 7.2 0 16H32C32 7.2 24.8 0 16 0Z" fill="#F0F0F0"/>
      <path d="M16 32C24.8 32 32 24.8 32 16H0C0 24.8 7.2 32 16 32Z" fill="#D80027"/>
      <path d="M0 10.7H32V21.3H0V10.7Z" fill="#0052B4"/>
    </svg>

    <!-- German Flag -->
    <svg v-else-if="country.toLowerCase() === 'de'" 
         :width="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         :height="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         viewBox="0 0 32 32" class="rounded-full">
      <circle cx="16" cy="16" r="16" fill="#000"/>
      <path d="M16 0C10.8 0 6.3 2.9 3.8 7.3H28.2C25.7 2.9 21.2 0 16 0Z" fill="#000"/>
      <path d="M3.8 7.3C1.5 10.4 0 13.9 0 16S1.5 21.6 3.8 24.7H28.2C30.5 21.6 32 18.1 32 16S30.5 10.4 28.2 7.3H3.8Z" fill="#D80027"/>
      <path d="M16 32C21.2 32 25.7 29.1 28.2 24.7H3.8C6.3 29.1 10.8 32 16 32Z" fill="#FFDA44"/>
    </svg>

    <!-- French Flag -->
    <svg v-else-if="country.toLowerCase() === 'fr'" 
         :width="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         :height="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         viewBox="0 0 32 32" class="rounded-full">
      <circle cx="16" cy="16" r="16" fill="#F0F0F0"/>
      <path d="M16 0C7.2 0 0 7.2 0 16S7.2 32 16 32" fill="#0052B4"/>
      <path d="M16 0V32C24.8 32 32 24.8 32 16S24.8 0 16 0Z" fill="#D80027"/>
    </svg>

    <!-- Spanish Flag -->
    <svg v-else-if="country.toLowerCase() === 'es'" 
         :width="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         :height="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         viewBox="0 0 32 32" class="rounded-full">
      <circle cx="16" cy="16" r="16" fill="#FFDA44"/>
      <path d="M16 0C10.8 0 6.3 2.9 3.8 7.3H28.2C25.7 2.9 21.2 0 16 0Z" fill="#D80027"/>
      <path d="M16 32C21.2 32 25.7 29.1 28.2 24.7H3.8C6.3 29.1 10.8 32 16 32Z" fill="#D80027"/>
    </svg>

    <!-- Italian Flag -->
    <svg v-else-if="country.toLowerCase() === 'it'" 
         :width="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         :height="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         viewBox="0 0 32 32" class="rounded-full">
      <circle cx="16" cy="16" r="16" fill="#F0F0F0"/>
      <path d="M16 0C9.8 0 4.4 3.9 1.6 9.3V22.7C4.4 28.1 9.8 32 16 32V0Z" fill="#6DA544"/>
      <path d="M30.4 9.3C27.6 3.9 22.2 0 16 0V32C22.2 32 27.6 28.1 30.4 22.7V9.3Z" fill="#D80027"/>
    </svg>

    <!-- Polish Flag -->
    <svg v-else-if="country.toLowerCase() === 'pl'" 
         :width="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         :height="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         viewBox="0 0 32 32" class="rounded-full">
      <circle cx="16" cy="16" r="16" fill="#F0F0F0"/>
      <path d="M16 32C24.8 32 32 24.8 32 16H0C0 24.8 7.2 32 16 32Z" fill="#D80027"/>
    </svg>

    <!-- Ukrainian Flag -->
    <svg v-else-if="country.toLowerCase() === 'ua'" 
         :width="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         :height="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         viewBox="0 0 32 32" class="rounded-full">
      <circle cx="16" cy="16" r="16" fill="#0057B7"/>
      <path d="M16 32C24.8 32 32 24.8 32 16H0C0 24.8 7.2 32 16 32Z" fill="#FFD700"/>
    </svg>

    <!-- Kazakh Flag -->
    <svg v-else-if="country.toLowerCase() === 'kz'" 
         :width="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         :height="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         viewBox="0 0 32 32" class="rounded-full">
      <circle cx="16" cy="16" r="16" fill="#00AFCA"/>
      <circle cx="16" cy="16" r="6" fill="#FFD700"/>
      <path d="M16 12L17 15H20L17.5 17L18.5 20L16 18L13.5 20L14.5 17L12 15H15L16 12Z" fill="#00AFCA"/>
    </svg>

    <!-- UAE Flag -->
    <svg v-else-if="country.toLowerCase() === 'uae'" 
         :width="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         :height="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         viewBox="0 0 32 32" class="rounded-full">
      <circle cx="16" cy="16" r="16" fill="#F0F0F0"/>
      <path d="M16 0C10.8 0 6.3 2.9 3.8 7.3H28.2C25.7 2.9 21.2 0 16 0Z" fill="#00732F"/>
      <path d="M16 32C21.2 32 25.7 29.1 28.2 24.7H3.8C6.3 29.1 10.8 32 16 32Z" fill="#000"/>
      <rect x="0" y="0" width="11" height="32" fill="#CE1126"/>
    </svg>

    <!-- Default flag if country not recognized -->
    <svg v-else 
         :width="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         :height="size === 'small' ? 24 : size === 'large' ? 40 : 32" 
         viewBox="0 0 32 32" class="rounded-full">
      <circle cx="16" cy="16" r="16" fill="#E5E7EB"/>
      <path d="M12 10H20V12H12V10ZM10 14H22V16H10V14ZM12 18H20V20H12V18Z" fill="#9CA3AF"/>
    </svg>

    <!-- Subtle shine effect -->
    <div class="absolute inset-0 rounded-full bg-gradient-to-br from-white/20 via-transparent to-transparent pointer-events-none"></div>
  </div>
</template>

<script setup>
const props = defineProps({
  country: {
    type: String,
    default: 'us',
    required: true
  },
  size: {
    type: String,
    default: 'medium',
    validator: (value) => ['small', 'medium', 'large'].includes(value)
  }
})
</script>

<style scoped>
.country-flag {
  background: linear-gradient(135deg, #f0f2f5 0%, #e8eaed 100%);
  border: 1px solid rgba(0, 0, 0, 0.1);
}

.country-flag:hover {
  transform: scale(1.05);
}

/* Smooth flag transitions */
svg {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Add subtle glow effect */
.country-flag::before {
  content: '';
  position: absolute;
  inset: -1px;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  border-radius: inherit;
  z-index: -1;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.country-flag:hover::before {
  opacity: 1;
}
</style>
