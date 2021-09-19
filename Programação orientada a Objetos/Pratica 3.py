#METODO CONSTRUCTOR

class Apple:
    def __init__(self, color, flavor, fruit): #CONSTRUTOR, AO INSTÂNCIAR UMA CLASSE __init__ Automáticamente copia os Atributos definidos
        self.color = color
        self.flavor = flavor
        self.fruit  = fruit
    
    def __str__(self): # Me permite imiprimir o resultado da string usando __str__ e não a posição da memório com vários números
        return "This apple is {} and its flavor is {}" .format(self.color, self.flavor)


fruit = Apple("Green", "Doce","Apple") #PARAMETROS PASSADOS PARA O MÉTODO CONSTRUTOR
print(fruit.color, fruit.flavor, fruit.fruit)

print(fruit) #Usando __str__ os parametros passados anteriormento foram mantidos e o resultado impresso por inteiro
#Edição
