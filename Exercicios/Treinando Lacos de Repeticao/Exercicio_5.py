# Exercício 5 - Desenho com Laços.

# Escreva um programa que utilize de laços for para a imprimir um triângulo retângulo com o caractere desejado.

#-----------------------------------------------------------------------------------------------------------------------------------#

caractere = input("Insira o caractere desejado para construir o triângulo: ")

for linha in range(1, 6):
    print(caractere * linha)

permissao = input("Gostaria de ver o triângulo de ponta cabeça? [S/N]").uper()

if permissao == "S":

    for linha in range(5, 0, -1):
        print(caractere * linha)

else:
    print("Fim do programa.")