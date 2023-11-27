import sensor
import servo_motor  
import time
# import camera
# import coap_communication
def main():
    piezo_sensor = sensor.PiezoSensor()
    current_servo_angle = 60  # Starting angle
    servo=servo_motor.ServoMotor()
    servo.set_angle( current_servo_angle)  # Initialize servo to start position

    # Warm-up phase: let the sensors stabilize
    warmup_time = 10  # seconds
    print("Warming up sensors...")
    end_time = time.time() + warmup_time
    while time.time() < end_time:
        piezo_sensor.read_sensors()  # Read sensors to let them stabilize
        time.sleep(0.5)  # Sleep a bit between readings

    print("Sensors stabilized, starting motion detection.")

    last_reading_1, last_reading_2 = piezo_sensor.read_sensors()  # Initialize last readings

    while True:
        readings_1, readings_2 = piezo_sensor.read_sensors()
        
        # Check if there's a significant change in pressure on either tile
        if abs(readings_1[0] - last_reading_1[0]) > 5000:  # Tile 1
            current_servo_angle = max(60, current_servo_angle - 30)  # Move 30 degrees to the left
            servo.set_angle(current_servo_angle)
        elif abs(readings_2[0] - last_reading_2[0]) > 5000:  # Tile 2
            current_servo_angle = min(120, current_servo_angle + 30)  # Move 30 degrees to the right
            servo.set_angle(current_servo_angle)

        # Update last readings
        last_reading_1, last_reading_2 = readings_1, readings_2

        #add implementations of COAP and Camra

if __name__ == "__main__":
    main()
