# Exercício 6 - List Comprehension.

# Crie uma list comprehension aninhada para gerar uma matriz 5x5 (uma lista de 5 listas, cada uma com 5 elementos) 
# onde o valor de cada elemento seja a soma dos seus índices (linha + coluna).

#-----------------------------------------------------------------------------------------------------------------------------------#

# Matriz que recebe dois list Comprehension de forma aninhada.
matriz = [[linha + coluna for coluna in range(5)] for linha in range(5)]

print(matriz)