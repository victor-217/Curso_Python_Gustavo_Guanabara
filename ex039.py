""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda
vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

import datetime

print('=-='*20)
print('\033[93mAlistamento ao serviço militar!\033[m'.center(65))
print('=-='*20)

ano = datetime.date.today().year

nascimento = int(input('>>> Qual o ano do seu nascimento? '))
idade = ano - nascimento

if idade < 18:
    anos = 18 - idade
    print(f'\n>> Ainda faltam {anos }ano(s) pra você se alistar ao serviço militar!')

elif idade == 18:
    print('\n>> Está na hora exata de você se alistar ao serviço militar!')

elif idade > 18:
    anos = idade - 18
    print(f'\n>> Já se passou {anos} ano(s) do seu alistamento ao serviço militar!')