#-----------------------------------------------------------------------------------------------------------------------------------#
# Criando arquivos para estudos de exercícios. PROTÓTIPO
#-----------------------------------------------------------------------------------------------------------------------------------#
# Apresentação do programa.
print("----------------------------------------------------------------------")
print("-----------BEM VINDO AO CRIADOR DE ARQUIVOS PERSONALIZADOS------------")
print("----------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------------------#

# Função para o método de Criação de arquivos.
def CriandoArquivos():

    # Try para realizar o tratamento de exceções.
    try:

        # Tratamento de erro durante a requisição do tipo de arquivo.
        tipoArquivo = False

        # Laço while para manter o loop ativo até que esteja tudo certo.
        while tipoArquivo == False:

            # Variável que receberá o tipo do arquivo.
            extencaoArquivo = input("""Qual o tipo de arquivo que você gostaria de criar? 
Exemplos:   || .txt || .py || .md || .html || .css || \n \n""").lower()
    
            # Caso o usuário esqueça de inserir o . antes do início do tipo do arquivo.
            if "." not in extencaoArquivo:
       
                # Realizará a notificação do erro e apresentará novamente.
                print("O tipo do arquivo não apresentou o . antes do tipo.")
                extencaoArquivo = "." + extencaoArquivo
            
            tipoArquivo = True

        # Tratamento de erro durante a requisição do path escolhido.
        caminhoArquivo = input("Insira o path onde se localizará o novo arquivo criado: \n \n")
    
        # Laço for para controlar a quantidade de arquivos criados.
        for i in range(3,5):

            # Usar o open com o mode x para criar o arquivo e escrever o número do exercício tanto no diretório quanto dentro dele utilizando o write.
            with open(file=f"{caminhoArquivo}\Exercicio_{str(i)}{extencaoArquivo}", mode="x") as arquivo:
        
                arquivo.write("# Exercicio " + str(i) + " - Dictionary Comprehension. \n \n")

                descricaoPersonalizada = input("Gostaria de adicionar alguma descrição para o arquivo? [S/N]\n \n").upper()
                
                while descricaoPersonalizada != "N":
                    
                    descricaoArquivo = input("Insira a descrição aqui: ")

                    arquivo.write("# "+ descricaoArquivo + "\n \n")

                    descricaoPersonalizada = input("Deseja continuar?")
                
                arquivo.write("#-----------------------------------------------------------------------------------------------------------------------------------#")

        print("\n Arquivo(s) criados com sucesso.")
    
    # Tratamento de exceção para caso o arquivo já esteja criado no repositório específico.
    except FileExistsError:
        
        print("Este arquivo já esxiste tente realizar outra ação.")

# Método para criar o arquivo.
CriandoArquivos()