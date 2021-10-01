#OS é a abreviação de "OPERACIONAL SYSTEM" or Sistema operacional.
#VERIFICAÇÃO NO DIRETÓRIO ATUAL
import os

cwd = os.getcwd()
print("O DIREÓTIO PRINCIPAL É:" + cwd) #CURRENT WORKING DIRECTORY or Diretório de trabalho atual

#ENCONTRAR CAMINHO ABSOLUTO DE UM ARQUIVO
arquivo = input("Digite o nome do arquivo: ")

#CRIA CAMINHO PATH ABSOLUTO
local_Arquiv = os.path.abspath(arquivo)
print("Local atual do arquivo {}: ".format(arquivo), local_Arquiv)

#VERIFICA SE O CAMINHO PATH EXISTE RETORNA TRUE ou FALSE
verifica_caminho = os.path.exists(local_Arquiv)
print("ESSE ARQUIVO EXISTE? ", verifica_caminho)

#VERIFICA SE É UM DIRETÓRIO
verifica_existencia_diretorio = os.path.isdir(arquivo)
print("É UM DIRETÓRIO?  ", verifica_existencia_diretorio)

#VERIFICA SE É UM ARQUIVO
verifica_Éarquivo = os.path.isfile(arquivo)
print("É ARQUIVO? ", verifica_Éarquivo)

#RETORNA A LISTA DE ARQUIVOS E DIRETÓRIOS
retorna_list_ARQV_e_DIRT = os.listdir(cwd)
print("LISTA DE ARQUIVOS E DIRETÓRIOS: ", retorna_list_ARQV_e_DIRT)