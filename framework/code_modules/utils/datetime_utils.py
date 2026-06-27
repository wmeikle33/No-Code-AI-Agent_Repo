from datetime import datetime, timezone


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def current_timestamp() -> str:
    return utc_now().isoformat()


def current_date() -> str:
    return utc_now().strftime("%Y-%m-%d")


def current_time() -> str:
    return utc_now().strftime("%H:%M:%S")
