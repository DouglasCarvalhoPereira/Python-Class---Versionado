class Carrinho_de_Compras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total_produtos(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        
        return print(total)

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
