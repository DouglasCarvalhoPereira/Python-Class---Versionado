import string
from typing import Text

txt = open('TOP_300_CLIENTES.txt','r')
new_num = txt.readlines()
num_11_digitos = [tel for tel in new_num if len(tel) != 11]

#sem_pontuação = ''.join([tel.replace(' ','') for tel in txt if tel not in string.punctuation])

print(num_11_digitos)

for tel in new_num:

    nonoDigito = tel[2]
    prox_4digitos = tel[3:7]
    ultimos_4digitos = tel[-5:]
    new_num = nonoDigito + " " + prox_4digitos + " " + ultimos_4digitos
                