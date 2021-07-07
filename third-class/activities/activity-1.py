# Implementar um programa em Python que recebe pelo teclado 5 notas e calcula a média.

# Utilizar uma variável do tipo lista para armazenar as notas. Ao final deve imprimir a média das notas.

notas = []
total = 0

for i in range(5):
  val = int(input("Informe a nota: "))
  notas.append(val)
  total = val + total

total = total / 5
print(f'Notas: {notas}')
print(f'Média: {total}')