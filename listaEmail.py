# -*- coding: utf-8 -*-

import wget

class Leitura:
    def obterArquivo(self):
        self.nomeArq = '[EFR]_3_Things_1'
        self.caminho = '/home/fernando/Aplicativos/Ingles/'
        self.url = ''

    def montagem(self):
        entrada = open(self.caminho + self.nomeArq + '.eml', 'r+')
        saida = open(self.caminho + self.nomeArq + '.html', 'w')
        inicia = False
        mostra1 = True
        mostra2 = True
        print('Passo 1. Gerando arquivo...')
        for linha in entrada:
            if linha.strip().startswith('<!DOCTYPE'):
                inicia = True
            if '<div align="center">' in linha:
                mostra1 = False
            if linha.strip().startswith('<div id="fromDMARC"'):
                mostra2 = False
            if not mostra2 and linha.strip().startswith('</body>'):
                mostra2 = True
            if inicia and mostra1 and mostra2 and len(linha.strip()) > 0:
                if ('.mp3' in linha):
                    self.url = linha
                saida.write(linha)
            if not mostra1 and linha.strip().startswith('</div>'):
                mostra1 = True
            if linha.strip().startswith('</html>'):
                break
        print('Passo 2. Arquivo gerado.')
        entrada.closed
        saida.closed

    def baixarMp3(self):
        if len(self.url) > 0:
            print('Passo 3. Baixando arquivo MP3...')
            self.url = self.url[self.url.index('http'):self.url.index('.mp3')+4]
            wget.download(self.url, self.caminho + self.nomeArq + '.mp3')
            print('Passo 4. Arquivo MP3 baixado.')
        else:
            print('Passo 3. Não existe arquivo MP3')

def main():
    ler = Leitura()
    ler.obterArquivo()
    ler.montagem()
    ler.baixarMp3()

if __name__ == '__main__':
    main()