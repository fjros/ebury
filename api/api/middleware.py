import falcon
import sqlalchemy
import sqlalchemy.orm as orm

from api.config import Configuration


class DatabaseSessionManager:
    """Falcon middleware that manages scoped SQLAlchemy sessions per request
    """

    def __init__(self, config: Configuration):
        self._engine = sqlalchemy.create_engine(config.database_url)
        self._session_factory = orm.scoped_session(orm.sessionmaker())
        self._session_factory.configure(bind=self._engine)

    def process_request(self, request: falcon.Request, response: falcon.Response):
        """Attach a scoped database session to this request
        """

        request.context.session = self._session_factory()

    def process_response(self, request, response, resource, req_succeeded):
        """Close the associated scoped session
        """

        self._session_factory.remove()
