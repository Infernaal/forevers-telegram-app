import { ref, inject, provide } from 'vue'

const BOTTOM_OFFSET_KEY = Symbol('bottomOffset')

// Composable для предоставления bottomOffset (используется в App.vue)
export function provideBottomOffset() {
  const bottomOffset = ref(120) // Значение по умолчанию
  
  provide(BOTTOM_OFFSET_KEY, bottomOffset)
  
  return {
    bottomOffset
  }
}

// Composable для использования bottomOffset (используется в компонентах)
export function useBottomOffset() {
  const bottomOffset = inject(BOTTOM_OFFSET_KEY, ref(120))
  
  return {
    bottomOffset
  }
}

// Composable для обновления bottomOffset (используется в BottomNavigation)
export function useBottomOffsetProvider() {
  const bottomOffset = inject(BOTTOM_OFFSET_KEY, ref(120))
  
  // Функция для обновления значения
  const updateBottomOffset = (newValue) => {
    bottomOffset.value = newValue
  }
  
  return {
    bottomOffset,
    updateBottomOffset
  }
}
