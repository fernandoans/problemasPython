# -*- coding: utf-8 -*-

# -----------------------------------------------------------------
# Arquivo para o Vídeo Problemas em Python 10
# Disponivel em https://youtu.be/ishz_YHogxs
# Autor: Fernando Anselmo
# Compilado com Python 3.5.1
# -----------------------------------------------------------------

from tkinter import *
import tkinter.filedialog
import tkinter.messagebox

NOME_APP = "Aplicação"
root = Tk()

def sair(event=None):
    if tkinter.messagebox.askokcancel("Sair", "Deseja realmente sair?"):
        root.destroy()

def showJanela(event=None):
    tkinter.messagebox.showinfo("Opção 1", "Esta é uma opção", icon='info')

def showSobre(event=None):
    tkinter.messagebox.showinfo("Sobre",
        "{}{}".format(NOME_APP, "\nMinha aplicação Gráfica\nPython com Gráfico"),
        icon='question')

def montarMenu():
    menu_bar = Menu(root)
    arq_menu = Menu(menu_bar, tearoff=0)
    aux_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Arquivo', underline=0, menu=arq_menu)
    menu_bar.add_cascade(label='Auxílio', underline=0, menu=aux_menu)
    root.config(menu=menu_bar)
    arq_menu.add_command(label='Opção 1', compound='left', command=showJanela)
    arq_menu.add_separator()
    arq_menu.add_command(label='Sair', accelerator='Alt+F4', compound='left', command=sair)
    aux_menu.add_command(label='Sobre...', compound='left', command=showSobre)

def principal():
    montarMenu()
    root.protocol('WM_DELETE_WINDOW', sair)
    root.title(NOME_APP)
    root.geometry("500x400")
    root.mainloop()

if __name__ == '__main__':
    principal()

