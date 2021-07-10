# -------------------------------------------------------------
# Optical Character Recognition ou Optical Character Reader
# -------------------------------------------------------------
# sudo apt-get install tesseract-ocr tesseract-ocr-por
# sudo pip install pytesseract
# tesseract LGPD01.png saida -l por
# -------------------------------------------------------------

from PIL import Image
import pytesseract

with open("/home/fernando/Pictures/Palestras/meuGDPR.txt", "w") as f:
    for i in range(1, 42):
        nomeImg = '/home/fernando/Pictures/Palestras/GDPR/GDPR' + \
            ('0' if i < 10 else '') + str(i) + '.png'
        f.writelines(pytesseract.image_to_string(
            Image.open(nomeImg), lang='por'))
