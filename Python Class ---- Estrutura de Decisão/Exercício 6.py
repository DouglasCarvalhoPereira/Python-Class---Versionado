numero1 = float(input('Digite o número 1: '))
numero2 = float(input('Digite o número 2: '))
numero3 = float(input('Digite o número 3: '))

if numero1 > numero2 and numero1 > numero3:
    print('O número 1 é o maior.')
elif numero2 > numero1 and numero2 > numero3:
    print('O número 2 é maior. ')
elif numero3 > numero2 and numero3 > numero1:
    print('O número 3 é o maior. ')
else:
    print('Incluso números iguais. ')