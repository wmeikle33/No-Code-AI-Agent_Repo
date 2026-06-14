import os


def get_required_env(key: str) -> str:
    value = os.getenv(key)

    if not value:
        raise ValueError(
            f"Required environment variable '{key}' not found."
        )

    return value


def get_optional_env(
    key: str,
    default: str | None = None
) -> str | None:
    return os.getenv(key, default)
