# 1) Fazer uma busca em uma string utilizando o método in. Tanto a string como a busca devem ser informados pelo usuário.

originalString = input("Enter a string: ")
searchString = input("Enter a value to search within the string: ")

if searchString in originalString:
  print(f'Exist {searchString} in {originalString}')
else:
  print(f'Does not exist {searchString} in {originalString}')

# 2) Implementar um login fake.
# - Utilizar o operador AND.
# - nome=root
# - senha=root123

name = input("Name: ")
password = input("Password: ")

if name in 'root' and password in 'root123':
  print('Successfully logged in')
else:
  print('Incorrect name or password')