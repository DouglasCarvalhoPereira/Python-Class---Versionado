letra = str(input(' Digite um aletra: ')).upper()
abcdario = str("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z").split()
vogais = str("A E I O U").split()

if letra in vogais:
    print('Vogal')
else:
    print('Consoante')
