
#TRABALHANDO COM BANCO DE DADOS
# 'r' - Abra o banco de dados existente apenas para leitura (padrão)
# 'w' - Abra o banco de dados existente para leitura e gravação
# 'c' - Abra o banco de dados para leitura e escrita, criando-o se não existir
# 'n' - Sempre crie um novo banco de dados vazio, aberto para leitura e escrita

import dbm

db = dbm.open('captions','c') #
db['suco.png'] = 'Suco Fit'
db['suco.png'] = 'Suco Fit Laranja' #Substitui o próximo
db['suco.png'] = 'Suco Fit Manga' #Também

print(db["suco.png"]) 

#PARA BANCO DE DADOS MÉTODOS COMO KEYS E ITEMS NÃO FUNCIONAM, MAS ITERAÇÃO COM FOR LOOP, SIM.
for key in db:
    print(key, db[key])
    db.close()


