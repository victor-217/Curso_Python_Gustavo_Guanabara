""" A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""

import datetime

ano = datetime.date.today().year

print('=-='*20)
print('Verifique sua categoria!'.center(60))
print('=-='*20)

nascimento = int(input('>>> Qual o seu ano de nascimento? '))
idade = ano - nascimento

if idade <= 9:
    print(f'\n>> Com a idade de {idade} sua categoria é a MIRIM!')
elif idade <= 14:
    print(f'\n>> Com a idade de {idade} sua categoria é INFANTIL!')
elif idade <= 19:
    print(f'\n>> Com a idade de {idade} sua categoria é JÚNIOR!')
elif idade <= 25:
    print(f'\n>> Com a idade de {idade} sua categoria é SÊNIOR!')
elif idade > 25:
    print(f'\n>> Com a idade de {idade} sua categoria é MASTER!')
