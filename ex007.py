"""EX007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média."""

nota1 = float(input('>>> Primeira nota do aluno: '))
nota2 = float(input('>>> Segunda nota do aluno: '))

media = (nota1+nota2)/2

print(f'\n>> Com notas {nota1} e {nota2} a média do aluno é de {media:.2}')

