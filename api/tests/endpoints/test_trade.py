from datetime import datetime

import falcon
from falcon import testing

from api.app import get_app


class TestTrades(testing.TestCase):

    def setUp(self):
        super().setUp()
        self.app = get_app()

    def test_create_trade_succeeds(self):
        trade_request = {
            'sell_currency': 'EUR',
            'sell_amount': 2350,
            'buy_currency': 'GBP',
            'buy_amount': 1805,
            'rate': 0.9621
        }
        r = self.simulate_post('/api/v1/trades', json=trade_request)
        self.assertEqual(r.status, falcon.HTTP_201)

        trade_response = r.json
        self.validate_response_body(trade_request, trade_response)

    def test_create_trade_fails_missing_body_return_400(self):
        r = self.simulate_post('/api/v1/trades')
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
        r = self.simulate_post('/api/v1/trades', json=trade_request)
        self.assertEqual(r.status, falcon.HTTP_400)

    def validate_response_body(self, request: dict, response: dict):
        trade_id = response['id']
        self.assertIsInstance(trade_id, str)
        self.assertEqual(len(trade_id), 9)
        self.assertTrue(trade_id.startswith('TR'))

        created_at = response['created_at']
        self.assertIsInstance(created_at, str)
        datetime.strptime(created_at, '%Y/%m/%d %H:%M:%S')  # str can be parsed as a datetime

        for field in request.keys():
            self.assertEqual(request[field], response[field])
