"""EX036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
então o empréstimo será negado."""

valor_casa = float(input('>>> Qual é o valor da casa? R$'))
salario_comprador = float(input('>>> Qual é o seu salário? R$'))
anos_pagamento = int(input('>>> Em quantos anos você pretende pagar? '))

prestacao_mensal = valor_casa / (anos_pagamento * 12)

if prestacao_mensal <= (salario_comprador * 0.3):
    print('>> Empréstimo aprovado!')
else:
    print('>> Empréstimo negado. A prestação mensal excede 30% do salário.')
