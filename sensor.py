"""Support for the Hive sensors."""
from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity

<<<<<<< HEAD
from . import DATA_HIVE, DOMAIN, HiveEntity

FRIENDLY_NAMES = {
    "Hub_OnlineStatus": "Hive Hub Status",
    "Hive_OutsideTemperature": "Outside Temperature",
}

DEVICETYPE_ICONS = {
    "Hub_OnlineStatus": "mdi:switch",
    "Hive_OutsideTemperature": "mdi:thermometer",
=======
from . import DATA_HIVE, DOMAIN

FRIENDLY_NAMES = {
    'Hub_OnlineStatus': 'Hive Hub Status',
    'Hive_OutsideTemperature': 'Outside Temperature',
}

DEVICETYPE_ICONS = {
    'Hub_OnlineStatus': 'mdi:switch',
    'Hive_OutsideTemperature': 'mdi:thermometer',
>>>>>>> 95b774e16077b3115f078416c31929227aba59c4
}


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up Hive sensor devices."""
    if discovery_info is None:
        return
<<<<<<< HEAD

    session = hass.data.get(DATA_HIVE)
    devs = []
    for dev in discovery_info:
        if dev["HA_DeviceType"] in FRIENDLY_NAMES:
            devs.append(HiveSensorEntity(session, dev))
    add_entities(devs)


class HiveSensorEntity(HiveEntity, Entity):
    """Hive Sensor Entity."""

=======
    session = hass.data.get(DATA_HIVE)

    if (discovery_info["HA_DeviceType"] == "Hub_OnlineStatus" or
            discovery_info["HA_DeviceType"] == "Hive_OutsideTemperature"):
        add_entities([HiveSensorEntity(session, discovery_info)])


class HiveSensorEntity(Entity):
    """Hive Sensor Entity."""

    def __init__(self, hivesession, hivedevice):
        """Initialize the sensor."""
        self.node_id = hivedevice["Hive_NodeID"]
        self.device_type = hivedevice["HA_DeviceType"]
        self.node_device_type = hivedevice["Hive_DeviceType"]
        self.session = hivesession
        self.data_updatesource = '{}.{}'.format(
            self.device_type, self.node_id)
        self._unique_id = '{}-{}'.format(self.node_id, self.device_type)
        self.session.entities.append(self)

>>>>>>> 95b774e16077b3115f078416c31929227aba59c4
    @property
    def unique_id(self):
        """Return unique ID of entity."""
        return self._unique_id

    @property
    def device_info(self):
        """Return device information."""
<<<<<<< HEAD
        return {"identifiers": {(DOMAIN, self.unique_id)}, "name": self.name}
=======
        return {
            'identifiers': {
                (DOMAIN, self.unique_id)
            },
            'name': self.name
        }

    def handle_update(self, updatesource):
        """Handle the new update request."""
        if '{}.{}'.format(self.device_type, self.node_id) not in updatesource:
            self.schedule_update_ha_state()
>>>>>>> 95b774e16077b3115f078416c31929227aba59c4

    @property
    def name(self):
        """Return the name of the sensor."""
        return FRIENDLY_NAMES.get(self.device_type)

    @property
    def state(self):
        """Return the state of the sensor."""
        if self.device_type == "Hub_OnlineStatus":
            return self.session.sensor.hub_online_status(self.node_id)
        if self.device_type == "Hive_OutsideTemperature":
            return self.session.weather.temperature()

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        if self.device_type == "Hive_OutsideTemperature":
            return TEMP_CELSIUS

    @property
    def icon(self):
        """Return the icon to use."""
        return DEVICETYPE_ICONS.get(self.device_type)

    def update(self):
        """Update all Node data from Hive."""
<<<<<<< HEAD
        self.session.core.update_data(self.node_id)
=======
        if self.session.core.update_data(self.node_id):
            for entity in self.session.entities:
                entity.handle_update(self.data_updatesource)
>>>>>>> 95b774e16077b3115f078416c31929227aba59c4
