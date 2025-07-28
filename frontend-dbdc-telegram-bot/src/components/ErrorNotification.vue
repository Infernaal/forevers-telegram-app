<template>
  <Transition
    name="error-notification"
    enter-active-class="transition-all duration-500 ease-out"
    leave-active-class="transition-all duration-300 ease-in"
    enter-from-class="opacity-0 transform translate-y-4 scale-95"
    enter-to-class="opacity-100 transform translate-y-0 scale-100"
    leave-from-class="opacity-100 transform translate-y-0 scale-100"
    leave-to-class="opacity-0 transform translate-y-2 scale-98"
  >
    <div
      v-if="isVisible"
      @click="$emit('close')"
      class="error-notification-container w-full max-w-[340px] mx-auto cursor-pointer"
      :class="containerPosition"
    >
      <!-- Triangular pointer pointing UP -->
      <div class="w-0 h-0 border-l-[6px] border-r-[6px] border-b-[6px] border-transparent absolute top-0 left-8 transform -translate-y-full z-10"
           style="border-bottom-color: rgb(255, 25, 25);"></div>
      
      <!-- Error notification body -->
      <div class="text-white rounded-full flex items-center px-3 py-2 border"
           style="
             background-color: rgb(255, 25, 25);
             border-color: rgb(206, 0, 0);
             border-width: 0.8px;
             box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px;
             filter: drop-shadow(rgba(255, 25, 25, 0.12) 0px 8px 12px);
             min-height: 44px;
           ">
        
        <!-- Warning Icon -->
        <div class="w-8 h-8 rounded-full bg-black bg-opacity-20 flex items-center justify-center mr-3 flex-shrink-0 border border-white border-opacity-30">
          <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M19.7408 16.2967L11.1162 1.64545C10.6472 0.784823 9.35324 0.784859 8.88114 1.6455C8.88114 1.64545 0.256622 16.2967 0.256622 16.2967C-0.427786 17.3687 0.337271 19.0391 1.60051 18.9993C1.60046 18.9993 18.3969 18.9993 18.3969 18.9993C19.6579 19.0374 20.4321 17.3725 19.7408 16.2967ZM8.86009 15.8781C9.15379 14.4507 11.1404 14.6596 11.1618 16.1205C11.0791 17.9021 8.59938 17.6324 8.86009 15.8781ZM11.1618 12.4632C11.1221 14.0415 8.87825 14.0442 8.83553 12.4631V6.86705C8.87991 5.28892 11.119 5.28691 11.1618 6.86707C11.1618 6.86705 11.1618 12.4632 11.1618 12.4632Z" fill="#FAFAFA"/>
          </svg>
        </div>
        
        <!-- Error Text Content -->
        <div class="flex-1 min-w-0">
          <div class="text-white font-semibold text-sm leading-4 mb-0.5">{{ title || "Can't be used" }}</div>
          <div class="text-white text-xs font-medium leading-tight opacity-95">{{ message }}</div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  },
  message: {
    type: String,
    default: 'Please enter the amount according to your limit'
  },
  title: {
    type: String,
    default: ''
  },
  position: {
    type: String,
    default: 'modal', // 'modal' for in-modal positioning, 'fixed' for fixed bottom positioning
    validator: (value) => ['modal', 'fixed'].includes(value)
  }
})

const containerPosition = computed(() => {
  if (props.position === 'modal') {
    return 'relative z-20'
  }
  return 'fixed left-1/2 transform -translate-x-1/2 z-50 px-4 error-notification-fixed'
})

defineEmits(['close'])
</script>

