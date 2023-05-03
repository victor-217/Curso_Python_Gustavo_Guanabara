"""EX032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

print('=-='*20)
print('Verificando se um ano é BISSEXTO!'.center(60))
print('=-='*20)

ano = int(input('>>> Que ano você deseja verificar? '))

if ano % 400 == 0 or ano % 100 != 0:
    print(f'>> O ano de {ano} é BISSEXTO!')
else:
    print(f'>> O ano de {ano} não é BISSEXTO!')
