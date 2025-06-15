# Eggtimer Ground Station using a Raspberry Pi Pico W

The is code for a Raspberry Pi Pico W using micropython. It reads in data from the [Eggfinder RX “Dongle” Receiver](https://eggtimerrocketry.com/home/eggfinder-gps-tracking-system/) over UART and transmits it over Bluetooth to any connected devices.
This is an alternative to the pre-sold bluetooth module as our team had issues. 
And phone or laptop can connect to the Ground Station using the nRF Connect App (or similar bluetooth app)

## Getting Started
- Flash the Pico W with the most recent version of micropython
- Upload this code to the Pico
- Connect the Eggfinder RX Receiver's RX, TX and GND pins (for the bluetooth module) to the UART and GND pins on the pico
- Connect the 3V3 Pin on the Pico to the + Pin on the Eggfinder Dongle
- Run the code

- On the nRF Connect App your pico device should appear and can be connected to
- Select the 'Read and Notify' Property
- Click the '⤓' button for location updates
- For data type choose 'uft-8'
- The incoming data can be copied using the ' ” ' button and pasted into google maps for location
