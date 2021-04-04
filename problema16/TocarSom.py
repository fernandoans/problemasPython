# -----------------------------------------------------------------
# Arquivo para o Vídeo Problemas em Python 16 - Tocar Som
# Esqueleto para a criação de um Player de Som
# Disponivel em https://youtu.be/8jpvvM6cc3k
# Autor: Fernando Anselmo
# Compilado com Python 3.5.1
# -----------------------------------------------------------------

import pyaudio
import wave
import os
import threading

class WavePlayerLoop(threading.Thread):

    def __init__(self, filepath, loop=True):
        super(WavePlayerLoop, self).__init__()
        self.filepath = os.path.abspath(filepath)
        self.loop = loop

    def run(self):
        CHUNK = 2048
        wf = wave.open(self.filepath, 'rb')
        player = pyaudio.PyAudio()
        stream = player.open(
            format=player.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )
        data = wf.readframes(CHUNK)
        while self.loop:
            stream.write(data)
            data = wf.readframes(CHUNK)
            if data == b'':
                # wf.rewind()
                self.stop()
        stream.close()
        player.terminate()

    def play(self):
        self.start()

    def stop(self):
        self.loop = False

def principal():
    tocar = WavePlayerLoop("Bass_NS2_05.wav")
    tocar.play()
    print('Olá')

if __name__ == "__main__":
    principal()




