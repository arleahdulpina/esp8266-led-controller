# ESP8266 Chip Micro Python

- make sure driver is installed correctly
- port is /dev/ttyUSB0
- baud rate 9600
- make sure user in in dialout group if permission is denied
  
# Getting Started
Requirements
- `pip install esptool`
- `pip install setuptools`
  
Erase Flash
- `python -m esptool --port /dev/ttyUSB0 erase_flash`

Deploy MicroPython Firmware
- `python -m esptool --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-1m-20200902-v1.13.bin`

# REPL
## WIFI
SSID: MicroPython7729e2
PSK: micropythoN

