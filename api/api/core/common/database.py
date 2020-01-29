from abc import ABC
from abc import abstractmethod
from typing import Any


class SessionManager(ABC):
    """Base class for database session managers
    """

    @abstractmethod
    def open(self) -> Any:
        """Open database session
        """

        pass

    @abstractmethod
    def close(self):
        """Close database session
        """

        pass
