from classes5 import Professor, Aluno

#HERANÇA
"""
Associação = USAR  |  Agregação = TEM  |  Composição = É DONO  |  Heranã = É

"""

professor = Professor('Tiago', 56, 'Masculino')
professor.falar()
professor.escrever()
aluno = Aluno('Pedro', 23, 'Masculino')
aluno.escrever()
aluna = Aluno('Julia', 20, "Feminino")