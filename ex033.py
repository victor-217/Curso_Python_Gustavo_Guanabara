"""EX033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

n1 = int(input('>>> Digite o primeiro valor: '))
n2 = int(input('>>> Digite o segundo valor: '))
n3 = int(input('>>> Digite o terceiro valor: '))

valores = [n1, n2, n3]

if n1 == n2 and n1 == n3:
    print('\n>> Os valores são todos iguais.')
else:
    print(f'\n>> O maior valor é {max(valores)}')
    print(f'\n>> O menor valor é {min(valores)}')
