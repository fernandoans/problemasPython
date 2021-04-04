# -----------------------------------------------------------------
# Arquivo para o Vídeo Problemas em Python 12 e 13 - Aplicação Venda
# Usado somente para testar o programa vendaDao.py
# Disponivel em:
#  https://youtu.be/OJ60fyX8Imo
#  https://youtu.be/SDT8tzUG2Ek
# Autor: Fernando Anselmo
# Compilado com Python 3.5.1
# -----------------------------------------------------------------

from vendaDao import Venda

venda = Venda()
venda.produto = "PenDrive 8Gb"
venda.vendedor = "Paula Maria"
venda.valUnitario = "20.00"
venda.quantidade = "350"
venda.unidade = "DF"
venda.inserirVenda()
venda.selecionarVenda()
print(venda.produto + " - " + venda.vendedor)
