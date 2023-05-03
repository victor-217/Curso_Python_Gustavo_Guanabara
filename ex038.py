"""Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

num1 = int(input('>>> Digite um número: '))
num2 = int(input('>>> Digite outro número: '))

if num1 > num2:
    print('\n>> O primeiro valor é o maior!')
elif num2 > num1:
    print('\n>> O segundo valor é o maior!')
else:
    print('\n>> Não existe valor maior, os dois são iguais!')
