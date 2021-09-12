winners = ["Douglas","Clayton","Lucas"]

for index, person in enumerate(winners): #ENUMERATE PERMITE USAR 2 INDI
    print("{} - {}" .format(index + 1, person))

def full_email(people):
    result = []
    for name, email in people:
        result.append('{} <{}>'. format(email, name))
    
    return print(result)

full_email(([("carvalhodouglas@gmail.com","Douglas Carvalho"),("almeida@gmail.com", "Tiago Almeira")]))

#CRIANDO UMA LISTA DE 1 ATÉ 10 COM MULTIPLOS DE 7
multiplos_7 = []

for x in range(1,11):
    multiplos_7.append(x*7)

print(multiplos_7)

#CRIANDO A MESMA LISTA, PORÉM COMPRIMIDA
multiplos_7 = [x*7 for x in range(1,11)]
print(multiplos_7)

#LENDO QUANTIDADE DE CARACTERES EM CADA STRING DE UMA LISTA
languages = ["Ingles", "Portugues", "Islandes", "Frances"]
lengths = [len(languade) for languade in languages]
print(lengths)

#COMPRENSÃO DE LISTAS USANDO LOOPS E IF
multiplos_3 = [x for x in range(0,11) if x % 3 == 0]
print(multiplos_3)

