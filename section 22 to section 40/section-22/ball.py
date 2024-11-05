from turtle import Turtle


class Ball(Turtle):
    """
    Classe que representa a bola do jogo Pong.
    """
    def __init__(self):
        """
        Construtor da classe Ball.
        """
        super().__init__()  # Chama o construtor da classe pai 
        self.shape(name="circle")  # Forma do objeto
        self.color("white")  # Cor do objeto
        self.penup()  # Desligar a caneta
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """
        Método para mover a bola
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Método para inverter a direção da bola no eixo y
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Método para inverter a direção da bola no eixo x
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        """
        Método para resetar a posição da bola
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
