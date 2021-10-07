from datetime import date, datetime
from random import randint

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome = "", idade = 0, ti = ''):
        self.nome = nome
        self.idade = idade

    #MÉTODO DE INSTÂNCIA - SELF se refere a instância
    def get_ano_nasciemento(self):
        print(self.ano_atual - self.idade)

    #MÉTODO DE CLASSE
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        """
        Método da classe, recebe os dois parâmetros da instância:
        NOME E IDADE, sendo calculado tanto o ano como idade

        """
        idade = cls.ano_atual - ano_nascimento
        return cls(print(nome, idade))

    #NÃO PRECISA DA INSTÂNCIA E NEM DA CLASSE, COMO SE FOSSE FORA DE UMA CLASSE. INDEPENDENTE
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


    