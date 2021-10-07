import string

question_1 = open('user1.txt','r').readlines()
question_2 = open('user2.txt','r').readlines()
question_3 = open('user3.txt','r').readlines()

#NOVO ARQUIVO
os_ganhadores = open('ganhadores.txt','w')

list = []
ganhadores = []


for user1 in question_1:
        list.append(user1)
for user2 in question_2:
        list.append(user2)
for user3 in question_3:
        list.append(user3)

for user in list:
    if user in question_1 and user in question_2 and user in question_3:
        if user not in ganhadores:
            ganhadores.append(user)

#GERA NOVO ARQUIVO COM GANHADORES
for line in ganhadores:
    os_ganhadores.write(line)