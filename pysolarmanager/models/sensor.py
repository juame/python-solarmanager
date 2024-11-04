from pysolarmanager.auth import SolarmanagerAuth
from pysolarmanager.models.tag import Tag


class Sensor:
    """Class that represents a Sensor of the Solarmanager API."""

    def __init__(self, raw_data: dict, auth: SolarmanagerAuth):
        """Initialize a Sensor object."""
        self.raw_data = raw_data
        self.auth = auth

        if raw_data.get('tag'):
            self._tag = Tag(raw_data.get('tag'), self.auth)
        else:
            self._tag = Tag({}, self.auth)

    @property
    def id(self) -> str:
        return self.raw_data["_id"]

    @property
    def priority(self) -> int:
        return self.raw_data.get('priority')

    @property
    def device_type(self) -> str:
        return self.raw_data.get('device_type')

    @property
    def signal(self) -> str:
        return self.raw_data.get('signal')

    @property
    def type(self) -> str:
        return self.raw_data.get('type')

    @property
    def device_group(self) -> str:
        return self.raw_data.get('device_group')

    @property
    def water_heater_type(self) -> str:
        return self.raw_data.get('waterHeaterType')

    @property
    def ip(self) -> str:
        return self.raw_data.get('ip')

    @property
    def mac(self) -> str:
        return self.raw_data.get('mac')

    @property
    def created_at(self) -> str:
        return self.raw_data.get('createdAt')

    @property
    def updated_at(self) -> str:
        return self.raw_data.get('updatedAt')

    @property
    def tag(self) -> Tag:
        return self._tag

    @property
    def data(self) -> dict:
        return self.raw_data.get('data')
