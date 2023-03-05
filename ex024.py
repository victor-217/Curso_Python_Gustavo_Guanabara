"""EX024: Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome 'SANTO'."""

nome = str(input('>>> Digite o nome de uma cidade: '))

separar = nome.upper().split()

print(f'\n>> A cidade de {nome.title()} começa com "Santo"? {"SANTO" in separar[0]}')
