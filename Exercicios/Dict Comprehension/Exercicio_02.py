# Exercício 2 - Dict Comprehension.

# Dada a lista de nomes nomes = ["ana", "carlos", "maria", "joão"], crie um dictionary comprehension que gere um dicionário onde as chaves são os nomes e os valores são o comprimento de cada nome.

#-----------------------------------------------------------------------------------------------------------------------------------#

nomes = ["ana", "carlos", "maria", "joão"]

dictNome = {nome: len(nome) for nome in nomes}

print(dictNome)