texto_user = input("Digite um texto para ser armazenado: \n")

#ABRIR EM MODO ESCRITA DELETA O CONTEÚDO EXISTENTE E ESCREVE DE NOVO.
#CRIA NOVO ARQUIVO DE TEXTO E ESCREVE DENTRO
abre_arquivo = open("testeComPalavras.txt", 'w', encoding="utf-8")

#SÓ ACEITA NÚMEROS SER FOR CONVERTIDO EM STRING
line2 = 42 
line1 = "Contiua no próximo episódio..."

#ESCREVE NO ARQUIVO DE *OPEN E RETORNA A QUANITDADE DE CARACTERES.
abre_arquivo.write("A Os números formatos como String a seguir usam o módulo como ferramenta '%d' '%g' '%s' \né diferente do inteiro 42\n " % (3, 0.3, 'line2'))
abre_arquivo.write(line1 + "\n")
abre_arquivo.write(texto_user)
abre_arquivo.close()

