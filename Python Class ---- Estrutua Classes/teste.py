class Pessoa:
    def __init__(self,nome,idade,peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        return self.idade
    def engordar(self, kilos):
        self.peso += kilos
        return self.peso
    def emagrecer(self,kilos_perdidos):
        self.peso -= kilos_perdidos
        return self.peso

    def crescer(self,anos):
        if self.idade<21:
            self.altura += (0.05)*anos
        return self.altura
Yann = Pessoa('Yann', 19, 68, 1.76)
print(Yann.__dict__)
print(f'seu nome é {Yann.nome}, você tem {Yann.idade} anos, pesa {Yann.peso} kgs e tem uma altura de {Yann.altura}')

Yann.envelhecer(1)
Yann.crescer(2)                     #não consegui fazer com que essa função utilizasse o parâmetro da função envelhecer automaticamente,
                                    # então precisei duplicar o parâmetro anos. Estou aberto a sugestões e conselhos :)
Yann.engordar(10)

print(Yann.__dict__)
print(f'seu nome é {Yann.nome}, você tem {Yann.idade} anos, pesa {Yann.peso} kgs e tem uma altura de {Yann.altura}')

Yann.emagrecer(5)

print(Yann.__dict__)
print(f'seu nome é {Yann.nome}, você tem {Yann.idade} anos, pesa {Yann.peso} kgs e tem uma altura de {Yann.altura}')
