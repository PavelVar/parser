"""Class with HTTP client for sending requests to the sites< returns results of such requests."""
import requests
from typing import Optional
from requests import Response


class HTTPClient:
    """Sends request and returns results according to queries"""

    @staticmethod
    def get(url: str, headers: Optional[dict] = None, params: Optional[dict] = None) -> Response:
        """Sends GET requests"""
        return requests.get(url, headers=headers, params=params)
