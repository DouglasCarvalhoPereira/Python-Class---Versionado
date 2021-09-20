#Classe Quadrado: Crie uma classe que modele um quadrado:
#
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
newTamanhoLado = int(input("Digite o tamanho do lado: "))

class Quadrado:
        ladoM = 0
        newLado = 0

        def mudarTLado(self, ):
            self.ladoM = newTamanhoLado
            return self.ladoM
 
        def retornaArea(self):
            print("O novo lado é {}, e a área é: {}²".format(self.ladoM, self.ladoM**2))

quadrado = Quadrado()
quadrado.mudarTLado()
print("O lado é {}." .format(quadrado.ladoM))
quadrado.retornaArea()