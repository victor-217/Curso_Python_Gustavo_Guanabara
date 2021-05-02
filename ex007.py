'''
MÉDIA ARITMÉTICA: Desenvolva  um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.
'''

nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Segundo nota do aluno: '))
media = (nota1 + nota2) / 2
print('\nA média entre {} e {} é igual a {:.1f}'.format(nota1, nota2, media))
