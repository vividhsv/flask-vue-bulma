import Vue from 'vue'
import VueRouter from 'vue-router'
import Landing from '../components/Landing.vue'
import Auth from '../components/auth/Auth.vue'
import Login from '../components/auth/Login.vue'
import Register from '../components/auth/Register.vue'
import Dashboard from '../components/dashboard/Dashboard.vue'
import ForgotPassword from '../components/auth/ForgotPassword.vue'
import ResetPassword from '../components/auth/ResetPassword.vue'

Vue.use(VueRouter)

var router = new VueRouter({
  routes: [
    {
      path: '/auth',
      component: Auth,
      redirect: '/auth/login',
      children: [
        {
          path: 'login',
          component: Login,
          meta: {requiresGuest: true}
        },
        {
          path: 'register',
          component: Register,
          meta: {requiresGuest: true}
        },
        {
          path: 'forgotpassword',
          component: ForgotPassword,
          meta: {requiresGuest: true}
        },
        {
          path: 'reset',
          component: ResetPassword,
          meta: {requiresGuest: true}
        }
      ]
    },
    {
      path: '/',
      component: Landing
    },
    {
      path: '/dashboard',
      component: Dashboard,
      meta: {requiresAuth: true}
    }
  ]
})

export default router
