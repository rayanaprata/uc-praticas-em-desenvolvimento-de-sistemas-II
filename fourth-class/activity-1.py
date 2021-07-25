# 1) Utilizando dicionário, implementar uma lista de contatos de telefone com python. Deve ter as funcionalidades de cadastrar, listar, remover e sair

contatos = {
  "Paulo": {
    "nome": "Paulo",
    "telefone": 5367470712,
  },
  "Maria": {
    "nome": "Maria",
    "telefone": 4472892260,
  },
  "Sara": {
    "nome": "Sara",
    "telefone": 2683735356,
  },

  "Jose": {
    "nome": "Jose",
    "telefone": 894578452,
  },
  "Jaime": {
    "nome": "Jaime",
    "telefone": 3578313808,
  },
  "Juca": {
    "nome": "Juca",
    "telefone": 1789156904,
  },
  "Mari": {
    "nome": "Juca",
    "telefone": 5367470712,
  },
  "Mateus": {
    "nome": "Juca",
    "telefone": 7156627616,
  },
  "Valeria": {
    "nome": "Juca",
    "telefone": 4472892260,
  },
}

comando = "continue"

while comando != "sair": 
  comando = input("Digite o comando desejado -> cadastrar, listar, remover ou sair: ")

  if comando == "cadastrar":
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    contatos[nome] = {
      "nome": nome,
      "telefone": telefone,
    }

  if comando == "listar":
    print(contatos)  

  if comando == "remover":
    nome = input("Nome: ")
    if nome in contatos:
      contato = contatos[nome]
      print(f'O contato de {nome} foi removido.')
      del contatos[nome]
      # incluir aqui o a função de remover do dicionario
    else:
      print("Contato não encontrado")  

  print()
