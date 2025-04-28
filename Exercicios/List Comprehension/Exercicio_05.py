# Exercício 5 - List Comprehension.

# Escreva um programa que receba uma lista de números e utilize list comprehension para retornar unicamente os números pares.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Lista de números.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Itera a lista com a condicional de números pares.
numerosPares = [numero for numero in numeros if numero % 2 == 0]

print(numerosPares)