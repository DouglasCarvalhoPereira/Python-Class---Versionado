#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
    #homem = (72.7*altura) - 58
    #print("O peso ideal para homens é {}: ".format(homem))
    #mulher = (62.1*altura) - 44.7
    #print("O peso ideal para mulher é {}: ".format(mulher))



altura = float(input("Qual sua altura? "))
print("Digite 1 se for homem e 2 se for mulher.")
sexo = int(input("Qual seu sexo? "))

if sexo == 1:
    homem = (72.7*altura) - 58
    print("O peso ideal para homens é {}: ".format(homem))
elif sexo == 2:
    mulher = (62.1*altura) - 44.7
    print("O peso ideal para mulher é {}: ".format(mulher))