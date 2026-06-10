from datetime import datetime, timedelta, timezone
from typing import Optional
import requests

from token_store_interface import TokenRecord, TokenStoreInterface


class TokenRefreshError(Exception):
    pass


def is_token_expired(
    token: TokenRecord,
    refresh_window_minutes: int = 5,
) -> bool:
    """
    Returns True if the token is expired or close to expiring.
    """
    if token.expires_at is None:
        return False

    now = datetime.now(timezone.utc)
    refresh_time = token.expires_at - timedelta(minutes=refresh_window_minutes)

    return now >= refresh_time


def refresh_oauth_token(
    token: TokenRecord,
    token_url: str,
    client_id: str,
    client_secret: str,
) -> TokenRecord:
    """
    Refreshes an OAuth access token using a refresh token.
    """

    if not token.refresh_token:
        raise TokenRefreshError("No refresh token available.")

    response = requests.post(
        token_url,
        data={
            "grant_type": "refresh_token",
            "refresh_token": token.refresh_token,
            "client_id": client_id,
            "client_secret": client_secret,
        },
        timeout=10,
    )

    if response.status_code != 200:
        raise TokenRefreshError(
            f"Token refresh failed: {response.status_code} {response.text}"
        )

    data = response.json()

    expires_in = data.get("expires_in")
    expires_at: Optional[datetime] = None

    if expires_in:
        expires_at = datetime.now(timezone.utc) + timedelta(seconds=expires_in)

    return TokenRecord(
        provider=token.provider,
        account_id=token.account_id,
        access_token=data["access_token"],
        refresh_token=data.get("refresh_token", token.refresh_token),
        expires_at=expires_at,
        scopes=token.scopes,
        metadata=token.metadata,
    )


def get_valid_token(
    provider: str,
    account_id: str,
    token_store: TokenStoreInterface,
    token_url: str,
    client_id: str,
    client_secret: str,
) -> TokenRecord:
    """
    Retrieves a valid token. Refreshes it if needed.
    """

    token = token_store.get_token(provider, account_id)

    if token is None:
        raise TokenRefreshError("No token found.")

    if not is_token_expired(token):
        return token

    refreshed_token = refresh_oauth_token(
        token=token,
        token_url=token_url,
        client_id=client_id,
        client_secret=client_secret,
    )

    token_store.save_token(refreshed_token)

    return refreshed_token

