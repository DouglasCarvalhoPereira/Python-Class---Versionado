#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    name = str(input('Nome de usuário: '))
    senha = str(input('Senha: '))
    if name == senha:
        print('Uusário e senha não podem ser iguais. Tente novamente!')
    else:
        print('Uusário e senhas salvos com sucesso.')
        break