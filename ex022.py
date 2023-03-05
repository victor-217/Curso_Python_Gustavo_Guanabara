"""EX022: Crie um programa que leia o nome completo de uma pessoa e mostre:
. O nome com todas letras maiúsculas
. O nome com todas minúsculas
. Quantas letras tem o nome completo (sem considerar os espaços).
. Quantas letras tem primeiro nome"""

nome = str(input('>>> Digite seu nome completo: '))

separar = nome.split()
join = ''.join(separar)

print(f'\n>> Seu nome em maiúsculas fica {nome.upper()}.')
print(f'>> Seu nome em minúsculas fica {nome.lower()}.')
print(f'>> Seu nome tem {len(join)} letras.')
print(f'>> Seu primeiro nome é {separar[0].title()} e tem {len(separar[0])} letras.')
