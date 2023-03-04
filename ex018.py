"""EX018: Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e da
tangente desse angulo."""

from math import cos, sin, tan, radians

angulo = float(input('>>> Digite o ângulo desejado: '))

rad = radians(angulo)

print(f'\n>> O ângulo de {angulo} tem o SENO {sin(rad):.2f}')
print(f'>> O ângulo de {angulo} tem o COSSENO {cos(rad):.2f}')
print(f'>> O ângulo de {angulo} tem a TANGENTE {tan(rad):.2f}')
