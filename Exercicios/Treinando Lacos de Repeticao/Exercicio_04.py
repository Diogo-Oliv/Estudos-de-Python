# Exercício 4 - Tabuada.

# Escreva um programa que imprima a tabuada de um número pedido pelo usuário até um limite também imposto por ele.

#-----------------------------------------------------------------------------------------------------------------------------------#


# Estado inicial do programa.
finalizado = False

# Loop While para realizar quantas tabuadas o usuário quiser.
while finalizado == False:

    # Variáveis para a tabuada.
    numTabuada = float(input("Digite o número para realizarmos sua tabuada (inteiro ou decimal): "))
    limiteTabuada = int(input("Digite até que número a tabuada será feita (recomendado = 10): "))

    # Loop for para a iteração da tabuada.
    for i in range(0, limiteTabuada + 1):
        print(f"{numTabuada} * {i} = {numTabuada * i}")
    
    # Confirmação do usuário para continuar ou não.
    confirmacao = input("Deseja fazer a tabuada de mais algum número? [S/N]: ")

    # Laço de repetição para caso de confirmação.
    if confirmacao == "S":
        print("Realizando nova tabuada...")
    
    # Finalização do loop.
    else:
        print("Encerrando o programa.")
        finalizado == True
        break