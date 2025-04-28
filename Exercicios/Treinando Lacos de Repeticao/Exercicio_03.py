# Exercício 3 - Validação de entrada.

# Escreva um programa que garanta um padrão de nomes de usuários e senhas válidos seguindo as seguintes regras:

# O nome de usuário deve ter, no mínimo 5 caracteres.
# A senha deve ter, no mínimo, 10 caracteres.

# Além disso, é necessário que o sistema continue pedindo informações até que todos os requisitos sejam atendidos. Quando o usuário
# inserir dados válidos, o programa deve exibir a mensagem "Cadastro realizado.".

#-----------------------------------------------------------------------------------------------------------------------------------#

# Status de validação inicialmente falso para  dar início ao loop While.
statusInicial = False

# Loop while para a repetição do processo até atender os requisitos.
while statusInicial == False:
  usuario = input("Digite seu nome de usuário: ")
  senha = input("Digite sua senha: ")

# Condicional caso tudo esteja de acordo.
  if (len(usuario) >= 5) and (len(senha) >= 10):
    print("Cadastro realizado com sucesso!")
    statusInicial = True

# Condicional para o nome de usuário.
  elif len(usuario) < 5:
    print("O nome de usuário deve ter pelo menos 5 caracteres")

# Condicional para a senha.
  elif len(senha) < 10:
    print("A senha deve ter pelo menos 10 caracteres")