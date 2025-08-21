// Service to get forevers prices from the API
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://dbdc-mini.dubadu.com/api/v1/dbdc'

class ForeversPricesService {
  // Get all forevers prices
  async getForeversPrices() {
    try {
      const response = await fetch(`${API_BASE_URL}/prices/forevers`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include'
      })

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`)
      }

      const data = await response.json()
      
      if (data.status === 'success' && data.data) {
        return {
          status: 'success',
          prices: data.data.discounted_prices || data.data.prices || [],
          discounts: data.data.discounts || []
        }
      } else {
        return {
          status: 'failed',
          message: data.message || 'Failed to get prices'
        }
      }
    } catch (error) {
      console.error('ForeversPricesService Error:', error)
      return {
        status: 'failed',
        message: error.message || 'Network error while fetching prices'
      }
    }
  }

  // Convert API prices to currency format for the calculator
  formatPricesForCalculator(prices) {
    const currencies = []
    
    // Map of API types to currency display info
    const typeMapping = {
      'forevers_value': { code: 'UAE', name: 'United Arab Emirates', country: 'uae' },
      'forevers_kazakhstan_value': { code: 'KZ', name: 'Kazakhstan', country: 'kz' },
      'forevers_germany_value': { code: 'DE', name: 'Germany', country: 'germany' },
      'forevers_poland_value': { code: 'PL', name: 'Poland', country: 'poland' },
      'forevers_ukraine_value': { code: 'UA', name: 'Ukraine', country: 'ukraine' }
    }

    prices.forEach(priceItem => {
      const mapping = typeMapping[priceItem.type]
      if (mapping) {
        currencies.push({
          ...mapping,
          rate: priceItem.value.toString()
        })
      }
    })

    // If no UAE found, add default (fallback)
    if (!currencies.find(c => c.code === 'UAE')) {
      currencies.unshift({
        code: 'UAE',
        name: 'United Arab Emirates', 
        country: 'uae',
        rate: '9'
      })
    }

    return currencies
  }
}

export default new ForeversPricesService()
