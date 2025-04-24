# Exercício 9 - Decimal para Binário.

# Escreva um programa que peça um número ao usuário e realize a conversão para binário.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Lista que receberá os valores da divisão em binário.
listaBinario = []

# Variável para inserir o número inteiro.
numero = int(input("Digite um número inteiro: "))

# Laço de repetição até o número chegar a 0.
while numero > 0:
    
    # Variável receberá o resto da divisão por 2.
    binario = numero % 2

    # Adiciona o valor à uma lista
    listaBinario.append(binario)

    # Número sofrerá a DIVISÃO INTEIRA (descarta a parte decimal).
    numero = numero // 2

# Imprimi a lista ao inverso para mostrar o número em Binário corretamente.
print(listaBinario[::-1])