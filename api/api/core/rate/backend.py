from typing import List

from api.core.currency.model import Currency
from api.core.rate.model import Rate


class RateBackend:
    """Base class for backends that provide us with exchange rates
    """

    def get_rates(self, currency: Currency) -> List[Rate]:
        """Return list of exchange rates from a 3rd-party service (backend)

        :raises `RateBackendErrorException`:
        :raises `RateBackendTimeoutException`:
        """

        raise NotImplementedError()


class RateBackendErrorException(Exception):
    """Exception raised when backend sends an error response
    """

    def __init__(self, status: str = None):
        self.status = status


class RateBackendTimeoutException(Exception):
    """Exception raised when a backend request times out
    """

    pass
