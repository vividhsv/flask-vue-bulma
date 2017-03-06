// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Router from './router'
import Http from './plugins/Http.js'
import Auth from './plugins/Auth.js'
import Notify from './plugins/Notify.js'
import Vuelidate from 'vuelidate'
import Store from './store'

Vue.use(Http)
Vue.use(Auth)
Vue.use(Notify)
Vue.use(Vuelidate)

// configure route guards
Router.beforeEach(function (to, from, next) {
  // prevent access to 'requiresGuest' routes
  if (to.matched.some(function (record) {
    return record.meta.requiresGuest
  }) && Vue.auth.loggedIn()) {
    next({
      path: '/dashboard'
    })
  } else if (to.matched.some(function (record) {
    return record.meta.requiresAuth
  }) && !Vue.auth.loggedIn()) {
    next({
      path: '/auth/login',
      query: {redirect: to.fullPath}
    })
  } else {
    next() // make sure to always call next()!
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store: Store,
  router: Router,
  template: '<App/>',
  components: {App}
})

