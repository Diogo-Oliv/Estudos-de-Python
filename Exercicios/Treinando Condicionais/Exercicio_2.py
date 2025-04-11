# Exercício 2 - Calculo de tempo de projeto.

# É necessário criar um programa que calcule o tempo necessário para concluir 4 atividades.
# Escreva um programa que receba o número de atividades e calcule o tempo total.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Calcular o tempo total necessário para concluir as atividades
# Caso alguma tenha valor negativo, retornar erro.

# Variáveis para cada atividade.
A = int(input("Informe os dias para a atividade A: "))
B = int(input("Informe os dias para a atividade B: "))
C = int(input("Informe os dias para a atividade C: "))
D = int(input("Informe os dias para a atividade D: "))

# Teste lógico para cada atividade de valor menor que 0.
if (A < 0) or (B < 0) or (C < 0) or (D < 0):
  print("ERRO: Os dias não podem ser negativos.")

else:
  print(f'''
        Dias para realizar a Atividade A: {A}
        Dias para realizar a Atividade A: {B}
        Dias para realizar a Atividade A: {C}
        Dias para realizar a Atividade A: {D}
        ''')