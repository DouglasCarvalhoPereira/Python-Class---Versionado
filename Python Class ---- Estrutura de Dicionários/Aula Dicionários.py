#Dicionários são mutávris

docs = {'txt':10, 'jpg':14, 'png':19, 'mp4': 15}

#Para acessar qualquer elemento do dicionário usam-se chaves por exemplo

docs['txt'] #10
docs['mp4'] #15

#Verficar se determinado elemento está presente no dicionário é simples

'TXT' in docs #Retorna True se estiver e False se não

#Para adicionar valores no icionário utilizamos a seguinte maneira:

docs['.py'] = 5 #Dessa forma ".py" ocupa a última posição do dicionário com '.py':5

#Ao adicionar uma chave que já existe a atual é substituida

docs['jpg'] = 23 #Nesse caso o 23 susbtituiu o 14

#Para excluir um elemento do dicionário utilizamos a palavra DEL 'del'

del docs['jpg'] #Sendo assim o elemento 'JPG' não consta mais no dicionári

print(docs)

#ACESSANDO ELEMENTOS DO DICIONÁRIO

for i in range(1):
    docs[i] = 'New Date' #Foi adicionado 'New Date' a cada posição de 'i'docs

print(docs)

for doc in docs:
    print(doc) #Dessa maneira exibo cada chave do dicionário


for key, element in docs.items(): #Usando ITEM() é possível acessar os dois elementos do dicionário.
    print(key, ': ', element)

#ACESSAR CHAVES OU VALORES DO DICIONÁRIO USA-SE

print('As chaves são: ', docs.keys()) #Para as chaves do dicionário
print('Os valores são : ',docs.values()) #Para os valores

#DESSA MANEIRA IMPRIMO TODAS AS CHAVES 
for value in docs.keys():
    print(value)

#DESSA MENIRA TOOS OS VALORES
for value in docs.values():
    print(value)   


