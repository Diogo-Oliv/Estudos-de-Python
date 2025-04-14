# Exercício 7 - Média de estudantes.

# Escreva um programa que calcule a média final dos alunos.
# Receba três notas e realize a média final delas.

#-----------------------------------------------------------------------------------------------------------------------------------#

# Notas dos alunos.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculo da média final
mediaFinal = (nota1 + nota2 + nota3) / 3

# Testes lógicos para o estado do aluno
if mediaFinal < 5:
  print("Média: {:.2f}".format(mediaFinal))
  print("Aluno Reprovado.")

elif (mediaFinal >= 5) and (mediaFinal < 7):
  print("Média: {:.2f}".format(mediaFinal))
  print("Aluno em Recuperação.")

elif (mediaFinal >= 7) and (mediaFinal <= 10):
  print("Média: {:.2f}".format(mediaFinal))
  print("Aluno Aprovado.")

else:
  print("Média: {:.2f}".format(mediaFinal))
  print("Nota inválida.")