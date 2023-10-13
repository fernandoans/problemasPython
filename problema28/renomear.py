import glob

# pip install mutagen
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

fpath = u"/home/fernando/Downloads/Music/Seventies Feel Good/*.mp3"
print(fpath)
files = glob.glob(fpath)

for fname in files:
    if fname.endswith(".mp3"):
        print("Processando... %s" % fname)
        audio = MP3(fname, ID3=EasyID3)
        audio["composer"] = audio["artist"]
        audio["artist"] = "Decada"
        audio["album"] = "Seventies Feel Good"
        audio.save()
        print("Processado... %s" % audio["composer"])

        # track - title - albumartist - date - genre
