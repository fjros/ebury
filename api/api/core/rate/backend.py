from abc import ABC
from abc import abstractmethod
from typing import List

from api.core.currency.model import Currency
from api.core.rate.model import Rate


class RateBackend(ABC):
    """Base class for backends that provide us with exchange rates
    """

    @abstractmethod
    def get_rates(self, currency: Currency) -> List[Rate]:
        """Return list of exchange rates from a 3rd-party service (backend)

        :raises `RateBackendErrorException`:
        :raises `RateBackendTimeoutException`:
        """

        pass  # pragma: no cover


class RateBackendErrorException(Exception):
    """Exception raised when backend sends an error response
    """

    def __init__(self, status: str = None):
        self.status = status

    def errors(self):
        return [
            {
                'loc': [''],
                'msg': 'error response from backend: {}'.format(self.status),
                'type': 'bad_gateway'
            }
        ]


class RateBackendTimeoutException(Exception):
    """Exception raised when a backend request times out
    """

    def errors(self):
        return [
            {
                'loc': [''],
                'msg': 'backend response timed out',
                'type': 'gateway_timeout'
            }
        ]
