<template>
  <div id="trade-form">
    <h1>New Trade</h1>
    <form>
      <label>Sell Currency</label>
      <select v-model="trade.sell_currency" @change="onSellCurrencyChange()">
        <option value></option>
        <option v-for="currency in currencies" v-bind:key="currency.symbol">{{ currency.symbol }}</option>
      </select>

      <label>Sell Amount</label>
      <input type="number" min="0.01" step="0.01" v-model="trade.sell_amount" @change="onSellAmountChange()"/>

      <label>Buy Currency</label>
      <select v-model="trade.buy_currency" @change="onBuyCurrencyChange()">
        <option v-for="currency in currencies" v-bind:key="currency.symbol">{{ currency.symbol }}</option>
      </select>

      <label>Buy Amount</label>
      <input type="number" v-model="trade.buy_amount" readonly />

      <label>Rate</label>
      <p>{{ trade.rate }}</p>

      <button @click.prevent="onSubmit">Create</button>
      <button @click.prevent="onCancel">Cancel</button>
    </form>
  </div>
</template>


<script>
export default {
  name: "trade-form",

  methods: {
    async createTrade() {
      if (
        this.trade.sell_currency === "" ||
        this.trade.buy_currency === "" ||
        this.trade.sell_amount <= 0 ||
        this.trade.buy_amount <= 0 ||
        this.trade.rate <= 0
      ) {
        // TODO: provide user with feedback
        return;
      }

      try {
        const response = await fetch("/api/v1/trades", {
          method: "post",
          body: JSON.stringify({
            sell_currency: this.trade.sell_currency,
            sell_amount: this.trade.sell_amount * 100, // cents
            buy_currency: this.trade.buy_currency,
            buy_amount: this.trade.buy_amount * 100, // cents
            rate: this.trade.rate
          })
        });
        const data = await response.json();
        this.currencies = data;
        this.$router.push({ path: "/" });
      } catch (error) {
        // TODO: provide user with feedback
        console.error(error);
      }
    },

    async getCurrencies() {
      try {
        const response = await fetch("/api/v1/currencies");
        const data = await response.json();
        this.currencies = data;
      } catch (error) {
        // TODO: provide user with feedback
        console.error(error);
      }
    },

    async getRates() {
      if (this.trade.sell_currency === "") {
        // the base currency is required to make the API call
        return;
      }

      try {
        // could cache rates to avoid API calls...
        // but likely "rate freshness" is more important here
        const response = await fetch("/api/v1/rates?symbol=" + this.trade.sell_currency);
        const data = await response.json();
        this.rates = data;

        this.setRate();
        this.setBuyAmount();
      } catch (error) {
        // TODO: provide user with feedback
        this.cleanUp();
        console.error(error);
      }
    },

    setRate() {
      let rate = this.rates.find(
        r =>
          r.sell_currency === this.trade.sell_currency &&
          r.buy_currency === this.trade.buy_currency
      );

      if (rate) {
        this.trade.rate = rate.rate;
      }
    },

    setBuyAmount() {
      this.trade.buy_amount =
        Math.round(this.trade.sell_amount * this.trade.rate * 100) / 100;
    },

    onSellCurrencyChange() {
      this.getRates();
    },

    onBuyCurrencyChange() {
      this.setRate();
      this.setBuyAmount();
    },

    onSellAmountChange() {
      this.setRate();
      this.setBuyAmount();
    },

    onSubmit() {
      this.createTrade();
    },

    onCancel() {
      this.$router.push({ path: "/" });
    },

    cleanUp() {
      this.rates = [];
      this.trade.rate = 0.0;
      this.trade.buy_amount = 0.0;
    }
  },

  data() {
    return {
      trade: {
        sell_currency: "",
        sell_amount: 1000.0,
        buy_currency: "",
        buy_amount: 0,
        rate: 0
      },
      currencies: [],
      rates: []
    };
  },

  mounted() {
    this.getCurrencies();
  }
};
</script>


<style scoped>
button {
  margin-top: 10px;
  margin-right: 10px;
}
</style>
