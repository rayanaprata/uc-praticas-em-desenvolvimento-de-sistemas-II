# Utilizando o banco de dados SQLITE e GUI do Python, implementar uma agenda de nomes e telefones.

from tkinter import *
import sqlite3

class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')
        return self.cursor.fetchall()

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

    def criarTab(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS agenda (''id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT NOT NULL,'
               'telefone INTEGER NOT NULL UNIQUE'
               ')')

if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.criarTab()
    
class Application:

    def __init__(self,toplevel):
        toplevel.title('Agenda')

        self.frm=Frame(toplevel)
        self.frm2=Frame(toplevel)
        self.frm.pack()
        self.frm2.pack()

        Label(self.frm,text='Bem vindo a agenda de telefone').pack()

        Label(self.frm2,text='Nome:').pack()
        self.nomeDig=Entry(self.frm2)
        self.nomeDig.pack()  

        Label(self.frm2,text='Telefone:').pack()
        self.telDig=Entry(self.frm2)
        self.telDig.pack()

        self.button=Button(self.frm2)
        self.button['text']='Cadastrar'
        self.button.bind('<Button-1>',self.cadastrar)
        self.button.pack()

        self.button=Button(self.frm2)
        self.button['text']='Mostrar cadastrados'
        self.button.bind('<Button-1>',self.mostrarCadastrados)
        self.button.pack()

        self.cadastrados=Label(self.frm2)
        self.cadastrados['text']=''
        self.cadastrados.pack()

    def cadastrar(self,event):
        nome=(self.nomeDig.get())
        tel=(self.telDig.get())

        agenda = AgendaDB('agenda.db')
        agenda.inserir(nome, tel)
        agenda.listar()

    def mostrarCadastrados(self, event):
        agenda = AgendaDB('agenda.db')
        contatos = agenda.listar()

        self.cadastrados['text'] = contatos
        self.cadastrados.pack()

root=Tk()
Application(root)
root.mainloop()
