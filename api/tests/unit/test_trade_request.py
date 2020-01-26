import unittest

from pydantic import ValidationError

from api.adapter.trade.resource import TradeRequest


class TestTradeRequest(unittest.TestCase):

    base_trade_request = {
        'sell_currency': 'EUR',
        'sell_amount': 2350,
        'buy_currency': 'GBP',
        'buy_amount': 1805,
        'rate': 0.9621
    }

    def test_trade_request_requires_mandatory_fields(self):
        for field in self.base_trade_request.keys():
            flawed_trade_request = self.base_trade_request.copy()
            flawed_trade_request.pop(field)

            with self.assertRaises(ValidationError):
                TradeRequest(**flawed_trade_request)

    def test_trade_request_requires_supported_currencies(self):
        currency_symbol = 'unknown'

        flawed_trade_request = self.base_trade_request.copy()
        flawed_trade_request.update({'sell_currency': currency_symbol})
        with self.assertRaises(ValidationError):
            TradeRequest(**flawed_trade_request)

        flawed_trade_request = self.base_trade_request.copy()
        flawed_trade_request.update({'buy_currency': currency_symbol})
        with self.assertRaises(ValidationError):
            TradeRequest(**flawed_trade_request)

    def test_trade_request_requires_positive_numbers(self):
        for number in [0, -1]:
            flawed_trade_request = self.base_trade_request.copy()
            flawed_trade_request.update({'sell_amount': number})
            with self.assertRaises(ValidationError):
                TradeRequest(**flawed_trade_request)

            flawed_trade_request = self.base_trade_request.copy()
            flawed_trade_request.update({'buy_amount': number})
            with self.assertRaises(ValidationError):
                TradeRequest(**flawed_trade_request)

            flawed_trade_request = self.base_trade_request.copy()
            flawed_trade_request.update({'rate': number})
            with self.assertRaises(ValidationError):
                TradeRequest(**flawed_trade_request)
