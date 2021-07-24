from google_speech import Speech

lang = "pt_BR"
sox_effects = ("speed", "1.06")

with open("LeiInovacao", "r") as f:
    texto = f.readlines()

textoFim = ""
totLin = 0
numPag = 1

for lin in texto:
    lin = lin.encode("utf-8").decode("utf-8").replace('\n', ' ')
    textoFim += lin
    totLin += 1
    if (totLin == 20):
        speech = Speech(textoFim, lang)
        speech.save("LeiInovacao" + str(numPag) + ".mp3")
        textoFim = ""
        totLin = 0
        numPag += 1

if (totLin > 0):
    speech = Speech(textoFim, lang)
    speech.save("LeiInovacao" + str(numPag) + ".mp3")
