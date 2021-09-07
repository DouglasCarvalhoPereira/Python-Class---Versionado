number1 = float(input('Digite o número 1: '))
number2 = float(input('Digite o número 2: '))

if number1 > number2:
    print('A opção A = {} é maior do que a opção B = {}.'.format(number1, number2))
elif number1 == number2 or number2 == number1:
    print('Resultados iguais.')
else:
    print('A opção B = {} é maior do que a opção A = {}.'.format(number2, number1))
