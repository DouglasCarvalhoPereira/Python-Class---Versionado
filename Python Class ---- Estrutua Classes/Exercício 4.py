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

    def envelhecer(self):
        if self.idade >= 21:
            self.altura = self.altura
        else:
            self.altura += 0.5

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self,peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def mostraPessoa(self):
        print(f'Nome: {self.nome} Idade: {self.idade} anos Peso: {self.peso} Kg Altura: {self.altura}')


        
      
douglas = Pessoa("Douglas", 22, 62, 169)
douglas.envelhecer()
douglas.mostraPessoa()