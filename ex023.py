"""EX023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
ex:Digite um número:1111
unidade: 1, dezena: 1, centena: 1, milhar:1 """

num = input('>>> Digite um número: ').zfill(4)

print('>> Analizando...')
print(f'\n> Unidade: {num[3]}')
print(f'> Dezena: {num[2]}')
print(f'> Centena: {num[1]}')
print(f'> Milhar: {num[0]}')
