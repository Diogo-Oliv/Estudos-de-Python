# Exercício 3 - Teste com Temperaturas

# Escreva um programa que receba uma temperatura e tenha como limite de temperatura ideal abaixo ou igual a 25° C.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Variável que recebe a temperatura.
temp = float(input("Digite a temperatura Atual: "))

# Se a temperatura for <= a 25 graus, está tudo certo.
if temp <= 25 and temp >= 0:
  print("Temperatura dentro do limite.")

# Caso contrátrio
elif temp > 25:
  print("Alerta! Temperatura acima do limite permitido.")

else:
  print("Alerta! Temperatura abaixo do limite permitido.-23")