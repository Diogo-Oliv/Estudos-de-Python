# Exercício 8 - Dict Comprehension.

#Dadas duas listas: chaves = ["a", "b", "c"] e valores = [10, 20, 30], crie um dictionary comprehension que combine essas 
# listas em um dicionário onde os elementos de chaves são as chaves e os elementos de valores são os valores correspondentes.

#-----------------------------------------------------------------------------------------------------------------------------------#

chaves = ["a", "b", "c"]
valores = [10, 20, 30]

dicionario = {chave:valor for chave, valor in zip(chaves, valores)}

print(dicionario)