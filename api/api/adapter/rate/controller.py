from typing import List

import falcon
from pydantic import ValidationError

from api.adapter.rate.resource import RateRequest
from api.adapter.rate.resource import RateResponse
from api.binding.transformer import TransformerBinding
from api.core.rate.backend import RateBackendErrorException
from api.core.rate.backend import RateBackendTimeoutException
from api.core.rate.model import Rate
from api.core.rate.service import RateService


class RatesController:
    """Controller of the /rates endpoint
    """

    def on_get(self, request: falcon.Request, response: falcon.Response):
        """Return the list of 'buy' rates for a given 'sell' currency

        The symbol of the 'sell' currency is given via a query param.
        """

        rate_request = self._parse_rate_request(request)
        rates = self._get_rates(rate_request.symbol)

        body = [RateResponse.from_rate(rate).dict() for rate in rates]
        response.body = TransformerBinding.get().serialize(body)
        response.status = falcon.HTTP_200

    def _parse_rate_request(self, request: falcon.Request) -> RateRequest:
        try:
            return RateRequest(symbol=request.get_param('symbol'))

        except ValidationError:
            raise falcon.HTTPBadRequest()

    def _get_rates(self, symbol: str) -> List[Rate]:
        service = RateService()

        try:
            return service.get_rates(symbol)

        except RateBackendErrorException:
            raise falcon.HTTPBadGateway()

        except RateBackendTimeoutException:
            raise falcon.HTTPGatewayTimeout()
