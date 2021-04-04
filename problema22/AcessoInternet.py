# pip install speedtest-cli

import speedtest
from datetime import datetime
import csv
from threading import Timer


def iniciarCSV():
    header = ['Dia', 'Hora', 'Download MByte/s',
              'Download Mbit/s', 'Upload MByte/s', 'Upload Mbit/s']
    with open('velocidadeinternet.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)


def gravar_dados(dt, ht, dB, db, uB, ub):
    dB = int(dB * 100) / 100
    db = int(db * 100) / 100
    uB = int(uB * 100) / 100
    ub = int(ub * 100) / 100
    campos = [dt, ht, dB, db, uB, ub]
    with open('velocidadeinternet.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(campos)


def leitura():
    st = speedtest.Speedtest()
    down = st.download()
    upld = st.upload()
    dia = datetime.now().strftime("%d/%m/%Y")
    hor = datetime.now().strftime("%H:%M")
    downB = down / 8 / 1024 / 1000
    downb = down * (10 ** - 6)
    upldB = upld / 8 / 1024 / 1000
    upldb = upld * (10 ** -6)
    gravar_dados(dia, hor, downB, downb, upldB, upldb)
    Timer(1800, leitura).start()


if __name__ == '__main__':
    print('Velocidade da Internet (colhendo dados)')
    iniciarCSV()
    leitura()
