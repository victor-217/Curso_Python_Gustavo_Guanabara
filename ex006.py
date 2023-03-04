"""EX006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""

from math import sqrt

num = float(input('>>> Digite um número: '))

print(f'>> Analizando o número {num}...')
print(f'> Seu DOBRO é {num*2}')
print(f'> Seu TRIPLO é {num*3}')
print(f'> Sua RAIZ QUADRADA é {sqrt(num):.2f}')
