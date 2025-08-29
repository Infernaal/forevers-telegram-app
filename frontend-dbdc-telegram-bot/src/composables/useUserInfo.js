import { ref, reactive } from 'vue'
import telegramUserService from '../services/telegramUserService.js'

// Глобальное состояние для кеширования
const userInfo = reactive({
  fullName: '',
  rank: '',
  photo: ''
})

const isLoading = ref(false)
const lastFetch = ref(0)
const CACHE_DURATION = 5 * 60 * 1000 // 5 минут в миллисекундах
let updateInterval = null

// Функция для получения данных пользователя
const fetchUserInfo = async (forceRefresh = false) => {
  const now = Date.now()
  
  // Проверяем, нужно ли обновлять данные
  if (!forceRefresh && lastFetch.value && (now - lastFetch.value < CACHE_DURATION)) {
    console.log('Using cached user data')
    return userInfo
  }

  // Избегаем множественных одновременных запросов
  if (isLoading.value) {
    console.log('Already fetching user data, waiting...')
    return userInfo
  }

  try {
    isLoading.value = true
    console.log('Fetching user data from API')
    
    const result = await telegramUserService.getUserInfo()
    const data = result?.data || {}
    
    if (result.status === 'success' && data) {
      userInfo.fullName = data?.full_name || ''
      userInfo.rank = data?.rank ? data.rank.toLowerCase().replace(/_/g, ' ') : 'none'
      userInfo.photo = data?.avatar && data.avatar.trim() && data.avatar.trim() !== ',' 
        ? data.avatar 
        : '/no-photo.svg'
    } else {
      // Fallback values
      userInfo.photo = '/no-photo.svg'
      userInfo.rank = 'none'
      userInfo.fullName = ''
    }
    
    lastFetch.value = now
  } catch (error) {
    console.error('Failed to fetch user info:', error)
    // При ошибке используем fallback значения, если данных еще нет
    if (!userInfo.photo) {
      userInfo.photo = '/no-photo.svg'
      userInfo.rank = 'none'
      userInfo.fullName = ''
    }
  } finally {
    isLoading.value = false
  }

  return userInfo
}

// Функция для запуска периодического обновления
const startPeriodicUpdate = () => {
  // Останавливаем предыдущий интервал, если он есть
  stopPeriodicUpdate()
  
  // Запускаем обновление каждые 5 минут
  updateInterval = setInterval(() => {
    console.log('Periodic user info update')
    fetchUserInfo(true) // Принудительное обновление
  }, CACHE_DURATION)
}

// Функция для остановки периодического обновления
const stopPeriodicUpdate = () => {
  if (updateInterval) {
    clearInterval(updateInterval)
    updateInterval = null
  }
}

// Функция для инициализации (загружает данные если их нет)
const initializeUserInfo = async () => {
  // Если данных нет или они устарели, загружаем
  if (!lastFetch.value || (Date.now() - lastFetch.value >= CACHE_DURATION)) {
    await fetchUserInfo()
  }
  
  // Запускаем периодическое обновление
  startPeriodicUpdate()
}

// Функция для получения иконки ра��га
const getRankIcon = (rank) => {
  const availableRanks = [
    'none', 'bronze', 'silver', 'gold', 'diamond', 'double diamond', 'ambassador', 'royal ambassador'
  ]
  const normalizedRank = (rank || '').toLowerCase().replace(/_/g, ' ')
  const validRank = availableRanks.includes(normalizedRank) ? normalizedRank.replace(/ /g, '-') : 'none'
  return `/${validRank}.svg`
}

// Очистка при выходе из приложения
const cleanup = () => {
  stopPeriodicUpdate()
}

// Экспортируем composable
export function useUserInfo() {
  return {
    userInfo,
    isLoading,
    fetchUserInfo,
    initializeUserInfo,
    startPeriodicUpdate,
    stopPeriodicUpdate,
    getRankIcon,
    cleanup
  }
}
