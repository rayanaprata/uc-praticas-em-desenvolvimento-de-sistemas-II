from PySimpleGUI import PySimpleGUI as sg
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

def janela_inicial():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Olá, bem vindo ao sistema de cadastro de clientes!')],
        [],
        [sg.Text('Operações disponíveis:')],
        [sg.Button('Cadastrar'), sg.Button('Atualizar'), sg.Button('Excluir')],
    ]
    return sg.Window('Sistema de Cadastro', layout=layout, finalize=True)

def janela_cadastro():
    sg.theme('Reddit')
    cadastro = [
        [sg.Text('Nome        '), sg.Input(key='nome')],
        [sg.Text('Sobrenome'), sg.Input(key='sobrenome')],
        [sg.Text('Idade         '), sg.Input(key='idade')],
        [sg.Text('Peso         '), sg.Input(key='peso')],
        [sg.Button('Cadastrar Cliente'), sg.Button('Voltar')],
    ]
    return sg.Window('Cadastro de Clientes', layout=cadastro, finalize=True)

def janela_atualiza():
    sg.theme('Reddit')
    atualiza = [
        [sg.Text('Id do Cliente        '), sg.Input(key='idAt')],
        [sg.Text('Nome        '), sg.Input(key='nomeAt')],
        [sg.Text('Sobrenome'), sg.Input(key='sobrenomeAt')],
        [sg.Text('Idade         '), sg.Input(key='idadeAt')],
        [sg.Text('Peso         '), sg.Input(key='pesoAt')],
        [sg.Button('Atualizar Cliente'), sg.Button('Voltar')],
    ]
    return sg.Window('Atualização de Clientes', layout=atualiza, finalize=True)

def janela_deleta():
    sg.theme('Reddit')
    deleta = [
        [sg.Text('Id do Cliente        '), sg.Input(key='idDel')],
        [sg.Button('Deletar Cliente'), sg.Button('Voltar')],
    ]
    return sg.Window('Cadastro de Clientes', layout=deleta, finalize=True)

# Criando janelas iniciais
janelaIni, janelaCad, janelaAt, janelaDel = janela_inicial(), None, None, None

# Loop de Leitura de eventos / Ler os eventos e extrair os dados da tela
while True:
    window, event, values = sg.read_all_windows()

    #Quando a janela for fechada
    if window == janelaIni and event == sg.WINDOW_CLOSED:
        break

    # Cadastrar
    if window == janelaIni and event == 'Cadastrar':
        janelaCad = janela_cadastro()
        janelaIni.hide()

    if window == janelaCad and event == 'Cadastrar Cliente':
        cadNome = values['nome']
        cadSobrenome = values['sobrenome']
        cadIdade = values['idade']
        cadPeso = values['peso']

        # INSERE UM REGISTRO NA BASE DE DADOS
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
                        '(%s, %s, %s, %s)'
                cursor.execute(sql, (cadNome, cadSobrenome, int(cadIdade), int(cadPeso)))
                conexao.commit()

        sg.popup(f'Cliente {cadNome} cadastrado com sucesso!')

        # ESTE SELECIONA OS DADOS DA BASE DE DADOS
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM clientes')
                resultado = cursor.fetchall()

                for linha in resultado:
                    print(linha)

    if window == janelaCad and event == 'Voltar':
        janelaCad.hide()
        janelaIni.un_hide()

    # Atualizar
    if window == janelaIni and event == 'Atualizar':
        janelaAt = janela_atualiza()
        janelaIni.hide()

    if window == janelaAt and event == 'Atualizar Cliente':
        atId = values['idAt']
        atNome = values['nomeAt']
        atSobrenome = values['sobrenomeAt']
        atIdade = values['idadeAt']
        atPeso = values['pesoAt']

        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'UPDATE clientes SET nome=%s, sobrenome=%s, idade=%s, peso=%s WHERE id=%s'
                cursor.execute(sql, (atNome, atNome, atIdade, atPeso, atId))
                conexao.commit()

        sg.popup(f'Cliente {atNome} atualizado com sucesso!')

    if window == janelaAt and event == 'Voltar':
        janelaAt.hide()
        janelaIni.un_hide()

    # Excluir
    if window == janelaIni and event == 'Excluir':
        janelaDel = janela_deleta()
        janelaIni.hide()

    if window == janelaDel and event == 'Deletar Cliente':
        delId = values['idDel']

        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'DELETE FROM clientes WHERE id=%s'
                cursor.execute(sql, (delId))
                conexao.commit()

        sg.popup(f'Cliente {delId} deletado sucesso!')

    if window == janelaDel and event == 'Voltar':
        janelaDel.hide()
        janelaIni.un_hide()







