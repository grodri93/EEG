from ble.ble import BLEAdapter


def print_nearby_devices(adapter):
    for device in adapter.nearby_devices:
        print 'device name:', device.name
        print 'device rssi:', device.rssi
        print 'device manufacturer_specific_data:', device.manufacturer_specific_data
        print ''

def main():
    adapter = BLEAdapter()
    adapter.start()

    print_nearby_devices(adapter)


if __name__ == '__main__':
    main()