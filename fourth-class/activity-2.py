# 2) Utilizando dicionários com lista, controlar o estoque de veículos, da lista criada anteriormente, onde as chaves são os modelo (nome) e os valores (quantidade, ano e preço). 
# Apresentar um flag para sair e para movimentação de vendas, atualizar o estoque e gerar o relatório.

veiculos = {
  'gol': {
    'quantidade': 15,
    'ano': 2019,
    'preco': 28.900
  },
  'onix': {
    'quantidade': 5,
    'ano': 2019,
    'preco': 27.800
  },
  'sandeiro': {
    'quantidade': 7,
    'ano': 2016,
    'preco': 15.700
  },
  'hb20': {
    'quantidade': 12,
    'ano': 2020,
    'preco': 38.500
  },
  'siena': {
    'quantidade': 9,
    'ano': 2016,
    'preco': 18.200
  },
  'prisma': {
    'quantidade': 6,
    'ano': 2015,
    'preco': 14.300
  },
  'voyage': {
    'quantidade': 4,
    'ano': 2020,
    'preco': 48.100
  },
  'uno': {
    'quantidade': 2,
    'ano': 2019,
    'preco': 28.400
  },
}

comando = "continue"

while comando != "sair": 
  comando = input("Digite o comando desejado -> atualizar estoque, relatorio ou sair: ")

  if comando == "atualizar estoque":
    opcAtualEstoque = input("Informe qual operação deseja fazer -> incluir, alterar ou remover: ")

    if opcAtualEstoque == "incluir" or opcAtualEstoque == "alterar":
      veiculo = input("Marca do veículo: ").strip()
      qtd = input("Quantidade: ").strip()
      ano = input("Ano: ").strip()
      preco = input("Preço: ").strip()
      veiculos[veiculo] = {
        'quantidade': qtd,
        'ano': ano,
        'preco': preco
      }

    if opcAtualEstoque == "remover":
      carro = input("Veículo: ")
      if carro in veiculos:
        del veiculos[carro]
        print(f'O veículo {carro} foi removido.')
      else:
        print("Veículo não encontrado.")  

  if comando == "relatorio":
    print(veiculos)

  print()