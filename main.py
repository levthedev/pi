# import espeak
import pytesseract
import pyttsx
from PIL import Image

text = pytesseract.image_to_string(Image.open('img/distorted.jpg'))
engine = pyttsx.init()
engine.say(text)
engine.runAndWait()
# es = espeak.ESpeak
# es.say(text)
