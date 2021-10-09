#HERANÇA
"""
Associação = USAR  |  Agregação = TEM  |  Composição = É DONO  |  Heranã = É

"""
class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.ferramenta = None

    def falar(self):
        print(f"{self.nome} está falando...")


class Professor(Pessoa):
    def escrever(self):
        print(f'O professor {self.nome} está escrevendo...')


class Aluno(Pessoa):
    def escrever(self):
        print(f'O aluno(a) {self.nome} está escrevendo...')