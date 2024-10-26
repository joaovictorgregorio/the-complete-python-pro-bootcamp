from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial Black", 21, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Pontuação inicial
        self.color("purple")
        self.penup()
        self.goto(0, 360)  # Posição inicial
        self.hideturtle()  # Esconde a tartaruga
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Função para atualizar a pontuação na tela
        """
        self.write(
            f"Score: {self.score}",
            align=ALIGNMENT,
            font=FONT
        )  # Atualiza a pontuação na tela

    def game_over(self):
        """
        Função para exibir "Game Over" na tela
        """
        self.goto(0, 0)  # Posição inicial
        self.write(
            "Game Over".upper(),
            align=ALIGNMENT,
            font=FONT
        )  # Exibe "Game Over" na tela

    def increase_score(self):
        """
        Função para aumentar a pontuação
        """
        self.score += 1  # Incrementa + 1 ao score
        self.clear()  # Limpa o score atual da tela
        self.update_scoreboard()  # Atualiza a pontuação na tela
