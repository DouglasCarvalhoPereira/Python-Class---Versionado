#COMPOSIÇÃO - RELAÇÃO MAIS FORTE ENTRE CLASSES
#CLASSE QUE SE TORNA DONA DA OUTRA CLASSE
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_cadastro(self):
        print("="*40)
        print("DADOS CADASTRAIS")
        print(f"NOME: {self.nome} \nIDADE: {self.idade}")
        print("="*40)
        print("ENDEREÇOS")
        for endereco in self.enderecos:
           print(f"{endereco.cidade} \ {endereco.estado}")
        print("="*40)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


