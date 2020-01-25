import json

import falcon
import requests_mock
import requests.exceptions
from falcon import testing

from api.app import get_app


class TestGetRates(testing.TestCase):

    fixer_endpoint = 'http://data.fixer.io/api/latest'

    def setUp(self):
        super().setUp()
        self.app = get_app()

    @requests_mock.Mocker()
    def test_get_eur_rates_succeeds(self, mock):
        mock.get(self.fixer_endpoint, status_code=200, text=fixture_get_eur_rates_succeeds)

        base = 'EUR'
        r = self.simulate_get('/api/v1/rates', params={'currency': base})
        self.assertEqual(r.status, falcon.HTTP_200)

        fixture = json.loads(fixture_get_eur_rates_succeeds)
        response_rates = r.json
        for response_rate in response_rates:
            sell_currency = response_rate['sell_currency']
            buy_currency = response_rate['buy_currency']
            rate = response_rate['rate']

            self.assertEqual(sell_currency, base)
            self.assertEqual(rate, fixture['rates'].get(buy_currency))

    @requests_mock.Mocker()
    def test_get_usd_rates_succeeds(self, mock):
        """This test simulates you have a paid plan in fixer.io
        """

        mock.get(self.fixer_endpoint, status_code=200, text=fixture_get_usd_rates_succeeds)

        base = 'USD'
        r = self.simulate_get('/api/v1/rates', params={'currency': base})
        self.assertEqual(r.status, falcon.HTTP_200)

        fixture = json.loads(fixture_get_usd_rates_succeeds)
        response_rates = r.json
        for response_rate in response_rates:
            sell_currency = response_rate['sell_currency']
            buy_currency = response_rate['buy_currency']
            rate = response_rate['rate']

            self.assertEqual(sell_currency, base)
            self.assertEqual(rate, fixture['rates'].get(buy_currency))

    def test_get_rates_fails_missing_currency_return_400(self):
        r = self.simulate_get('/api/v1/rates')
        self.assertEqual(r.status, falcon.HTTP_400)

    def test_get_rates_fails_unknown_currency_return_400(self):
        r = self.simulate_get('/api/v1/rates', params={'currency': 'unknown'})
        self.assertEqual(r.status, falcon.HTTP_400)

    @requests_mock.Mocker()
    def test_get_usd_rates_fails_free_plan_return_502(self, mock):
        """This test simulates you have a free plan in fixer.io
        """

        mock.get(self.fixer_endpoint, status_code=200, text=fixture_get_usd_rates_fails)

        base = 'USD'
        r = self.simulate_get('/api/v1/rates', params={'currency': base})
        self.assertEqual(r.status, falcon.HTTP_502)

    @requests_mock.Mocker()
    def test_get_rates_fails_backend_error_return_502(self, mock):
        mock.get(self.fixer_endpoint, status_code=400)

        base = 'EUR'
        r = self.simulate_get('/api/v1/rates', params={'currency': base})
        self.assertEqual(r.status, falcon.HTTP_502)

    @requests_mock.Mocker()
    def test_get_rates_fails_backend_timeout_return_504(self, mock):
        mock.get(self.fixer_endpoint, exc=requests.exceptions.Timeout)

        base = 'EUR'
        r = self.simulate_get('/api/v1/rates', params={'currency': base})
        self.assertEqual(r.status, falcon.HTTP_504)


