string = 'Douglas Programador Python Especialista'
qnt_letras = 5
new_list = '-'.join([letter for letter in string])
new_list = '-'.join([string[indice:indice + qnt_letras] for indice in range(0, len(string), qnt_letras)])

print(new_list)