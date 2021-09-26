ref_arquivo = open("words.txt","r")
<<<<<<< Updated upstream
lista_de_linhas = ref_arquivo.read()
print(lista_de_linhas)
=======
linhas = ref_arquivo.readline()
for linha in linhas:
    print(linha)
>>>>>>> Stashed changes
