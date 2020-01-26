import falcon

from api.adapter.currency.controller import CurrenciesController
from api.adapter.rate.controller import RatesController
from api.adapter.trade.controller import TradesController
from api.config import Configuration


def get_app() -> falcon.API:
    """WSGI entry point
    """

    config = Configuration()

    api = falcon.API()
    api.add_route('{}/currencies'.format(config.base_uri), CurrenciesController())
    api.add_route('{}/rates'.format(config.base_uri), RatesController(config))
    api.add_route('{}/trades'.format(config.base_uri), TradesController())
    return api
