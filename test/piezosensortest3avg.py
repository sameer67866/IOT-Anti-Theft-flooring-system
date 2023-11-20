
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c, address=0x4A)

# Create single-ended inputs for 4 channels
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

# Function to read from the sensors and calculate average
def read_and_average_piezos():
    values = [chan0.value, chan1.value, chan2.value, chan3.value]
    voltages = [chan0.voltage, chan1.voltage, chan2.voltage, chan3.voltage]

    average_value = sum(values) / len(values)
    average_voltage = sum(voltages) / len(voltages)

    print(f"Average Sensor Value: {average_value}, Average Voltage: {average_voltage:.2f}V")

# Read the sensor values and calculate average every second
while True:
    read_and_average_piezos()
    time.sleep(1)
