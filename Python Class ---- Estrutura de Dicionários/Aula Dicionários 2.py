#CONTADOR DE LETRAS EM UMA STRING

def count_letters(text):
    result = {} 
    cont = 0
    for letter in text:
        cont += 1

        if letter not in result:
            result[letter] = 0 #SE A LETRA NÃO CONSTA NO DICIONÁRIO RECEBE '0'
        result[letter] = result[letter] + 1 #CADA VEZ QUE A O LOOP PERCORRER A LISTA A LETRA RECEBE O VALOR, SE ELA NÃO ESTIVER PRESENTE RECEBE 0

    return print('TOTAL DE CARACTERES: ', cont, '\nCARACTERES POR LETRA: ', result)

count_letters('Testando quantos vezes vezes uma letra aparece na string.')