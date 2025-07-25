import { createRouter, createWebHistory } from 'vue-router'
import StartView from '../views/StartView.vue'
import WalletView from '../views/WalletView.vue'
import FavoritesView from '../views/FavoritesView.vue'
import CartView from '../views/CartView.vue'
import HoldersView from '../views/HoldersView.vue'
import RentOutView from '../views/RentOutView.vue'
import RentOutTransactionView from '../views/RentOutTransactionView.vue'
import ProfileView from '../views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'start',
      component: StartView,
    },

    {
      path: '/wallet',
      name: 'wallet',
      component: WalletView,
    },
    {
      path: '/favorites',
      name: 'favorites',
      component: FavoritesView,
    },
    {
      path: '/cart',
      name: 'cart',
      component: CartView,
    },
    {
      path: '/holders',
      name: 'holders',
      component: HoldersView,
    },
    {
      path: '/rent-out',
      name: 'rent-out',
      component: RentOutView,
    },
    {
      path: '/rent-out-transactions',
      name: 'rent-out-transactions',
      component: RentOutTransactionView,
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
    },
    // Redirect /home to /wallet as default
    {
      path: '/home',
      redirect: '/wallet'
    }
  ],
})

export default router
