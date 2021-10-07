class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}" .format(
            name = self.name, sound = self.sound))

class Piglet(Animal): #Erdado da Classe Animal através do construtor
    sound = "Oink!" #Alterado parametro Sound

class Vaca(Animal):  #Erdado da Classe Animal através do construtor
    sound = "Muuu" #Alterado parametro Sound

class Cachorro(Animal): #Erdado da Classe Animal através do construtor
    sound = "Au Au" #Alterado parametro Sound


hamlet = Piglet("Hamlet")    
hamlet.speak()

sandra = Vaca("Sandra")
sandra.speak()

scot = Cachorro("Scot")
scot.speak()