from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('\nA hipotenusa vai medir {:.2f}'.format(hip))
