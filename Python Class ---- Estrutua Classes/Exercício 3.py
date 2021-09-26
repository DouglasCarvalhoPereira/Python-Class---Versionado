import math
#Classe Retangulo: Crie uma classe que modele um retangulo:
#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de 
# um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de 
# rodapés necessárias para o local.

comprimento_Usuario = ""
altura_Usuario = ""

while comprimento_Usuario == "":
    comprimento_Usuario = input("Digite o comprimento: ")
    if comprimento_Usuario == "":
        print("Erro: CAMPO VAZIO")

while altura_Usuario == "": 
    altura_Usuario = input("Digite a altura: ")
    if altura_Usuario == "":
        print("Erro: CAMPO VAZIO")

class Retangulo:
    tamanha_rodape = 0.2 #cm
    metragem_piso = 0.50 * 0.50 #m²

    def __init__(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura

    def __str__(self):
        pass
        #return "O é {} e a altura {}. A área é igual a {}m² e Perimetro {}.".format(self.comprimento, self.altura)

    def alteraValoresDeMedida(self):
        self.comprimento = float(comprimento_Usuario)
        self.altura = float(altura_Usuario)
        return print("O comprimento é {} e a altura {}." .format(self.comprimento, self.altura))

    def calcularArea(self):
        self.area = self.comprimento * self.altura
        return print("A área é  {:.0f} M²." .format(self.area))

    def calcularPerimetro(self):
        self.perimetro = 2 * (self.comprimento + self.altura)
        return print("O perimetro é {:.0f} M." .format(self.perimetro))

    def calcula_quantidade_Piso(self):
        self.quantidade_Piso = math.ceil(self.area / self.metragem_piso)

        return print("A quantidade de PISO necessária para essa area é {} unidade(s)." .format(self.quantidade_Piso))

    def calcula_qauntidade_de_rodape(self):
        self.quantidade_Rodapé = self.perimetro / self.tamanha_rodape
        return print("A quantidade de RODAPÉ necessária para essa area é {:.0f} unidade(s)." .format(self.quantidade_Rodapé))


new_objeto = Retangulo(comprimento_Usuario, altura_Usuario)
new_objeto.alteraValoresDeMedida()
new_objeto.calcularArea()
new_objeto.calcularPerimetro()
new_objeto.calcula_quantidade_Piso()
new_objeto.calcula_qauntidade_de_rodape()