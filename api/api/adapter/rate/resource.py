from pydantic import BaseModel
from pydantic import validator

from api.adapter.common.resource import ToDictMixin
from api.core.currency.model import Currency
from api.core.rate.model import Rate


class RateRequest(BaseModel):
    """API request model to query the rates for a given base ('sell') currency
    """

    symbol: str

    @validator('symbol')
    def symbol_must_be_supported(cls, symbol):
        return Currency(symbol).symbol


class RateResponse(ToDictMixin):
    """API response model for an exchange rate
    """

    def __init__(self, sell_currency: str, buy_currency: str, rate: float):
        self.sell_currency = sell_currency
        self.buy_currency = buy_currency
        self.rate = rate

    @classmethod
    def from_rate(cls, rate: Rate):
        return RateResponse(rate.sell_currency.symbol, rate.buy_currency.symbol, rate.rate)
