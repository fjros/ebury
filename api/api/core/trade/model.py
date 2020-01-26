import random
import string
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from api.core.currency.model import Currency
from api.orm import Base


class Trade(Base):
    """Trade model
    """

    __tablename__ = 'trade'

    id = Column(String(9), primary_key=True)
    sell_currency = Column(String(3), nullable=False)
    sell_amount = Column(Integer, nullable=False)
    buy_currency = Column(String(3), nullable=False)
    buy_amount = Column(Integer, nullable=False)
    rate = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def build(cls, sell_currency: Currency, sell_amount: int,
              buy_currency: Currency, buy_amount: int, rate: float):
        """Build corresponding trade

        This should implement the business requirements for the trade. Since I don't know them, I'm
        just going to implement a simple rule as an example:

        a) If rate < 1  => sell_amount > buy_amount
        b) If rate >= 1 => sell_amount <= buy_amount

        :raises `InconsistentTradeException`:
        """

        if (rate < 1 and sell_amount <= buy_amount) or (rate >= 1 and sell_amount > buy_amount):
            raise InconsistentTradeException()

        trade_id = cls._generate_trade_id()
        return Trade(id=trade_id,
                     sell_currency=sell_currency.symbol,
                     sell_amount=sell_amount,
                     buy_currency=buy_currency.symbol,
                     buy_amount=buy_amount,
                     rate=rate)

    @classmethod
    def _generate_trade_id(cls):
        """Generate unique id for a trade

        It consists of the 'TR' prefix + 7 alphanumerics. For this implementation I've chosen to
        just generate a random string. However, I wouldn't do this in a real project.

        I'd go for either UUIDs or way longer identifiers with (at least) random and
        timestamp-based parts. Alternatively we could rely on the database, but I don't like that
        approach very much.
        """

        return 'TR' + ''.join(random.choices(string.ascii_letters + string.digits, k=7))


class InconsistentTradeException(Exception):
    """Raised when a trade violates its invariants
    """

    pass
