from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    """
    Código que cria a cobra, adiciona os quadrantes e mantém a movimentação da
    cobra agrupada em um só lugar para facilitar o código do main.py e do
    snake_game.py
    """
    def __init__(self):
        """
        Inicializa a cobra com três quadrantes na tela
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Cria a cobra
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Adiciona um novo quadrante à cobra

    def add_segment(self, position):
        """
        Adiciona um novo quadrante à cobra
        """
        new_segment = Turtle(shape="square")  # Cria um novo quadrante
        new_segment.color("pink")  # Cor do quadrante
        new_segment.penup()  # Remove o tracejado da linha quando se move
        new_segment.goto(position)  # Adiciona novos quadrantes a tela
        self.segments.append(new_segment)

    def extend(self):
        """
        Adiciona um novo quadrante à cobra
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Movimenta a cobra, adicionando um novo quadrante na frente e removendo
        o último quadrante.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Movimenta a cobra para cima
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Movimenta a cobra para baixo
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Movimenta a cobra para esquerda
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Movimenta a cobra para direita
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
