"""EX035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo."""

reta1 = float(input('>>> Comprimento da primeira reta: '))
reta2 = float(input('>>> Comprimento da segunda reta: '))
reta3 = float(input('>>> Comprimento da terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print(">> Os comprimentos informados formam um triângulo.")
else:
    print(">> Os comprimentos informados não formam um triângulo.")
