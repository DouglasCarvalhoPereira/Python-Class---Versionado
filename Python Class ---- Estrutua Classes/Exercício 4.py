#Classe Pessoa: Crie uma classe que modele uma pessoa:
#
#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa 
# pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def __str__(self) -> str:
        pass

    def envelhecer(self, anos):
        self.idade += anos
        return self.idade

    def engordar(self, kilos):
        self.peso += kilos
        return self.peso

    def emagrecer(self,perda_peso):
        self.peso -= perda_peso

    def crescer(self, anos):
        if anos < 21:
            self.idade += (0.5)*(anos)

douglas = Pessoa("Douglas", 26, 62, 1.69)
douglas.envelhecer()