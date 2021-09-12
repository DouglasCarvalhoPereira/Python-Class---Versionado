lista = []

print('Lista antes: ', lista)

lista.append('a')
lista.append('b')
lista.append('c')
lista.append('d')
lista.append('e')
lista.append('f')
lista.append('g')
lista.append('h')
lista.append('i')

lista.insert(4, "MEIO") #String adicionado a posição 4.
lista.insert(30, 'FIM') #Se o indíce no caso '30' for maior que o comprimento atual, será adicionado na última posição.

lista.remove('a') #Remove da lista
lista.remove('i') #Remove da lista
 
lista.sort() #Classifica em ordem crescente por padrão

lista.reverse() #Inverte a ordem dos elementos de uma lista

lista.clear() #Remove todos os itens da lista

lista.copy() #Cria uma cópia da lista

lista.extend() #Acrescenta outra lista ou elementos ao final da lista

 

print('Lista depois: ', lista)

lista.pop(2) #Remove o indice.

print('Após .pop()', lista)

lista[0] = 'COMEÇO' # Susbtitui index passado 

print(lista)
