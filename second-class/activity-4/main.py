# 1) Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

intNum = input("Enter an integer: ")

def isnumber(value):
  try:
    float(value)
  except ValueError:
    return False
  return True

if not intNum.isnumeric():
  print(f'{intNum} is not an integer or is not a number')
elif isnumber(int(intNum)):
  if int(intNum) % 2 == 0:
    print(f'The number {intNum} is even')
  else:
    print(f'The number {intNum} is odd')

# 2) Faça um programa que solicita ao usuário o horário e baseado no horário responda bom dia 0-11, boa tarde 12-17 e boa note 18 – 23

import time
timeNow = int(time.strftime('%H', time.localtime()))

if timeNow >= 0 and timeNow <= 12:
  print('good morning')
elif timeNow >= 12 and timeNow <= 17:
  print('good afternoon')
elif timeNow >= 18 and timeNow <= 23:
  print('good night')

# 3) Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto". Se o nome tiver 5 e 6 letras escreva "Seu nome é normal". Se o nome tiver mais de 6 letras escreva "Seu nome é muito grande".

name = input("Type your name: ")
sizeName = len(name)

if sizeName <= 4:
  print('your name is short')
elif sizeName > 4 and sizeName < 7:
  print('your name is normal')
else:
  print('your name is too big')
