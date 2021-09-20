#Classe Bola: Crie uma classe que modele uma bola:
#
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

variavel = input("Digite a cor: ")

class Bola:
    #Atributos
    cor = "Azul"
    circunf = 10
    material = "Couro"

    #Metodos
    def trocaCor(self):
        self.cor = variavel
        return self.cor

    def mostraCor(self):
        print("A nova cor é: {}" .format(self.cor))


newBola = Bola()
print("A cor atual é: {}".format(newBola.cor))
newBola.trocaCor()
newBola.mostraCor()
