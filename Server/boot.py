try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
from network import WLAN

# import esp
# esp.osdebug(None)

import gc
gc.collect()

ssid = 'Realme 2 Pro'
password = '12345678'

station = WLAN(mode=WLAN.STA)

# station.active(True)
station.connect(ssid=ssid, auth=(WLAN.WPA2,password))

while station.isconnected() == False:
    print(".",end='')
    pass

print('Connection successful')
print(station.ifconfig())

# led = Pin(2, Pin.OUT)
Pin.exp_board.G16
led = Pin(Pin.exp_board.G16, mode=Pin.OUT)
Pin.exp_board.G16.id()
