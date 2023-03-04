"""EX019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
que ajude ele, lendo os nomes deles e escrevendo o nome do escolhido."""

from random import choice

aluno1 = input('>>> Primeiro aluno: ').title()
aluno2 = input('>>> Segundo aluno: ').title()
aluno3 = input('>>> Terceiro aluno: ').title()
aluno4 = input('>>> Quarto aluno: ').title()

alunos = [aluno1, aluno2, aluno3, aluno4]

print(f'\n>> Os alunos participantes do são {alunos}')
print(f'> O aluno escolhido foi {choice(alunos)}')
