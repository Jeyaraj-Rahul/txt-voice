from PyPDF2 import PdfReader
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

path = input("Enter the path of the PDF file: ")

try:
    reader = PdfReader(path)
except Exception as e:
    print("Error reading PDF:", e)
    exit()

for page in reader.pages:
    text = page.extract_text()
    if text:
        engine.say(text)
        engine.runAndWait()