# Exercício 8 - List Comprehension.

# Dadas duas listas: nomes = ["Ricardo", "Mariana", "Júlia"] e sobrenomes = ["Silva", "Oliveira", "Souza"], crie uma list comprehension que
# gere uma lista com o nome completo de cada pessoa (nome + " " + sobrenome).

#-----------------------------------------------------------------------------------------------------------------------------------#

# Dados iniciais.
nomes = ["Ricardo", "Mariana", "Júlia"]
sobrenomes = ["Silva", "Oliveira", "Souza"]

# Junta os valores de indicer iguais das duas listas utilizando o zip dentro do list comprehension.
nomeCompleto = [(nome + " " + sobrenome) for nome, sobrenome in zip(nomes, sobrenomes)]

print(nomeCompleto)