#Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de 
# CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação 
# dos dígitos verificadores e dos caracteres de formatação.

verificador_cpf = int(input('Digite seu CPF: [000.000.000-00] ')).replace('.','')
print(verificador_cpf)



