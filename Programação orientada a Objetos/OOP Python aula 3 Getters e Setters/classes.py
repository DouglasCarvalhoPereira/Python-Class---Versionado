class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
        return self.preco


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str):
            print("É número, digite novamente")
        
        self._nome = valor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, config_preco):
        if isinstance(config_preco, str):
            config_preco = float(config_preco.replace('R$', ''))
        
        self._preco = config_preco


           