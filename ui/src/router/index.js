import Vue from 'vue'
import VueRouter from 'vue-router'
import Landing from '../components/Landing.vue'
import Auth from '../components/auth/Auth.vue'
import Login from '../components/auth/Login.vue'
import Register from '../components/auth/Register.vue'
import Dashboard from '../components/dashboard/Dashboard.vue'
import ForgotPassword from '../components/auth/ForgotPassword.vue'
import ResetPassword from '../components/auth/ResetPassword.vue'
import Profile from '../components/user/Profile.vue'
import Base from '../components/Base.vue'
import User from '../components/user/User.vue'
import Settings from '../components/user/settings/Settings.vue'
import ChangeInfo from '../components/user/settings/ChangeInfo.vue'
import ChangeEmail from '../components/user/settings/ChangeEmail.vue'
import ChangePassword from '../components/user/settings/ChangePassword.vue'
import DeleteUser from '../components/user/settings/DeleteUser.vue'

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
      component: Base,
      redirect: '/landing',
      children: [
        {
          path: 'landing',
          component: Landing
        }
      ]
    },
    {
      path: '/user',
      component: User,
      redirect: '/user/profile',
      children: [
        {
          path: 'profile',
          component: Profile,
          meta: {requiresAuth: true}
        },
        {
          path: 'settings',
          component: Settings,
          redirect: '/user/settings/info',
          meta: {requiresAuth: true},
          children: [
            {
              path: 'info',
              component: ChangeInfo
            },
            {
              path: 'email',
              component: ChangeEmail
            },
            {
              path: 'changepassword',
              component: ChangePassword
            },
            {
              path: 'delete',
              component: DeleteUser
            }
          ]
        }
      ]
    },
    {
      path: '/dashboard',
      component: Dashboard,
      meta: {requiresAuth: true}
    }
  ]
})

export default router
