# Exercício 6 - Controle de Acesso

# Escreva um programa que realize o controle de acesso com base no horário de acesso.
# Usar a hora atual e comparar o horário válido para a entrada (08 até às 18)

#-----------------------------------------------------------------------------------------------------------------------------------#

# Recebe a hora atual.
horaAtual = float(input("Digite a hora atual (formato 24 horas): "))

# Definição do horário de início e de fim do funcionamento
horaInicio = 8
horaFim = 18

# Teste lógico para saber se o horário de entrada é válido
if horaAtual > horaInicio and horaAtual < horaFim:
    print("Acesso concedido.")

else:
    print("Acesso negado.")