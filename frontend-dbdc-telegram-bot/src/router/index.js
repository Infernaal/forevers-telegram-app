import { createRouter, createWebHistory } from 'vue-router'
import StartView from '../views/StartView.vue'
import LoaderView from '../views/LoaderView.vue'
import AccountCheckView from '../views/AccountCheckView.vue'
import EmailVerificationView from '../views/EmailVerificationView.vue'
import VerificationCodeView from '../views/VerificationCodeView.vue'
import WalletView from '../views/WalletView.vue'
import FavoritesView from '../views/FavoritesView.vue'
import CartView from '../views/CartView.vue'
import HoldersView from '../views/HoldersView.vue'
import RentOutView from '../views/RentOutView.vue'
import RentOutTransactionView from '../views/RentOutTransactionView.vue'
import CalculatorView from '../views/CalculatorView.vue'
import SelectTypePayment from '../views/SelectTypePayment.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'start',
      component: StartView,
    },
    {
      path: '/loader',
      name: 'loader',
      component: LoaderView,
    },
    {
      path: '/account-check',
      name: 'account-check',
      component: AccountCheckView,
    },
    {
      path: '/email-verification',
      name: 'email-verification',
      component: EmailVerificationView,
    },
    {
      path: '/verification-code',
      name: 'verification-code',
      component: VerificationCodeView,
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
      path: '/calculator',
      name: 'calculator',
      component: CalculatorView,
    },
    {
      path: '/select-payment',
      name: 'select-payment',
      component: SelectTypePayment,
    },

    // Redirect /home to /wallet as default
    {
      path: '/home',
      redirect: '/wallet'
    }
  ],
})

export default router
