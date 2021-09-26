ref_arquivo = open("words.txt","r")
lista_de_linhas = ref_arquivo.readlines()
for i in lista_de_linhas:
    print(i + "APROVADO")