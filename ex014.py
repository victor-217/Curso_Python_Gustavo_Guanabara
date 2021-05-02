'''
CONVERSOR DE TEMPERATURA  : Escreva um programa que converta uma temperatura
digitada em °C e converta em °F.
'''

temp = float(input('Informe a temperatura em °C: '))
f = (temp * 9 / 5) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(temp, f))
