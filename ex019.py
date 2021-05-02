from random import choice

a1 = input('Primeiro aluno: ').title()
a2 = input('Segundo aluno: ').title()
a3 = input('Terceiro aluno: ').title()
a4 = input('Quarto aluno: ').title()
lista = [a1, a2, a3, a4]
print('\nOs alunos participantes do sao {}'.format(lista))
print('O aluno escolhido foi {}'.format(choice(lista)))
