from api.adapter.common.serializer import DictTransformerMixin
from api.core.rate.model import Rate


class RateResponse(DictTransformerMixin):
    """API response model for an exchange rate
    """

    def __init__(self, sell_currency: str, buy_currency: str, rate: float):
        self.sell_currency = sell_currency
        self.buy_currency = buy_currency
        self.rate = rate

    @classmethod
    def from_rate(cls, rate: Rate):
        return RateResponse(rate.sell_currency.symbol, rate.buy_currency.symbol, rate.rate)
