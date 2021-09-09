name = input('Digite seu nome: ')
others_name = [name, "Carvalho", "Pereira"]
list = "Douglas Carvalho Pereira"

print(name.upper())#Maiusculo

print(name.lower())#Minusculo

print(name.strip())#Remove Espaço entre os caracteres
print(name.lstrip())#Elimina Espaços do lado esquerdo 
print(name.rstrip())#Elimina Espaços do lado direito

print(name.count("D"))#Conta quantas vezes esse caracter existe dentro da string

print(name.endswith("glas"))#Retorna se a string terina com determinada substring

print(name.isnumeric())#Retorna se a string é numerica
print(name.isalpha())#Retorna se a string é alfabetica


print("...".join(others_name))#Contactenou as strings com Join, definindo o que entraria entre cada caracretere

#Não preciso saber se o usuário digitou maiusculo ou minusculo, é só converter.

if name.lower() == 'douglas':
    print("Ok, todos os caracteres convertidos em minúsculos para verificação!")

print(list.split())#Converte uma frase com espaço em String individual

#Todos os métodos disponíveis
#https://docs.python.org/3/library/stdtypes.html#string-methods

#Documento de sitxe e fotmatação oficial
#https://docs.python.org/3/library/string.html#formatstrings