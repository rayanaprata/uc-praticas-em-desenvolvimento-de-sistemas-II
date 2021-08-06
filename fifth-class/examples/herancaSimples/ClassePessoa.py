class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    def Estudando(self):
        print(f'{self.nomeclasse} está falando...')
    
class Professor(Pessoa):
    def PepararAula(self):
        print('Professor preparando aula...')
    
class Aluno(Pessoa):
    def AssistindoAula(self):
        print('Aluno está assistindo aula...')


