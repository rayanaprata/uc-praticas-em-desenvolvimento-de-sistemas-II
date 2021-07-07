# 1)Escreve um programa em Python que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a posição de início

# – Primeira string: AABBEFAATT
# – Segunda string: BE
# – Resultado: BE encontrado na posição 3 de AABBEFAATT

firstStr = input("Type first string: ")
secondStr = input("Type second string: ")

if secondStr in firstStr:
  pos = firstStr.find(secondStr)
  print(f'Result: {secondStr} found at position {pos} of {firstStr}')