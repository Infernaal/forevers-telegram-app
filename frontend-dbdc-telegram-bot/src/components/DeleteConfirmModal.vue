<template>
  <Transition
    name="modal"
    enter-active-class="transition-all duration-300 ease-out"
    leave-active-class="transition-all duration-200 ease-in"
    enter-from-class="opacity-0 backdrop-blur-0 scale-95"
    enter-to-class="opacity-100 backdrop-blur-md scale-100"
    leave-from-class="opacity-100 backdrop-blur-md scale-100"
    leave-to-class="opacity-0 backdrop-blur-0 scale-95"
  >
    <div
      v-if="isVisible"
      class="fixed inset-0 flex items-center justify-center z-50 px-4"
      style="background: rgba(2, 7, 14, 0.20); backdrop-filter: blur(9px);"
      @click="onCancel"
    >
      
      <!-- Modal Content -->
      <div
        @click.stop
        class="relative bg-dbd-off-white rounded-[20px] shadow-xl font-montserrat w-full max-w-[320px] mx-auto transition-all duration-300 p-6 flex flex-col items-center gap-6"
      >
        <!-- Icon Container -->
        <div class="modal-icon">
          <div class="icon-wrapper">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path d="M12 9V13M12 17H12.01M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="#ef4444" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
        </div>

        <!-- Content -->
        <div class="modal-body">
          <!-- Title -->
          <h3 class="modal-title">Delete Position?</h3>

          <!-- Description -->
          <p class="modal-description">
            Are you sure you want to delete this item?
          </p>
        </div>

        <!-- Actions -->
        <div class="modal-actions">
          <!-- Cancel Button -->
          <button
            @click="onCancel"
            class="action-button action-button-secondary"
          >
            <span>No</span>
          </button>

          <!-- Confirm Button -->
          <button
            @click="onConfirm"
            class="action-button action-button-danger"
          >
            <span>Yes</span>
          </button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { watch } from 'vue'

const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['cancel', 'confirm'])

const onCancel = () => {
  if (window.triggerHaptic) {
    window.triggerHaptic('impact', 'light')
  }
  emit('cancel')
}

const onConfirm = () => {
  if (window.triggerHaptic) {
    window.triggerHaptic('notification', 'warning')
  }
  emit('confirm')
}

const handleKeyDown = (event) => {
  if (event.key === 'Escape' && props.isVisible) {
    onCancel()
  } else if (event.key === 'Enter' && props.isVisible) {
    onConfirm()
  }
}

// Watch for visibility changes to add/remove event listeners
watch(() => props.isVisible, (isVisible) => {
  if (isVisible) {
    document.addEventListener('keydown', handleKeyDown)
    document.body.style.overflow = 'hidden'
  } else {
    document.removeEventListener('keydown', handleKeyDown)
    document.body.style.overflow = ''
  }
})
</script>

<style scoped>
/* Base Modal Styles */
.modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 50;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}

