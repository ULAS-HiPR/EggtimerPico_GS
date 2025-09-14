import time
import bluetooth
from ble_server import BLESimplePeripheral
from machine import Pin, UART
import gps_parser
import struct

    
tx = Pin(0)
rx = Pin(1)


    
uart = UART(0, 9600, tx=tx, rx=rx)       
ble = bluetooth.BLE()
p = BLESimplePeripheral(ble)
file_name = 'gps_data.txt'

time.sleep(3)
    

gps = gps_parser.GPSReader(uart)

data = []
time_since_fix = time.time()
time_since_save = time.time()
last_data = 'no data'
while True:
    
    #raw = uart.read()
    #if raw:
    #    print(raw.decode())
    #else:
    #    print('none')
    try:
        gps_data = gps.get_data()
    
        if (gps_data.latitude) or (gps_data.longitude):
            location_data = str(gps_data.latitude).encode('utf-8') + " " + str(gps_data.longitude).encode('utf-8')
            last_data = location_data
            time_since_fix = time.time()
        sending_data = last_data + ', ' + str(time.time() - time_since_fix)
        p.send(sending_data)
        print(sending_data)

    except:
        pass
        
    time.sleep(0.5)

        