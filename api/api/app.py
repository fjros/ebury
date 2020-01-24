import falcon

from api.adapter.currency import CurrenciesController

BASE_URI = '/api/v1'


def get_app() -> falcon.API:
    """WSGI entry point
    """

    api = falcon.API()
    api.add_route('{}/currencies'.format(BASE_URI), CurrenciesController())
    return api
