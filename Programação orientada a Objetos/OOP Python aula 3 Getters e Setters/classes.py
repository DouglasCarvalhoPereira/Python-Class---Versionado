#Associação entre escritos, maquina de escrever, caneta e pape.
class Escritor:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

class Ceneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

class Maquina_Escrever:
    pass
