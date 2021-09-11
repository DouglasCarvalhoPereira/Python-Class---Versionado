#TUPLAS - SEQUÊNCIAS DE ELEMENTOS IMUTÁVEIS
listas = ['Douglas', 'Clayton', 'Lucas'] #MUTÁVEIS
tuplas = ('Douglas', 'Clayton', 'Lucas') #IMUTÁVEIS



nome_completo = ('Douglas', 'Carvalho', 'Pereira')


#ESSE MODELO DE FUNÇÃO RETORNA UMA TUPLA E EXEMPLIFICA A IMPORTÂNCIA DA IMUTABILIDADE

segundos_usuario = int(input("Quantos segundos: "))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = ( seconds - hours * 3600 ) // 60 
    remainig_seconds = seconds - hours * 3600 - minutes * 60
    result = hours,minutes,remainig_seconds

    return result

print(convert_seconds(segundos_usuario))


#NESSE CASO É PASSADO UM TUPLA COMO PARAMETRO, ONDE CADA STRING É NOMEADA DE FORMA DIFERENTE DENTRO DA PRÓRPIA FUNÇÃO

def file_size(file_info):
    nome, formato, tamanho = file_info
    return("{:.2f}".format(tamanho / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

