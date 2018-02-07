from ble.ble import BLEAdapter
from ble.gang import GanglionDongle
import time

ADDR = 'EA:1D:67:A3:CF:C2'

def print_nearby_devices(adapter):
    for device in adapter.nearby_devices:
        print('device name:', device.name)
        print('device rssi:', device.rssi)
        print('device manufacturer_specific_data:', device.manufacturer_specific_data)
        print('')

def main():
    #adapter = BLEAdapter()
    #adapter.start()

    #print_nearby_devices(adapter)

    dongle = GanglionDongle()
    dongle.start()
    dongle.connect(ADDR)
    dongle.subscribe()
    dongle.stream()

    time.sleep(100)




if __name__ == '__main__':
    main()