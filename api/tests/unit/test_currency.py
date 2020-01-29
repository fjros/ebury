import unittest

from api.core.currency.model import Currency


class TestCurrency(unittest.TestCase):

    def test_currencies_are_equal(self):
        self.assertEqual(Currency('EUR'), Currency('eur'))

    def test_currencies_are_not_equal(self):
        self.assertNotEqual(Currency('EUR'), Currency('USD'))
