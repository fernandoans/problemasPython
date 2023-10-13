# pip install gTTS
# pip install playsound
from gtts import gTTS
import gtts
from playsound import playsound

# Diretório + nome do arquivo
audio = "saida.mp3"

# Linguagem do Texto
language = "pt-br"

# Texto a ser pronunciado
texto = "Com a biblioteca gTTS é possível criar arquivos de áudio com a frase ou texto que desejar."

sp = gTTS(text=texto, lang=language, slow=False)
sp.save(audio)

# Ouvir
playsound(audio)
