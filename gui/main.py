# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\main.ui'
#
# Created: Mon Feb 12 20:35:45 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.right = QtGui.QGridLayout()
        self.right.setObjectName("right")
        self.graph = GraphicsLayoutWidget(self.centralwidget)
        self.graph.setObjectName("graph")
        self.right.addWidget(self.graph, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.right, 0, 1, 1, 1)
        self.left = QtGui.QGridLayout()
        self.left.setObjectName("left")
        self.connection = QtGui.QGridLayout()
        self.connection.setObjectName("connection")
        self.btn_connect = QtGui.QPushButton(self.centralwidget)
        self.btn_connect.setObjectName("btn_connect")
        self.connection.addWidget(self.btn_connect, 1, 0, 1, 1)
        self.btn_disconnect = QtGui.QPushButton(self.centralwidget)
        self.btn_disconnect.setEnabled(False)
        self.btn_disconnect.setObjectName("btn_disconnect")
        self.connection.addWidget(self.btn_disconnect, 1, 1, 1, 1)
        self.left.addLayout(self.connection, 1, 0, 1, 1)
        self.btn_start_stream = QtGui.QPushButton(self.centralwidget)
        self.btn_start_stream.setEnabled(False)
        self.btn_start_stream.setObjectName("btn_start_stream")
        self.left.addWidget(self.btn_start_stream, 2, 0, 1, 1)
        self.btn_stop_stream = QtGui.QPushButton(self.centralwidget)
        self.btn_stop_stream.setEnabled(False)
        self.btn_stop_stream.setObjectName("btn_stop_stream")
        self.left.addWidget(self.btn_stop_stream, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.left.addItem(spacerItem, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.left, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Gaia is Rachet!", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_connect.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_disconnect.setText(QtGui.QApplication.translate("MainWindow", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_start_stream.setText(QtGui.QApplication.translate("MainWindow", "Start Streaming", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_stop_stream.setText(QtGui.QApplication.translate("MainWindow", "Stop Streaming", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import GraphicsLayoutWidget
