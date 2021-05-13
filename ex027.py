"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""

nome = input('Digite seu nome completo: ').strip().title()
separa = nome.split()
print('\nSeu primeiro nome é {}'.format(separa[0]))
print('Seu último nome é {}'.format(separa[-1]))
