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
      :style="{ bottom: `max(${effectiveBottomOffset + 5}px, calc(${effectiveBottomOffset + 5}px + var(--tg-content-safe-area-inset-bottom)))` }"
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
import { useBottomOffset } from '../composables/useBottomNavigation.js'

const { visible, message, hide } = useApiErrorNotifier()
const { bottomOffset: globalBottomOffset } = useBottomOffset()

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

// Используем глобальный bottomOffset если не передан проп
const effectiveBottomOffset = computed(() => {
  return props.bottomOffset !== 120 ? props.bottomOffset : globalBottomOffset.value
})
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
  min-height: 44px;
  height: auto;
  flex-direction: row;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
  border-radius: 1000px;
  border: 1px solid #E53935;
  background: #F44336;
  box-shadow: 4px 8px 12px 0 rgba(229, 57, 53, 0.13);
  padding: 12px 16px;
  min-width: 200px;
  max-width: calc(100vw - 32px);
  width: calc(100vw - 48px);
  justify-content: center;
  transition: all 0.3s ease;
}
.error-notification-content:hover {
  background: #E53935;
  transform: translateY(-1px);
  box-shadow: 4px 12px 16px 0 rgba(229, 57, 53, 0.2);
}
.error-icon-container {
  display: flex;
  justify-content: center;
  align-items: center;
  align-self: flex-start;
  flex-shrink: 0;
  margin-top: 1px;
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
  white-space: normal;
  word-wrap: break-word;
  overflow-wrap: break-word;
  flex: 1;
  min-width: 0;
}
@media (max-width: 374px) {
  .error-notification-container {
    left: 16px;
    right: 16px;
    transform: none;
  }
  .error-notification-content {
    min-width: 200px;
    width: calc(100vw - 48px);
    max-width: calc(100vw - 32px);
    min-height: 44px;
    height: auto;
    align-items: center;
    padding: 12px 16px;
    flex-direction: row;
  }
  .error-notification-container .error-message {
    margin-left: 8px;
    line-height: 20px;
    font-size: 13px;
    text-align: center;
    flex: 1;
  }
  .error-notification-container .error-icon-container {
    flex-shrink: 0;
    align-self: flex-start;
    margin-top: 2px;
  }
}
</style>
