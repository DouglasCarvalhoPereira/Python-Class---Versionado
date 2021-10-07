from pessoa import Pessoa

p1 = Pessoa("Pedro", 26, "M") #CRINDO A PRIMEIRA PESSOA
p2 = Pessoa("Maria", 29, "F" ) #CRIANDO A SEGUNDA PESSOA

p1.falar('Cinema') #OBEJTOS INDEPENDENTES
print(p1.get_yeaars_old())

p2.falar('Festa') #OBJETOS INDEPENDENTES

print(p1.ano_atual) #Usar a variável da pessoa
print(p2.ano_atual) #Usar a variável da pessoa


print(Pessoa.ano_atual) #Usar a variável da Classe


p1.comer('mamão')
p1.parar_comer()
p1.comer('maça')
p1.comer("mamao")
p1.parar_comer()
p1.parar_comer()
p1.comer("pera")
p1.falar() #PEDRO não pdoe falar enquanto come
p1.comer('Banana')


