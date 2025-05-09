# Exercicio 5 - Dict Comprehension.

# Dada a lista de tuplas alunos = [("Ana", 8.5), ("Carlos", 7.0), ("Mariana", 9.2), ("João", 6.5)], crie um dictionary comprehension que gere um dicionário onde as chaves são os nomes dos alunos e os valores são "Aprovado" se a nota for maior ou igual a 7.0, e "Reprovado" caso contrário.

#-----------------------------------------------------------------------------------------------------------------------------------#

alunos = [("Ana", 8.5), ("Carlos", 7.0), ("Mariana", 9.2), ("João", 6.5)]

notas = {aluno[0]: "Aprovado" if aluno[1] >= 7 else "Reprovado" for aluno in alunos}

print(notas)