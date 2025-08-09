import { ref, computed } from 'vue'

export function useBottomOffset() {
  const bottomNavRef = ref(null)
  
  const bottomOffset = computed(() => {
    return bottomNavRef.value?.bottomOffset || 120
  })
  
  return {
    bottomNavRef,
    bottomOffset
  }
}
