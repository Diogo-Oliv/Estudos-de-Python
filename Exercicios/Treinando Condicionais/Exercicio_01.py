# Exercício 1 - Monitorando vendas de um comércio.

# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles foi o mais vendido.
# No caso de quantidades iguais, imprima a mensagem de empate.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Produtos para análise: Maçã e Banana
#Identificar qual teve a maior venda

# Receber o número de vendas dos produtos

maca = int(input("Digite a quantidade de maçãs vendidas: "))
banana = int(input("Digite a quantidade de bananas vendidas: "))

# Condicional para saber qual tem o maior valor

if banana > maca:
  print("As bananas tiveram mais vendas")

elif maca > banana:
  print("As maçãs tiveram mais vendas")

else:
  print("Não foi possível realizar a operação!")