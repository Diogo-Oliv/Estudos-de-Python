# Exercício 4 - Teste de IMC.

# Escreva um programa que realize o calculo do IMC de uma pessoa, leve em consideração as seguintes métricas:

# IMC menor que 18.5 = abaixo do peso.
# IMC maior que 18.5 e menor que 25 = peso normal.
# IMC maior que 25 = acima do peso.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Peso e Altura do usuário.
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Operação inicial do IMC.
IMC = peso / (altura ** 2)

# Valor do IMC.
print(f"Seu IMC é {IMC:.1f}")

# Condicionais do IMC para Categorização do peso.
if IMC <= 18.5:
    print("Usuário abaixo do peso!")

elif IMC > 18.5 and IMC <= 25.0:
    print("Usuário de peso normal!")

else:
    print("Usuário muito acima do peso!")