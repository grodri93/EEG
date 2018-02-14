import sys
from PySide import QtGui, QtCore
from gui import main
from ble.gang import GanglionDongle
import datetime
import pyqtgraph as pg
ADDR = 'EA:1D:67:A3:CF:C2'


class MainWindow(QtGui.QMainWindow, main.Ui_MainWindow):
    """ Class implmentation of the main window."""
    stream_data = QtCore.Signal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btn_connect.clicked.connect(self._clicked_connect)
        self.btn_disconnect.clicked.connect(self._clicked_disconnect)
        self.btn_start_stream.clicked.connect(self._clicked_start_streaming)
        self.btn_stop_stream.clicked.connect(self._clicked_stop_streaming)

        self.stream_data.connect(self._recv_stream_data)

        self.dongle = GanglionDongle(self.stream_data.emit)
        self.dongle.start()

    def _recv_stream_data(self):
        ch = self.dongle.data()

        self.ch1_plot.setData(ch[4], ch[0])
        self.ch2_plot.setData(ch[4], ch[1])
        self.ch3_plot.setData(ch[4], ch[2])
        self.ch4_plot.setData(ch[4], ch[3])

    def _clicked_connect(self):
        self.dongle.connect(ADDR)
        self.dongle.subscribe()

        self.btn_connect.setEnabled(False)
        self.btn_disconnect.setEnabled(True)
        self.btn_start_stream.setEnabled(True)
        self.btn_stop_stream.setEnabled(False)

    def _clicked_disconnect(self):
        self.dongle.connected_device.disconnect()

        self.btn_connect.setEnabled(True)
        self.btn_disconnect.setEnabled(False)
        self.btn_start_stream.setEnabled(False)
        self.btn_stop_stream.setEnabled(False)

    def _clicked_start_streaming(self):
        axisItems = {'bottom': TimeAxisItem(orientation='bottom')}
        axisItems['bottom'].setLabel(text='Time', units=u" H:M:S",
                                     unitPrefix=' ', **{'font-size':'6pt'})

        self.graph.clear()
        self.plot1 = self.graph.addPlot(title='Channel 1', axisItems=axisItems)
        self.graph.nextRow()
        self.plot2 = self.graph.addPlot(title='Channel 2', axisItems=axisItems)
        self.graph.nextRow()
        self.plot3 = self.graph.addPlot(title='Channel 3', axisItems=axisItems)
        self.graph.nextRow()
        self.plot4 = self.graph.addPlot(title='Channel 4', axisItems=axisItems)

        self.ch1_plot = self.plot1.plot(pen='w', title='channel 1')
        self.ch2_plot = self.plot2.plot(pen='b', title='channel 1')
        self.ch3_plot = self.plot3.plot(pen='r', title='channel 1')
        self.ch4_plot = self.plot4.plot(pen='g', title='channel 1')



        self.dongle.stream()

        self.btn_start_stream.setEnabled(False)
        self.btn_stop_stream.setEnabled(True)

    def _clicked_stop_streaming(self):
        self.dongle.stop_stream()

        self.btn_start_stream.setEnabled(True)
        self.btn_stop_stream.setEnabled(False)


class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super(TimeAxisItem, self).__init__(*args, **kwargs)

    def tickStrings(self, values, scale, spacing):

        return_val = [self.ts2str(value) for value in values]
        return return_val

    def ts2str(self, value):
        """Convert timestamp into datetime object."""
        print(value)
        return datetime.datetime.fromtimestamp(value).strftime("%H:%M:%S")

    def labelString(self):
        s = '%s (H:M:S)' % self.labelText
        style = "color:black;font-size:8pt"
        return "<span style='%s'>%s</span>" % (style, s)


def main():
    APP = QtGui.QApplication(sys.argv)

    MAIN_WINDOW = MainWindow()
    MAIN_WINDOW.show()

    APP.exec_()


if __name__ == '__main__':
    main()
