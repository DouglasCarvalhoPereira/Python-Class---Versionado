#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo 
#compreendido por eles.

while True:
    x = int(input('Digite o ponto A. '))
    y = int(input('Digite o ponto B. '))

    for i in range(x,y,1):
        print(i, end = ' ')
    print('\n')