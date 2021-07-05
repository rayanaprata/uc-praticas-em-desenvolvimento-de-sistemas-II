# 1)Implementar um programa em Python que recebe um nome e a idade de um cliente e informe se tiver idade maior que 18 pode pegar empréstimo.

name = input("Type your name: ")
age = input("Type your age: ")

if int(age) > 18:
  print('You can get a loan.')
else:
  print('You cannot get a loan. You must be over 18 years of age for this.')

# 2)Mesmo exemplo, mas condição dentro de um limite de 20 até 40 

# Por exemplo:
# - muito_jovem < 20
# - muito_velho < 40
# - 20 =< idade >= 40 (inclusive)
# - Utilizar operador and

if int(age) < 20:
  print(f'{name} you are very youg')
elif int(age) > 40:
  print(f'{name} you are very old')
elif int(age) >= 20 and int(age) <= 40:
  print(f'{name} you can get a loan')
