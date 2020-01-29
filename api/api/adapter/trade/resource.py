from pydantic import BaseModel
from pydantic import root_validator
from pydantic import validator

from api.adapter.common.resource import ToDictMixin
from api.core.currency.model import Currency
from api.core.trade.model import Trade


class TradeRequest(BaseModel):
    """API request model for a trade
    """

    sell_currency: str
    sell_amount: int
    buy_currency: str
    buy_amount: int
    rate: float

    @validator('sell_currency')
    def sell_currency_symbol_supported(cls, symbol):
        return cls._validate_supported_symbol(symbol)

    @validator('sell_amount')
    def sell_amount_positive(cls, amount):
        return cls._validate_positive_number(amount)

    @validator('buy_currency')
    def buy_currency_symbol_supported(cls, symbol):
        return cls._validate_supported_symbol(symbol)

    @validator('buy_amount')
    def buy_amount_positive(cls, amount):
        return cls._validate_positive_number(amount)

    @validator('rate')
    def rate_positive(cls, rate):
        return cls._validate_positive_number(rate)

    @root_validator
    def trade_consistency(cls, values):
        sell_amount = values.get('sell_amount')
        buy_amount = values.get('buy_amount')
        rate = values.get('rate')

        Trade.check_consistency(sell_amount, buy_amount, rate)
        return values

    @classmethod
    def _validate_positive_number(cls, amount):
        if amount <= 0:
            raise ValueError('number must be greater than zero')

        return amount

    @classmethod
    def _validate_supported_symbol(cls, symbol):
        return Currency(symbol).symbol


class TradeResponse(ToDictMixin):
    """API response model for a trade
    """

    def __init__(self,
                 id: str,
                 sell_currency: str,
                 sell_amount: int,
                 buy_currency: str,
                 buy_amount: int,
                 rate: float,
                 created_at: str):
        self.id = id
        self.sell_currency = sell_currency
        self.sell_amount = sell_amount
        self.buy_currency = buy_currency
        self.buy_amount = buy_amount
        self.rate = rate
        self.created_at = created_at

    @classmethod
    def from_trade(cls, trade: Trade):
        return TradeResponse(trade.id,
                             trade.sell_currency,
                             trade.sell_amount,
                             trade.buy_currency,
                             trade.buy_amount,
                             trade.rate,
                             trade.created_at.strftime('%Y/%m/%d %H:%M:%S GMT'))
