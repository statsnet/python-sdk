import os
from typing import Any, NoReturn

import httpx


class ClientException(Exception):
    def __init__(self, endpoint: str, status_code: int, response_content: bytes) -> NoReturn:
        self.endpoint = endpoint
        self.status_code = status_code
        self.response_content = response_content

    def __str__(self) -> str:
        return f"Request to {self.endpoint} unsuccessful. Status code: {self.status_code}. Response content: {self.response_content}"

    def __repr__(self) -> str:
        return "<ClientException(endpoint='%s', status_code=%s, response_content='%s')>" % (
            self.endpoint,
            self.status_code,
            self.response_content,
        )

class Client:
    def __init__(self, api_key: str = None):
        if not api_key:
            api_key = os.getenv("STATSNET_API_KEY")
        if not api_key:
            raise ValueError("No api key provided. Set via argument or environment variable STATSNET_API_KEY.")

        self.client: httpx.Client = httpx.Client(
            headers={"Authorization": f"Bearer {api_key}"}, base_url="https://statsnet.co/api/v2"
        )

    def __request(self, method: str, endpoint: str, params: dict = None, json: Any = None) -> Any:
        r = self.client.request(method, endpoint, params=params, json=json)
        if not r.is_success:
            raise ClientException(endpoint, r.status_code, r.content)
        match r.headers["Content-Type"]:
            case "application/json":
                return r.json()

    def __get(self, endpoint: str, params: dict = None, json: Any = None) -> Any:
        return self.__request("GET", endpoint, params, json)

    def __post(self, endpoint: str, params: dict = None, json: Any = None) -> Any:
        return self.__request("POST", endpoint, params, json)
