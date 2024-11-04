from typing import List

from pysolarmanager.auth import SolarmanagerAuth
from pysolarmanager.models.gateway import GatewayResponse
from pysolarmanager.models.sensor import Sensor


class Solarmanager:
    """Class to communicate with the Solarmanager API."""

    def __init__(self, auth: SolarmanagerAuth) -> None:
        """Initialize the API and store the auth so we can make requests."""
        self.auth = auth

    async def get_info_gateway(self, solarmanager_id: str) -> GatewayResponse:
        """Get gateway info."""
        resp = await self.auth.request(
            "get",
            f"v1/info/gateway/{solarmanager_id}")
        resp.raise_for_status()
        return GatewayResponse(await resp.json(), self.auth)

    async def get_info_sensors(self, solarmanager_id: str) -> List[Sensor]:
        """Get sensors info."""
        resp = await self.auth.request(
            "get",
            f"v1/info/sensors/{solarmanager_id}")
        resp.raise_for_status()
        return [Sensor(sensor, self.auth) for sensor in await resp.json()]
