class Piglet:
    name = "Google"
    years = 0

    def speak(self): #O Parametro "SELF" permite acessar os atributos, como (NAME).
        print("Oink Oink {}!".format(self.name))

    def pig_years(self):
        return self.years * 18


teste = Piglet()
teste2 = Piglet()
teste3 = Piglet()
teste.name = "Douglas"
teste2.name = "Clayton"
teste3.name = "Lucas"
teste.speak()
teste2.speak()
teste3.speak()

teste.years = 10
print(teste.pig_years())
