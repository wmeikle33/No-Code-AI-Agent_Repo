from abc import ABC, abstractmethod


class Connector(ABC):

    @abstractmethod
    def health_check(self):
        pass
