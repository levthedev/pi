import io
import pytesseract
import pyttsx
import pycamera
from time import sleep
from PIL import Image

stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_preview()
    sleep(5)
    camera.capture(stream, format="jpeg")

print("captured photo")
stream.seek(0)
image = Image.open(stream)
text = pytesseract.image_to_string(image)
text = text.replace("\n", ", ").replace("\r", "").encode("ascii", "ignore")
print("converted text: {}".format(text))
engine = pyttsx.init()
print("created engine")
engine.say(text)
print("added text to queue")
engine.runAndWait()
print("said text")
