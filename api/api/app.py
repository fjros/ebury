import falcon

from api.adapter.currency.controller import CurrenciesController
from api.adapter.rate.controller import RatesController
from api.adapter.trade.controller import TradesController
from api.config import Configuration
from api.middleware import SessionManagerMiddleware


def get_app() -> falcon.API:
    """WSGI entry point
    """

    session_manager = SessionManagerMiddleware()
    api = falcon.API(middleware=[session_manager])

    config = Configuration()
    api.add_route('{}/currencies'.format(config.base_uri), CurrenciesController())
    api.add_route('{}/rates'.format(config.base_uri), RatesController())
    api.add_route('{}/trades'.format(config.base_uri), TradesController())

    return api
