<template>
  <div id="app">
    <img alt="Ebury logo" src="./assets/logo.png">

    <h1>Booked Trades</h1>
    <trade-table :trades="trades"/>
  </div>
</template>

<script>
import TradeTable from './components/TradeTable.vue'

export default {
  name: 'app',

  components: {
    TradeTable
  },

  methods: {
    async getTrades() {
      try {
        const response = await fetch('http://localhost:8000/api/v1/trades')
        const data = await response.json()
        this.trades = data
      } catch (error) {
        // TODO: provide user with feedback
        console.error(error)
      }
    }
  },

  data() {
    return {
      trades: []
    }
  },

  mounted() {
    this.getTrades()
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 25px;
  margin-left: 30px;
}
</style>
