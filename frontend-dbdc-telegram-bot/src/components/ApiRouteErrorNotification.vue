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
  height: 36px;
  flex-direction: row;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
  border-radius: 1000px;
  border: 1px solid #E53935;
  background: #E53935;
  box-shadow: 4px 8px 12px 0 rgba(229, 57, 53, 0.13);
  padding: 8px 14px;
  width: 320px;
  justify-content: center;
  white-space: nowrap;
  transition: all 0.3s ease;
}
.error-notification-content:hover {
  background: #b71c1c;
  transform: translateY(-1px);
  box-shadow: 4px 12px 16px 0 rgba(229, 57, 53, 0.2);
}
.error-icon-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
}
.error-icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
}
.error-message {
  color: #FFF;
  font-family: Montserrat;
  font-size: 14px;
  font-style: normal;
  font-weight: 600;
  line-height: 20px;
  text-align: center;
  margin-left: 6px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
@media (max-width: 374px) {
  .error-notification-container {
    left: 16px;
    transform: none;
    width: calc(100vw - 32px);
    max-width: calc(100vw - 32px);
  }
  .error-notification-content {
    width: 100%;
    min-width: 0;
    padding: 10px 8px;
  }
}
</style>
