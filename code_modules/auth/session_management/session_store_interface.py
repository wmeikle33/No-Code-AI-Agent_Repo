from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, Dict, Any


class SessionStoreInterface(ABC):
    """
    Abstract session storage backend.

    Implementations may use:
    - Redis
    - PostgreSQL
    - DynamoDB
    - Memory Store
    """

    @abstractmethod
    def create_session(
        self,
        session_id: str,
        data: Dict[str, Any],
        expires_at: datetime,
    ) -> None:
        pass

    @abstractmethod
    def get_session(
        self,
        session_id: str,
    ) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def update_session(
        self,
        session_id: str,
        data: Dict[str, Any],
    ) -> None:
        pass

    @abstractmethod
    def delete_session(
        self,
        session_id: str,
    ) -> None:
        pass

    @abstractmethod
    def extend_session(
        self,
        session_id: str,
        expires_at: datetime,
    ) -> None:
        pass

    @abstractmethod
    def session_exists(
        self,
        session_id: str,
    ) -> bool:
        pass
