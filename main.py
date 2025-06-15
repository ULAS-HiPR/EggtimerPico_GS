import time
import bluetooth
from ble_server import BLESimplePeripheral
from machine import Pin, UART
import gps_parser
import struct
    
tx = Pin(4)
rx = Pin(5)


    
uart = UART(1, 9600, tx=tx, rx=rx)       
ble = bluetooth.BLE()
p = BLESimplePeripheral(ble)

time.sleep(3)
    
gps = gps_parser.GPSReader(uart)

loop = 0
while True:
    

    gps_data = gps.get_data()
    
    print(gps_data.has_fix, gps_data.latitude, gps_data.longitude)
    sending_data = str(gps_data.latitude).encode('utf-8') + " " + str(gps_data.longitude).encode('utf-8')
    
    p.send(sending_data)
    print(sending_data, loop)
    loop += 1
    time.sleep(0.5)

        