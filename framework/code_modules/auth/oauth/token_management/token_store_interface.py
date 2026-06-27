from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any


@dataclass
class TokenRecord:
    provider: str
    account_id: str
    access_token: str
    refresh_token: Optional[str]
    expires_at: Optional[datetime]
    scopes: list[str]
    metadata: Dict[str, Any]


class TokenStoreInterface(ABC):
    """
    Abstract interface for storing and retrieving OAuth tokens.

    Implementations may use:
    - encrypted database storage
    - cloud secret managers
    - local development files
    - in-memory test stores
    """

    @abstractmethod
    def save_token(self, token: TokenRecord) -> None:
        pass

    @abstractmethod
    def get_token(self, provider: str, account_id: str) -> Optional[TokenRecord]:
        pass

    @abstractmethod
    def delete_token(self, provider: str, account_id: str) -> None:
        pass

    @abstractmethod
    def update_access_token(
        self,
        provider: str,
        account_id: str,
        access_token: str,
        expires_at: Optional[datetime],
    ) -> None:
        pass

    @abstractmethod
    def list_tokens_for_provider(self, provider: str) -> list[TokenRecord]:
        pass
