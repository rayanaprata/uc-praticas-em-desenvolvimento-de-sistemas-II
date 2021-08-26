import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='user',
        password='user',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


#INSERE UM REGISTRO NA BASE DE DADOS
with conecta() as conexao:
   with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
              '(%s, %s, %s, %s)'
        cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
        conexao.commit()

# ESTE SELECIONA OS DADOS DA BASE DE DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)


