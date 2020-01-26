import sqlalchemy.orm as orm

from api.core.trade.model import Trade
from api.core.trade.repository import TradeRepository


class SqlAlchemyTradeRepository(TradeRepository):
    """Trade database repository
    """

    def __init__(self, session: orm.Session):
        self._session = session

    def save(self, trade: Trade) -> Trade:
        """Save trade in database
        """

        self._session.add(trade)
        self._session.commit()

        return trade
