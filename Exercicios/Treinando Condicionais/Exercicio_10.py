# Exercício 10 - Aprovação de crédito.

# Escreva um programa para solicitar crédito, sua aprovação dependerá dos seguintes aspectos:

# O valor da renda mensal deve ser maior que R$ 3.500,00
# O valor da aprovação não pode ultrapassar 30% da renda.

#-----------------------------------------------------------------------------------------------------------------------------------#

#Coleta de dados
rendaMensal = float(input("Digite o valor da sua renda mensal: "))
parcela = float(input("Digite o valor do crédito desejado: "))

porcentagem = (parcela / rendaMensal) * 100

if (rendaMensal > 3500) and (parcela <= 30):
  print("Crédito aceito.")

elif rendaMensal <= 3500:
  print("Crédito negado: renda insuficiente.")

else:
  print(f"Crédito negado: Parcela acima de {porcentagem:.0f}% da renda.")