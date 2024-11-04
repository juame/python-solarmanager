
import os
import asyncio
import aiohttp

from pysolarmanager import Solarmanager, SolarmanagerAuth


async def main():

    username = os.getenv("SOLARMANAGER_EMAIL")
    password = os.getenv("SOLARMANAGER_PASSWORD")
    solarmanager_id = os.getenv("SOLARMANAGER_ID")

    if not username or not password or not solarmanager_id:
        raise ValueError("Please set the SOLARMANAGER_EMAIL, SOLARMANAGER_PASSWORD, and SOLARMANAGER_ID environment variables.")  # noqa: E501

    async with aiohttp.ClientSession() as session:
        auth = SolarmanagerAuth(
            username,
            password,
            session)
        api = Solarmanager(auth)

        response = await auth.request(
            "get",
            f"v1/info/gateway/{solarmanager_id}")
        response.raise_for_status()
        print(f"Response: {await response.json()}")

        gateway_response = await api.get_info_gateway(solarmanager_id)
        print(f"The gateway {gateway_response.gateway.name} with firmware v{gateway_response.gateway.firmware} is {gateway_response.gateway.signal}.")  # noqa: E501

        sensors = await api.get_info_sensors(solarmanager_id)
        print(f"Found {len(sensors)} sensors.")

        for sensor in sensors:
            print(f"Sensor ID: {sensor.id}, Type: {sensor.type}, Tag Name: {sensor.tag.name}")  # noqa: E501

asyncio.run(main())
