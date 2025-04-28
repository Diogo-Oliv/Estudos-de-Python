# Exercício 9 - Número Par ou Ímpar.

# Escreva um programa que verifica se um número é par ou ímpar.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Coletando um número.
num = int(input("Digite um número inteiro: "))

# Teste de paridade com o uso do operdador módulo.
if num % 2 == 0:
    print(f"O número {num} é par.")

else:
    print(f"O número {num} é ímpar.")