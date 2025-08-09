import { ref } from 'vue'

export function useWallet() {
  const foreversBalance = ref(0)
  const loyaltyBalance = ref(0)
  const bonusBalance = ref(0)
  const isLoading = ref(false)
  const error = ref(null)

  const fetchWalletData = async () => {
    isLoading.value = true
    error.value = null
    
    try {
      const response = await fetch('https://dbdc-mini.dubadu.com/api/v1/dbdc/forevers/96')
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const result = await response.json()
      
      // Forevers balance
      foreversBalance.value = parseFloat(result?.forevers_balance?.balance || 0)
      
      // Loyalty program
      const loyalty = result?.wallets?.find(w => w.type === 'loyalty_program')
      loyaltyBalance.value = loyalty ? parseFloat(loyalty.amount) : 0
      
      // Bonus
      const bonus = result?.wallets?.find(w => w.type === 'bonus')
      bonusBalance.value = bonus ? parseFloat(bonus.amount) : 0
      
    } catch (err) {
      console.error('Failed to fetch wallet data:', err)
      error.value = err.message
    } finally {
      isLoading.value = false
    }
  }

  return {
    foreversBalance,
    loyaltyBalance,
    bonusBalance,
    isLoading,
    error,
    fetchWalletData
  }
}
