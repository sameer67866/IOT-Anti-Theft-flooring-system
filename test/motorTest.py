import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set GPIO 23 as output and set PWM signal
servoPin = 23
GPIO.setup(servoPin, GPIO.OUT)

# Set frequency to 50Hz
pwm = GPIO.PWM(servoPin, 50)
pwm.start(0)

def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servoPin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servoPin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        angle = float(input("Enter angle (0 to 180): "))
        setAngle(angle)
finally:
    # Clean up
    pwm.stop()
    GPIO.cleanup()
