# Ground Station for Eggtimer RX

This is to provide bluetooth functionality to the Eggtimer RX Module, as HiPR has had issues with the provided bluetooth modules. The raspberry pi pico can connect to a phone or laptop over bluetooth to real the eggtimer telemetry.

## Hardware:
- Raspberry Pi Pico W
- Eggtimer RX Module
- Some wires

## Setup
1. Flash the Pico with MicroPython
2. Connect Pin 1 (RX) on the Pico to PGM TX on the Eggtimer
3. Connect GND on the Pico to PGM GND on the Eggtimer
4. Connect 3V3 on the Pico to PGM 3V3 on the Eggtimer
5. Copy this code over to the Pico

## Using
For iPhone use the nRF Connect App
1. Connect to the Pico (Name can be changed in ble_server.py, line 31)
2. Press the arrow down with line, this will continusly read data (see red circle on image)
3. Press the " symbol an change the format to 'UTF-8'
   
   <img src="https://github.com/user-attachments/assets/72298018-9700-4857-8733-b2c97bb805c4" alt="nrf connect screenshot" height="400">
4. The data recvied (seen in the 'Value' section) is 'Latitiude, Longitude, seconds since last gps fix', if no radio data is recvied, 'no data' will appear
