# Exercício 1 - Entendendo Laços.

# Desenvolva um programa que processe uma lista de n nomes de clientes.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Lista de clientes.
clientes = []

# Número de clientes escolhido pelo usuário.
numClientes = int(input("Insira o número total de clientes: "))

# Laço de repetição que usa o numClientes como contador e adiciona os clientes para a lista.
for i in range(1, numClientes + 1):
  cliente = input(f"Insira o nome do {i}° cliente: ")
  clientes.append(cliente)

# Laço para mostrar todos os valores da lista de clientes.
for j in clientes:
  print(j)