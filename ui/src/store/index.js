import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    current_user: {}
  },
  getters: {
    getFullName (state) {
      return `${state.current_user.first_name} ${state.current_user.last_name}`
    }
  },
  mutations: {
    set_me (state, user) {
      state.current_user = user
    }
  },

  actions: {
    set_me ({commit}) {
      Vue.http.get('/users/me')
        .then((response) => {
          commit('set_me', response.data)
        })
    }
  }

})

export default store
