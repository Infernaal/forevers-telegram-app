import { ForeversPurchaseService } from './foreversPurchaseService.js'
import UaeDepositsService from './uaeDepositsService.js'

// Plan tier definitions with forevers requirements
export const PLAN_TIERS = [
  {
    id: 'start',
    name: 'Start',
    icon: '/plan-start.svg',
    minForevers: 0,
    maxForevers: 100,
    color: '#8C4CD1'
  },
  {
    id: 'business',
    name: 'Business',
    icon: '/plan-business.svg',
    minForevers: 101,
    maxForevers: 500,
    color: '#FF6800'
  },
  {
    id: 'business-plus',
    name: 'Business+',
    icon: '/plan-business-+.svg',
    minForevers: 501,
    maxForevers: 1000,
    color: '#2019CE'
  },
  {
    id: 'premium',
    name: 'Premium',
    icon: '/plan-premium.svg',
    minForevers: 1001,
    maxForevers: null, // Unlimited
    color: '#07B80E'
  }
]

class PlanService {
  /**
   * Get current forevers pricing from API
   */
  async getForeversPricing() {
    try {
      const response = await ForeversPurchaseService.getForeversPrices()
      if (response.status === 'success' && response.data) {
        return response.data.discounted_prices || response.data.prices
      }
      return []
    } catch (error) {
      console.error('Failed to fetch forevers pricing:', error)
      return []
    }
  }

  /**
   * Calculate the most affordable forevers needed for a plan
   * Uses UAE pricing as base (cheapest option typically)
   */
  async calculateForeversNeeded(targetForevers) {
    const prices = await this.getForeversPricing()
    if (!prices || prices.length === 0) {
      return { error: 'Unable to fetch pricing' }
    }

    // Find UAE price (typically the cheapest)
    const uaePrice = prices.find(p => p.type === 'UAE')
    if (!uaePrice) {
      return { error: 'UAE pricing not available' }
    }

    const totalCost = targetForevers * parseFloat(uaePrice.value)
    return {
      forevers: targetForevers,
      costUSD: totalCost,
      rateUSD: parseFloat(uaePrice.value),
      region: 'UAE'
    }
  }

  /**
   * Determine user's current plan based on total forevers balance
   */
  getCurrentPlan(totalForevers) {
    for (let i = PLAN_TIERS.length - 1; i >= 0; i--) {
      const tier = PLAN_TIERS[i]
      if (totalForevers >= tier.minForevers) {
        return {
          ...tier,
          isMaxLevel: tier.id === 'premium'
        }
      }
    }
    return {
      ...PLAN_TIERS[0],
      isMaxLevel: false
    }
  }

  /**
   * Get the next plan tier
   */
  getNextPlan(currentPlanId) {
    const currentIndex = PLAN_TIERS.findIndex(tier => tier.id === currentPlanId)
    if (currentIndex === -1 || currentIndex === PLAN_TIERS.length - 1) {
      return null // Already at max level
    }
    return PLAN_TIERS[currentIndex + 1]
  }

  /**
   * Calculate progress to next level
   */
  calculateProgress(totalForevers, currentPlan, nextPlan) {
    if (!nextPlan) {
      return 100 // Max level reached
    }

    const currentMin = currentPlan.minForevers
    const nextMin = nextPlan.minForevers
    const progress = ((totalForevers - currentMin) / (nextMin - currentMin)) * 100
    
    return Math.min(Math.max(progress, 0), 100)
  }

  /**
   * Calculate forevers needed to reach next level
   */
  getForeversToNextLevel(totalForevers, nextPlan) {
    if (!nextPlan) {
      return 0 // Already at max level
    }
    
    const needed = nextPlan.minForevers - totalForevers
    return Math.max(needed, 0)
  }

  /**
   * Get complete plan information for user based on UAE deposits
   */
  async getUserPlanInfo(userBalance = null) {
    // Get UAE deposits total instead of forevers balance
    const uaeDepositsResponse = await UaeDepositsService.getUserUaeDeposits()

    let totalUaeDeposits = 0
    if (uaeDepositsResponse.status === 'success' && uaeDepositsResponse.data) {
      totalUaeDeposits = parseFloat(uaeDepositsResponse.data.total_uae_deposits || 0)
    }

    // Convert UAE deposits to equivalent forevers for plan calculation
    // Assuming 1 forevers = 1 USD (adjust if different)
    const equivalentForevers = totalUaeDeposits

    const currentPlan = this.getCurrentPlan(equivalentForevers)
    const nextPlan = this.getNextPlan(currentPlan.id)
    const progress = this.calculateProgress(equivalentForevers, currentPlan, nextPlan)
    const foreversToNext = this.getForeversToNextLevel(equivalentForevers, nextPlan)

    let upgradeInfo = null
    if (foreversToNext > 0) {
      upgradeInfo = await this.calculateForeversNeeded(foreversToNext)
    }

    return {
      currentPlan,
      nextPlan,
      totalForevers: equivalentForevers,
      totalUaeDeposits,
      progress,
      foreversToNext,
      upgradeInfo,
      isMaxLevel: currentPlan.isMaxLevel
    }
  }
}

export const planService = new PlanService()
export default planService
