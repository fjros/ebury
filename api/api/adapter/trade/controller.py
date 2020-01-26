import falcon

from api.adapter.common.deserializer import Deserializer
from api.adapter.common.serializer import Serializer
from api.adapter.trade.resource import TradeRequest
from api.adapter.trade.resource import TradeResponse
from api.core.currency.model import Currency
from api.core.trade.model import Trade
from api.core.trade.model import InconsistentTradeException
from api.core.trade.service import TradeService


class TradesController:
    """Controller of the /trades endpoint
    """

    def on_post(self, request: falcon.Request, response: falcon.Response):
        """Create a trade
        """

        trade_request = self._parse_trade_request(request)
        trade = self._create_trade(trade_request)

        body = TradeResponse.from_trade(trade).dict()
        response.body = Serializer.output(body)
        response.set_header('Location', '{}/{}'.format(request.uri, trade.id))
        response.status = falcon.HTTP_201

    def _parse_trade_request(self, request: falcon.Request) -> TradeRequest:
        try:
            payload = request.stream.read(request.content_length or 0).decode('utf-8')
            resource = Deserializer.input(payload)
            return TradeRequest(**resource)

        except Exception:
            raise falcon.HTTPBadRequest()

    def _create_trade(self, trade_request: TradeRequest) -> Trade:
        sell_currency = Currency(trade_request.sell_currency)
        buy_currency = Currency(trade_request.buy_currency)

        service = TradeService()
        try:
            return service.create_trade(sell_currency, trade_request.sell_amount,
                                        buy_currency, trade_request.buy_amount,
                                        trade_request.rate)

        except InconsistentTradeException:
            raise falcon.HTTPBadRequest()
