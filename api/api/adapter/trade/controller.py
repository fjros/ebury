from typing import List

import falcon
from pydantic import ValidationError

from api.adapter.common.error import HTTPErrorResponse
from api.adapter.trade.resource import TradeRequest
from api.adapter.trade.resource import TradeResponse
from api.binding.transformer import TransformerBinding
from api.core.trade.model import Trade
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

        except ValidationError as e:
            raise HTTPErrorResponse(falcon.HTTP_400, errors=e.errors())

        except Exception:
            raise HTTPErrorResponse(
                falcon.HTTP_400,
                errors=[{'loc': [''], 'msg': 'cannot read request body', 'type': 'value_error'}]
            )

    def _create_trade(self, request_context, trade_request: TradeRequest) -> Trade:
        service = TradeService(request_context.session)
        return service.create_trade(trade_request.sell_currency,
                                    trade_request.sell_amount,
                                    trade_request.buy_currency,
                                    trade_request.buy_amount,
                                    trade_request.rate)

    def _get_trades(self, request_context) -> List[Trade]:
        service = TradeService(request_context.session)
        return service.get_trades()
