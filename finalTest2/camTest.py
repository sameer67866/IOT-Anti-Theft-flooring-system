import time
from picamera2 import Picamera2, Preview
from datetime import datetime

def take_picture():
    picam = Picamera2()
    config = picam.create_preview_configuration()
    picam.configure(config)
    picam.start_preview(Preview.QTGL)
    picam.start()
    time.sleep(2)
    
    # Generate filename based on current date and time
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
    picam.capture_file(filename)
    picam.close()
    return filename

