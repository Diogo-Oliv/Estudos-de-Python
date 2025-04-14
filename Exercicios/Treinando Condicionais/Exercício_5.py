# Exercício 5 - Controle de orçamento.

# Escreva um programa que receba o total de despesas e informe se ultrapassou um limite especificado pelo usuário.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Variável para limitar o orçamento máximo.
orcMax = float(input("Digite o orçamento limite (R$): "))

# Variável de orçamento.
orc = float(input("Digite o total de despesas do mês (R$): "))

# Teste lógico para saber se o limite foi ultrapassado ou não.
if orc < orcMax and orc > 0:
    print("Valor dentro do limite estipulado.")

elif orc == orcMax:
    print("Valor igual ao limite do orçamento.")

elif orc > orcMax:
    print("Valor acima do limite estipulado.")

else:
    print("Valor inválido")