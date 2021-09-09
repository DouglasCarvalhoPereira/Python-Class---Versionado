soma = 0
media = 0
cont = 5
for i in range(cont):
    numero = int(input('Digite um número: '))
    soma += numero
    media = soma/cont


print("A soma é {soma}." .format(soma=soma))
print("A media é {:.0f}." .format(media))