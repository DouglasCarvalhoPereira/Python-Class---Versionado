#Associação entre escritor, maquina de escrever e caneta.
class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        #VARIÁVEL FERRAMENTA FICOU PROGRAMADA PARA RECEBER UM VALOR
        self.__ferramenta = None

    def __str__(self):
        return '{__nome}'
        
    #GETTER NOME
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self):
        return self.__nome

    #GETTER FERRAMENTA 
    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Ceneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @property
    def texto(self):
        return self.__texto

    def escrever(self, nome, texto):
        print(f"{nome}, {texto}")



class Maquina_Escrever:
    def __init__(self, tipo):
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    def escrever(self, nome, texto):
        print(f"{nome}, {texto}")
    
    
