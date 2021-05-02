from math import cos, sin, tan, radians

ang = float(input('Digite o ângulo desejado: '))
rad = radians(ang)
print('\nO ângulo de {} tem o SENO {:.2f}'.format(ang, sin(rad)))
print('O ângulo de {} tem o COSSENO {:.2f}'.format(ang, cos(rad)))
print('O ângulo de {} tem a TANGENTE {:.2f}'.format(ang, tan(rad)))
