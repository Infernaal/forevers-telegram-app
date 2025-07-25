import { ref, computed } from 'vue'

// Global cart state
const cartItems = ref([])
const isAddingToCart = ref(false)

export function useCart() {
  // Computed properties
  const cartItemsCount = computed(() => cartItems.value.length)
  const cartTotal = computed(() => {
    return cartItems.value.reduce((total, item) => total + (item.foreversAmount * item.usdRate), 0)
  })

  // Methods
  const addToCart = async (item) => {
    isAddingToCart.value = true
    
    try {
      // Create cart item
      const cartItem = {
        id: `${item.balance.id}-${Date.now()}`,
        balanceId: item.balance.id,
        country: item.balance.country,
        code: item.balance.code,
        foreversAmount: item.foreversAmount,
        usdRate: item.balance.usdRate,
        totalCost: item.foreversAmount * item.balance.usdRate,
        addedAt: new Date().toISOString()
      }

      // Add to cart
      cartItems.value.push(cartItem)

      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 500))
      
      return true
    } catch (error) {
      console.error('Failed to add to cart:', error)
      return false
    } finally {
      isAddingToCart.value = false
    }
  }

  const removeFromCart = (itemId) => {
    const index = cartItems.value.findIndex(item => item.id === itemId)
    if (index > -1) {
      cartItems.value.splice(index, 1)
    }
  }

  const clearCart = () => {
    cartItems.value = []
  }

  const getCartItems = () => {
    return [...cartItems.value]
  }

  return {
    // State
    cartItems,
    isAddingToCart,

    // Computed
    cartItemsCount,
    cartTotal,

    // Methods
    addToCart,
    removeFromCart,
    clearCart,
    getCartItems
  }
}
