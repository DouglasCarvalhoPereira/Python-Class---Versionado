import os
#FUNÇÃO NAVEGA POR UM DIRETÓRIO, EXIBE OS NOMES DE TODOS OS ARQUIVOS E CHAMA A SI MESMO
#RECURSIVAMENTE EM TODOS OS DIRETÓRIOS
cwd = os.getcwd()

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name) #Recebe o nome de um diretório e o de um arquivo e os une em um caminho completo
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)-1

walk(cwd)