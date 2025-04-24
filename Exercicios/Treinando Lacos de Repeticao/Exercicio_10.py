# Exercício 10 - Ordenação de valores.

# Escreva um programa que receba uma lista de números e ordene os valores em ordem crescente.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Lista de valores desordenadas.
numeros = [1, 5, 9, 3, 4, 2, 5, 1, 10, 4, 3]

# Variável que receberá o tamanho da lista.
num = len(numeros)

# Laço que itera todos os elementos da lista.
for i in range(num - 1):

    # Laço que compara os elementos adjacentes e realiza as trocas de posição.
    for j in range(num - 1 - i):

        # Compara dois elementos adjacentes na lista.
        if numeros[j] > numeros[j + 1]:

            # Realiza a troca dos valores conforme a condicional anterior.
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print(numeros)