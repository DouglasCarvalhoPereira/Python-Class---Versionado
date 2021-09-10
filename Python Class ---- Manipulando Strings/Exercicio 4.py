name = str(input('Digite um nome: ')).upper()

for i in range(0, len(name)+1):
    print(name[:i])