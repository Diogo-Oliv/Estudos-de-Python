# Exercício 5 - Desenho com Laços.

# Escreva um programa que utilize de laços for para a imprimir um triângulo retângulo com o caractere desejado.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Escolha do caractere pelo usuário (podendo ser tanto um número quanto um símbolo).
caractere = input("Insira o caractere desejado para construir o triângulo: ")

# Laço para iterar as linhas.
for linha in range(1, 6):
    print(caractere * linha)

# Comando para inverter ou não o triângulo
permissao = input("Gostaria de ver o triângulo de ponta cabeça? [S/N]").upper()

# Condicional para realizar a inversão.
if permissao == "S":

    # Laço for realizando a iteração inversa.
    for linha in range(5, 0, -1):
        print(caractere * linha)

else:
    print("Fim do programa.")