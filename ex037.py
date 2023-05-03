"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual
será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

num = int(input('>>> Escreva um número: '))
print('-'*30)
escolha = int(input('Bases de conversão'
                    '\n[ 1 ] BINÁRIO'
                    '\n[ 2 ] OCTAL'
                    '\n[ 3 ] HEXADECIMAL '
                    '\n>>> Sua escolha: '))

if escolha == 1:
    print(f'\n>> O número {num} convertido em BINÁRIOS é {bin(num)}')
elif escolha == 2:
    print(f'\n>> O número {num} convertido em OCTAL é {oct(num)}')
elif escolha == 3:
    print(f'\n>> O número {num} convertido em HEXADECIMAL é {hex(num)}')
