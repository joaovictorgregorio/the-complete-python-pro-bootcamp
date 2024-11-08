from turtle import Turtle


class Racket(Turtle):
    """
    Classe que representa as raquetes do jogo Pong e suas funcionalidades.
    """
    def __init__(self, position):
        """
        Construtor da classe Racket.
        :param position: Posição inicial da raquete
        """
        super().__init__()  # Chama o construtor da classe pai
        self.shape(name='square')  # Forma do objeto
        self.color('white')  # Cor do objeto
        self.shapesize(stretch_wid=5, stretch_len=1)  # Tamanho do objeto
        self.penup()  # Desligar a caneta
        self.goto(position)  # Posição inicial do objeto

    def go_up(self):
        """
        Método para mover a raquete para cima
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Método para mover a raquete para baixo
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
