"""
Created on Mon Sep 2 21:30 2024

@author: keagan
This script will contain all the code to implement features listed in 'functionality_UI.txt'.
And will connect the other qlabinterface scripts.
"""
import asyncio
from bleak import BleakScanner
import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QStackedWidget, QTextEdit, QFileDialog


class IntroWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Pinetime Heartbeat Interface")
        self.setGeometry(0, 0, 400, 400)

        #Initialize QStackedWidget
        self.central_widget = QStackedWidget(self)
        self.setCentralWidget(self.central_widget)

        #Layout 1: Initial Layout
        layout1_widget = QWidget(self)
        layout1_vbox = QVBoxLayout()
        self.scan_button = QPushButton("Scan for devices", self)
        self.scan_button.clicked.connect(self.on_scan_button_clicked)
        self.connect_all_button = QPushButton("Connect all devices", self)
        self.connect_one_button = QPushButton("Connect one device", self)
        self.disconnect_button = QPushButton("Disconnect all devices", self)
        layout1_vbox.addWidget(self.scan_button)
        layout1_vbox.addWidget(self.connect_all_button)
        layout1_vbox.addWidget(self.connect_one_button)
        layout1_vbox.addWidget(self.disconnect_button)
        layout1_widget.setLayout(layout1_vbox)

        # Layout 2: After Scanning
        layout2_widget = QWidget(self)
        layout2_vbox = QVBoxLayout()
        self.num_devices_textbox = QLineEdit(self)
        self.device_info_textbox = QTextEdit(self)
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.on_back_button_clicked)
        layout2_vbox.addWidget(self.num_devices_textbox)
        layout2_vbox.addWidget(self.device_info_textbox)
        layout2_vbox.addWidget(self.back_button)
        layout2_widget.setLayout(layout2_vbox)

        #Add layouts to the QStackedWidget
        self.central_widget.addWidget(layout1_widget)  #Index 0
        self.central_widget.addWidget(layout2_widget)  #Index 1

        #Start with layout 1
        self.central_widget.setCurrentIndex(0)

    def on_scan_button_clicked(self):
        #Change to the second layout
        self.central_widget.setCurrentIndex(1)
        #Running the bleak function
        try:
            async def main():
                devices = await BleakScanner.discover()
                for d in devices:
                    print(d)
                return devices
            devices = asyncio.run(main())
            print(devices)
            #Showing how many devices there are around
            self.num_devices_textbox.setText(f"Number of devices: {len(devices)} ")
            #Showing the all device information
            self.device_info = []
            for device in devices:
                self.device_info_textbox.insertPlainText(str(device)+"\n")
                #Adding device address and name to list to be accessed later
                self.device_info.append([device.address,device.name])
            print(self.device_info)
        except Exception as e:
            print(f"An error occurred: {e}")

    def on_back_button_clicked(self):
        #Go back to the first layout
        self.central_widget.setCurrentIndex(0)

if __name__ == '__main__':
    try:
        from bleak.backends.winrt.util import allow_sta
        allow_sta()
    except ImportError:
        pass
    app = QApplication(sys.argv)
    start_window = IntroWindow()
    start_window.show()
    sys.exit(app.exec())
