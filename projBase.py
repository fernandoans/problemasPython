# -----------------------------------------------------------------
# Arquivo para o Vídeo Problemas em Python 08
# Disponivel em https://www.youtube.com/watch?v=K0Pzs-7elyE
# Autor: Fernando Anselmo
# Compilado com Python 3.5.1
# -----------------------------------------------------------------

import sqlite3

cur = None

def criarBase():
    cur.execute("PRAGMA Foreign_Keys=True")
    cur.execute("drop table if exists turma")
    cur.execute("drop table if exists professor")
    cur.execute("drop table if exists aluno")
    cur.execute('''
        create table aluno(
            ID INTEGER PRIMARY KEY,
            nome VARCHAR(30) NOT NULL)
        ''')
    cur.execute('''
        create table professor(
            ID INTEGER PRIMARY KEY,
            nome VARCHAR(30) NOT NULL,
            materia VARCHAR(30) NOT NULL)
        ''')
    cur.execute('''
        create table turma(
            IDaluno INTEGER NOT NULL REFERENCES aluno(ID),
            IDprofessor INTEGER NOT NULL REFERENCES professor(ID),
            data DATE NOT NULL,
            PRIMARY KEY(IDaluno, IDProfessor))
        ''')

def carregarDados():
    alunos = [
        [1, 'Maria Silva'],
        [2, 'Helena Buarque'],
        [3, 'Alex Silva']
    ]
    aluno_sql = '''
        INSERT INTO aluno
            (ID, nome) VALUES (?, ?)
        '''
    professores = [
        [1, 'Fernando Anselmo', 'Java'],
        [2, 'Soares Maria', 'SQL']
    ]
    professor_sql = '''
        INSERT INTO professor
            (ID, nome, materia) VALUES (?, ?, ?)
        '''
    turmas = [
        [1, 1, '2017/01/04'],
        [2, 1, '2017/09/05'],
        [1, 2, '2017/01/20'],
        [3, 2, '2017/11/19']
    ]
    turma_sql = '''
        INSERT INTO turma
            (IDaluno, IDprofessor, data) VALUES (?, ?, ?)
        '''
    cur.executemany(aluno_sql, alunos)
    cur.executemany(professor_sql, professores)
    cur.executemany(turma_sql, turmas)

def mostrarDados():
    for dado in cur.execute('''
            SELECT prof.nome, alu.nome, prof.materia, tur.data
            FROM turma tur 
            INNER JOIN aluno alu ON (tur.IDaluno = alu.ID)
            INNER JOIN professor prof ON (tur.IDprofessor = prof.ID)
            ''').fetchall():
        print(dado[0] + " - " + dado[1] + " - " + dado[2] + " - " + dado[3])

def exemploBD():
    global cur
    db = sqlite3.connect('curso.db')
    cur = db.cursor()
    # criarBase()
    # carregarDados()
    mostrarDados()
    cur.close()
    db.commit()
    db.close()

if __name__ == "__main__":
    exemploBD()
