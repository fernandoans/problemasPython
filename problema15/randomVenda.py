# -----------------------------------------------------------------
# Arquivo para o Vídeo Problemas em Python 15 - Aplicação Venda
# Gerar dados Randômicos
# Disponivel em:
#  https://youtu.be/zYKRmQT4LeI
# Autor: Fernando Anselmo
# Compilado com Python 3.5.1
# -----------------------------------------------------------------

import MySQLdb
from random import randint

listProduto = ['Meia Socket|3.45', 'Calça Nylon|8.25', 'Camiseta|5.00', 'Camisa Polo|8.00', 'Meia Algodão|4.80']
listVendedor = ['Pedro Madureira', 'Paulo Nogueira', 'Judas Barroso', 'Lucas Ramos', 'Marcia Madalena']
listUnidade = ['DF', 'RJ', 'SP', 'MG']

produto = ''
vendedor = ''
valUnitario = ''
quantidade = ''
unidade = ''
dataCria = ''

class Banco(object):
    def conectar(self):
        self.db = MySQLdb.connect(db = 'corp', host = '127.0.0.1', port = 3306,
                                  user = 'root', passwd = 'root')
        self.cur = self.db.cursor()

    def desconectar(self):
        self.cur.close()
        self.db.close()

class Venda(object):

    def __init__(self, id = 0, produto = "", vendedor = "", valUnitario = "",
                 quantidade = "", unidade = "", dataCria = ""):
        self.info = {}
        self.id = id
        self.produto = produto
        self.vendedor = vendedor
        self.valUnitario = valUnitario
        self.quantidade = quantidade
        self.unidade = unidade
        self.dataCria = dataCria

    def inserirVenda(self):
        banco = Banco()
        banco.conectar()
        banco.cur.execute(
            "INSERT INTO venda (produto, vendedor, valUnitario, quantidade, " +
            "unidade, createdAt, updatedAt) values ('" +
            self.produto + "', '" + self.vendedor + "', " +
            self.valUnitario + ", " + self.quantidade + ", '" +
            self.unidade + "', '" + self.dataCria + "', NOW())"
        )
        banco.db.commit()
        banco.desconectar()

def montarDados():
    global produto, vendedor, valUnitario, quantidade, unidade, dataCria
    selProdPreco = listProduto[randint(0,4)]
    produto = selProdPreco.split('|')[0]
    valUnitario = selProdPreco.split('|')[1]
    vendedor = listVendedor[randint(0,4)]
    quantidade = randint(10,1000)
    unidade = listUnidade[randint(0,3)]
    dataCria = '2016/' + str(randint(1,12)) + '/' + str(randint(1,28))

def cadastrarDados():
    venda = Venda()
    venda.produto = produto
    venda.vendedor = vendedor
    venda.valUnitario = valUnitario
    venda.quantidade = str(quantidade)
    venda.unidade = unidade
    venda.dataCria = dataCria
    venda.inserirVenda()

def processar():
    for x in range(1, 100):
        montarDados()
        cadastrarDados()

if __name__ == '__main__':
    processar()












