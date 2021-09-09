name = str(input('Nome: '))
idade = int(input('Idade: '))
salario = float(input('Salário: '))
sexo = input('Digite seu sexo, F ou M: ').upper()
estado_civil = input('Estado civil: ').lower()

while (len(name) < 3):
    print('NOME COM MENOS DE 3 CARACTERES! ERRO')
    name = str(input('Nome: '))

while (idade < 0) or (idade > 150):
    print('Idade inválida. ')
    idade = int(input('Idade: '))

while (salario < 0):
    print('Salário inválio. ')
    salario = float(input('Salário: '))

while (sexo.upper()!='F') and (sexo.upper()!='M'):
    print('Sexo inválido. ')
    sexo = str(input('Digite seu sexo, F ou M: '))

while (estado_civil != 's') and (estado_civil != 'c') and (estado_civil != 'v') and (estado_civil != 'd'):
    print('Estado civil inválido. Digite S, C, V ou D. ')
    estado_civil = str(input('Estado civil: '))