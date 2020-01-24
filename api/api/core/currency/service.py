from typing import List

from api.core.currency import Currency


class CurrencyService:
    """Application Service that deals with currencies
    """

    _currencies = [Currency(symbol) for symbol in Currency.all_symbols()]

    def get_currencies(self) -> List[Currency]:
        """Return set of pre-defined list of currencies

        Given the low likelihood of change, no need to query fixer.io API continuously.
        In a real-world example we might retrieve this list from a memory cache (periodically
        updated by a background job).
        """

        return self._currencies
