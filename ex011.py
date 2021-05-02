print('='*5, 'Pintando a parede', '='*5)
lar = float(input('Qual a largura da parede? (mt)'))
alt = float(input('Qual a altura da parede? (mt)'))
area = lar * alt
tinta = area / 2
print('Com uma área de {}mts será necessário de {}lts de tinta para pinta-lá. '.format(area, tinta))
