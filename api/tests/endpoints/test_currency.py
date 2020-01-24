import falcon
from falcon import testing

from api.app import get_app
from api.core.currency.model import Currency


class TestGetCurrencies(testing.TestCase):

    def setUp(self):
        super().setUp()
        self.app = get_app()

    def test_get_currencies_succeeds(self):
        r = self.simulate_get('/api/v1/currencies')
        self.assertEqual(r.status, falcon.HTTP_200)

        response_symbols = {currency['symbol'] for currency in r.json}
        expected_symbols = Currency.all_symbols()
        self.assertSetEqual(response_symbols, set(expected_symbols))