<style scoped>
/* Error notification container styling */
.error-notification-container {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Fixed positioning bottom spacing based on BottomNavigation height */
.error-notification-fixed {
  bottom: calc(84px + env(safe-area-inset-bottom, 0px)); /* 64px nav + 20px spacing for small screens */
}

/* Responsive positioning for fixed bottom notifications */
@media (max-width: 374px) {
  .error-notification-fixed {
    bottom: calc(84px + env(safe-area-inset-bottom, 0px)) !important; /* 64px nav + 20px spacing */
    left: 16px !important;
    right: 16px !important;
    transform: none !important;
    max-width: calc(100vw - 32px) !important;
  }

  /* Hide pointer on very small screens for fixed positioning */
  .error-notification-fixed .w-0 {
    display: none;
  }
}

@media (min-width: 375px) and (max-width: 430px) {
  .error-notification-fixed {
    bottom: calc(88px + env(safe-area-inset-bottom, 0px)) !important; /* 68px nav + 20px spacing */
  }
}

@media (min-width: 431px) and (max-width: 768px) {
  .error-notification-fixed {
    bottom: calc(150px + env(safe-area-inset-bottom, 0px)) !important; /* 88px nav + 62px spacing */
  }

  /* Larger notification for tablets */
  .error-notification-fixed .text-white.rounded-full {
    min-height: 52px;
    padding: 14px 20px;
  }

  .error-notification-fixed .text-sm {
    font-size: 14px;
  }

  .error-notification-fixed .text-xs {
    font-size: 12px;
  }
}

@media (min-width: 769px) {
  .error-notification-fixed {
    bottom: calc(180px + env(safe-area-inset-bottom, 0px)) !important; /* 100px nav + 80px spacing */
  }

  /* Even larger notification for desktop */
  .error-notification-fixed .text-white.rounded-full {
    min-height: 60px;
    padding: 18px 24px;
  }

  .error-notification-fixed .w-8.h-8 {
    width: 40px;
    height: 40px;
    min-width: 40px;
    min-height: 40px;
  }

  .error-notification-fixed .text-sm {
    font-size: 16px;
    line-height: 20px;
  }

  .error-notification-fixed .text-xs {
    font-size: 14px;
    line-height: 18px;
  }
}

/* Telegram mini app optimizations */
@media (max-width: 480px) {
  /* Adjust pointer for mobile */
  .error-notification-container .w-0 {
    border-l-width: 8px;
    border-r-width: 8px;
    border-b-width: 8px;
  }

  /* Smaller text for mobile */
  .error-notification-container .text-base {
    font-size: 14px;
  }

  .error-notification-container .text-sm {
    font-size: 12px;
  }
}

/* Telegram WebApp specific styles */
@media (max-height: 600px) {
  .error-notification-fixed {
    bottom: calc(64px + env(safe-area-inset-bottom, 0px)) !important; /* Reduced spacing for small height screens */
  }
}

/* Touch-friendly for Telegram */
.error-notification-container {
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

/* Safe area support for notifications */
@supports (padding: max(0px)) {
  .error-notification-fixed {
    bottom: max(84px, calc(84px + env(safe-area-inset-bottom))) !important;
  }

  @media (min-width: 375px) and (max-width: 430px) {
    .error-notification-fixed {
      bottom: max(88px, calc(88px + env(safe-area-inset-bottom))) !important;
    }
  }

  @media (min-width: 431px) and (max-width: 768px) {
    .error-notification-fixed {
      bottom: max(150px, calc(150px + env(safe-area-inset-bottom))) !important;
    }
  }

  @media (min-width: 769px) {
    .error-notification-fixed {
      bottom: max(180px, calc(180px + env(safe-area-inset-bottom))) !important;
    }
  }
}

/* Error notification animations */
.error-notification-enter-active,
.error-notification-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.error-notification-enter-from {
  opacity: 0;
  transform: translateY(20px) scale(0.9);
}

.error-notification-leave-to {
  opacity: 0;
  transform: translateY(-10px) scale(0.95);
}

/* Perfect styling to match Figma */
.error-notification-container .bg-red-500 {
  background-color: #FF1919;
  border-color: #CE0000;
}

/* Icon styling */
.error-notification-container .w-8.h-8 {
  width: 32px;
  height: 32px;
  min-width: 32px;
  min-height: 32px;
}

/* Typography matching Figma */
.error-notification-container .font-semibold {
  font-weight: 600;
}

.error-notification-container .font-medium {
  font-weight: 500;
}

/* Responsive adjustments for modal positioning */
@media (max-width: 320px) {
  .error-notification-container {
    max-width: 95%;
  }
  
  .error-notification-container .px-3 {
    padding-left: 8px;
    padding-right: 8px;
  }
}
</style>
