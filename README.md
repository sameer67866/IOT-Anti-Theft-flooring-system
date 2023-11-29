# IOT Anti-Theft Flooring System 

Project for CSC 4980 - Security in IOT (Fall '23). This project uses a Raspberry Pi to implement an Anti-Theft Flooring System over a CoAP server.

## Objective

- Developing a Theft Detection System IoT application
- Use analog sensor input to trigger camera activation and server response 
- Knowledge on Raspberry Libraries for proper resource/sensor implementation
- Interfacing Servo Motor and Camera Module over CoAP


## Implementation

![Circuit image](https://github.com/sameer67866/IOT-Anti-Theft-flooring-system/blob/main/IOTImplementation.jpg?raw=true)


## Schematics

![Circuit image](https://github.com/sameer67866/IOT-Anti-Theft-flooring-system/blob/main/IOTCircuitImage.jpg?raw=true)

## Raspberry Pi Modules Used

- Raspberry Pi Camera Module
- ADS 1115 Chip
- Piezo-electric sensors
- Servo motor


## Built With

* [Smptlib](https://docs.python.org/3/library/smtplib.html) - SMTP protocol client for sending email alerts
* [Picamera2](https://github.com/raspberrypi/picamera2) - For camera module Interfacing 
* [Adafruit CircuitPython ADS1115](https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15) - For interfacing with ADS chip

## Demonstration

* [Demo video](https://drive.google.com/file/d/1ySCxcmnDBW4AQXz50BMR1iuclCvnnUgW/view?usp=sharing)
* [Presentation](https://1drv.ms/p/s!Aike8jU30iDOgZZKH180BO12HymP0g?e=jNXHjP)
* [Project poster](https://docs.google.com/presentation/d/1p_RyZlE7ew_euwt0hkcAPQ_A-vDhHCEu/edit?usp=sharing&ouid=106989836719408766777&rtpof=true&sd=)

## Authors

* **[Abdul Shoaib Mohammed](https://github.com/moidshoaib)**
* **[Muhammad Sameer](https://github.com/sameer67866)**
* **[Talha Ansari](https://github.com/VetinariLives)**


## Acknowledgments

* Professor - Dr. Haoxin Wang

## Pi Setup
### To run pip3 commands:
```bash
sudo apt-get install python3-pip
sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
```
### To install Adafruit CircuitPython ADS library:
```bash
pip3 install adafruit-circuitpython-ads1x15
```
### To enable I2C on Pi
```bash
raspi-config
```
Select Interfacing Options > I2C.

Select Yes when prompted to enable the I2C interface.

Select Yes when prompted to automatically load the I2C kernel module.

Select Finish.
```bash
sudo reboot
```
