from api.adapter.common import DictTransformerMixin
from api.core.currency import Currency


class CurrencyResponse(DictTransformerMixin):
    """API response model for a currency
    """

    def __init__(self, symbol: str):
        self.symbol = symbol

    @classmethod
    def from_currency(cls, currency: Currency):
        return CurrencyResponse(currency.symbol)
