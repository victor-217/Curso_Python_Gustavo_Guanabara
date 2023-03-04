"""EX017: Desenvolva um programa que leia a comprimento do cateto oposto e do cateto adjacente de triangulo retagulo,
calcule e mostre o comprimento da hipotenusa."""

from math import hypot

co = float(input('>>> Comprimento do cateto oposto: '))
ca = float(input('>>> Comprimento do cateto adjacente: '))

hip = hypot(co, ca)

print(f'\n>> A hipotenusa vai medir {hip:.2f}')
