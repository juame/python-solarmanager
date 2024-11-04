from pysolarmanager.auth import SolarmanagerAuth


class Data:
    """
    Data class for storing data specific to each device from Solarmanager.
    """

    def __init__(self, raw_data: dict, auth: SolarmanagerAuth):
        """Initialize a Sensor object."""
        self.raw_data = raw_data
        self.auth = auth

    # device_type = car, type = Car
    @property
    def battery_capacity(self) -> int:
        return self.raw_data.get('batteryCapacity')

    # device_type = device, type = "Smart Plug"
    @property
    def smart_plug_charging_type(self) -> str:
        return self.raw_data.get('smartPlugChargingType')

    # device_type = device, type = "Car Charging"
    @property
    def charging_mode(self) -> int:
        return self.raw_data.get('chargingMode')
