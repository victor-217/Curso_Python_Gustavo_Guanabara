'''
DISSECANDO UMA VARIÁVEL: Faça um programa que leia algo pelo  teclado e mostre na tela seu tipo
primitivo e todas as informações possíveis sobre ele.
'''

algo = input('Digite algo: ')
print('\nTipo primitivo {}'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É Alfabético? {}'.format(algo.isalpha()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('É um número? {}'.format(algo.isnumeric()))
print('Está em maiúsculo? {}'.format(algo.isupper()))
print('Está em minúsculo? {}'.format(algo.islower()))
print('Está capitalizada? {}'.format(algo.istitle()))
