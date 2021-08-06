class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

    def falar(self):
        print(f'{self.nomeclasse} estou em CLIENTE...')
    
class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome
            
    def falar(self):
        print('Imprime outra coisa')

        super().falar()
        Pessoa.falar(self)
        print(f'{self.nome} {self.sobrenome}')
        