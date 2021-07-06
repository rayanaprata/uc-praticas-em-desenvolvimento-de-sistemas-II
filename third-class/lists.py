# create a list with 15 elements

for v in range(15):
  print(v)

# creating a list with ranges
# range(start=0, stop, step=1)

l = list(range(100, 1100, 50))
print(l)

for t in range(3, 34, 3):
  print(t, end=" - ")
print()

while True:
  count = 0
  num = int(input("Informe o numero: "))
  mult = int(input("Informe o multiplo: "))

  for n in range(num):
    if n % mult == 0:
      count += 1
      print(n)
  print(f'Há {count} multiplos de {mult} em {num}')
  sair = input("Deseja continuar s-[sim] ou n[não]")
  if sair == 's':
    break

# Lists in Python is a type of variable that allows you to store multiple values

# A value from a list is accessed by an index

# A list can contain zero or more elements of the same type or different types, including other lists

# The size of a list is equal to the number of elements it contains