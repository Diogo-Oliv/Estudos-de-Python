# Exercício 9 - List Comprehension.

# Dada a lista de listas dados = [[1, 2], [3, 4, 5], [6]], crie uma list comprehension que "achate" 
# essa lista em uma única lista contendo todos os números.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Dados iniciais.
dados = [[1, 2], [3, 4, 5], [6]]

dadosUnicos = [dado for subdados in dados for dado in subdados]

print(dadosUnicos)