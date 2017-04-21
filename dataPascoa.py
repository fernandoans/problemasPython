# -*- coding: utf-8 -*-

# -----------------------------------------------------------------
# Arquivo para o Vídeo Problemas em Python 05
# Disponivel em https://www.youtube.com/watch?v=wbM7YhfcSqs&t=176s
# Autor: Fernando Anselmo
# Compilado com Python 3.5.1
# -----------------------------------------------------------------

from datetime import date

class Pascoa:

    def mostrar(self, mes):
        # Monta a data exata da Pásco no Ano
        dtPA = date(self.ano, mes, self.dia)
        # Carnaval ocorre 47 dias antes
        dtCN = date.fromordinal(dtPA.toordinal() - 47)
        # Corpus Christ ocorre 60 dias depois
        dtCC = date.fromordinal(dtPA.toordinal() + 60)
        print("O Carnaval é em ", dtPA.strftime('%d/%m/%Y'))
        print("a Páscoa em ", dtCN.strftime('%d/%m/%Y'))
        print("e Corpus Christ em ", dtCC.strftime('%d/%m/%Y'))

    def obterAno(self):
        self.ano = int(input("Informe o Ano:"))

    def realizarCalculo(self):
        p1 = (19 * (self.ano % 19) + 24) % 30
        p2 = (2 * (self.ano % 4) + 4 * (self.ano % 7) + 6 * p1 + 5) % 7
        res = p1 + p2
        if res > 9:
            self.dia = res - 9
            self.mostrar(4)
        else:
            self.dia = res + 22
            self.mostrar(3)

def principal():
    pascoa = Pascoa()
    pascoa.obterAno()
    pascoa.realizarCalculo()

if __name__ == '__main__':
    principal()