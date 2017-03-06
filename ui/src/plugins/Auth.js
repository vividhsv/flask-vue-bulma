var AuthPlugin = {
  setToken (token) {
    localStorage.setItem('authToken', token)
  },

  destoryToken () {
    localStorage.removeItem('authToken')
  },

  getToken () {
    var token = localStorage.getItem('authToken')

    if (!token) {
      return null
    } else {
      return token
    }
  },

  loggedIn () {
    if (this.getToken()) {
      return true
    } else {
      return false
    }
  }
}

export default function (Vue) {
  Vue.auth = AuthPlugin

  Object.defineProperties(Vue.prototype, {
    $auth: {
      get () {
        return Vue.auth
      }
    }
  })
}
