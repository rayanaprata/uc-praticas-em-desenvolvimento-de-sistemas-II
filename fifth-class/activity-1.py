# Implementar o diagrama contendo as classes Pessoa, Estudante e Professor

class Pessoa:
  def __init__(self, nome, idade, email):
    self.nome = nome
    self.idade = idade
    self.email = email

  def falar(self):
    print('Falar')

  def listar(self):
    print('Listar')

class Estudante(Pessoa):
  def __init__(self, nome, idade, email, matricula):
    Pessoa.__init__(self, nome, idade, email)
    self.matricula = matricula

  def verAula(self):
    print(f'{self.nome} está assistindo aula.')

  def falar(self):
    print(f'Estudante {self.nome} está falando.')

class Professor(Pessoa):
  def __init__(self, nome, idade, email, regAdm):
    Pessoa.__init__(self, nome, idade, email)
    self.regAdm = regAdm

  def prepararAula(self):
    print(f'{self.nome} está preparando aula.')

  def falar(self):
    print(f'Professor(a) {self.nome} está falando.')

estudante = Estudante('Rayana', 21, 'rayanaprata@uol.com.br', 6005070)
estudante.falar()
estudante.verAula()

professor = Professor('Marcos', 40, 'marcos@gmail.com', 809845)
professor.falar()
professor.prepararAula()
