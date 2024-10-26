from turtle import Turtle
import random


class Food(Turtle):  # Herda da classe Turtle

    def __init__(self):
        super().__init__()  # Chama o construtor da classe pai
        self.shape("turtle")  # Cria um círculo
        self.penup()  # Remove o tracejado da linha quando se move
        self.shapesize(
            stretch_len=0.5,
            stretch_wid=0.5)  # Reduz o tamanho do círculo
        self.color("red")  # Cor do círculo
        self.speed("fastest")  # Velocidade da animação do círculo
        self.refresh()

    def refresh(self):
        """
        Define uma nova posição aleatória para o alimento na tela
        """
        random_x = random.randint(-580, 580)  # Posição aleatória no eixo x
        random_y = random.randint(-380, 380)  # Posição aleatória no eixo y
        self.goto(random_x, random_y)
