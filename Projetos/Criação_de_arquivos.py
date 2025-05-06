# Criando arquivos para estudos de exercícios. PROTÓTIPO

# Apresentação do programa.
print("----------------------------------------------------------------------")
print("-----------BEM VINDO AO CRIADOR DE ARQUIVOS PERSONALIZADOS------------")
print("----------------------------------------------------------------------")

tipoArquivo = False

while tipoArquivo == False:

    tipoArquivo = input("""Qual o tipo de arquivo que você gostaria de criar? 
                        Exemplos:   || .txt || .py || .md || .html || .css ||""").lower()
    
    if "." not in tipoArquivo:
        print("O tipo do arquivo não apresentou o . antes do tipo.")
        tipoArquivo = input("""Qual o tipo de arquivo que você gostaria de criar? 
        Exemplos:   || .txt || .py || .md || .html || .css || """).lower()
    else:
        tipoArquivo = True

def CriandoArquivos(tipoArquivo):

    # Laço for para controlar a quantidade de arquivos criados.
    for i in range(3,5):

        # Usar o open com o mode x para criar o arquivo e escrever o número do exercício tanto no diretório quanto dentro dele utilizando o write.
        with open(file="E:\Diogo\MeusProjetos\Estudos-de-Python\Exercicios\Dict Comprehension\Exercicio_" + str(i) + tipoArquivo, mode="x") as arquivo:
        
            arquivo.write("# Exercício " + str(i) + " - Dictionary Comprehension. \n")
            arquivo.write("\n")
            arquivo.write("#-----------------------------------------------------------------------------------------------------------------------------------#")

CriandoArquivos(tipoArquivo)