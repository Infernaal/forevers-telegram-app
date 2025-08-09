<template>
  <Transition
    name="success-notification"
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
      class="success-notification-container"
      :style="{ bottom: `${props.bottomOffset + 30}px` }"
    >
      <div class="success-notification-content">
        <!-- Check Icon Circle -->
        <div class="check-icon-container">
          <svg class="check-icon" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="10" cy="10" r="10" fill="#129E0F"/>
            <path d="M6 10L8.5 12.5L14 7" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>

        <!-- Success Message -->
        <span class="success-message">{{ message }}</span>
      </div>
    </div>
  </Transition>
</template>

<script setup>
const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  },
  message: {
    type: String,
    default: 'Success!'
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
.success-notification-container {
  position: fixed;
  left: 50%;
  transform: translateX(-50%);
  z-index: 50;
  cursor: pointer;
  font-family: 'Montserrat', sans-serif;
}

.success-notification-content {
  display: inline-flex;
  height: 44px;
  flex-direction: row;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
  border-radius: 1000px;
  border: 1px solid #129E0F;
  background: #129E0F;
  box-shadow: 4px 8px 12px 0 rgba(7, 184, 14, 0.13);
  padding: 10px 16px;
  width: 343px;
  justify-content: center;
  white-space: nowrap;
  transition: all 0.3s ease;
}

.success-notification-content:hover {
  background: #0f8a0c;
  transform: translateY(-1px);
  box-shadow: 4px 12px 16px 0 rgba(7, 184, 14, 0.2);
}

.check-icon-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
}

.check-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.success-message {
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

  .success-notification-content {
    width: calc(100vw - 32px);
    max-width: 343px;
    white-space: normal;
    min-height: 44px;
    height: auto;
    align-items: center;
    padding: 10px 16px;
    flex-direction: row;
  }

  .success-notification-container .success-message {
    white-space: normal;
    overflow: visible;
    text-overflow: unset;
    margin-left: 8px;
    line-height: 16px;
    font-size: 13px;
    text-align: center;
    flex: 1;
  }

  .success-notification-container .check-icon-container {
    flex-shrink: 0;
    align-self: flex-start;
    margin-top: 1px;
  }
}


@media (min-width: 431px) and (max-width: 768px) {
  .success-notification-content {
    width: 400px;
    height: 52px;
    padding: 14px 20px;
  }

  .success-message {
    font-size: 16px;
    line-height: 24px;
  }

  .check-icon {
    width: 24px;
    height: 24px;
  }
}

@media (min-width: 769px) {
  .success-notification-content {
    width: 480px;
    height: 60px;
    padding: 18px 24px;
  }

  .success-message {
    font-size: 18px;
    line-height: 26px;
    font-weight: 600;
  }

  .check-icon {
    width: 28px;
    height: 28px;
  }
}

/* Telegram mini app optimizations */
@media (max-width: 480px) {
  .success-notification-container {
    position: fixed;
    z-index: 1000;
  }
}


/* Success notification animations */
.success-notification-enter-active,
.success-notification-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.success-notification-enter-from {
  opacity: 0;
  transform: translateX(-50%) translateY(20px) scale(0.9);
}

.success-notification-leave-to {
  opacity: 0;
  transform: translateX(-50%) translateY(-10px) scale(0.95);
}

/* Touch-friendly optimizations */
.success-notification-container {
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

/* Blur effect when modal is open */
.blur-notification .success-notification-container {
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
