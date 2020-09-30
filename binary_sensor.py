"""Support for the Hive binary sensors."""
<<<<<<< HEAD
from homeassistant.components.binary_sensor import BinarySensorEntity

from . import DATA_HIVE, DOMAIN, HiveEntity

DEVICETYPE_DEVICE_CLASS = {"motionsensor": "motion", "contactsensor": "opening"}
=======
from homeassistant.components.binary_sensor import BinarySensorDevice

from . import DATA_HIVE, DOMAIN

DEVICETYPE_DEVICE_CLASS = {
    'motionsensor': 'motion',
    'contactsensor': 'opening',
}
>>>>>>> 95b774e16077b3115f078416c31929227aba59c4


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up Hive sensor devices."""
    if discovery_info is None:
        return
<<<<<<< HEAD

    session = hass.data.get(DATA_HIVE)
    devs = []
    for dev in discovery_info:
        devs.append(HiveBinarySensorEntity(session, dev))
    add_entities(devs)


class HiveBinarySensorEntity(HiveEntity, BinarySensorEntity):
    """Representation of a Hive binary sensor."""

=======
    session = hass.data.get(DATA_HIVE)

    add_entities([HiveBinarySensorEntity(session, discovery_info)])


class HiveBinarySensorEntity(BinarySensorDevice):
    """Representation of a Hive binary sensor."""

    def __init__(self, hivesession, hivedevice):
        """Initialize the hive sensor."""
        self.node_id = hivedevice["Hive_NodeID"]
        self.node_name = hivedevice["Hive_NodeName"]
        self.device_type = hivedevice["HA_DeviceType"]
        self.node_device_type = hivedevice["Hive_DeviceType"]
        self.session = hivesession
        self.attributes = {}
        self.data_updatesource = '{}.{}'.format(self.device_type,
                                                self.node_id)
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
    def device_class(self):
        """Return the class of this sensor."""
        return DEVICETYPE_DEVICE_CLASS.get(self.node_device_type)

    @property
    def name(self):
        """Return the name of the binary sensor."""
        return self.node_name

    @property
    def device_state_attributes(self):
        """Show Device Attributes."""
        return self.attributes

    @property
    def is_on(self):
        """Return true if the binary sensor is on."""
<<<<<<< HEAD
        return self.session.sensor.get_state(self.node_id, self.node_device_type)
=======
        return self.session.sensor.get_state(
            self.node_id, self.node_device_type)
>>>>>>> 95b774e16077b3115f078416c31929227aba59c4

    def update(self):
        """Update all Node data from Hive."""
        self.session.core.update_data(self.node_id)
<<<<<<< HEAD
        self.attributes = self.session.attributes.state_attributes(self.node_id)
=======
        self.attributes = self.session.attributes.state_attributes(
            self.node_id)
>>>>>>> 95b774e16077b3115f078416c31929227aba59c4
