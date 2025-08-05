<template>
  <div :class="[
    'country-flag rounded-full overflow-hidden flex items-center justify-center relative',
    'shadow-sm transition-all duration-300 hover:shadow-md',
    size === 'small' ? 'w-6 h-6' : size === 'large' ? 'w-10 h-10' : 'w-8 h-8'
  ]">
    <!-- Dynamic flag image from public/flags folder -->
    <img 
      :src="flagSrc" 
      :alt="`${country} flag`"
      class="w-full h-full object-cover rounded-full"
      @error="handleImageError"
    />

    <!-- Subtle shine effect -->
    <div class="absolute inset-0 rounded-full bg-gradient-to-br from-white/20 via-transparent to-transparent pointer-events-none"></div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'

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

const imageError = ref(false)

// Map country names/codes to the actual file names in public/flags
const countryCodeMap = {
  'france': 'FR',
  'fr': 'FR',
  'spain': 'ES', 
  'es': 'ES',
  'india': 'IN',
  'in': 'IN',
  'japan': 'JP',
  'jp': 'JP',
  'ireland': 'IE',
  'ie': 'IE',
  'new zealand': 'NZ',
  'nz': 'NZ',
  'australia': 'AU',
  'au': 'AU',
  'germany': 'DE',
  'de': 'DE',
  'uae': 'UAE',
  'ae': 'UAE',
  'italy': 'IT',
  'it': 'IT',
  'norway': 'NO',
  'no': 'NO',
  'malta': 'MT',
  'mt': 'MT',
  'singapore': 'SG',
  'sg': 'SG',
  'china': 'CN',
  'cn': 'CN',
  'kz': 'KZ',
  'kazakhstan': 'KZ',
  'poland': 'PL',
  'pl': 'PL',
  'ua': 'UA',
  'ukraine': 'UA',
  'canada': 'CA',
  'ca': 'CA',
  'united kingdom': 'GB',
  'uk': 'GB',
  'gb': 'GB',
  'usa': 'USA',
  'us': 'USA',
  'united states': 'USA',
  'south korea': 'KR',
  'korea': 'KR',
  'kr': 'KR',
  'portugal': 'PT',
  'pt': 'PT',
  'netherlands': 'NL',
  'nl': 'NL'
}

const flagSrc = computed(() => {
  if (imageError.value) {
    return '/flags/default.svg' // fallback if needed
  }
  
  const countryKey = props.country.toLowerCase()
  const countryCode = countryCodeMap[countryKey] || props.country.toUpperCase()
  return `/flags/States=${countryCode}.svg`
})

const handleImageError = () => {
  imageError.value = true
}
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
img {
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
