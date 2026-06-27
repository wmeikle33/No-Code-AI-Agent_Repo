import os


def get_env(key: str) -> str:
    value = os.getenv(key)

    if value is None:
        raise ValueError(
            f"Missing environment variable: {key}"
        )

    return value
