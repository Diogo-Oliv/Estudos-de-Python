# Exercício 1 - Dict Comprehension.

# Crie um dictionary comprehension que gere um dicionário com os números de 1 a 5 (inclusive) como chaves e seus cubos como valores.

#-----------------------------------------------------------------------------------------------------------------------------------#

cubos = {numero: numero**3 for numero in range(1, 6)}

print(cubos)