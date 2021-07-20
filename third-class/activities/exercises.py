# 1) Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.

def receiveUser(salutation, name):
  print(f'{salutation} {name}')

salutation = input("Type a greeting: ")
name = input("Type a name: ")

receiveUser(salutation, name)

# # 2) Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.

def sumOfThreeNumbers(a, b, c):
  print(a + b + c)

sumOfThreeNumbers(1, 2, 3)

# # 3) Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.

def percentual(x, y):
  return x + (x * (y/100))

print(percentual(100, 10))

# # 4) Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.

def fizzBuzz(num):
  if not num.isnumeric():
    return "Its not a number"
  elif (int(num) % 3) == 0:
    return "Fizz" 
  elif (int(num) % 5) == 0:
    return "Buzz" 
  elif (int(num) % 3) == 0 and (num % 5) == 0:
    return "FizzBuzz"
  else:
    return num

num = input("Type a number: ")
print(fizzBuzz(num))

# 5) Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.

def ofLegalAge(x):
  return (x >= 18)

def driversLicense(age):
    if ofLegalAge(age):
      return "can do this"
    else:
      return "can't do this'"

print(driversLicense(20))

# 6) Utilizando a função randint, gerar números aleatório entre 0 e 100.
# • Obs.: a função randin geram aleatoriamente um número inteiro dentro de um intervalo dado pelo usuário. Semelhantemente a função random(), o limite inferior do intervalo é incluído, mas o superior não. Podemos também inicializar um array numpy com valores aleatórios.

import random
x = random.randint(0, 100)
print(x)

# Dado um array=["maria", "pedro", "jose", "matheus", "joão", "rosa", "mario"], implementar uma rotina no Phtyon que realize uma busca pela palavra informada pelo usuário e no final leia o array.

people = ["maria", "pedro", "jose", "matheus", "joão", "rosa", "mario"]

def searchByName(word):
  if word in people:
    print(f'The name {word} was found in the list.')
  else:
    print('The name was not found in the list.')

searchByName(input("Type a name to find in the list of people: "))
print('array:', people)