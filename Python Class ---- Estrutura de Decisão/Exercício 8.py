#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

produto_um = float(input('Qual o valor do primeiro produto: '))
produto_dois = float(input('Qual o valor do segundo produto: '))
produto_tres = float(input('Qual o valor do terceiro produto: '))

if produto_um < produto_dois and produto_um < produto_tres:
    print('O produto N° 1 = {} é o mais barato. '.format(produto_um))
elif produto_dois < produto_um and produto_dois <produto_tres:
    print('O produto N° 2 = {} é o mais barato. '.format(produto_dois))
elif produto_tres <produto_um and produto_tres <produto_dois:
    print('O produto N° 3 = {} é o mais barato. '.format(produto_tres))

