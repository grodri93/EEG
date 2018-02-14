from .ble import BLEAdapter
from .parser import decompressDeltas19Bit
import struct
import time
import queue
import csv
BLE_RECEIVE = "2d30c082-f39f-4ce6-923f-3484ea480596"
BLE_SEND = "2d30c083-f39f-4ce6-923f-3484ea480596"
BLE_DISCONNECT = "2d30c084-f39f-4ce6-923f-3484ea480596"


class GanglionDongle(BLEAdapter):
    def __init__(self, recv_data):
        super(GanglionDongle, self).__init__()
        self.ch1 = []
        self.ch2 = []
        self.ch3 = []
        self.ch4 = []
        self.ts = []
        self.rx_queue = queue.Queue()
        self.recv_data = recv_data
        self.ts_name = str(int(time.time()))

    def _receive_callback(self, handle, value):
        packet = struct.unpack(str(len(value)) + 'B', value)
        packet_id = packet[0]

        if packet_id == 0:
            print('raw')
            #self.parseRaw(start_byte, unpac[1:])
        # 18-bit compression with Accelerometer
        elif packet_id >= 1 and packet_id <= 100:
            print('18-bit')
            #self.parse18bit(start_byte, unpac[1:])
        # 19-bit compression without Accelerometer
        elif packet_id >=101 and packet_id <= 200:
            data = decompressDeltas19Bit(packet[1:])
            self.ch1.extend([data[0][0], data[1][0]])
            self.ch2.extend([data[0][1], data[1][1]])
            self.ch3.extend([data[0][2], data[1][2]])
            self.ch4.extend([data[0][3], data[1][3]])
            t = time.time()
            self.ts.extend([t, t + (1 / 200.0)])

            with open('data_%s.csv' % self.ts_name, 'a') as data_file:
                file_writer = csv.writer(data_file, delimiter=',')
                file_writer.writerow([str(t), str(data[0][0]), str(data[0][1]), str(data[0][2]), str(data[0][3])])
                file_writer.writerow([str(t + (1 / 200.0)), str(data[1][0]), str(data[1][1]), str(data[1][2]), str(data[1][3])])

            self.rx_queue.put([self.ch1, self.ch2, self.ch3, self.ch4, self.ts])

            if len(self.ts) >= 500:
                self.ch1 = self.ch1[2:]
                self.ch2 = self.ch2[2:]
                self.ch3 = self.ch3[2:]
                self.ch4 = self.ch4[2:]
                self.ts = self.ts[2:]

            self.recv_data()

                    # Impedance Channel
        elif packet_id >= 201 and packet_id <= 205:
            print('Impedance')
            #self.parseImpedance(start_byte, packet[1:])
        # Part of ASCII -- TODO: better formatting of incoming ASCII
        elif packet_id == 206:
            print("%\t" + str(packet[1:]))
            self.receiving_ASCII = True
        # End of ASCII message
        elif packet_id == 207:
            print("%\t" + str(packet[1:]))
            print ("$$$")
        else:
            print("Warning: unknown type of packet: " + str(packet_id))

    def data(self):
        return self.rx_queue.get()


    def subscribe(self):
        self.ch1 = []
        self.ch2 = []
        self.ch3 = []
        self.ch4 = []
        self.ts = []
        self.ts_name = str(int(time.time()))
        self.connected_device.subscribe(BLE_RECEIVE,
                                        callback=self._receive_callback)

    def stream(self):
        self.ch1 = []
        self.ch2 = []
        self.ch3 = []
        self.ch4 = []
        self.ts = []
        #packet = struct.pack('c', str("b"))
        packet = bytearray(b'b')
        self.connected_device.start(BLE_SEND, packet)

    def stop_stream(self):
        packet = bytearray(b's')
        self.connected_device.start(BLE_SEND, packet)

    def plotdata(self):
        self.plot1.plot(self.ts, self.ch1)
        self.plot1.plot(self.ts, self.ch2)
        self.plot1.plot(self.ts, self.ch3)
        self.plot1.plot(self.ts, self.ch4)
