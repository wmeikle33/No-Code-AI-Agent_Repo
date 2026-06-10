
from typing import List

from code_modules.connectors.base.connector import Connector


class GmailConnector(Connector):

    def __init__(self, credentials_path: str):
        self.credentials_path = credentials_path

    def health_check(self) -> dict:
        return {
            "status": "healthy",
            "connector": "gmail",
        }

    def get_messages(
        self,
        max_results: int = 10
    ) -> List[dict]:

        raise NotImplementedError

    def send_message(
        self,
        to: str,
        subject: str,
        body: str
    ) -> dict:

        raise NotImplementedError
