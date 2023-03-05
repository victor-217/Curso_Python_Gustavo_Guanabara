"""EX020: O mesmo professor do desafio anterior quer sortear a ordem de apresentacao dos trabalhos
dos alunos. Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""


from random import shuffle

aluno1 = str(input('>>> Primeiro aluno: ').title())
aluno2 = str(input('>>> Segundo aluno: ').title())
aluno3 = str(input('>>> Terceiro aluno: ').title())
aluno4 = str(input('>>> Quarto aluno: ').title())

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)

print('\n>> A ordem de apresentação será:')
print(alunos)
