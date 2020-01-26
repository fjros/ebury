from typing import List

from api.core.trade.model import Trade


class TradeRepository:
    """Trade database repository
    """

    def find_all(self) -> List[Trade]:
        """Retrieve all trades from the database
        """

        raise NotImplementedError()

    def save(self, trade: Trade) -> Trade:
        """Save trade in database
        """

        raise NotImplementedError()
