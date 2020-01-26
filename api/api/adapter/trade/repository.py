from typing import List

import sqlalchemy.orm as orm

from api.core.trade.model import Trade
from api.core.trade.repository import TradeRepository


class SqlAlchemyTradeRepository(TradeRepository):
    """Trade database repository
    """

    def __init__(self, session: orm.Session):
        self._session = session

    def find_all(self) -> List[Trade]:
        """Retrieve all trades from the database
        """

        return self._session.query(Trade).all()

    def save(self, trade: Trade) -> Trade:
        """Save trade in database
        """

        self._session.add(trade)
        self._session.commit()

        return trade
