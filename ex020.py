from random import shuffle

a1 = str(input('Primeiro aluno: ').title())
a2 = str(input('Segundo aluno: ').title())
a3 = str(input('Terceiro aluno: ').title())
a4 = str(input('Quarto aluno: ').title())
lista = [a1, a2, a3, a4]
shuffle(lista)
print('\nA ordem de apresentação será')
print(lista)
