#HERANÇA
class Pessoa:
    def __init__ (self, name, altura, olhos):
        self.name = name
        self.altura = altura
        self.olhos = olhos
        
    def __str__(self):
        return "Hello, i'm {}, i have {} height and {} eyes, good Morning" .format(self.name, self.altura, self.olhos)

class Brother_1(Pessoa):
    pass

class Brother_2(Pessoa):
    pass

douglas = Pessoa("Douglas","1,69", "Blue")
clayton = Brother_1("Clayton","1,69", "Brown")
lucas = Brother_2("Lucas","1,75", "Brown")
print(douglas)
print(clayton)
print(lucas)