import Axios from 'axios'

var HttpPlugin = Axios.create({
  baseURL: '/api/v1'
})

export default function (Vue) {
  Vue.http = HttpPlugin

  Object.defineProperties(Vue.prototype, {
    $http: {
      get () {
        return Vue.http
      }
    }
  })
}
