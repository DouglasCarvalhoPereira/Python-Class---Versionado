#AGREGAÇÃO E COMPOSIÇÃO
#Uma classe usa a outra complemento e uma depende da outra
from classes3 import Carrinho_de_Compras, Produto

carinhoDeCompras = Carrinho_de_Compras()
p1 = Produto('Calça', 100)
p2 = Produto('Boné', 60)
p3 = Produto('Chinelo', 90)
p4 = Produto('Camisa', 230)


carinhoDeCompras.inserir_produto(p1)
carinhoDeCompras.inserir_produto(p2)
carinhoDeCompras.inserir_produto(p3)
carinhoDeCompras.inserir_produto(p4)

carinhoDeCompras.lista_produtos()
carinhoDeCompras.soma_total_produtos()