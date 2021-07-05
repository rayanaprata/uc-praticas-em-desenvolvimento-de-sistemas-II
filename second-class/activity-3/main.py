# Implementar um programa em Python que recebe um nome e sobrenome e escreva a quantidade de caracteres total.

name = input("Type your name: ")
lastname = input("Enter your last name: ")

fullNameLen = len(name) + len(lastname)

print(f'The name has {fullNameLen} characters in total.')