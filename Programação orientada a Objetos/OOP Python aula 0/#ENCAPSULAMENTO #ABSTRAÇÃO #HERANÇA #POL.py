#ENCAPSULAMENTO #ABSTRAÇÃO #HERANÇA #POLIMORFISMO

#ENCAPSULAMENTO

#NÃO É OBRIGATÓRIO, MAS É UMA BOA PRÁTICA PARA PRODUZIR CLASSES MAIS EFICIENTES

"""
3 maiores Vantagens
    1 Tornar mudanças invisiveis
    2 Facilitar a reutilização do código
    3 Reduzir os efeitos colcateriais

Um bom objeto encapsulado possui um INTERFACE BEM DEFINIDA.

Exemplo de omo encapsular? Controle Remoto.

======================================
           <<interface>>
            CONTROLADOR
======================================

+ ligar()
+ desligar()
+ abrirMenu()
+ fecharMenu()
+ maisVolume()
+ menusVolume()
+ ligarMudo()
+ desligarMudo()
+ play()
+ pause()

======================================

Todos os métodos de encapsulamento precisam ser públicos (+)
Esses métodos não recebem código somente chama a execução da função.


======================================
            CONTROLE REMOTO
======================================
- volume
- ligado
- tocando
======================================

+ ligar()
+ desligar()
+ abrirMenu()
+ fecharMenu()
+ maisVolume()
+ menusVolume()
+ ligarMudo()
+ desligarMudo()
+ play()
+ pause()

- setVolume()
- getVolume()
- setLigado()
- getLigado()
- settocando()
- getTocando()

======================================

class ControleRemoto:
    //Atributos
    - volume int
    - ligado bool
    - tocando bool

    //Métodos Especiais
    publico Metodo Construtor()
        volume = 50
        ligado = false
        tocando = falso
    fimMetodo

    privado Metodo getVolume()
        return volume
    fimMetodo

    privado Metodo getLigado()
        return volume
    fimMetodo

    privado Metodo getTocando()
        return volume
    fimMetodo

    privado Metodo setVolume(v:Int)
        volume = v
    fimMeto

    privado Metodo setLigado(l: logico)
        volume = l
    fimMeto

    privado Metodo setTocando(t: logico)
        tocando = t
    fimMeto

    FimClasse



    classe ControleRemoto implementa Controlador
            
            + ligar()
                setLigado(verdadeiro)

            FimMétodo

            + desligar()
                setDesligado(falso)

            FimMétodo

            + abrirMenu()
                Escreva(getLigado())
                Escreva(getVolume())
                para i = 0 ate getVolume() passo 10 faca
                    Escreva("|")
                    FimPara
                    Escreva(getTocando())

                FimMétodo

            + fecharMenu()
                Escreva("Fechando Menu...")

            FimMétodo

            + maisVolume()
                se (getLigado()) entao
                    setVolume(getVolume() + 1)
                    FimSe

            FimMétodo

            + menusVolume()
                se(getLigado() - 1)
                FimSe

            FimMétodo

            + ligarMudo()
                Se (Se (getLigado and getVolume > 0) entao
                    setVolume(0)
                FimSe

            FimMétodo

            + desligarMudo()
                Se (getLigado() and getVolume() = 0) entao
                    setVolume(50)
                FimSe
            FimMétodo

            + play()
                se (gteLigado and not getTocando()) entao
                setTocando(Verdadeiro)

            FimMétodo

            + pause()
                Se (getLigado and getTocando()) entao
                    setTocando(Falso)
                FimSe
            FimMétodo


#ENCAPSULAMENTO TODOS OS ATRIBUTOS DEVEM SER PRIVADOS PARA PROTEJE-LOS




"""

#HERANÇA



#POLIMORFISMO



