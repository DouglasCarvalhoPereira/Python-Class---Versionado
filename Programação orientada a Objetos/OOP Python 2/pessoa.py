class Pessoa:
     def __init__(self, nome, idade, sexo, comendo=False, falando=False):
         self.nome = nome
         self.idade = idade
         self.sexo = sexo
         self.comendo = comendo
         self.falando = falando

     def comer(self):
        print(f"{self.nome} está comendo!")
        self.comendo = True
