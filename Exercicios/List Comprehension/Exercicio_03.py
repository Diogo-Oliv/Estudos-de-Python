# Exercício 3 - List Comprehension.

# Escreva um programa que receba uma lista de temperaturas em Celsius, crie uma list comprehension que converta cada temperatura 
# para Fahrenheit. A fórmula para conversão é: (F = \frac{9}{5}C + 32).

#-----------------------------------------------------------------------------------------------------------------------------------#

# Temperaturas para realizar as converções.
temperaturas_celsius = [0, 10, 20, 30, 40]

# List Comprehension realizando a converção e iteração da lista das temperaturas em celcius.
temperaturas_Fahrenheit = [(celcius * (9 / 5) + 32) for celcius in temperaturas_celsius]

print(temperaturas_Fahrenheit)