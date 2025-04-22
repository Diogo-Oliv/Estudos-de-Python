# Exercício 6 - Sequência de Fibonacci.

# Escreva um programa que realize a sequência de Fibonacci do início até um limite estipulado pelo usuário.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Variáveis iniciais.
num1 = 0
num2 = 1

# limite estipulado pelo usuário.
limite = int(input("Digite um número para o limite da sequência de Fibonacci: "))

# Valor inicial da contagem de Fibonacci = 0.
print(num1)

# Laço for para a iteração da sequência.
for i in range (2, limite + 1):
    # Soma dos dois primeiros números.
    somador = num1 + num2

    # Vai printar na tela o valor do somador sempre que houver um número novo.
    print(somador, " ")

    # O valor inicialmente de 0 se torna 1
    num1 = num2

    # O valor de 1 se torna a soma de seus valores anteriores.
    num2 = somador