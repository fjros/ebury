from typing import Any
from typing import List

from api.binding.repository import TradeRepositoryBinding
from api.core.currency.model import Currency
from api.core.trade.model import Trade


class TradeService:
    """Application Service that deals with foreign currency trades

    It needs a database session object which is understood by the underlying repository.
    """

    def __init__(self, session: Any):
        self._repository = TradeRepositoryBinding.get(session)

    def create_trade(self, sell_currency: Currency, sell_amount: int,
                     buy_currency: Currency, buy_amount: int, rate: float) -> Trade:
        """Create trade

        :raises `InconsistentTradeException`:
        """

        trade = Trade.build(sell_currency, sell_amount, buy_currency, buy_amount, rate)
        return self._repository.save(trade)

    def get_trades(self) -> List[Trade]:
        """Get list of booked trades
        """

        return self._repository.find_all()
