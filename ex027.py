"""EX027: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente."""

nome = str(input('>>> Digite seu nome completo: ').strip())

separar = nome.split()

print(f'\n>> Seu primeiro nome é {separar[0].title()}')
print(f'>> Seu último nome é {separar[-1].title()}')
