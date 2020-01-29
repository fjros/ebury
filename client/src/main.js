import Vue from 'vue'
import Router from 'vue-router'
import Toasted from 'vue-toasted';
import App from './App.vue'
import TradeTable from './components/TradeTable.vue'
import TradeForm from './components/TradeForm.vue'

Vue.config.productionTip = false
Vue.use(Router)
Vue.use(Toasted)

const router = new Router({
  mode: 'history',
  routes: [
    { path: "/", redirect: { name: 'trades' } },
    { path: '/trades', name: 'trades', component: TradeTable },
    { path: '/new', name: 'new', component: TradeForm }
  ]
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
