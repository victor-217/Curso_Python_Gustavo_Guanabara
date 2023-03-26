"""EX029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

vel = int(input('>>> Qual a velocidade do carro? '))

if vel <= 80:
    print('\n>> Tenha uma boa viagem!')
else:
    multa = (vel - 80)*7

    print('\n>> Você ultrapassou o limite de velocidade de 80Km/h!')
    print(f'> Valor da multa a ser pago R${multa}')
