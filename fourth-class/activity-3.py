# 3) Utilizando dicionário do Python, implementar um programa para controlar uma lista de contatos de telefone: A cada nome da agenda deverá armazenar: Nome, Sobrenome, Telefone celular, Telefone comercial, E-mail. Deverá conter as funções de cadastro, busca por nome e relatório na tela.

contatos = {
  "Paulo": {
    "nome": "Paulo",
    "sobrenome": "Forgas",
    "tel-celular": 5367470712,
    "tel-comercial": 92260364,
    "email": "paulo@gmail.com"
  },
  "Maria": {
    "nome": "Maria",
    "sobrenome": "Souza",
    "tel-celular": 4472892260,
    "tel-comercial": 85987564,
    "email": "maria@gmail.com"
  },
  "Sara": {
    "nome": "Sara",
    "sobrenome": "Martins",
    "tel-celular": 2683735356,
    "tel-comercial": 87540964,
    "email": "sara@gmail.com"
  },
}

comando = "continue"

while comando != "sair": 
  comando = input("Digite o comando desejado -> cadastrar, listar, busca por nome, remover ou sair: ")

  if comando == "cadastrar":
    nome = input("Nome: ").strip()
    sobrenome = input("Sobrenome: ").strip()
    celular = input("Telefone Celular: ").strip()
    comercial = input("Telefone Comercial: ").strip()
    email = input("Email: ").strip()
    contatos[nome] = {
      "nome": nome,
      "sobrenome": sobrenome,
      "tel-celular": celular,
      "tel-comercial": comercial,
      "email": email
    }

  if comando == "listar":
    print(contatos)  

  if comando == "busca por nome":
    nome = input("Contato que deseja encontrar: ").strip()
    if nome in contatos:
      print(contatos[nome])

  if comando == "remover":
    nome = input("Nome: ")
    if nome in contatos:
      contato = contatos[nome]
      print(f'O contato de {nome} foi removido.')
      del contatos[nome]
    else:
      print("Contato não encontrado")  

  print()