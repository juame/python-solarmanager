from pysolarmanager.auth import SolarmanagerAuth


class Tag:
    """Class that represents a Tag object of the Solarmanager API."""

    def __init__(self, raw_data: dict, auth: SolarmanagerAuth):
        """Initialize a Tag object."""
        self.raw_data = raw_data
        self.auth = auth

    @property
    def id(self) -> str:
        return self.raw_data["_id"]

    @property
    def name(self) -> str:
        return self.raw_data.get('name')
