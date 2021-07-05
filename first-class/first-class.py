
"""  Implementar um programa em Python que recebe os
dados de nome, idade, altura, peso e calcule o IMC.  """

name = input("Type your name: ")
age = input("Type your age: ")
height = float(input("Type your height: "))
weight = float(input("Type your weight: "))

imc = weight / (height*2)

print(name, "have", age, "years old and,", weight, "kilos and measures", height, "meters. Your IMC is", imc)

# print(f'{name} have {age} years old and {weight} kilos and measures {height} meters. Your IMC is {imc}.')

