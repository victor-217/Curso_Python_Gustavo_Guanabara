"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.
"""

cidade = str(input('Em que cidade você mora? ')).lower()
separa = cidade.split()
print('A cidade começa com Santo? {}'.format('santo' in separa[0]))
