"""EX031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas."""

km = float(input('>>> Qual a distância a ser percorrida na viagem? (Km)'))

if km <= 200:
    valor1 = km * 0.50
    print(f'>> O valor da passagem a ser pago por {km}Km é de R${valor1:.2f} ')
    print('>> Boa viagem!')

elif km > 200:
    valor2 = km * 0.45
    print(f'>> O valor da passagem a ser pago por {km}Km é de R${valor2:.2f}')
    print('>> Boa viagem!')
