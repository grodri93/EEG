from .ble import BLEAdapter
import struct
BLE_RECEIVE = "2d30c082-f39f-4ce6-923f-3484ea480596"
BLE_SEND = "2d30c083-f39f-4ce6-923f-3484ea480596"
BLE_DISCONNECT = "2d30c084-f39f-4ce6-923f-3484ea480596"


class GanglionDongle(BLEAdapter):
    def __init__(self):
        super(GanglionDongle, self).__init__()

    def _receive_callback(self, handle, value):
        print(value)

    def subscribe(self):
        self.connected_device.subscribe(BLE_RECEIVE,
                                        callback=self._receive_callback)

    def stream(self):
        #packet = struct.pack('c', str("b"))
        packet = bytearray(b'b')
        self.connected_device.start(BLE_SEND, packet)
