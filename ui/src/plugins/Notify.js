import Notify from "../components/notify";


const NotifyPlugin = {
  install(Vue) {
    Vue.prototype.$notify = Notify
  }
}

export default NotifyPlugin