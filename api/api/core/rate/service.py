from typing import List

from api.core.currency.model import Currency
from api.core.rate.backend import RateBackend
from api.core.rate.model import Rate


class RateService:
    """Application Service that deals with exchange rates
    """

    def __init__(self, backend: RateBackend):
        self.backend = backend

    def get_rates(self, currency: Currency) -> List[Rate]:
        """Return list of exchange rates for the given 'sell' currency

        Exchange rates are retrieved from a 3rd-party provider (backend).

        :raises `BackendError`: Error response from rates backend.
        :raises `BackendTimeout`: Timed out before getting response from rates backend.
        """

        return self.backend.get_rates(currency)
