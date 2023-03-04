"""EX011: Faça um programa que leia a largura e altura de uma parede em metros,
calcule sua área e a quantidade de tinta nescessária para pintá-la, sabendo
que cada litro de tinta pinta uma área de 2m²."""

print('\033[95m========= CALCULO DE MATERIAIS =========\033[m')

lar = float(input('>>> Qual a largura da parede? (m)'))
alt = float(input('>>> Qual a altura da parede? (m)'))

area = lar * alt

print(f'\n>> Para pintar uma área de {lar*alt}m² será nescessário {area/2}l de tinta. ')

