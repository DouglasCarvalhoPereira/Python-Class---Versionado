#ENCAPSULAMENTO É FEITO PARA PROTEGER A CLASSE, ATRIBUTO OU MÉTODO E ETC
"""
public, protected e private em Python é susbtituido por:

=> _            (public _) #NÃO DEVE SER ACESSADA FORA DA CLASSE, pode ser modificado, mas não é recomendado
=> __           (_NOMECLASSE__nomeatributo) #PROIB O ACESSO AO ATRIBUTO, mas pode ser modificado

"""

class BaseDate:
    def __init__(self):
        self.__dados = {} #ATRIBUTO PRINCIPAL DESPROTEGIDO, SE FOR ALTERADO QUEBRA TODA A CLASSE

    @property
    def dados(self):
        return self.__dados

    @dados.setter
    def dados(self, valor):
        self.__dados = valor
        return self.__dados

    def inserir_Cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self ):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def deletar_cliente(self, id):
        del self.__dados['clientes'][id]


    

db = BaseDate()
db.inserir_Cliente(1, 'Tiago')
db.inserir_Cliente(2, 'Marcelo')
db.inserir_Cliente(3, 'Joana')

db.deletar_cliente(3)
db.lista_clientes()

#print(db.__dados) #NÃO É POSSÍVEL ACESSAR O ATRIBUTO APÓS TER SIDO ADICIONADO "__"
print(db._BaseDate__dados) #PARA TAL SITUAÇÃO USAR

print(db.dados) #USANDO GETTER PARA ACESSAR O DADO