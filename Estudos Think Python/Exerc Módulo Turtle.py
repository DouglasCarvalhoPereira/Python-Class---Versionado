import turtle            # permite usar as funções e objetos do módulo turtle


wn = turtle.Screen()     # cria uma janela gráfica
wn.bgcolor("lightgreen")         # define a cor de fundo da janela

alex = turtle.Turtle()   # cria um turtle chamado alex
alex.color("blue")               # tess fica azul
alex.pensize(2)
alex.forward(200)        # manda o alex se mover 150 unidades para frente
alex.left(120)            # roda de 90 graus para a esquerda
alex.forward(75)         # desenha o segundo lado do retângulo