fixture_get_eur_rates_succeeds = '''{
    "success": true,
    "timestamp": 1579890665,
    "base": "EUR",
    "date": "2020-01-24",
    "rates": {
        "AED": 4.050953,
        "AFN": 84.922779,
        "ALL": 122.007026,
        "AMD": 528.1404,
        "ANG": 1.825643,
        "AOA": 547.642879,
        "ARS": 66.272101,
        "AUD": 1.616784,
        "AWG": 1.985198,
        "AZN": 1.879288,
        "BAM": 1.955002,
        "BBD": 2.227277,
        "BDT": 93.598704,
        "BGN": 1.954818,
        "BHD": 0.415837,
        "BIF": 2084.458237,
        "BMD": 1.102888,
        "BND": 1.490382,
        "BOB": 7.628039,
        "BRL": 4.614157,
        "BSD": 1.103143,
        "BTC": 0.00013,
        "BTN": 78.643003,
        "BWP": 11.836095,
        "BYN": 2.329913,
        "BYR": 21616.603938,
        "BZD": 2.223579,
        "CAD": 1.449394,
        "CDF": 1859.469493,
        "CHF": 1.070651,
        "CLF": 0.031061,
        "CLP": 857.058545,
        "CNY": 7.650407,
        "COP": 3717.879415,
        "CRC": 623.811483,
        "CUC": 1.102888,
        "CUP": 29.226531,
        "CVE": 110.702423,
        "CZK": 25.154011,
        "DJF": 196.005682,
        "DKK": 7.473114,
        "DOP": 58.982881,
        "DZD": 132.185931,
        "EGP": 17.422767,
        "ERN": 16.543714,
        "ETB": 35.45828,
        "EUR": 1,
        "FJD": 2.390514,
        "FKP": 0.843344,
        "GBP": 0.843313,
        "GEL": 3.181876,
        "GGP": 0.843344,
        "GHS": 6.19276,
        "GIP": 0.843344,
        "GMD": 56.413149,
        "GNF": 10367.147179,
        "GTQ": 8.482885,
        "GYD": 230.114639,
        "HKD": 8.572263,
        "HNL": 27.407194,
        "HRK": 7.443836,
        "HTG": 109.202738,
        "HUF": 336.131618,
        "IDR": 15009.808782,
        "ILS": 3.810423,
        "IMP": 0.843344,
        "INR": 78.635364,
        "IQD": 1312.436668,
        "IRR": 46437.097778,
        "ISK": 137.409236,
        "JEP": 0.843344,
        "JMD": 152.228912,
        "JOD": 0.781991,
        "JPY": 120.508711,
        "KES": 111.278462,
        "KGS": 77.030442,
        "KHR": 4467.799497,
        "KMF": 492.605329,
        "KPW": 992.666087,
        "KRW": 1290.58888,
        "KWD": 0.335062,
        "KYD": 0.919319,
        "KZT": 417.553182,
        "LAK": 9807.982978,
        "LBP": 1667.959112,
        "LKR": 200.296795,
        "LRD": 213.960648,
        "LSL": 15.915094,
        "LTL": 3.256542,
        "LVL": 0.667126,
        "LYD": 1.548195,
        "MAD": 10.639013,
        "MDL": 19.524831,
        "MGA": 4037.67319,
        "MKD": 61.588918,
        "MMK": 1618.259231,
        "MNT": 3030.222391,
        "MOP": 8.83074,
        "MRO": 393.730857,
        "MUR": 40.533339,
        "MVR": 17.040036,
        "MWK": 810.623028,
        "MXN": 20.743562,
        "MYR": 4.483282,
        "MZN": 69.86248,
        "NAD": 15.915089,
        "NGN": 398.698106,
        "NIO": 37.785357,
        "NOK": 9.976851,
        "NPR": 125.828851,
        "NZD": 1.669701,
        "OMR": 0.42462,
        "PAB": 1.103143,
        "PEN": 3.667658,
        "PGK": 3.730523,
        "PHP": 56.050425,
        "PKR": 170.620851,
        "PLN": 4.253784,
        "PYG": 7192.819198,
        "QAR": 4.015657,
        "RON": 4.782237,
        "RSD": 117.524152,
        "RUB": 68.587541,
        "RWF": 1031.200239,
        "SAR": 4.137672,
        "SBD": 9.155119,
        "SCR": 15.108519,
        "SDG": 49.964881,
        "SEK": 10.554671,
        "SGD": 1.490228,
        "SHP": 0.843344,
        "SLL": 10698.013547,
        "SOS": 642.984052,
        "SRD": 8.22538,
        "STD": 23779.135614,
        "SVC": 9.652999,
        "SYP": 567.985996,
        "SZL": 15.915081,
        "THB": 33.671577,
        "TJS": 10.694571,
        "TMT": 3.860108,
        "TND": 3.114597,
        "TOP": 2.537787,
        "TRY": 6.555608,
        "TTD": 7.458909,
        "TWD": 33.136824,
        "TZS": 2542.666315,
        "UAH": 26.937693,
        "UGX": 4053.883279,
        "USD": 1.102888,
        "UYU": 41.184932,
        "UZS": 10527.065909,
        "VEF": 11.015098,
        "VND": 25556.671161,
        "VUV": 128.681078,
        "WST": 2.91508,
        "XAF": 655.622889,
        "XAG": 0.06082,
        "XAU": 0.000701,
        "XCD": 2.98061,
        "XDR": 0.799493,
        "XOF": 656.218701,
        "XPF": 119.777602,
        "YER": 276.056823,
        "ZAR": 15.901222,
        "ZMK": 9927.319033,
        "ZMW": 15.967483,
        "ZWL": 355.129923
    }
}
'''

