import falcon

from api.adapter.currency.controller import CurrenciesController
from api.adapter.rate.controller import RatesController
from api.adapter.trade.controller import TradesController
from api.config import Configuration
from api.middleware import DatabaseSessionManager


def get_app() -> falcon.API:
    """WSGI entry point
    """

    config = Configuration()
    session_manager = DatabaseSessionManager(config)

    api = falcon.API(middleware=[session_manager])

    api.add_route('{}/currencies'.format(config.base_uri), CurrenciesController())
    api.add_route('{}/rates'.format(config.base_uri), RatesController(config))
    api.add_route('{}/trades'.format(config.base_uri), TradesController())

    return api
