import pyautogui
import pytesseract
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

typing_box = (310, 340, 670, 378)

while True:
    img = ImageGrab.grab(bbox=typing_box).convert('L')
    text = pytesseract.image_to_string(img, lang='eng', config='--psm 7')
    text = text.strip().replace('\n', '')

    if text:
        print(text)
        pyautogui.typewrite(text)
        #pyautogui.press('enter')
    else:
        print("errer")
        time.sleep(0.05)