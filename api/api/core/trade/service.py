from api.core.currency.model import Currency
from api.core.trade.model import Trade


class TradeService:
    """Application Service that deals with foreign currency trades
    """

    def create_trade(self, sell_currency: Currency, sell_amount: int,
                     buy_currency: Currency, buy_amount: int, rate: float) -> Trade:
        """Create trade

        :raises `InconsistentTradeException`:
        """

        return Trade.build(sell_currency, sell_amount, buy_currency, buy_amount, rate)
