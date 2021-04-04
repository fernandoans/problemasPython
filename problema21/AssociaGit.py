#!/usr/bin/env python3

import sys
import os
from github import Github

path = "/home/fernando/Aplicativos/Projetos/"

username = "[UsuarioGit]"
password = "[Token]"


def criar():
    print("Para criar o projeto são necessários as seguintes informações:")
    nomeProj = input("Nome do projeto:")
    tipo = input("Tipo do projeto:")
    try:
        os.makedirs(path + "proj" + tipo + "/" + nomeProj)
        gh = Github(username, password)
        user = gh.get_user()
        rep = user.create_repo(nomeProj)
        print("Repositório criado com sucesso!")
    except OSError as ex:
        print("Problemas:", ex)


if __name__ == "__main__":
    print("Criação de Projetos no GitHub")
    criar()
