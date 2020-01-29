from typing import Dict
from typing import List
from typing import Union

from pydantic import BaseModel

from api.adapter.common.http import HttpJson
from api.adapter.common.http import HttpJsonErrorException
from api.adapter.common.http import HttpJsonTimeoutException
from api.core.currency.model import Currency
from api.core.rate.backend import RateBackend
from api.core.rate.backend import RateBackendErrorException
from api.core.rate.backend import RateBackendTimeoutException
from api.core.rate.model import Rate


class FixerRateBackend(RateBackend):
    """Rate backend implementation for fixer.io
    """

    base_currency = Currency('EUR')
    endpoint = 'http://data.fixer.io/api/latest'
    timeout = 5  # seconds

    def __init__(self, access_key: str):
        self._access_key = access_key

    def get_rates(self, currency: Currency) -> List[Rate]:
        """Return list of exchange rates from fixer.io

        :raises `RateBackendErrorException`: Error response from fixer.io
        :raises `RateBackendTimeoutException`: Timed out before getting response from fixer.io
        """

        q_params = {'access_key': self._access_key}
        if currency != self.base_currency:
            q_params.update({'base': currency.symbol})

        try:
            raw_response = HttpJson.get(self.endpoint, q_params)

        except HttpJsonErrorException as e:
            raise RateBackendErrorException(e.status)

        except HttpJsonTimeoutException:
            raise RateBackendTimeoutException()

        response = FixerResponse(**raw_response)
        return response.get_rates()


class FixerResponse(BaseModel):
    """Response from fixer.io
    """

    success: bool                             # common

    timestamp: int = None                     # success response
    base: str = None
    rates: Dict[str, float] = None

    error: Dict[str, Union[int, str]] = None  # error response

    def get_rates(self) -> List[Rate]:
        """Build list of rate models from the fixer.io response

        :raises `RateBackendErrorException`: Error response from fixer.io
        """

        if not self.success:
            raise RateBackendErrorException()

        return [
            Rate(Currency(self.base), Currency(buy_currency), rate)
            for buy_currency, rate in self.rates.items()
        ]
