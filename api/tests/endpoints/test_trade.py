from datetime import datetime

import falcon
import sqlalchemy
from falcon import testing

from api.app import get_app
from api.config import Configuration


class TestTrades(testing.TestCase):

    endpoint = '/api/v1/trades'

    @classmethod
    def setUpClass(cls):
        cls.engine = sqlalchemy.create_engine(Configuration().database_url)

    def setUp(self):
        super().setUp()
        self.app = get_app()
        self.conn = self.engine.connect()

    def tearDown(self):
        self.conn.execute("DELETE FROM trade")

    def test_create_trade_succeeds(self):
        trade_request = {
            'sell_currency': 'EUR',
            'sell_amount': 2350,
            'buy_currency': 'GBP',
            'buy_amount': 1805,
            'rate': 0.9621
        }
        r = self.simulate_post(self.endpoint, json=trade_request)
        self.assertEqual(r.status, falcon.HTTP_201)

        trade_response = r.json
        self.validate_response_body(trade_request, trade_response)

    def test_create_trade_fails_missing_body_return_400(self):
        r = self.simulate_post(self.endpoint)
        self.assertEqual(r.status, falcon.HTTP_400)

    def test_create_trade_fails_inconsistent_return_400(self):
        """Rate doesn't make sense for the given amounts
        """

        trade_request = {
            'sell_currency': 'EUR',
            'sell_amount': 2350,
            'buy_currency': 'GBP',
            'buy_amount': 1805,
            'rate': 1
        }
        r = self.simulate_post(self.endpoint, json=trade_request)
        self.assertEqual(r.status, falcon.HTTP_400)

    def test_get_trades_success_empty_list(self):
        r = self.simulate_get(self.endpoint)
        self.assertEqual(r.status, falcon.HTTP_200)

        trades_response = r.json
        self.assertEqual(len(trades_response), 0)

    def test_get_trades_success_two_trades(self):
        trade_request = {
            'sell_currency': 'EUR',
            'sell_amount': 2350,
            'buy_currency': 'GBP',
            'buy_amount': 1805,
            'rate': 0.9621
        }

        for i in range(2):
            r = self.simulate_post(self.endpoint, json=trade_request)
            self.assertEqual(r.status, falcon.HTTP_201)

        r = self.simulate_get(self.endpoint)
        self.assertEqual(r.status, falcon.HTTP_200)

        trades_response = r.json
        self.assertEqual(len(trades_response), 2)
        for trade_response in trades_response:
            self.validate_response_body(trade_request, trade_response)

    def validate_response_body(self, request: dict, response: dict):
        trade_id = response['id']
        self.assertIsInstance(trade_id, str)
        self.assertEqual(len(trade_id), 9)
        self.assertTrue(trade_id.startswith('TR'))

        created_at = response['created_at']
        self.assertIsInstance(created_at, str)
        datetime.strptime(created_at, '%Y/%m/%d %H:%M:%S GMT')  # str can be parsed as a datetime

        for field in request.keys():
            self.assertEqual(request[field], response[field])
