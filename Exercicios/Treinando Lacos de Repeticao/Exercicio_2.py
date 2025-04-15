# Exercício 2 - Laço While.

# Escreva um programa que utiliza um laço While para contar até um certo número escolhido previamente.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Variáveis com os valores iniciais e finais
numFinal = int(input("Insira o número máximo da contagem: "))
numInicial = 0

# Laço While para iterar o valor de numInicial até ele se tornar maior que o numFinal + 1 para termos o valor exato.
while numInicial < numFinal + 1:
    print(f"num: {numInicial}")
    numInicial += 1