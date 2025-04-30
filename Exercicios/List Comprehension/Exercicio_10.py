# Exercício 10 - List Comprehension.

# Dada uma lista de frases: frases = ["sol e lua", "mar azul", "céu estrelado", "terra plana", "vento forte"]
# Crie uma list comprehension aninhada que faça o seguinte: 
# 1. Para cada frase na lista, divida-a em palavras.
# 2. Filtre as palavras que têm mais de 3 letras.
# 3. Para as palavras restantes, pegue apenas a primeira letra.
# Final: O resultado final deve ser uma lista de listas (uma "matriz" de iniciais), onde cada sublista corresponde a uma frase original.

#Dica: Você precisará de uma list comprehension externa para iterar pelas frases e uma list comprehension interna 
# para processar as palavras de cada frase, aplicando o filtro e a transformação.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Lista de frases.
frases = ["sol e lua", "mar azul", "céu estrelado", "terra plana", "vento forte"]

# Passo 1. Dividir as frases em palavras.
listaDePalavras = [[palavra for palavra in frase.split()] for frase in frases]

print("Passo 1. Dividir em palavras: ")
print(listaDePalavras)
print("Fim do primeiro passo.")

# Passo 2. Filtrar as palavras com mais de 3 letras.
listaDePalavras = [[palavra for palavra in frase.split() if len(palavra) > 3] for frase in frases]

print("Passo 2. Filtrar palavras com mais de 3 letras: ")
print(listaDePalavras)
print("Fim do segundo passo.")

# Passo 3. Pegando a Primeira Letra das Palavras Filtradas.
listaDePalavras = [[palavra[0] for palavra in frase.split() if len(palavra) > 3] for frase in frases]

print("Passo 3. mostrar apenas a primeira letra dessas palavras: ")
print(listaDePalavras)
print("Fim do terceiro passo.")