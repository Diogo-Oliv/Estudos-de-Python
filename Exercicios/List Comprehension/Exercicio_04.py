# Exercício 4 - List Comprehension.

# Escreva um programa que receba uma lista de nomes e use List Comprehension para retornar o comprimento de cada item da lista em uma nova lista.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Lista de palavras.
palavras = ["python", "é", "uma", "linguagem", "poderosa"]

# Pega o tamanho de cada item iterado na lista de pelavras.
comprimentoPalavras = [len(palavra) for palavra in palavras]

print(comprimentoPalavras)