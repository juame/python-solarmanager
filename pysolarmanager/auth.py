import aiohttp
from aiohttp import ClientResponse, ClientSession


class SolarmanagerAuth:
    """Class to make authenticated requests to the Solarmanager API."""

    def __init__(self,
                 username: str,
                 password: str,
                 websession: ClientSession,
                 base_url: str = "https://cloud.solar-manager.ch"):
        self._auth = aiohttp.BasicAuth(username, password)
        self._websession = websession

        self._base_url = base_url

    async def request(self,
                      method: str,
                      path: str,
                      **kwargs) -> ClientResponse:
        """Make request on the api and return response data."""
        headers = kwargs.get("headers") or {}
        headers["accept"] = "application/json"

        return await self._websession.request(
            method,
            f"{self._base_url}/{path}",
            **kwargs,
            auth=self._auth,
            headers=headers
        )
