# Exercício 7 - Dict Comprehension.

# Dada a lista de números numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crie um dictionary comprehension que gere um dicionário onde as 
# chaves são os números e os valores são "par" para números pares e "ímpar" para números ímpares.

#-----------------------------------------------------------------------------------------------------------------------------------#

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numerosDict = {numero: "Par" if numero % 2 == 0 else "Ímpar" for numero in numeros}

print(numerosDict)