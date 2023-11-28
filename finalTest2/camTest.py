import time
from picamera2 import Picamera2, Preview
from datetime import datetime

# Initialize and start the camera when the module is imported
picam = Picamera2()
config = picam.create_preview_configuration()
picam.configure(config)
picam.start_preview(Preview.QTGL)
picam.start()
time.sleep(2)  # Camera warm-up time

def take_picture():
    # Generate filename based on current date and time
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
    picam.capture_file(filename)
    return filename

def stop_camera():
    picam.stop_preview()
    picam.close()

