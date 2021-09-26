ref_arquivo = open("recomeco.txt")
linhas = ref_arquivo.readline()
for linha in linhas:
    print(linha)    

text = open('recomeco.txt')
print(text.readlines())
print(text.read())
print(text.read())
print(text.read())
print(text.read())
print(text.read())
print(text.readline())
print(text.readlines())
for line in text:
    print(line)
