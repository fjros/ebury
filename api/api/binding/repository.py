from typing import Any

from api.adapter.trade.repository import SqlAlchemyTradeRepository
from api.core.trade.repository import TradeRepository


class TradeRepositoryBinding:
    """Return concrete implementation of the `TradeRepository` abstract class
    """

    @classmethod
    def get(cls, session: Any) -> TradeRepository:
        return SqlAlchemyTradeRepository(session)
