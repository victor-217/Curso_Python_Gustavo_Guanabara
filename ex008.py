'''
CONVERSOR DE MEDIDAS : Escreva um programa que leia um valor em metros e o exiba
convertidos em centrimetros e milímetros.
'''

mt = float(input('Uma distância em metros:  '))
km = mt / 1000
hm = mt / 100
dam = mt / 10
dm = mt * 10
cm = mt * 100
mm = mt * 1000
print('A medida de {}m corresponde a'.format(mt))
print('{}Km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
