# Exercício 7 - Contagem de vogais e consoantes.

# Escreva um programa que imprima a quantidade de vogais e consoantes em uma string.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Variáveis para vogal e consoantes inicialmente iguais a 0.
numVogal = 0
numConsoante = 0

# Frase digitada pelo usuário.
frase = input("Digite uma frase para realizarmos a contagem de vogais e consoantes: ").lower()

# Laço for para a iteração de cada caractere da frase.
for i in frase:
    
    # Laço if imenso devido à ausência do uso de libs, levando em conta as vogais e suas variações.
    if (i == 'a') or (i == 'á') or (i == 'à') or (i == 'ã') or (i == 'e') or (i == 'é') or (i == 'ê') or (i == 'i') or (i == 'í') or (i == 'o') or (i == 'ó') or (i == 'õ') or (i == 'u'):

        # Aumento no número de vogais.
        numVogal += 1
    
    # Conficional para ignorar o caso de aparecimento de espaço.
    elif i == ' ':
        continue

    # O mesmo para pontuação.
    elif (i == ',') or  (i == '.') or (i == '!') or (i == '?'):
        continue
    
    # Consoante por eliminação.
    else:
        numConsoante += 1

# Print final com a resposta das contagens.
print(f"Na frase digitada tivemos o total de {numVogal} Vogais e {numConsoante} consoantes.")