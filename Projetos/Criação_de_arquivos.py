#-----------------------------------------------------------------------------------------------------------------------------------#
# Criando arquivos para estudos de exercícios. PROTOTIPO
#-----------------------------------------------------------------------------------------------------------------------------------#
# Bibliotecas importadas.
import os
#-----------------------------------------------------------------------------------------------------------------------------------#
# Apresentacao do programa.
print("----------------------------------------------------------------------")
print("-----------BEM VINDO AO CRIADOR DE ARQUIVOS PERSONALIZADOS------------")
print("----------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------------------#
class AlterarArquivos():
#-----------------------------------------------------------------------------------------------------------------------------------#
    # Método construtor.
    def __init__(self):
        super().__init__()
#-----------------------------------------------------------------------------------------------------------------------------------#
    # Solicita ao usuário a ação desejada e trata as entradas.
    def obterAcaoUsuario(self):

        # Continua perguntando até a entrada ser válida.
        while True:
            
            # Executa o código, caso não haja exceções, não cai no except.
            try:

                # Pede ao usuário um número para realizar alguma ação do programa.
                acao = int(input("""Que tipo de operação gostaria de realizar?
1 - Criar arquivos;
2 - Ler arquivos.
"""))

                # Caso a ação esteja certa, retorna ela mesma.
                if acao in [1, 2]:
                    return acao
                
                # Caso contrário, invalida e refaz a pergunta.
                else:
                    print("Opção não válida. Por favor, escolha entre 1 e 2.")
            
            # Refaz a pergunta tratando da exceção de valor inválido (não numérico ou não inteiro)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número (1 ou 2).")
#-----------------------------------------------------------------------------------------------------------------------------------#
    # Função que executa a ação escolhida pelo usuário.
    def executarAcao(self):
        
        # Armazena o resultado da função quem obtém o valor nesta variável.
        acaoEscolhida = self.obterAcaoUsuario()

        # Switch Case no python. Cada caso irá começar os passos de outra função determinada.
        match acaoEscolhida:
            
            # Caso 1 vai para a criarArquivo.
            case 1:
                self.criarArquivo()
            
            # Caso 2 vai para a LerArquivo.
            case 2:
                self.lerArquivo()
#-----------------------------------------------------------------------------------------------------------------------------------#
    # Funcao para criar arquivos.
    def criarArquivo(self):

        print("\n----- Criar Arquivo(s) -----")

        # Try para realizar o tratamento de excecoes.
        try:

            # Tratamento de erro durante a requisicao do tipo de arquivo.
            tipoArquivoValido = False
            
            # Inicialização da variável.
            extensaoArquivo = ""

            # Laço while para manter o loop ativo ate que esteja tudo certo.
            while not tipoArquivoValido:

                # Variavel que recebera o tipo do arquivo e trata caso tenha letras maiúsculas ou espaços extras.
                extencaoArquivo = input("""Qual o tipo de arquivo que você gostaria de criar? Exemplos:
|| .txt || .py || .md || .html || .css || \n \n""").lower().strip()

                # Verifica se a string é vazia.
                if not extencaoArquivo:
                    print("O tipo de arquivo não pode estar vazio.")
                    continue

                # Caso o usuario esqueça de inserir o "." antes do inicio do tipo do arquivo.
                if "." not in extencaoArquivo:

                    # Realizara a notificacao e arruma.
                    print("O tipo do arquivo nao apresentou o . antes do tipo.")
                    extencaoArquivo = "." + extencaoArquivo
                    
                    # Mostra ao usuário a versão corrigida.
                    print(f"A extensão foi corrigida para: {extensaoArquivo}")
                
                tipoArquivoValido = True

            # Tratamento de erro durante a requisicao do path escolhido.
            caminhoArquivo = input("Insira o path onde se localizara o novo arquivo criado: \n \n").strip()

            # Verifica se há valor na variável.
            if not caminhoArquivo:
                print("O caminho do arquivo não pode ser vazio.")
                
                # Sai da função se o caminho for inválido
                return 
        
            # Variavel que pede ao usuario o numero de arquivos para criar.
            while True:
                
                # Exceção para validar a quantidade de arquivos.
                try:

                    # Pede ao usuário uma quantidade de arquivos.
                    quantidadeArquivos = int(input("Quantos arquivos voce gostaria de criar? "))
                    
                    # Verifica se o valor é maior que 0.
                    if quantidadeArquivos > 0:
                        break
                    
                    else:
                        print("A quantidade de arquivos deve ser maior que zero.")

                # Exceção para o controle do tipo do valor.    
                except ValueError:
                    print(f"O valor {quantidadeArquivos} não é valido. Por favor, insira um número válido para a quantidade.")
            
            # Laço for para controlar a quantidade de arquivos criados.
            for i in range(1, quantidadeArquivos + 1):
                
                tentativaAtualSucesso = False

                # Loop para tentativas de criaçãodo i-ésimo arquivo.
                while not tentativaAtualSucesso:
                    nomeArquivoValido = False
                    nomeArquivo = ""

                    while not nomeArquivoValido:
                        nomeArquivo = input(f"Insira o nome do {i}º arquivo (sem a extensão): ").strip()

                        if nomeArquivo:
                            nomeArquivoValido = True
                        
                        else:
                            print("O nome do arquivo não pode ser vazio.")

                    # Controi o caminho completo do arquivo.
                    caminhoCompleto = os.path.join(caminhoArquivo, f"{nomeArquivo}{extensaoArquivo}")

                    try:

                        # Usa o open() em conjunto do uso das variaveis adquiridas ate agora para a criacao do arquivo.
                        # O modo "x" cria um novo arquivo e falha se ele já existir.
                        with open(file=caminhoCompleto, mode="x", encoding="utf-8") as arquivo:
                            
                            # Mostra o numero do arquivo sendo criado.
                            print(f"Criando o seu {i}° Arquivo de {quantidadeArquivos}: {caminhoCompleto}")

                            # Pergunta ao usuario se e necessario adicionar alguma descrição.
                            descricaoPersonalizada = input("Gostaria de adicionar alguma descricao para o arquivo? [S/N]\n \n").upper()

                            # Condicional para o caso de positivo.
                            if descricaoPersonalizada == "S":
                                print("Insira as descrições. Digite 'FIM' em uma nova linha para parar.")

                                # Cria um loop até o usuário digitar a palavra chave para finalizar a descrição.
                                while True:
                                    descricaoLinha = input()
                                    
                                    if descricaoLinha.upper() == "FIM":
                                        break

                                    arquivo.write(descricaoLinha + "\n")
                                
                                arquivo.write("\n")
                            
                            arquivo.write("#-----------------------------------------------------------------------------------------------------------------------------------#")
                        
                        # Confirma a criação do arquivo no PATH selecionado.
                        print(f"\n Arquivo {caminhoCompleto} criado com sucesso.")

                        # Marca como sucesso para sair do loop while interno.
                        tentativaAtualSucesso = True
                        
                    # Captura caso o arquivo já exista.
                    except FileExistsError:
                        print(f"ERRO: O arquivo '{caminhoCompleto}' já existe. Tente um nome diferente ou apague o existente.")
                        
                        # Dá a escolha de refazer o processo para o usuário.
                        retry = input("Gostaria de tentar um nome diferente para este arquivo? [S/N]: \n \n").upper()
                        
                        # Se a resposta for diferente de sim, então refaz o loop.
                        if retry != "S":
                            tentativaAtualSucesso = True

                    # Captura outros erros de sistema operacional, como caminho inválido.
                    except OSError as e:
                        print(f"ERRO ao criar o arquivo '{caminhoCompleto}': {e}")
                        print("Verifique se o caminho da pasta é válido e se você tem permissão para escrever nela.")

                        # Dá a escolha de refazer o processo para o usuário.
                        retry = input("Gostaria de tentar um nome diferente para este arquivo? [S/N]: \n \n").upper()
                        
                        # Se a resposta for diferente de sim, então refaz o loop.
                        if retry != "S":
                            tentativaAtualSucesso = True
            
                print("\nProcesso de criação de arquivo(s) concluído.")
        
        except Exception as e:
            print(f"Ocorreu um erro inesperado durante a criação de arquivos: {e}")
#-----------------------------------------------------------------------------------------------------------------------------------#
    # Função para ler arquivos.
    def lerArquivo(self):
        
        print("\n----- Ler Arquivo(s) -----")

        try:

            caminhoArquivoLeitura = input("Digite o caminho completo do arquivo que deseja ler: ").strip()

            if not caminhoArquivoLeitura:
                print("O caminho do arquivo não pode ser vazio.")
                return
            
            with open(file=caminhoArquivoLeitura, mode="r", encoding="utf-8") as arquivo:
                print("\nConteúdo do arquivo:")
                print(arquivo.read())
        
        except FileNotFoundError:
            print(f"Erro: Arquivo '{caminhoArquivoLeitura}' não encontrado.")
        
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")
#-----------------------------------------------------------------------------------------------------------------------------------#   
if __name__ == "__main__":

    programaArquivos = AlterarArquivos()

    while True:
        programaArquivos.executarAcao()
        continuar = input("Deseja realizar outra operação? [S/N]: \n \n").upper()

        if continuar != "S":
            break
    
    print("Programa finalizado.")
#-----------------------------------------------------------------------------------------------------------------------------------#