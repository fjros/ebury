from api.adapter.rate.backend import FixerRateBackend
from api.core.rate.backend import RateBackend
from api.config import Configuration


class RateBackendBinding:
    """Return concrete implementation of the `RateBackend` abstract class
    """

    config = Configuration()

    @classmethod
    def get(cls) -> RateBackend:
        return FixerRateBackend(cls.config.fixer_access_key)
