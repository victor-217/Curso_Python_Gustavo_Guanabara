"""EX025: Crie um programa que leia o nome de uma pessoa e diga se
ela tem 'SILVA' no nome."""

nome = str(input('>>> Digite seu nome completo: ')).lower()
print(f'>> Seu nome tem "SILVA"? {"silva" in nome}')
