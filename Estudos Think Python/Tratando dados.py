import string

txt = open('TOP_300_CLIENTES.txt','r+').readlines()

#new_text = open('Formatado.txt','w')
sem_pontuação = ''.join([tel.replace(" ","") for tel in txt if tel not in string.punctuation])
txt.write(sem_pontuação)


for tel in new_text:
    nonoDigito = tel[2:]
    prox_4digitos = tel[3:7]
    ultimos_4digitos = tel[-5:]
    new_num = nonoDigito + " " + prox_4digitos + " " + ultimos_4digitos
    print(new_num, end='')
                