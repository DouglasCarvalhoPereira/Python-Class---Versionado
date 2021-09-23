import random
#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve 
# possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos 
# são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor 
# default zero e os demais atributos são obrigatórios.
class contaCorrente():
    def __init__(self,nome , saldo):
        self.numero_de_conta = gerador_de_conta.aleatorio(self)
        self.nome = nome
        self.saldo = saldo

    def __str__(self) -> str:
        return 

    def altera_Nome(self, nome):
        self.altera_Nome = nome

    def deposito(self, saldo):
        conta_deposito = 0
        conta_deposito += saldo
        return self.conta_deposito

    def saque(self):
        pass


class gerador_de_conta(contaCorrente):
    def __init__(self, n_conta):
        self.n_conta = n_conta
    
    def aleatorio(self):
        self.n_conta = random.randint(1, 1000)
        return self.n_conta




douglas = contaCorrente("Douglas", 100)