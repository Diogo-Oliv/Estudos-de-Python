# Exercício 7 - List Comprehension.

# Dada a lista de números numeros = [-2, -1, 0, 1, 2], crie uma list comprehension que gere uma nova lista onde 
# os números negativos sejam substituídos por 0, e os números não negativos permaneçam os mesmos.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Lista de números.
numeros = [-2, -1, 0, 1, 2]

# Transforma os números menores que 0 em 0 ustilizando list comprehension.
numerosPositivos = [0 if numero < 0 else numero for numero in numeros]

print(numerosPositivos)