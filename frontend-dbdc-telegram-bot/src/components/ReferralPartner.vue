<template>
  <div class="w-full h-12 rounded-lg bg-white bg-opacity-50 flex items-center px-3">
    <!-- User Icon -->
    <div class="flex items-center gap-2 flex-1">
      <div class="flex-shrink-0">
        <svg class="w-6 h-6" viewBox="0 0 18 22" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path 
            d="M14.2511 12.4974C15.4932 12.4974 16.5 13.5045 16.5 14.7467V15.3222C16.5 16.2166 16.1805 17.0816 15.5989 17.7611C14.0295 19.5949 11.6422 20.5 8.49673 20.5C5.35076 20.5 2.96466 19.5946 1.39831 17.7601C0.818531 17.081 0.5 16.2174 0.5 15.3245V14.7467C0.5 13.5045 1.50689 12.4974 2.74896 12.4974H14.2511ZM14.2511 13.9977H2.74896C2.33534 13.9977 2.00005 14.333 2.00005 14.7467V15.3245C2.00005 15.8602 2.19117 16.3784 2.53904 16.7858C3.79239 18.2538 5.75834 18.9997 8.49673 18.9997C11.2351 18.9997 13.2028 18.2537 14.4593 16.7855C14.8082 16.3779 14.9999 15.8589 14.9999 15.3222V14.7467C14.9999 14.333 14.6647 13.9977 14.2511 13.9977ZM8.49673 0.5C11.2582 0.5 13.4969 2.73897 13.4969 5.50088C13.4969 8.2628 11.2582 10.5017 8.49673 10.5017C5.73521 10.5017 3.49656 8.2628 3.49656 5.50088C3.49656 2.73897 5.73521 0.5 8.49673 0.5ZM8.49673 2.00026C6.56366 2.00026 4.99661 3.56755 4.99661 5.50088C4.99661 7.43422 6.56366 9.00147 8.49673 9.00147C10.4298 9.00147 11.9968 7.43422 11.9968 5.50088C11.9968 3.56755 10.4298 2.00026 8.49673 2.00026Z" 
            fill="white"
          />
        </svg>
      </div>

      <!-- "Your partner" label -->
      <span class="text-white text-sm font-medium leading-[18px]">Your partner</span>
    </div>

    <!-- Partner Info Container -->
    <div class="flex flex-col items-end justify-center">
      <!-- Partner Name -->
      <div class="text-white text-base font-medium leading-5">
        {{ partnerName }}
      </div>
      <!-- Partner User ID Link -->
      <div class="text-dbd-primary text-sm font-semibold leading-4 underline underline-offset-auto">
        {{ partnerUserId }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

// Props
const props = defineProps({
  partnerFirstName: {
    type: String,
    default: ''
  },
  partnerLastName: {
    type: String,
    default: ''
  },
  partnerUserId: {
    type: String,
    default: ''
  }
})

// Computed properties
const partnerName = computed(() => {
  if (props.partnerFirstName && props.partnerLastName) {
    return `${props.partnerFirstName} ${props.partnerLastName}`
  }
  return 'Unknown Partner'
})
</script>

<style scoped>
/* Component-specific styles */
</style>
