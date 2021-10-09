from classes4 import Cliente

cliente1 = Cliente('Luiz', 67)
cliente1.inserir_endereco('Brasília', 'DF')
cliente1.inserir_endereco('Rio de Janeiro', 'RJ')
cliente1.inserir_endereco('Belo Horizonte', 'MG')
cliente1.lista_cadastro()

cliente2 = Cliente('Tiago', 34)
cliente2.inserir_endereco('São Paulo', 'SP')
cliente2.lista_cadastro()


#Se a classe cliente for excluída, os endereços serão automáticamente.