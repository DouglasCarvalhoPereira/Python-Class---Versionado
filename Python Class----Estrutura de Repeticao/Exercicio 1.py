while True:
    nota = int(input('De 0 a 10, qual a sua nota? '))
    if nota > 10:
        print('Por favor digite uma nota de 0 a 10.')
    else:
        print('Sua nota foi computada!')
        break