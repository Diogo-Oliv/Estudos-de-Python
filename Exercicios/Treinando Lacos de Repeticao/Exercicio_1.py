# Exercício 1 - Entendendo Laços.

# Desenvolva um programa que processe uma lista de n nomes de clientes.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Lista de clientes.
clientes = []

numClientes = int(input("Insira o número total de clientes: "))

for i in range(1, numClientes + 1):
  cliente = input(f"Insira o nome do {i}° cliente: ")
  clientes.append(cliente)

for j in clientes:
  print(j)