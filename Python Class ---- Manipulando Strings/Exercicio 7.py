texto = str(input('Digite uma frase: ')).lower()

print(texto.count(' '))
vogais = ['a','e','i','o','u']

for v in vogais:
    cont_vogal = texto.count(v)
    print(str(v).upper(), ':',  cont_vogal, end='  ')