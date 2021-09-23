import random

class aleatorio:
    
    def aleatorio(self):
        self.numero = random.randint(1, 50)
        return print(self.numero)


conta = aleatorio()
conta.aleatorio()