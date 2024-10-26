from turtle import Screen, Turtle
from racket import Racket
import os

os.system('cls')  # Limpar o terminal

screen = Screen()
racket = Turtle()

screen.setup(width=800, height=600)  # 800 x 600 pixels
screen.bgcolor('black')  # Cor de fundo
screen.title('Pong')  # Titulo da janela
screen.tracer(0)  # Desligar a animação

right_racket = Racket((350, 0))
left_racket = Racket((-350, 0))
top_racket = Racket((0, 0))

screen.listen()  # Escutar eventos do teclado
screen.onkey(right_racket.go_up, key='e')  # Tecla para cima
screen.onkey(right_racket.go_down, key='d')  # Tecla para baixo
screen.onkey(left_racket.go_up, key='w')  # Tecla para cima
screen.onkey(left_racket.go_down, key='s')  # Tecla para baixo

game_is_on = True  # Flag para controlar o jogo
while game_is_on:
    screen.update()  # Atualizar a tela

screen.exitonclick()  # Fechar tela após o click do mouse
