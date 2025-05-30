# Exercício 6 - Dict Comprehension.

# Dada a lista de palavras palavras = ["livro", "caneta", "borracha", "caderno", "lápis"], crie um dictionary comprehension que gere 
# um dicionário onde as chaves são as palavras e os valores são True se a palavra tiver mais de 5 letras, e False caso contrário.

#-----------------------------------------------------------------------------------------------------------------------------------#

palavras = ["livro", "caneta", "borracha", "caderno", "lápis"]

palavrasComCincoLetras = {palavra: True if len(palavra) > 5 else False for palavra in palavras}

print(palavrasComCincoLetras)