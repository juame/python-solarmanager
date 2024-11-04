from pysolarmanager import SolarmanagerAuth


class Gateway:
    """Class that represents a Gateway object of the Solarmanager API."""

    def __init__(self, raw_data: dict, auth: SolarmanagerAuth):
        """Initialize a Gateway object."""
        self.raw_data = raw_data
        self.auth = auth

    @property
    def id(self) -> str:
        """Return the ID of the gateway."""
        return self.raw_data["_id"]

    @property
    def signal(self) -> str:
        """Return the signal status of the gateway."""
        return self.raw_data["signal"]

    @property
    def name(self) -> str:
        """Return the name of the gateway."""
        return self.raw_data["name"]

    @property
    def sm_id(self) -> str:
        """Return the unique ID of the Solarmanager."""
        return self.raw_data["sm_id"]

    @property
    def owner(self) -> str:
        """Return the owner of the gateway."""
        return self.raw_data["owner"]

    @property
    def firmware(self) -> str:
        """Return the firmware version of the gateway."""
        return self.raw_data["firmware"]

    @property
    def last_error_date(self) -> str:
        """Return the date of the last error."""
        return self.raw_data["lastErrorDate"]

    @property
    def mac(self) -> str:
        """Return the MAC address of the gateway."""
        return self.raw_data["mac"]

    @property
    def ip(self) -> str:
        """Return the IP address of the gateway."""
        return self.raw_data["ip"]

    @property
    def is_installation_completed(self) -> bool:
        """Return if the installation is completed."""
        return self.raw_data["isInstallationCompleted"]


class GatewayResponse:
    """Class that represents a Gateway response of the Solarmanager API."""

    def __init__(self, raw_data: dict, auth: SolarmanagerAuth):
        """Initialize a GatewayResponse object."""
        self.raw_data = raw_data
        self.auth = auth
        self._gateway = Gateway(self.raw_data["gateway"], self.auth)

    @property
    def gateway(self) -> Gateway:
        """Return the gateway."""
        return self._gateway
