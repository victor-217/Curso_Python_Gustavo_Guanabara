"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
. O nome com todas letras maiúsculas
. O nome com todas minúsculas
. Quantas letras tem o nome completo (sem considerar os espaços).
. Quantas letras tem primeiro nome
"""
nome = input('Digite seu nome completo: ').strip().title()
separa = nome.split()
print('\nSeu nome em maiúsculas fica {}'.format(nome.upper()))
print('Seu nome em minúsculas fica {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(''.join(separa))))
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
