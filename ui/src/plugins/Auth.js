var AuthPlugin = {
  setToken: function (token) {
    localStorage.setItem('authToken', token);
  },

  destoryToken: function () {
    localStorage.removeItem('authToken');
  },

  getToken: function () {
    var token = localStorage.getItem('authToken');

    if (!token) {
      return null;
    } else {
      return token;
    }
  },

  loggedIn: function () {
    if (this.getToken())
      return true;
    else
      return false;
  }
};

export default function (Vue) {
  Vue.auth = AuthPlugin;

  Object.defineProperties(Vue.prototype, {
    $auth: {
      get: function () {
        return Vue.auth;
      }
    }
  })
}
