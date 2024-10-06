import flet as ft
import asyncio
import threading
import numpy as np
from bleak import BleakScanner, BleakClient
from bleak.exc import BleakDeviceNotFoundError, BleakError


class DeviceWorker:
    def __init__(self, devices, page):
        self.devices = devices
        self.page = page
        print(devices)

    async def connect_to_device(self, address):
        print(f"Connect to device: {address}")
        HEART_RATE_UUID = "00002a37-0000-1000-8000-00805f9b34fb"
        STEP_COUNT_UUID = "00030001-78fc-48fe-8e23-433b3a1942d0"
        RAW_XYZ_UUID = "00030002-78fc-48fe-8e23-433b3a1942d0"

        try:
            async with BleakClient(address) as client:
                heart_buffer = await client.read_gatt_char(HEART_RATE_UUID)
                step_buffer = await client.read_gatt_char(STEP_COUNT_UUID)
                raw_buffer = await client.read_gatt_char(RAW_XYZ_UUID)

                raw_data = np.frombuffer(raw_buffer, dtype=np.int16)
                step_data = np.frombuffer(step_buffer, dtype=np.int16)
                heart_data = np.frombuffer(heart_buffer, dtype=np.int8)

                result = f"Device {address} connected.\nMotion: {raw_data}\nHeart Rate: {heart_data[1]}\nStep Count: {step_data[0]}\n"
                return result
        except Exception as e:
            return f"Error connecting to device {address}: {e}"
        except BleakDeviceNotFoundError:
            return f"Device {address} not found"
        finally:
            if client.is_connected:
                await client.disconnect()

    async def connect_all_devices(self):
        await asyncio.sleep(1)
        results = []
        print(f"Devices to connect: {self.devices}")
        try:
            for device in self.devices:
                print(f"Connecting to device: {device[0]}")
                result = await self.connect_to_device(device[0])
                print(f"Emitting result for device: {result}")
                results.append(result)
                self.page.controls[1].value += result
                self.page.update()
            return results
        except Exception as e:
            print(f"Error connecting to device: {e}")

    def run(self):
        try:
            print("Connecting to devices")
            results = asyncio.run(self.connect_all_devices())
            print(f"Connection results: {results}")
            return results
        except Exception as e:
            print(f"Error connecting to devices: {e}")


def main(page: ft.Page):
    device_info = []
    page.title = "Pinetime Heartbeat Interface"

    def on_scan_button_click(e):
        page.controls[1].value = "Scanning for devices..."
        page.update()

        async def scan_devices():
            try:
                devices = await BleakScanner.discover()
                if not devices:
                    raise BleakError("No devices found")
                for d in devices:
                    print(d)
                page.controls[1].value = f"Number of devices: {len(devices)}"
                device_info.clear()
                for device in devices:
                    if device.name == "InfiniTime":
                        device_info.append([device.address, device.name])
                print(device_info)
                page.update()
            except BleakError as e:
                page.controls[1].value = "Error: Bluetooth is off"
                page.update()
            except Exception as e:
                page.controls[1].value = f"Error: {e}"
                page.update()

        asyncio.run(scan_devices())

    def on_connect_all_button_click(e):
        page.controls[2].value = "Connecting to all devices..."
        page.update()
        worker = DeviceWorker(device_info, page)
        thread = threading.Thread(target=worker.run)
        thread.start()

    def exit_button_click(e):
        page.window.close()


    scan_button = ft.ElevatedButton(text="Scan for devices", on_click=on_scan_button_click)
    connect_all_button = ft.ElevatedButton(text="Connect all devices", on_click=on_connect_all_button_click)
    exit_button = ft.ElevatedButton(text="Exit", on_click=exit_button_click)
    device_output = ft.TextField(label="Output", multiline=True, width=400, height=200)
    device_data_output = ft.TextField(label="Device Data", multiline=True, width=400, height=200)

    page.add(scan_button, device_output, connect_all_button, device_data_output, exit_button)


ft.app(target=main)
