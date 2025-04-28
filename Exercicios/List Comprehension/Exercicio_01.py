# Exercício 1 - List Comprehension.

# Escreva um programa que use List Comprehension e insira em uma lista uma sequência de 0 a 10.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Variável do número inicial igual a 0.
numero = 0

# List Comprehension iterando o número até 10.
numeros = [numero for numero in range(0, 11)]

# Imprime a lista completa de 0 a 10.
print(numeros)