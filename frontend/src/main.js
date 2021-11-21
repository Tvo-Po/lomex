import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

import './assets/styles/main.css'

import APIPlugin from './plugins/api'

Vue.use(APIPlugin)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
