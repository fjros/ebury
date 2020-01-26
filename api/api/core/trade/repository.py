from api.core.trade.model import Trade


class TradeRepository:
    """Trade database repository
    """

    def save(self, trade: Trade) -> Trade:
        """Save trade in database
        """

        raise NotImplementedError()
