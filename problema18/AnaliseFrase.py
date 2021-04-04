from textblob import TextBlob

frase = TextBlob("Fernando está apaixonado pelo Facebook, por causa das redes sociais. Ele gosta muito")
traduz = TextBlob(str(frase.translate(to="en")))
print(traduz.tags)
print(traduz.words)
print("Polaridade: ", traduz.polarity) # -1 < p < 1
print("Subjetividade:", traduz.subjectivity) # 0 < s < 1