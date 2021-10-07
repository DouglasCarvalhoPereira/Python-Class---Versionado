#VISIBILIDADE EM UM OBJETO
#ESTUDAR UML - DIAGRAMA DE CLASSES

"""TODA CLASSE É UM RETANGULO"""
"""

#MODERADORES DE VISIBILIDADE

+ PÚBLICO
    #A Classe atual e todoas as outras clases pode ter acesso a ela

- PRIVADA
    #Somente a Classe atual pode mexer nele

# PROTEGIDO
    #A classe atual e todas as sub-classes

"""

"""
======
Caneta #COMEÇA COM LETRA MAIUSCULA
======
   + modelo
   + cor
   - ponta
   # carga
   # tampa
======

Atributos #INICIAIS MINUSCULAS
   + escrever()
   + rabiscar()
   + pintar()
   - tampar()
   - destampar()
    
======
Métodos() #COM PARENTESES
======


"""
"""
#MÉTODOS ESPECIAIS - MÉTODOS ACESSORES  - 
 ===========================================================                   
                    
                    GETTERS - ACESSOR

============================================================
#MÉTODO SEGURO E RECOMENDADO
============================================================
e = new Estante #Criando um objeto a partir da classe ESTANTE
t = e.getTotDoc() # Método Acessor - Verifica e retorna o valor

============================================================
MÉTODO NÃO SEGURO E NÃO RECOMENDADO
============================================================
e = new Estante #Criando um objeto a partir da classe ESTANTE
t = e.getTotDoc # Acesso direto aos arquivos, ou atributo.



 ===========================================================                   
                    
                    SETTERS - MODIFICADORES - MUTANTES

============================================================
#MÉTODO SEGURO E RECOMENDADO
============================================================
e = new Estante #Criando um objeto a partir da classe ESTANTE
t = e.setTotDoc(doc) # Método Acessor - Verifica e modifica o valor

============================================================
MÉTODO NÃO SEGURO E NÃO RECOMENDADO
============================================================
e = new Estante #Criando um objeto a partir da classe ESTANTE
t = e.setTotDoc # Acesso direto para modificar qualquer arquivo ou atributo





 ===========================================================                   
                    
                    CONSTRUCT - CONSTRUTOR

============================================================
#MÉTODO SEGURO E RECOMENDADO
============================================================
Classe Caneta:
     Metodo construtor(modelo:Caractere, cor:Caractere, ponta: Real) #PARAMETROS
        tampar()
        cor = "Azul"
    Fim Metodo

FimClasse


e = new Caneta #Toda vez que eu instanciar ou criar um objeto a partir da classe inicia com um padrão. Nesse caso TAMPADA e AZUL
        ("BIC", "AZUL", 0.5)

          
============================================================
MÉTODO NÃO SEGURO E NÃO RECOMENDADO
============================================================
e = new Estante #Criando um objeto a partir da classe ESTANTE
t = e.setTotDoc # Acesso direto para modificar qualquer arquivo ou atributo










"""


"""
=============================================================

APLICAÇÃO DOS MÉTODOS ESPECIAIS

=============================================================

======
Caneta #COMEÇA COM LETRA MAIUSCULA
======
   + modelo
   + cor
   - ponta
   # carga
   # tampa
======

Atributos #INICIAIS MINUSCULAS

   + getModelo() #Métodos de acess GET
   + setModelo(m) #Métodos de modificação SET
   + getCor()
   + setCor(c)
   + getPonta()
   + setPonta(p)
   + getCarga()
   + setCarga(c)
   + getTampa()
   + setTampa(t)
    
======
Métodos() #COM PARENTESES
======

"""