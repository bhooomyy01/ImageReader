from PIL import Image
import pytesseract
import win32com.client

#Include tesseract exe. path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

# image object
image = Image.open('image1.png')

#Pass image object to text

text = pytesseract.image_to_string(image, lang='eng')

print(text)

speaker=win32com.client.Dispatch("SAPI.SpVoice")
speaker.speak(text)
#To stop execution Press CTRL + Z