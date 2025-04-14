# Exercício 8 - Cálculo de Pedágio.

# Escreva um programa para realizar o cálculo de pedágio dependendo da distância percorrida e da distância percorrida.

# Até 150 km: R$ 15,00
# Entre 150 km e 300 km: R$ 25,00
# Acima de 300 km: R$ 30,00

#-----------------------------------------------------------------------------------------------------------------------------------#

# Coleta o valor da distância percorrida
dist = float(input("Digite a distância percorrida (em km): "))

# Teste lógico para realizar a cobrança do pedágio
if dist < 150:
  print("Valor do pedágio: R$ 15,00")

elif dist >= 150 and dist <= 300:
  print("Valor do pedágio: R$ 25,00")

elif dist > 300:
  print("Valor do pedágio: R$ 30,00")