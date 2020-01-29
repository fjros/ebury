from api.core.currency.model import Currency


class Rate:
    """Rate model
    """

    def __init__(self, sell_currency: Currency, buy_currency: Currency, rate: float):
        self._sell_currency = sell_currency
        self._buy_currency = buy_currency
        self._rate = rate

    @property
    def sell_currency(self) -> Currency:
        return self._sell_currency

    @property
    def buy_currency(self) -> Currency:
        return self._buy_currency

    @property
    def rate(self) -> float:
        return self._rate
