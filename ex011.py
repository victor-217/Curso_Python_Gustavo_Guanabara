'''
PINTANDO PAREDE: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta nescessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
'''

lar = float(input('Qual a largura da parede? (mt)'))
alt = float(input('Qual a altura da parede? (mt)'))
area = lar * alt
tinta = area / 2
print('Com uma área de {}mts será necessário de {}lts de tinta para pinta-lá. '.format(area, tinta))
