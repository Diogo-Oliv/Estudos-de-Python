# Exercício 9 - Dict Comprehension.

# Dada a lista de strings itens = ["produto1=10", "produto2=25", "produto3=5"], crie um dictionary comprehension que processe cada 
# string, separando o nome do produto do seu preço, e gere um dicionário onde os nomes dos produtos são as chaves (em minúsculo) 
# e os preços são os valores (como inteiros).

#-----------------------------------------------------------------------------------------------------------------------------------#

itens = ["produto1=10", "produto2=25", "produto3=5"]

produtos = {item.split("=")[0].lower(): int(item.split("=")[1]) for item in itens}

print(produtos)