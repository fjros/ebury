<template>
  <div id="trade-table">
    <h1>Booked Trades</h1>
    <thead>
      <tr>
        <th>Sell CCY</th>
        <th>Sell Amount</th>
        <th>Buy CCY</th>
        <th>Buy Amount</th>
        <th>Rate</th>
        <th>Date Booked</th>
      </tr>
    </thead>

    <template v-if="hasTrades">
      <!-- show trades -->
      <tbody>
        <tr v-for="trade in trades" :key="trade.id">
          <td>{{ trade.sell_currency }}</td>
          <td>{{ trade.sell_amount / 100 }}</td>
          <td>{{ trade.buy_currency }}</td>
          <td>{{ trade.buy_amount / 100 }}</td>
          <td>{{ trade.rate }}</td>
          <td>{{ new Date(trade.created_at).toLocaleString() }}</td>
        </tr>
      </tbody>
    </template>

    <template v-else>
      <!-- show message if no trades yet -->
      <p>No trades booked yet</p>
    </template>

    <router-link to="/new" tag="button">New Trade</router-link>
  </div>
</template>


<script>
export default {
  name: "trade-table",

  methods: {
    async getTrades() {
      try {
        const response = await fetch("http://localhost:8000/api/v1/trades");
        const data = await response.json();
        this.trades = data;
      } catch (error) {
        // TODO: provide user with feedback
        console.error(error);
      }
    }
  },

  data() {
    return {
      trades: []
    };
  },

  mounted() {
    this.getTrades();
  },

  computed: {
    hasTrades: function() {
      return this.trades.length;
    }
  }
};
</script>


<style scoped>
button {
  margin-top: 10px;
  margin-right: 10px;
}
</style>
