import random
#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve 
# possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos 
# são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor 
# default zero e os demais atributos são obrigatórios.
class contaCorrente():

    def __init__(self, nome = '', saldo = 0, numero_de_conta = ()):
        self.nome = nome
        self.saldo = saldo
        self.numero_de_conta = gerador_de_conta.aleatorio(self)


    def __str__(self) -> str:
        pass 

    def altera_Nome(self, nome):
        self.nome = nome
        return self.nome

    def deposito(self, saldo = 0):
        self.saldo += saldo
        return self.saldo

    def saque(self, saldo = 0):
        self.saldo -= saldo
        return self.saldo

    def mostrarConta(self):
        return print(f"Número CC: {self.numero_de_conta} \nNome: {self.nome} \nSaldo: {self.saldo}")




class gerador_de_conta(contaCorrente): #NÚMERO ALEATÓRIO POR DIVERSÃO, VAI QUE CAI UMA CONTA MILIONÁRIA
    def __init__(self, n_conta):
        self.n_conta = n_conta
    
    def aleatorio(self):
        self.n_conta = random.randint(1, 1000)
        return self.n_conta




douglas = contaCorrente()
douglas.altera_Nome("Douglas")
douglas.deposito(100000000.0)
douglas.saque()
douglas.mostrarConta()