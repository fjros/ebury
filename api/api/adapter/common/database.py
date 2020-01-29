import sqlalchemy
import sqlalchemy.orm as orm

from api.config import Configuration
from api.core.common.database import SessionManager


class SqlAlchemySessionManager(SessionManager):

    def __init__(self):
        config = Configuration()

        self._engine = sqlalchemy.create_engine(config.database_url)
        self._session_factory = orm.scoped_session(orm.sessionmaker())
        self._session_factory.configure(bind=self._engine)

    def open(self) -> orm.Session:
        """Open database session
        """

        return self._session_factory()

    def close(self):
        """Close database session
        """

        self._session_factory.remove()
