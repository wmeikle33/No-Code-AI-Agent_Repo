import time
from dataclasses import dataclass


@dataclass
class ExecutionMetrics:
    workflow_name: str
    execution_time: float
    success: bool


class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self) -> float:
        if self.start_time is None:
            raise RuntimeError(
                "Timer was never started."
            )

        return time.perf_counter() - self.start_time
