"""EX015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. calcule o valor a pagar sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

dias = int(input(">>> Por quantos dias o carro foi alugado? "))
km = float(input(">>> Quantos Km foram percorridos? (Km)"))

valor_final = (dias*60) + km*0.15

print(f"\n>> Com {dias} alugado(s) e {km}Km percorrido(s), o valor a ser pago é de R${valor_final:.2f}")
