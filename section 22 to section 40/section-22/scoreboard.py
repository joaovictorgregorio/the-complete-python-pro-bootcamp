from turtle import Turtle


class Scoreboard(Turtle):
    """
    Classe que representa o placar do jogo Pong.
    """
    def __init__(self):
        """
        Construtor da classe Scoreboard.
        """
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Método para atualizar o placar
        """
        self.clear()
        self.goto(-100, 200)
        self.write(
            self.left_score,
            align='center',
            font=('Courier', 70, 'normal'))
        self.goto(100, 200)
        self.write(
            self.right_score,
            align='center',
            font=('Courier', 70, 'normal'))

    def left_score(self):
        """
        Método para atualizar o placar da esquerda
        """
        self.l_score += 1
        self.update_scoreboard()

    def right_score(self):
        """
        Método para atualizar o placar da direita
        """
        self.r_score += 1
        self.update_scoreboard()
