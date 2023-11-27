import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create two ADC objects using the I2C bus for two ADS1115 chips
ads1 = ADS.ADS1115(i2c)  # Default address 0x48
ads2 = ADS.ADS1115(i2c, address=0x4A)  # Second chip with address 0x4A

# Create single-ended inputs for 4 channels on each ADS1115 chip
channels_ads1 = [AnalogIn(ads1, ADS.P0), AnalogIn(ads1, ADS.P1), AnalogIn(ads1, ADS.P2), AnalogIn(ads1, ADS.P3)]
channels_ads2 = [AnalogIn(ads2, ADS.P0), AnalogIn(ads2, ADS.P1), AnalogIn(ads2, ADS.P2), AnalogIn(ads2, ADS.P3)]

# Function to read and average values from a list of channels
def read_and_average_channels(channels):
    values = [channel.value for channel in channels]
    voltages = [channel.voltage for channel in channels]
    average_value = sum(values) / len(values)
    average_voltage = sum(voltages) / len(voltages)
    return average_value, average_voltage

# Main loop to read and print averages for each ADS1115 chip
while True:
    avg_value_1, avg_voltage_1 = read_and_average_channels(channels_ads1)
    avg_value_2, avg_voltage_2 = read_and_average_channels(channels_ads2)

    print(f"Tile 1 - Average Sensor Value: {avg_value_1}, Average Voltage: {avg_voltage_1:.2f}V")
    print(f"Tile 2 - Average Sensor Value: {avg_value_2}, Average Voltage: {avg_voltage_2:.2f}V")

    time.sleep(1)
