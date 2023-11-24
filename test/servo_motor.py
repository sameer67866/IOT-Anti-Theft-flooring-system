import RPi.GPIO as GPIO
import time

class ServoMotor:
    def __init__(self):
        # Set up the GPIO mode
        GPIO.setmode(GPIO.BCM)

        # Set GPIO 17 as output and set PWM signal
        self.servoPin = 17
        GPIO.setup(self.servoPin, GPIO.OUT)

        # Set frequency to 50Hz
        self.pwm = GPIO.PWM(self.servoPin, 50)
        self.pwm.start(0)

    def set_angle(self, angle):
        duty = angle / 18 + 2
        GPIO.output(self.servoPin, True)
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(self.servoPin, False)
        self.pwm.ChangeDutyCycle(0)

    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()