.modal-backdrop {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.modal-content {
  position: relative;
  background: #FAFAFA;
  border-radius: 1.25rem;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
  padding: 1.5rem;
  width: 100%;
  max-width: 20rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  transform: translateZ(0);
  will-change: transform;
}

/* Icon */
.modal-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-wrapper {
  width: 3.5rem;
  height: 3.5rem;
  background: #fef2f2;
  border: 2px solid #fecaca;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Content */
.modal-body {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.modal-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #02070E;
  margin: 0;
  line-height: 1.4;
}

.modal-description {
  font-size: 0.875rem;
  color: #4B4D50;
  margin: 0;
  line-height: 1.5;
}

/* Actions */
.modal-actions {
  display: flex;
  gap: 0.75rem;
  width: 100%;
}

.action-button {
  flex: 1;
  padding: 0.75rem 1.5rem;
  border-radius: 1.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  outline: none;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
  min-height: 2.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.action-button-secondary {
  background: #FAFAFA;
  color: #4B4D50;
  border: 1px solid #d1d5db;
}

.action-button-secondary:hover {
  background: #f3f4f6;
  border-color: #9ca3af;
}

.action-button-secondary:active {
  transform: scale(0.98);
  background: #e5e7eb;
}

.action-button-danger {
  background: #FF1919;
  color: white;
  border: 1px solid #FF1919;
}

.action-button-danger:hover {
  background: #dc2626;
  border-color: #dc2626;
}

.action-button-danger:active {
  transform: scale(0.98);
  background: #b91c1c;
}

/* Responsive Styles */

/* Small Mobile (≤374px) */
@media (max-width: 374px) {
  .modal-overlay {
    padding: 0.75rem;
  }

  .modal-content {
    max-width: 100%;
    padding: 1.25rem;
    gap: 1.25rem;
    border-radius: 1rem;
  }

  .icon-wrapper {
    width: 3rem;
    height: 3rem;
  }

  .modal-title {
    font-size: 1rem;
  }

  .modal-description {
    font-size: 0.8125rem;
  }

  .action-button {
    padding: 0.625rem 1.25rem;
    font-size: 0.8125rem;
    min-height: 2.5rem;
    border-radius: 1.25rem;
  }

  .modal-actions {
    gap: 0.5rem;
  }
}

/* Regular Mobile (375px-430px) */
@media (min-width: 375px) and (max-width: 430px) {
  .modal-overlay {
    padding: 1rem;
  }

  .modal-content {
    max-width: 18rem;
    padding: 1.375rem;
    gap: 1.375rem;
  }

  .icon-wrapper {
    width: 3.25rem;
    height: 3.25rem;
  }

  .modal-title {
    font-size: 1.0625rem;
  }

  .modal-description {
    font-size: 0.875rem;
  }

  .action-button {
    min-height: 2.625rem;
  }
}

/* Tablets (431px-768px) */
@media (min-width: 431px) and (max-width: 768px) {
  .modal-overlay {
    padding: 1.5rem;
  }

  .modal-content {
    max-width: 22rem;
    padding: 2rem;
    gap: 1.75rem;
    border-radius: 1.5rem;
  }

  .icon-wrapper {
    width: 4rem;
    height: 4rem;
  }

  .modal-title {
    font-size: 1.25rem;
  }

  .modal-description {
    font-size: 1rem;
  }

  .action-button {
    padding: 1rem 2rem;
    font-size: 1rem;
    min-height: 3rem;
    border-radius: 1.75rem;
  }

  .modal-actions {
    gap: 1rem;
  }
}

/* Desktop (≥769px) */
@media (min-width: 769px) {
  .modal-overlay {
    padding: 2rem;
  }

  .modal-content {
    max-width: 24rem;
    padding: 2.5rem;
    gap: 2rem;
    border-radius: 1.75rem;
  }

  .icon-wrapper {
    width: 4.5rem;
    height: 4.5rem;
  }

  .modal-title {
    font-size: 1.375rem;
  }

  .modal-description {
    font-size: 1.125rem;
  }

  .action-button {
    padding: 1.125rem 2.25rem;
    font-size: 1.125rem;
    min-height: 3.25rem;
    border-radius: 2rem;
  }

  .modal-actions {
    gap: 1.25rem;
  }
}

/* Landscape (height ≤500px) */
@media (max-height: 500px) and (orientation: landscape) {
  .modal-content {
    padding: 1rem;
    gap: 1rem;
    max-width: 16rem;
  }

  .icon-wrapper {
    width: 2.5rem;
    height: 2.5rem;
  }

  .modal-title {
    font-size: 0.875rem;
  }

  .modal-description {
    font-size: 0.75rem;
  }

  .action-button {
    padding: 0.5rem 1rem;
    font-size: 0.75rem;
    min-height: 2rem;
    border-radius: 1rem;
  }

  .modal-actions {
    gap: 0.5rem;
  }
}

/* Animation Classes */
.modal-enter-active {
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.modal-leave-active {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.6, 1);
}

.modal-enter-from {
  opacity: 0;
  transform: scale(0.9) translateY(20px);
}

.modal-leave-to {
  opacity: 0;
  transform: scale(0.95) translateY(-10px);
}

/* Touch Optimizations */
@media (hover: none) and (pointer: coarse) {
  .action-button:hover {
    background: inherit;
    border-color: inherit;
  }

  .action-button-secondary:active {
    background: #e5e7eb;
  }

  .action-button-danger:active {
    background: #b91c1c;
  }
}

/* Accessibility */
@media (prefers-reduced-motion: reduce) {
  .modal-enter-active,
  .modal-leave-active,
  .action-button {
    transition: none;
  }

  .action-button:active {
    transform: none;
  }
}

/* Dark Mode Support */
@media (prefers-color-scheme: dark) {
  .modal-content {
    background: #1a1a1a;
    border: 1px solid #374151;
  }

  .modal-title {
    color: #ffffff;
  }

  .modal-description {
    color: #d1d5db;
  }

  .action-button-secondary {
    background: #2a2a2a;
    color: #d1d5db;
    border-color: #4b5563;
  }

  .action-button-secondary:hover {
    background: #374151;
  }

  .action-button-secondary:active {
    background: #4b5563;
  }

  .icon-wrapper {
    background: #2a1f1f;
    border-color: #4b1f1f;
  }
}

/* Performance */
.modal-content,
.action-button {
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

/* Typography */
* {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-tap-highlight-color: transparent;
}
</style>
