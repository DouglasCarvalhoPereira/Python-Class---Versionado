#PROGRAMAÇÃO ORIENTADA A OBJETOS

#UMA CLASSE RESPONDE TRÊS PERGUNTAS
#UMA CLASSE É UM MOLDE DO OBJETO

#QUE COISAS EU TENHO? - ATRIBUTOS
#COISAS QUE EU FAÇO? - MÉTODOS
#COMO EU ESTOU AGORA? - ESTADO

#INSTACIAR É GERAR UM OBJETO A PARTIR DE UMA CLASS


class Caneta:
    #ATRIBUTOS
    modelo: Caractere
    cor: Caractere
    ponta: Real
    carga: Inteiro
    tampa: Lógico

    #MÉTODOS
    Metodo rabiscar()
        se (tampa) então
            escreva('erro')
        senao
            escreva('Ola')
        FIMSE
    
    Fim do método

    Metodo tampar()
    fim 

    #ESTADO (MOMENTO ATUAL)
    Destampada
    Azul
    90% de carga


    #INSTACIAR É GERAR UM OBJETO A PARTIR DE UMA CLASS
    
    c1 = nova Caneta #INSTACIADO
    c1.cor = 'Azul'
    c1.ponta = 0.6
    c1.carga = 50%
    c1.rabiscar()

    c2.nova Caneta
    c2.cor = 'Vermelho'
    c2.ponta = 1.0
    c2.carga = 100%
    c2.tampar()



    #CLASSE
    """
    Define os atributos e métodos comuns que serão compartilhados por um objeto.

    Posso criar um classe mas nunca criar uma objeto. Um objeto é uma instacia de uma classe.   
    
    """

    #ABSTRAÇÃO
    """
    Atributos semelhantes mas com estados diferentes.

    Quais atributos mais importam nesse momento? Então eu ignoro todos os outros e foco nos que vou utilizar.
    
    """
