# pip install google_speech

from google_speech import Speech
import PyPDF2

# ABRIR O ARQUIVO PDF
book = open("oop.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
# print(pages)


# OBTER O TEXTO
page = pdfReader.getPage(7)
text = page.extractText().encode("utf-8").decode("utf-8")

# LER O TEXTO
lang = "pt_BR"
speech = Speech(text, lang)
sox_effects = ("speed", "1.06")
# speech.play(sox_effects)

# GRAVAR ARQUIVO
speech.save("Oop.mp3")
