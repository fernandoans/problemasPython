# -----------------------------------------------------------------
# Arquivo para o Vídeo Problemas em Python 11 e 14 - Aplicação Venda
# Tela de Vendas
# Disponivel em https://youtu.be/rdPL5v-RwOs
# Finalizada em https://youtu.be/436lM99wRhY (junção com a DAO)
# Autor: Fernando Anselmo
# Compilado com Python 3.5.1
# -----------------------------------------------------------------

from tkinter import *
from vendaDao import Venda

vendaDao = Venda()

class Venda:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master, padx=5, pady=5)
        self.container1.pack()
        self.lblpin = Label(self.container1, text="PIN:", font=self.fonte, width=10, anchor=E, justify=RIGHT)
        self.lblpin.pack(side=LEFT)
        self.txtpin = Entry(self.container1, font=self.fonte, width=10)
        self.txtpin.pack(side=LEFT)
        self.btnbuscar = Button(self.container1, text="Buscar", font=self.fonte, width=10)
        self.btnbuscar["command"] = self.buscarVenda
        self.btnbuscar.pack(side=RIGHT, padx=10)

        self.container2 = Frame(master, padx=5, pady=5)
        self.container2.pack()
        self.lblproduto = Label(self.container2, text="Produto:", font=self.fonte, width=15, anchor=E, justify=RIGHT)
        self.lblproduto.pack(side=LEFT)
        self.txtproduto = Entry(self.container2, font=self.fonte, width=25)
        self.txtproduto.pack(side=LEFT)

        self.container3 = Frame(master, padx=5, pady=5)
        self.container3.pack()
        self.lblvendedor = Label(self.container3, text="Vendedor:", font=self.fonte, width=15, anchor=E, justify=RIGHT)
        self.lblvendedor.pack(side=LEFT)
        self.txtvendedor = Entry(self.container3, font=self.fonte, width=25)
        self.txtvendedor.pack(side=LEFT)

        self.container4 = Frame(master, padx=5, pady=5)
        self.container4.pack()
        self.lblvalor = Label(self.container4, text="Valor Unitário:", font=self.fonte, width=15, anchor=E, justify=RIGHT)
        self.lblvalor.pack(side=LEFT)
        self.txtvalor = Entry(self.container4, font=self.fonte, width=25)
        self.txtvalor.pack(side=LEFT)

        self.container5 = Frame(master, padx=5, pady=5)
        self.container5.pack()
        self.lblquantidade = Label(self.container5, text="Quantidade:", font=self.fonte, width=15, anchor=E, justify=RIGHT)
        self.lblquantidade.pack(side=LEFT)
        self.txtquantidade = Entry(self.container5, font=self.fonte, width=25)
        self.txtquantidade.pack(side=LEFT)

        self.container6 = Frame(master, padx=5, pady=5)
        self.container6.pack()
        self.lblunidade = Label(self.container6, text="Unidade:", font=self.fonte, width=15, anchor=E, justify=RIGHT)
        self.lblunidade.pack(side=LEFT)
        self.txtunidade = Entry(self.container6, font=self.fonte, width=25)
        self.txtunidade.pack(side=LEFT)

        self.container7 = Frame(master, padx=5, pady=10)
        self.container7.pack()
        self.btninserir = Button(self.container7, text="Inserir", font=self.fonte, width=10)
        self.btninserir["command"] = self.inserirVenda
        self.btninserir.pack(side=RIGHT, padx=10)
        self.btnalterar = Button(self.container7, text="Alterar", font=self.fonte, width=10)
        self.btnalterar["command"] = self.alterarVenda
        self.btnalterar.pack(side=RIGHT, padx=10)
        self.btnexcluir = Button(self.container7, text="Excluir", font=self.fonte, width=10)
        self.btnexcluir["command"] = self.excluirVenda
        self.btnexcluir.pack(side=RIGHT, padx=10)

    def buscarVenda(self):
        vendaDao.id = int(self.txtpin.get())
        vendaDao.produto = ''
        vendaDao.vendedor = ''
        vendaDao.valUnitario = ''
        vendaDao.quantidade = ''
        vendaDao.unidade = ''
        vendaDao.selecionarVenda()
        self.carregarCampos()

    def inserirVenda(self):
        self.carregarObjeto()
        vendaDao.inserirVenda()
        self.limparCampos()

    def alterarVenda(self):
        self.carregarObjeto()
        vendaDao.alterarVenda()
        self.limparCampos()

    def excluirVenda(self):
        vendaDao.id = int(self.txtpin.get())
        vendaDao.excluirVenda()
        self.limparCampos()

    def carregarObjeto(self):
        vendaDao.produto = self.txtproduto.get()
        vendaDao.vendedor = self.txtvendedor.get()
        vendaDao.valUnitario = self.txtvalor.get()
        vendaDao.quantidade = self.txtquantidade.get()
        vendaDao.unidade = self.txtunidade.get()

    def limparCampos(self):
        self.txtproduto.delete(0, END)
        self.txtvendedor.delete(0, END)
        self.txtvalor.delete(0, END)
        self.txtquantidade.delete(0, END)
        self.txtunidade.delete(0, END)

    def carregarCampos(self):
        self.txtproduto.insert(INSERT, vendaDao.produto)
        self.txtvendedor.insert(INSERT, vendaDao.vendedor)
        self.txtvalor.insert(INSERT, vendaDao.valUnitario)
        self.txtquantidade.insert(INSERT, vendaDao.quantidade)
        self.txtunidade.insert(INSERT, vendaDao.unidade)










