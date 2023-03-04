"""EX014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus
Fahrenheit. """

print("\033[95mCONVERSOR DE TEMPERATURA\033[m")

celsius = float(input("\n>>> Digite um temperatura em ºC: "))

fahrenheit = celsius*1.8+32

print(f"\n>> A temperatura de {celsius}ºC equivale a {fahrenheit:.1f}ºF")
