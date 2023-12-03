import sensor
import servo_motor
import time
from camera import take_picture  # Import the take_picture function
from sendGmailAlert import send_email_with_filename  # Import the email sending function


def main():
	piezo_sensor = sensor.PiezoSensor()
	current_servo_angle = 45  # Starting angle
	servo=servo_motor.ServoMotor()
	servo.set_angle(current_servo_angle)  # Initialize servo to start position

   	 # Warm-up phase: let the sensors stabilize
	warmup_time = 10  # seconds
	print("Warming up sensors...")
	end_time = time.time() + warmup_time
	while time.time() < end_time:
		piezo_sensor.read_sensors()  # Read sensors to let them stabilize
       		# time.sleep(0.1)  # Sleep a bit between readings

	print("Sensors stabilized, starting motion detection.")

	last_reading_1, last_reading_2 = piezo_sensor.read_sensors()  # Initialize last readings

	while True:
		readings_1, readings_2 = piezo_sensor.read_sensors()
		print(f"tile 1 avg: {readings_1[0]}, Tile2:{readings_2[0]}")

        	# Check if there's a significant change in pressure on either tile
		if abs(readings_1[0] - last_reading_1[0]) > 5000:  # Tile 1
			if (current_servo_angle !=70):
				current_servo_angle = 70  # Move 30 degrees to the left
				servo.set_angle(current_servo_angle)
				filename = take_picture()  # Take picture and get filename
				print(f"Picture taken: {filename}")
				filename = take_picture()  # Take another picture and get filename
				send_email_with_filename(filename)  # Send email with filename

		elif abs(readings_2[0] - last_reading_2[0]) > 5000:  # Tile 2
			if (current_servo_angle != 20):
				current_servo_angle = 20  # Move 30 degrees to the right
				servo.set_angle(current_servo_angle)
				filename = take_picture()  # Take picture and get filename
				print(f"Picture taken: {filename}")
				filename = take_picture()  # Take another picture and get filename
				send_email_with_filename(filename)  # Send email with filename

        	# Update last readings
		last_reading_1, last_reading_2 = readings_1, readings_2

        #add implementations of COAP and Camra

if __name__ == "__main__":
	main()
