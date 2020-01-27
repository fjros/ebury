import Vue from 'vue'
import Router from 'vue-router'
import App from './App.vue'
import TradeTable from './components/TradeTable.vue'

Vue.config.productionTip = false
Vue.use(Router)

const router = new Router({
  routes: [
    { path: "/", redirect: { name: 'trades' } },
    { path: '/trades', name: 'trades', component: TradeTable }
  ]
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
