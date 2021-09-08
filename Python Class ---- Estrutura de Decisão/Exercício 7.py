primeiro = float(input('Digite o primeiro número: '))
segundo = float(input('Digite o segundo número: '))
terceiro = float(input('Digite o terceiro número: '))

#ENCONTRANDO O MAIOR
if primeiro > segundo and primeiro > terceiro:
    print('O Primeiro é o maior.')
elif segundo > primeiro and segundo > terceiro:
    print('O Segundo é o maior.')
elif terceiro > primeiro and terceiro > segundo:
    print('O Tercero é o maior')

#ENCONTRANDO O MENOR
if primeiro < segundo and primeiro < terceiro:
    print('O Primeiro é o menor.')
elif segundo < primeiro and segundo < terceiro:
    print('O Segundo é o menor.')
elif terceiro < segundo and terceiro < primeiro:
    print('O Terceiro é o menor.')