'''
SORTEANDO ITEM NA LISTA: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''

from random import choice

a1 = input('Primeiro aluno: ').title()
a2 = input('Segundo aluno: ').title()
a3 = input('Terceiro aluno: ').title()
a4 = input('Quarto aluno: ').title()
lista = [a1, a2, a3, a4]
print('\nOs alunos participantes do sao {}'.format(lista))
print('O aluno escolhido foi {}'.format(choice(lista)))
