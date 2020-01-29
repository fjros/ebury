from abc import ABC
from abc import abstractmethod
from typing import List

from api.core.trade.model import Trade


class TradeRepository(ABC):
    """Trade database repository
    """

    @abstractmethod
    def find_all(self) -> List[Trade]:
        """Retrieve all trades from the database
        """

        raise NotImplementedError()

    @abstractmethod
    def save(self, trade: Trade) -> Trade:
        """Save trade in database
        """

        raise NotImplementedError()
