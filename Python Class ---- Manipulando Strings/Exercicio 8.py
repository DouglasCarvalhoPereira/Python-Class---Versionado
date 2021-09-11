#CONFIRMA SE É PALINDROMO OU NÃO
texto = input('Digite uma algo: ').upper()
juntas = texto.replace(' ','')

if juntas == juntas[::-1]:
    print('Palindromo')
else:
    print("'",texto,"'" ' Não é um palindromo')