"""EX004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possíveis sobre ele."""

algo = input('>>> Digite algo: ')

print(f'\n>> O seu tipo primitivo é {type(algo)}')
print(f'>> Só tem espaços? {algo.isspace()}')
print(f'>> É alfanúmerico? {algo.isalnum()}')
print(f'>> É alfabético? {algo.isalpha()}')
print(f'>> É um número? {algo.isnumeric()}')
print(f'>> Está em maiúsculas? {algo.isupper()}')
print(f'>> Está em minúsculas? {algo.islower()}')
print(f'>> Está capitalizada? {algo.istitle()}')
