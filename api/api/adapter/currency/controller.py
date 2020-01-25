import falcon

from api.adapter.common.serializer import Serializer
from api.adapter.currency.resource import CurrencyResponse
from api.core.currency.service import CurrencyService


class CurrenciesController:
    """Controller of the /currencies endpoint
    """

    def on_get(self, request: falcon.Request, response: falcon.Response):
        """Return the list of available currencies
        """

        service = CurrencyService()
        currencies = service.get_currencies()

        body = [CurrencyResponse.from_currency(currency).dict() for currency in currencies]
        response.body = Serializer.output(body)
        response.status = falcon.HTTP_200
