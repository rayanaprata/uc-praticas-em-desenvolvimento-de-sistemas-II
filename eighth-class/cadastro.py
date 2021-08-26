import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='root',
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
""""
#INSERE UM REGISTRO NA BASE DE DADOS
with conecta() as conexao:
   with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
              '(%s, %s, %s, %s)'
        cursor.execute(sql, ('Jack', 'Monroe', 112, 220)) 
        conexao.commit()
"""
""" 
#DELETE DE UM REGISTRO NA BASE DE DADOS
with conecta() as conexao:
   with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id=%s'
        cursor.execute(sql, (3))
        conexao.commit()
"""
""" 
#DELETE DE VÁRIOS REGISTROS NA BASE DE DADOS
with conecta() as conexao:
   with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
        cursor.execute(sql, (14, 20))
        conexao.commit()
"""

#EDITAR  REGISTRO NA BASE DE DADOS
with conecta() as conexao:
   with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('Benedito', 4))
        conexao.commit()


# CONSULTA OS DADOS DA BASE DE DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)





