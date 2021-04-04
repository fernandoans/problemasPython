# -----------------------------------------------------------------
# Arquivo para o Vídeo Problemas em Python 17 - Sons
# Tocar sons de 8 bits através de beeps sobre a biblioteca pyaudio
# Disponivel em https://youtu.be/q39DeeNcILg
# Autor: Fernando Anselmo
# Compilado com Python 3.6
# -----------------------------------------------------------------
import pyaudio
from time import sleep

#        Tuner
# 2092 = 130.8 Hz C3
# 2346 = 146.8 Hz D3
# 2638 = 164.8 Hz E3
# 2793 = 174.6 Hz F3
# 3135 = 196.0 Hz G3
# 3518 = 220.0 Hz A3
# 3950 = 246.9 Hz B3

# 4185 = 261.6 Hz C4
# 4700 = 293.7 Hz D4
# 5275 = 329.6 Hz E4
# 5590 = 349.2 Hz F4
# 6270 = 392.0 Hz G4
# 7040 = 440.0 Hz A4
# 7900 = 493.9 Hz B4
# myRates = [2092,2346,2638,2793,3135,3518,3950]
myRates = [4185,4700,5275,5590,6270,7040,7900]
for v_rate in myRates:
    stream = pyaudio.PyAudio().open(format=pyaudio.paInt8,
        channels=1, rate=v_rate, output=True)
    for beep_num in range(0,2):
        for n in range(0,100,1):
            stream.write("\x00\x30\x5a\x76\x7f\x76\x5a\x30\x00\xd0\xa6\x8a\x80\x8a\xa6\xd0")
        sleep(1.2)
stream.close()
pyaudio.PyAudio().terminate()

