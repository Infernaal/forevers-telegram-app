import { ForeversPurchaseService } from './foreversPurchaseService.js'
import DepositsService from './depositsService.js'

// Plan tier definitions with USD thresholds based on UAE deposits
export const PLAN_TIERS = [
  {
    id: 'none',
    name: 'None',
    icon: '/plan-none.svg',
    minForevers: 0,
    maxForevers: 49.99,
    color: '#393636ff'
  },
  {
    id: 'start',
    name: 'Start',
    icon: '/plan-start.svg',
    minForevers: 50,
    maxForevers: 99.99,
    color: '#8C4CD1'
  },
  {
    id: 'business',
    name: 'Business',
    icon: '/plan-business.svg',
    minForevers: 100,
    maxForevers: 499.99,
    color: '#63B3ED'
  },
  {
    id: 'business-plus',
    name: 'Business+',
    icon: '/plan-business-+.svg',
    minForevers: 500,
    maxForevers: 999.99,
    color: '#ff9046ff'
  },
  {
    id: 'premium',
    name: 'Premium',
    icon: '/plan-premium.svg',
    minForevers: 1000,
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
      return []
    }
  }

  /**
   * Calculate the most affordable forevers needed for a plan
   * Uses UAE pricing as base (cheapest option typically)
   */
  async calculateForeversNeeded(targetAmount) {
    const prices = await this.getForeversPricing()
    if (!prices || prices.length === 0) {
      return { error: 'Unable to fetch pricing' }
    }

    // Find UAE price (typically the cheapest)
    const uaePrice = prices.find(p => p.type === 'UAE')
    if (!uaePrice) {
      return { error: 'UAE pricing not available' }
    }

    const foreversNeeded = targetAmount / parseFloat(uaePrice.value)
    return {
      forevers: Math.ceil(foreversNeeded),
      costUSD: targetAmount,
      rateUSD: parseFloat(uaePrice.value),
      region: 'UAE'
    }
  }

  /**
   * Determine user's current plan based on total UAE deposits
   */
  getCurrentPlan(totalAmount) {
    for (let i = PLAN_TIERS.length - 1; i >= 0; i--) {
      const tier = PLAN_TIERS[i]
      if (totalAmount >= tier.minForevers) {
        return {
          ...tier,
          isMaxLevel: tier.id === 'premium'
        }
      }
    }
    return {
      ...PLAN_TIERS[0], // Default to 'none' plan
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
  calculateProgress(totalAmount, currentPlan, nextPlan) {
    if (!nextPlan) {
      return 100 // Max level reached
    }

    const currentMin = currentPlan.minForevers
    const nextMin = nextPlan.minForevers
    const progress = ((totalAmount - currentMin) / (nextMin - currentMin)) * 100

    return Math.min(Math.max(progress, 0), 100)
  }

  /**
   * Calculate USD amount needed to reach next level
   */
  getForeversToNextLevel(totalAmount, nextPlan) {
    if (!nextPlan) {
      return 0 // Already at max level
    }

    const needed = nextPlan.minForevers - totalAmount
    return Math.max(needed, 0)
  }

  /**
   * Get complete plan information for user based on UAE deposits
   */
  async getUserPlanInfo(userBalance = null) {
    // Get UAE deposits total using new deposits service
    const totalUaeDeposits = await DepositsService.getUaeTotalForPlan()

    // Convert UAE deposits to equivalent forevers for plan calculation
    // Assuming 1 forevers = 1 USD (adjust if different)
    const equivalentForevers = totalUaeDeposits

    const currentPlan = this.getCurrentPlan(equivalentForevers)
    const nextPlan = this.getNextPlan(currentPlan.id)
    const progress = this.calculateProgress(equivalentForevers, currentPlan, nextPlan)
    const foreversToNext = this.getForeversToNextLevel(equivalentForevers, nextPlan)

    let upgradeInfo = null
    let foreversUaeNeeded = 0
    if (foreversToNext > 0) {
      upgradeInfo = await this.calculateForeversNeeded(foreversToNext)
      // Calculate how many UAE forevers need to be purchased
      if (upgradeInfo && !upgradeInfo.error) {
        foreversUaeNeeded = upgradeInfo.forevers
      }
    }

    return {
      currentPlan,
      nextPlan,
      totalForevers: equivalentForevers,
      totalUaeDeposits,
      progress,
      foreversToNext, // USD amount needed
      foreversUaeNeeded, // Number of UAE forevers to buy
      upgradeInfo,
      isMaxLevel: currentPlan.isMaxLevel
    }
  }
}

export const planService = new PlanService()
export default planService
