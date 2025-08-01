<template>
  <div class="terms-container">
    <div class="terms-wrapper">
      <label class="terms-label">
        <input
          type="checkbox"
          :checked="modelValue"
          @change="$emit('update:modelValue', $event.target.checked)"
          class="terms-checkbox"
        />
        <span class="terms-text">
          I agree that I have read the 
          <a href="#" @click.prevent="$emit('open-terms')" class="terms-link">Terms and Conditions</a>
        </span>
      </label>
    </div>
  </div>
</template>

<script setup>
defineProps({
  modelValue: {
    type: Boolean,
    default: false
  }
})

defineEmits(['update:modelValue', 'open-terms'])
</script>

<style scoped>
.terms-container {
  width: 100%;
  max-width: 375px;
  min-height: 44px;
  z-index: 20;
}

.terms-wrapper {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  width: 100%;
}

.terms-label {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  cursor: pointer;
  width: 100%;
}

.terms-checkbox {
  width: 24px;
  height: 24px;
  border-radius: 4px;
  border: 1px solid #7E7E7E;
  background: #FAFAFA;
  cursor: pointer;
  flex-shrink: 0;
  margin-top: 2px;
  appearance: none;
  -webkit-appearance: none;
  position: relative;
  transition: all 0.2s ease;
}

.terms-checkbox:checked {
  background: #2019CE;
  border-color: #2019CE;
}

.terms-checkbox:checked::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #FAFAFA;
  font-size: 14px;
  font-weight: bold;
}

.terms-text {
  flex: 1;
  color: #FAFAFA;
  font-family: Montserrat;
  font-size: 16px;
  font-weight: 500;
  line-height: 22px;
}

.terms-link {
  color: #FF6800;
  text-decoration: underline;
}

/* Touch-friendly optimizations */
.terms-container {
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

.terms-label {
  -webkit-user-select: none;
  user-select: none;
}

/* Responsive adjustments */
@media (max-width: 375px) {
  .terms-container {
    padding: 0 8px;
  }

  .terms-text {
    font-size: 14px;
    line-height: 20px;
  }

  /* Keep checkbox size same as tablet/desktop for better usability */
  .terms-checkbox {
    width: 24px;
    height: 24px;
  }
}

@media (max-width: 320px) {
  .terms-container {
    padding: 0 12px;
  }

  .terms-text {
    font-size: 13px;
    line-height: 18px;
  }

  /* Keep checkbox size same as tablet/desktop for better usability */
  .terms-checkbox {
    width: 24px;
    height: 24px;
  }
}
</style>
