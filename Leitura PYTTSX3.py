# sudo apt-get update && sudo apt-get install espeak
# 1. pip install pyttsx3
# 2. sudo apt install libespeak1
# 3. pip install pypdf2

import pyttsx3

# Habilitar e Corrigir a Voz
speaker = pyttsx3.init('espeak') # sapi5 - nsss - espeak

speaker.setProperty('volume', 1.0) # 0.0 a 1.0

voices = speaker.getProperty('voices')
# for voice in voices:
#    print("Using voice:", voice.id)

voices = speaker.getProperty('voices')
for voice in voices:
    print(voice.languages[0])
    if voice.languages[0] == b'\x02en-us':
        print(voice)
        speaker.setProperty('voice', voice.id)
        break

speaker.setProperty('rate', 125)

# Falar o Texto
speaker.say("Hello World. My name is Fernando")
speaker.runAndWait()
speaker.stop()

# Outras Vozes pelo SO

# sudo apt-get install gnustep-gui-runtime
# say "hello"

# festival
# sudo apt-get install festival
# echo "hello" | festival --tts

# spd
# sudo apt-get install speech-dispatcher
# spd-say "hello"

# espeak
# sudo apt-get install espeak
# espeak "hello"