"""EX008: Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros."""

mt = float(input('Uma distância em metros:  '))

km = mt / 1000
hm = mt / 100
dam = mt / 10
dm = mt * 10
cm = mt * 100
mm = mt * 1000

print(f'A medida de {mt}m corresponde a')
print(f'{km}Km')
print(f'{hm}hm')
print(f'{dm}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')
