# pip install google_speech

from google_speech import Speech
import PyPDF2

# ABRIR O ARQUIVO PDF
book = open("oop.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages
# print(pages)

# OBTER O TEXTO
page = pdfReader.getPage(7)
text = page.extractText().encode("utf-8").decode("utf-8")
text = text.replace('\n', '')
print(text)

# LER O TEXTO
lang = "en_us"
speech = Speech(text, lang)
# speech.play()

# GRAVAR ARQUIVO
speech.save("saidaOOP.mp3")