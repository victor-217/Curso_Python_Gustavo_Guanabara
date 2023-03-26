"""Ex028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se
o usuário venceu ou perdeu."""

from random import randint
from time import sleep

print('=--='*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinha-lo!'.center(80))
print('=--='*20)

num = int(input('>>> Sua escolha: '))
pc = randint(0, 5)

print('\033[35mPENSANDO...\033[m')
sleep(1)

if num == pc:
    print(f'\n>> VOCÊ GANHOU! Eu pensei no número {pc}!')
else:
    print(f'\n>> VOCÊ PERDEU! Eu pensei no número {pc}!')
