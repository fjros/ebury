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
  data() {
    return {
      trades: []
    }
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
