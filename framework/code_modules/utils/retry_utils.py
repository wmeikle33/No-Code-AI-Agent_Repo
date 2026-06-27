
import time
from functools import wraps


def retry(
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)

                except Exception:
                    if attempt == max_attempts - 1:
                        raise

                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper

    return decorator
