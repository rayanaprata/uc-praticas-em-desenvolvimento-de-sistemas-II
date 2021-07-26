
prova = open('respostas.txt','r')
gabarito = open('gabarito.txt', 'r')
respostasProva = prova.readlines()
respostasGabarito = gabarito.readlines()

with open("respostas.txt") as f:
    nomeAluno = next(f).rstrip() #rstrip() serve para remover o caracter de nova linha no final da linha pq o readline() retorna a linha com uma nova linha à direita.

prova.close()


def correcao(listaResposta, listaGabarito):
  qtdResCertas = 0

  for i in range (len(listaGabarito)):
    resposta = listaResposta[i+1].rsplit('\n')
    gabarito = listaGabarito[i].rsplit('\n')

    if(resposta == gabarito):
      #print(f'O aluno acertou a questão {i+1}')
      qtdResCertas += 1
    # else:
    #   print(f'O aluno errou a questão {i+1}')

  qtdPerguntas = len(listaGabarito)
  media = (10 / qtdPerguntas) * qtdResCertas

  if media >= 6:
    resultado = 'Aprovado'
  else:
    resultado = 'Reprovado'

  rel = open("Relatorio.txt", "w+")
  rel.write(f'O aluno {nomeAluno} acertou {qtdResCertas} perguntas de {qtdPerguntas}, sendo {resultado} com media {media}!')
  rel.close()


correcao(respostasProva, respostasGabarito)

