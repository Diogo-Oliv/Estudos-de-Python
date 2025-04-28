# Exercício 2 - List Comprehension.

# Escreva um programa que receba uma lista de nomes e crie uma list comprehension gerando uma nova lista com todos os nomes em maiúsculo.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Lista de nomes.
nomes = ["ana", "carlos", "maria", "joão"]

# List Comprehension transformando cada nome para letras maiúsculas.
nomesMaiusculos = [nome.upper() for nome in nomes]

print(nomesMaiusculos)