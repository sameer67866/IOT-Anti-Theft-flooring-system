import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class PiezoSensor:
    def __init__(self):
        # Create the I2C bus
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # Create two ADC objects using the I2C bus for two ADS1115 chips
        self.ads1 = ADS.ADS1115(self.i2c)  # Default address 0x48 used for chip 1 connected to GND
        self.ads2 = ADS.ADS1115(self.i2c, address=0x4A)  # Second chip with address 0x4A Connected to SDA for different address

        # Create single-ended inputs for 4 channels on each ADS1115 chip
        self.channels_ads1 = [AnalogIn(self.ads1, ADS.P0), AnalogIn(self.ads1, ADS.P1), 
                              AnalogIn(self.ads1, ADS.P2), AnalogIn(self.ads1, ADS.P3)]
        self.channels_ads2 = [AnalogIn(self.ads2, ADS.P0), AnalogIn(self.ads2, ADS.P1), 
                              AnalogIn(self.ads2, ADS.P2), AnalogIn(self.ads2, ADS.P3)]

    def read_and_average_channels(self, channels):
        values = [channel.value for channel in channels]
        voltages = [channel.voltage for channel in channels]
        average_value = sum(values) / len(values)
        average_voltage = sum(voltages) / len(voltages)
        return average_value, average_voltage

    def read_sensors(self):
        avg_value_1, avg_voltage_1 = self.read_and_average_channels(self.channels_ads1)
        avg_value_2, avg_voltage_2 = self.read_and_average_channels(self.channels_ads2)
        return (avg_value_1, avg_voltage_1), (avg_value_2, avg_voltage_2)

if __name__ == "__main__":
    sensor = PiezoSensor()
    while True:
        readings_1, readings_2 = sensor.read_sensors()
        print(f"Tile 1 - Average Sensor Value: {readings_1[0]}, Average Voltage: {readings_1[1]:.2f}V")
        print(f"Tile 2 - Average Sensor Value: {readings_2[0]}, Average Voltage: {readings_2[1]:.2f}V")
