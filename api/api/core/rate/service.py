from typing import List

from api.binding.backend import RateBackendBinding
from api.core.currency.model import Currency
from api.core.rate.model import Rate


class RateService:
    """Application Service that deals with exchange rates
    """

    def __init__(self):
        self._backend = RateBackendBinding.get()

    def get_rates(self, symbol: str) -> List[Rate]:
        """Return list of exchange rates for the given 'sell' currency

        Exchange rates are retrieved from a 3rd-party provider (backend).

        :raises `BackendError`: Error response from rates backend.
        :raises `BackendTimeout`: Timed out before getting response from rates backend.
        """

        currency = Currency(symbol)
        return self._backend.get_rates(currency)
