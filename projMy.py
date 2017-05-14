# -----------------------------------------------------------------
# Arquivo para o Vídeo Problemas em Python 09
# Disponivel em https://www.youtube.com/watch?v=sUn48z91if0
# Autor: Fernando Anselmo
# Compilado com Python 3.5.1
# -----------------------------------------------------------------

import json
import peewee
from peewee import *

db = MySQLDatabase('teste', host='127.0.0.1', port=3306, user='root', passwd='root')

class Aluno(peewee.Model):
    matricula = PrimaryKeyField()
    nome = CharField(max_length=30)
    status = BooleanField(default=True)

    def save(self, *args, **kwargs):
        return super(Aluno, self).save(*args, **kwargs)

    class Meta:
        database = db

def exemploDB():
    db.create_tables([Aluno])

def incluirAlunos():
    nomes = [
        {'nome': nomes}
        for nomes in ['Pedro', 'Paulo', 'Lucas']]
    query = Aluno.insert_many(nomes).return_id_list()
    query.execute()

def listarAlunos():
    try:
        alunos = Aluno.select(Aluno.matricula, Aluno.nome).where(Aluno.status != 0).order_by(Aluno.nome).dicts()
        if alunos.exists():
            alunosJSON = []
            for aluno in alunos:
                registro = {"matricula": aluno["matricula"], "nome": aluno["nome"]}
                alunosJSON.append(registro)
            return json.dumps(alunosJSON)
        else:
            print("Sem dados existentes")
    except Exception as e:
        print("Erro ao tentar listar:", str(e))

def exemploDB():
    db.create_tables([Aluno])
    incluirAlunos()
    print(listarAlunos())

if __name__ == '__main__':
    exemploDB()
