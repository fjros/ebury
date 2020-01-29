from api.adapter.common.database import SqlAlchemySessionManager
from api.core.common.database import SessionManager


class SessionManagerBinding:
    """Return concrete implementation of the `SessionManager` abstract class
    """

    @classmethod
    def get(cls) -> SessionManager:
        return SqlAlchemySessionManager()
