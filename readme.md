# steps

1. [X] capture photo using RPi camera module/webcam
2. [ ] determine if photo is oriented correctly
3. [ ] determine that image contains text
4. [ ] preprocess the photo to white out non-text, make it greyscale, fix contrast, etc
5. [X] use tesseract ocr to extract text
6. [ ] use spellcheck library to spellcheck
7. [X] convert text to speech


## photo capture


## preprocessing
http://www.fmwconcepts.com/imagemagick/textcleaner/index.php
https://raw.githubusercontent.com/jasonlfunk/ocr-text-extraction/master/extract_text
https://stackoverflow.com/questions/28935983/preprocessing-image-for-tesseract-ocr-with-opencv
https://www.webuildinternet.com/2016/10/01/kraken-the-unknown-python-ocr-system/

## ocr
https://github.com/tesseract-ocr/tesseract/wiki
https://github.com/madmaze/pytesseract

## spellchecking
https://pypi.python.org/pypi/pygtkspellcheck
https://pypi.python.org/pypi/Whoosh/
https://pypi.python.org/pypi/autocorrect/0.1.0
https://github.com/rfk/pyenchant
http://norvig.com/spell-correct.html

## text-to-speech
https://launchpad.net/python-espeak
https://pypi.python.org/pypi/pyTTS
http://pythonprogramminglanguage.com/text-to-speech/
https://pypi.python.org/pypi/pyttsx

## theory
OCR TTS overview/architecture - https://sci-hub.io/10.1016/j.protcy.2014.10.135
State of the art, shaking image - https://sci-hub.io/10.1109/TMECH.2013.2261083
Better Indian RPi OCR - https://www.ijareeie.com/upload/2016/may/17_Image.pdf
Indian RPi OCR - https://arxiv.org/pdf/1405.6627.pdf
Another Indian RPi OCR - http://research.ijcaonline.org/ncpsia2015/number4/ncpsia17270.pdf

## battery
https://www.adafruit.com/product/1565

sudo apt-get install python-distutils-extra tesseract-ocr tesseract-ocr-eng libopencv-dev libtesseract-dev libleptonica-dev python-all-dev swig libcv-dev python-opencv python-numpy python-setuptools build-essential espeak tesseract-ocr-dev
