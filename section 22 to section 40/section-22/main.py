from turtle import Screen, Turtle
from racket import Racket
from ball import Ball
from scoreboard import Scoreboard
import os
import time

os.system('cls')  # Limpar o terminal

screen = Screen()
racket = Turtle()

screen.setup(width=800, height=600)  # 800 x 600 pixels
screen.bgcolor('black')  # Cor de fundo
screen.title('Pong')  # Titulo da janela
screen.tracer(0)  # Desligar a animação

right_racket = Racket((350, 0))
left_racket = Racket((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()  # Escutar eventos do teclado
screen.onkey(right_racket.go_up, key='Up')  # Tecla para cima
screen.onkey(right_racket.go_down, key='Down')  # Tecla para baixo
screen.onkey(left_racket.go_up, key='w')  # Tecla para cima
screen.onkey(left_racket.go_down, key='d')  # Tecla para baixo

game_is_on = True  # Flag para controlar o jogo
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # Atualizar a tela
    ball.move()  # Mover a bola

    # Detectar colisão com a parede superior e inferior
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Inverter a direção da bola

    # Detectar colisão com a raquete
    if ball.distance(right_racket) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(left_racket) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detectar quando a bola passa da raquete
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_score()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_score()

screen.exitonclick()  # Fechar tela após o click do mouse
