import pygatt
import logging


DEBUG = False
if DEBUG:
    logging.basicConfig()
    logging.getLogger('pygatt').setLevel(logging.DEBUG)

ADDRESS_TYPE = pygatt.BLEAddressType.random


class BLEDongle(object):
    """A wrapper for the BGAPI backend from the pygatt library."""

    def __init__(self):
        # BGAPI variables
        self.adapter = pygatt.BGAPIBackend()
        # BLEDongle variables
        self.connected_device = None
        self.connected_device_rssi = None
        self.scanned_devices = []

    def connect_dongle(self):
        """Connect to BLED USB dongle."""
        try:
            self.adapter.start()
            return True
        except:
            return False

    def disconnect_dongle(self):
        """Disconnect to BLED USB dongle."""
        try:
            self.adapter.stop()
            return True
        except:
            return False

    def subscribe(self):
        """Blank, meant to be overriding."""
        pass

    def connect(self, address):
        """Connect to BLE device directly."""
        try:
            if self.adapter.adapter_started():
                device = self.adapter.connect(address, address_type=ADDRESS_TYPE)
                self.connected_device = device
                return True
            else:
                self.connected_device = None
                return False
        except:
            self.connected_device = None
            return False

    def disconnect(self):
        """Disconnect from the current connected BLE device."""
        try:
            self.connected_device.disconnect()
            self.connected_device = None
            return True
        except:
            self.connected_device = None
            return False

    def scan(self):
        """Do one scan."""
        try:
            if self.adapter.adapter_started():
                self.scanned_devices = self.adapter.scan(timeout=2, active=False)
                return True
            else:
                self.scanned_devices = []
                return False
        except:
            self.scanned_devices = []
            return False

    def rssi(self):
        """Get the most current rssi value."""
        try:
            self.connected_device_rssi = self.connected_device.get_rssi()
            return True
        except:
            self.connected_device_rssi = -101
            return False

    def device_connected(self):
        if self.connected_device is None:
            return False
        else:
            return self.connected_device.connected()

    def dongle_connected(self):
        return self.adapter.adapter_started()


if __name__ == '__main__':
    pass
