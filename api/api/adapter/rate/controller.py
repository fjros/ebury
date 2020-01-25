import falcon

from api.config import Configuration
from api.adapter.common.serializer import Serializer
from api.adapter.rate.resource import RateResponse
from api.adapter.rate.backend import FixerRateBackend
from api.core.currency.model import Currency
from api.core.rate.service import RateService
from api.core.rate.backend import RateBackendErrorException
from api.core.rate.backend import RateBackendTimeoutException


class RatesController:
    """Controller of the /rates endpoint
    """

    def __init__(self, config: Configuration):
        self.config = config

    def on_get(self, request: falcon.Request, response: falcon.Response):
        """Return the list of 'buy' rates for a given 'sell' currency
        """

        backend = FixerRateBackend(self.config.fixer_access_key)
        service = RateService(backend)

        symbol = request.get_param('currency')
        currency = Currency(symbol)
        try:
            rates = service.get_rates(currency)

        except RateBackendErrorException:
            raise falcon.HTTPBadGateway()

        except RateBackendTimeoutException:
            raise falcon.HTTPGatewayTimeout()

        body = [RateResponse.from_rate(rate).dict() for rate in rates]
        response.body = Serializer.output(body)
        response.status = falcon.HTTP_200
