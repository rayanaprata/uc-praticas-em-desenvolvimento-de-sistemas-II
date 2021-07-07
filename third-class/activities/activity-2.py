# Dada a lista L_total=[9,5,6,4,8,12,11,15,0,1,3,2], selecione os elementos impares e pares, guardando-os em sua respectiva lista, L_impar e L_par. Após imprima as três listas.

l_total = [9,5,6,4,8,12,11,15,0,1,3,2]
l_impar = []
l_par = []

for i in range(len(l_total)):
  if l_total[i] % 2 == 0:
    l_par.append(l_total[i])
  else:
    l_impar.append(l_total[i])

print(f'Total: {l_total}')
print(f'Par: {l_par}')
print(f'Ímpar: {l_impar}')
