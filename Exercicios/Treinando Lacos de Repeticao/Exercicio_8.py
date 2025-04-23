# Exercício 8 - Palíndromo.

# Escreva um programa que peça ao usuário uma palavra ou frase e imprima se a entrada é um palíndromo ou não.

# Palíndromo = palavra, frase ou sequência que permanece a mesma quando lida de trás para frente

#-----------------------------------------------------------------------------------------------------------------------------------#

# Palavra ou frase para o usuário inserir
texto = input("Digite uma palavra ou uma frase para a verificação de um palíndromo: ").lower()

# Lista de caracteres inicialmente vazia para uma futura comparação.
textoLista = []

# Laço for para iterar todos os caracteres da palavra ou frase.
for i in texto:
    # Adiciona cada caractere na lista.
    if i == ' ':
        continue
    else:
        textoLista.append(i)

# Comparação de listas normal e inversamente para ver se é um Palíndromo.
if textoLista == textoLista[::-1]:
    print('Essa palavra ou frase é um Palíndromo.')
else:
    print('Essa palavra ou frase não é um Palíndromo')