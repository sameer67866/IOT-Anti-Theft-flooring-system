import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c, address=0x4A)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Function to read from the sensor
def read_piezo():
    print(f"Pressure Value: {chan.value}, Voltage: {chan.voltage:.2f}V")

# Read the sensor value every second
while True:
    read_piezo()
    time.sleep(2)
