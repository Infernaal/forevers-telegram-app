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
      v-if="visible"
      @click="hide"
      class="error-notification-container"
      :style="{ bottom: `max(${props.bottomOffset + 5}px, calc(${props.bottomOffset + 5}px + var(--tg-content-safe-area-inset-bottom)))` }"
    >
      <div class="error-notification-content">
        <!-- Error Icon Circle -->
        <div class="error-icon-container">
          <svg class="error-icon" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="10" cy="10" r="10" fill="#E53935"/>
            <path d="M10 6V10" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="10" cy="14" r="1" fill="white"/>
          </svg>
        </div>
        <span class="error-message" v-html="message"></span>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { computed } from 'vue'
import { useApiErrorNotifier } from '../composables/useApiErrorNotifier.js'
const { visible, message, hide } = useApiErrorNotifier()
const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  },
  message: {
    type: String,
    default: 'Failed!'
  },
  blurWhenModalOpen: {
    type: Boolean,
    default: false
  },
  bottomOffset: {
    type: Number,
    default: 120
  }
})

defineEmits(['close'])
</script>

<style scoped>
.error-notification-container {
  position: fixed;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10000;
  cursor: pointer;
  font-family: 'Montserrat', sans-serif;
}

.error-notification-content {
  display: inline-flex;
  height: 44px;
  flex-direction: row;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
  border-radius: 1000px;
  border: 1px solid #E53935;
  background: #E53935;
  box-shadow: 4px 8px 12px 0 rgba(7, 184, 14, 0.13);
  padding: 10px 16px;
  width: 343px;
  justify-content: center;
  white-space: nowrap;
  transition: all 0.3s ease;
}

.error-notification-content:hover {
  background: #b71c1c;
  transform: translateY(-1px);
  box-shadow: 4px 12px 16px 0 rgba(7, 184, 14, 0.2);
}

.error-icon-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
}

.error-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.error-message {
  color: #FFF;
  font-family: Montserrat;
  font-size: 15px;
  font-style: normal;
  font-weight: 600;
  line-height: 22px;
  text-align: center;
  margin-left: 8px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Responsive adjustments */
@media (max-width: 374px) {
  .success-notification-container {
    left: 16px;
    right: 16px;
    transform: none;
  }

  .error-notification-content {
    width: calc(100vw - 32px);
    max-width: 343px;
    white-space: normal;
    min-height: 44px;
    height: auto;
    align-items: center;
    padding: 10px 16px;
    flex-direction: row;
  }

  .error-notification-container .error-message {
    white-space: normal;
    overflow: visible;
    text-overflow: unset;
    margin-left: 8px;
    line-height: 16px;
    font-size: 13px;
    text-align: center;
    flex: 1;
  }

  .error-notification-container .error-icon-container {
    flex-shrink: 0;
    align-self: flex-start;
    margin-top: 1px;
  }
}


@media (min-width: 431px) and (max-width: 768px) {
  .error-notification-content {
    width: 400px;
    height: 52px;
    padding: 14px 20px;
  }

  .error-message {
    font-size: 16px;
    line-height: 24px;
  }

  .error-icon {
    width: 24px;
    height: 24px;
  }
}

@media (min-width: 769px) {
  .error-notification-content {
    width: 480px;
    height: 60px;
    padding: 18px 24px;
  }

  .error-message {
    font-size: 18px;
    line-height: 26px;
    font-weight: 600;
  }

  .error-icon {
    width: 28px;
    height: 28px;
  }
}

/* Telegram mini app optimizations */
@media (max-width: 480px) {
  .error-notification-container {
    position: fixed;
    z-index: 10002;
  }
}


/* Error notification animations */
.error-notification-enter-active,
.error-notification-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.error-notification-enter-from {
  opacity: 0;
  transform: translateX(-50%) translateY(20px) scale(0.9);
}

.error-notification-leave-to {
  opacity: 0;
  transform: translateX(-50%) translateY(-10px) scale(0.95);
}

/* Touch-friendly optimizations */
.error-notification-container {
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

/* Blur effect when modal is open */
.blur-notification .error-notification-container {
  filter: blur(4px);
  opacity: 0.6;
  transition: filter 0.3s ease, opacity 0.3s ease;
  pointer-events: none;
}

/* Global blur classes that can be applied from parent components */
:global(.blur-notification) {
  filter: blur(4px) !important;
  opacity: 0.6 !important;
  transition: filter 0.3s ease, opacity 0.3s ease !important;
  pointer-events: none !important;
}
</style>
