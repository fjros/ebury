from typing import List

import falcon

from api.adapter.trade.resource import TradeRequest
from api.adapter.trade.resource import TradeResponse
from api.binding.transformer import TransformerBinding
from api.core.currency.model import Currency
from api.core.trade.model import Trade
from api.core.trade.model import InconsistentTradeException
from api.core.trade.service import TradeService


class TradesController:
    """Controller of the /trades endpoint
    """

    def on_get(self, request: falcon.Request, response: falcon.Response):
        """Get list of trades
        """

        trades = self._get_trades(request.context)

        body = [TradeResponse.from_trade(trade).dict() for trade in trades]
        response.body = TransformerBinding.get().serialize(body)
        response.status = falcon.HTTP_200

    def on_post(self, request: falcon.Request, response: falcon.Response):
        """Create a trade
        """

        trade_request = self._parse_trade_request(request)
        trade = self._create_trade(request.context, trade_request)

        body = TradeResponse.from_trade(trade).dict()
        response.body = TransformerBinding.get().serialize(body)
        response.set_header('Location', '{}/{}'.format(request.uri, trade.id))
        response.status = falcon.HTTP_201

    def _parse_trade_request(self, request: falcon.Request) -> TradeRequest:
        try:
            payload = request.stream.read(request.content_length or 0).decode('utf-8')
            resource = TransformerBinding.get().deserialize(payload)
            return TradeRequest(**resource)

        except Exception:
            raise falcon.HTTPBadRequest()

    def _create_trade(self, request_context, trade_request: TradeRequest) -> Trade:
        sell_currency = Currency(trade_request.sell_currency)
        buy_currency = Currency(trade_request.buy_currency)

        service = TradeService(request_context.session)
        try:
            return service.create_trade(sell_currency,
                                        trade_request.sell_amount,
                                        buy_currency,
                                        trade_request.buy_amount,
                                        trade_request.rate)

        except InconsistentTradeException:
            raise falcon.HTTPBadRequest()

    def _get_trades(self, request_context) -> List[Trade]:
        service = TradeService(request_context.session)
        return service.get_trades()
