<template>
    <div id="trade-table">
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

        <template v-if="hasTrades">  <!-- show trades -->
            <tbody>
            <tr v-for="trade in trades" :key="trade.id">
                    <td>{{ trade.sell_currency }}</td>
                    <td>{{ trade.sell_amount }}</td>
                    <td>{{ trade.buy_currency }}</td>
                    <td>{{ trade.buy_amount }}</td>
                    <td>{{ trade.rate }}</td>
                    <td>{{ trade.created_at }}</td>
                </tr>
            </tbody>
        </template>
        
        <template v-else>            <!-- show message if no trades yet -->
            <p>No trades booked yet</p>
        </template>
    </div>
</template>


<script>
    export default {
        name: 'trade-table',
        props: {
            trades: Array,
        },
        computed: {
            hasTrades: function() {
                return this.trades.length
            }
        }
    }
</script>


<style scoped></style>
