# 1)Escreva um programa em Python que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.

# Primeira string: AAACTBF
# Segunda string: CBT
# Resultado: CBT

# A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras comuns a ambas

firstStr = input("Type first string: ")
secondStr = input("Type second string: ")
resultStr = []

i = 0
count = 0
while i < len(firstStr):
  letter = firstStr[i]
  j=i
  while j < len(secondStr):
    if firstStr[j] == letter:
      resultStr.insert(count, secondStr[j])
      count += 1
    j += 1
  i += 1

print(resultStr)