fixture_get_usd_rates_succeeds = '''{
    "success": true,
    "timestamp": 1579890665,
    "base": "USD",
    "date": "2020-01-24",
    "rates": {
        "AED": 4.050953,
        "AFN": 84.922779,
        "ALL": 122.007026,
        "AMD": 528.1404,
        "ANG": 1.825643,
        "AOA": 547.642879,
        "ARS": 66.272101,
        "AUD": 1.616784,
        "AWG": 1.985198,
        "AZN": 1.879288,
        "BAM": 1.955002,
        "BBD": 2.227277,
        "BDT": 93.598704,
        "BGN": 1.954818,
        "BHD": 0.415837,
        "BIF": 2084.458237,
        "BMD": 1.102888,
        "BND": 1.490382,
        "BOB": 7.628039,
        "BRL": 4.614157,
        "BSD": 1.103143,
        "BTC": 0.00013,
        "BTN": 78.643003,
        "BWP": 11.836095,
        "BYN": 2.329913,
        "BYR": 21616.603938,
        "BZD": 2.223579,
        "CAD": 1.449394,
        "CDF": 1859.469493,
        "CHF": 1.070651,
        "CLF": 0.031061,
        "CLP": 857.058545,
        "CNY": 7.650407,
        "COP": 3717.879415,
        "CRC": 623.811483,
        "CUC": 1.102888,
        "CUP": 29.226531,
        "CVE": 110.702423,
        "CZK": 25.154011,
        "DJF": 196.005682,
        "DKK": 7.473114,
        "DOP": 58.982881,
        "DZD": 132.185931,
        "EGP": 17.422767,
        "ERN": 16.543714,
        "ETB": 35.45828,
        "EUR": 1,
        "FJD": 2.390514,
        "FKP": 0.843344,
        "GBP": 0.843313,
        "GEL": 3.181876,
        "GGP": 0.843344,
        "GHS": 6.19276,
        "GIP": 0.843344,
        "GMD": 56.413149,
        "GNF": 10367.147179,
        "GTQ": 8.482885,
        "GYD": 230.114639,
        "HKD": 8.572263,
        "HNL": 27.407194,
        "HRK": 7.443836,
        "HTG": 109.202738,
        "HUF": 336.131618,
        "IDR": 15009.808782,
        "ILS": 3.810423,
        "IMP": 0.843344,
        "INR": 78.635364,
        "IQD": 1312.436668,
        "IRR": 46437.097778,
        "ISK": 137.409236,
        "JEP": 0.843344,
        "JMD": 152.228912,
        "JOD": 0.781991,
        "JPY": 120.508711,
        "KES": 111.278462,
        "KGS": 77.030442,
        "KHR": 4467.799497,
        "KMF": 492.605329,
        "KPW": 992.666087,
        "KRW": 1290.58888,
        "KWD": 0.335062,
        "KYD": 0.919319,
        "KZT": 417.553182,
        "LAK": 9807.982978,
        "LBP": 1667.959112,
        "LKR": 200.296795,
        "LRD": 213.960648,
        "LSL": 15.915094,
        "LTL": 3.256542,
        "LVL": 0.667126,
        "LYD": 1.548195,
        "MAD": 10.639013,
        "MDL": 19.524831,
        "MGA": 4037.67319,
        "MKD": 61.588918,
        "MMK": 1618.259231,
        "MNT": 3030.222391,
        "MOP": 8.83074,
        "MRO": 393.730857,
        "MUR": 40.533339,
        "MVR": 17.040036,
        "MWK": 810.623028,
        "MXN": 20.743562,
        "MYR": 4.483282,
        "MZN": 69.86248,
        "NAD": 15.915089,
        "NGN": 398.698106,
        "NIO": 37.785357,
        "NOK": 9.976851,
        "NPR": 125.828851,
        "NZD": 1.669701,
        "OMR": 0.42462,
        "PAB": 1.103143,
        "PEN": 3.667658,
        "PGK": 3.730523,
        "PHP": 56.050425,
        "PKR": 170.620851,
        "PLN": 4.253784,
        "PYG": 7192.819198,
        "QAR": 4.015657,
        "RON": 4.782237,
        "RSD": 117.524152,
        "RUB": 68.587541,
        "RWF": 1031.200239,
        "SAR": 4.137672,
        "SBD": 9.155119,
        "SCR": 15.108519,
        "SDG": 49.964881,
        "SEK": 10.554671,
        "SGD": 1.490228,
        "SHP": 0.843344,
        "SLL": 10698.013547,
        "SOS": 642.984052,
        "SRD": 8.22538,
        "STD": 23779.135614,
        "SVC": 9.652999,
        "SYP": 567.985996,
        "SZL": 15.915081,
        "THB": 33.671577,
        "TJS": 10.694571,
        "TMT": 3.860108,
        "TND": 3.114597,
        "TOP": 2.537787,
        "TRY": 6.555608,
        "TTD": 7.458909,
        "TWD": 33.136824,
        "TZS": 2542.666315,
        "UAH": 26.937693,
        "UGX": 4053.883279,
        "USD": 1.102888,
        "UYU": 41.184932,
        "UZS": 10527.065909,
        "VEF": 11.015098,
        "VND": 25556.671161,
        "VUV": 128.681078,
        "WST": 2.91508,
        "XAF": 655.622889,
        "XAG": 0.06082,
        "XAU": 0.000701,
        "XCD": 2.98061,
        "XDR": 0.799493,
        "XOF": 656.218701,
        "XPF": 119.777602,
        "YER": 276.056823,
        "ZAR": 15.901222,
        "ZMK": 9927.319033,
        "ZMW": 15.967483,
        "ZWL": 355.129923
    }
}
'''

fixture_get_usd_rates_fails = '''
{"success":false,"error":{"code":105,"type":"base_currency_access_restricted"}}
'''
