from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import os
import time

os.system("cls")  # Limpa o terminal

screen = Screen()
screen.setup(width=1200, height=800)  # Tamanho da tela
screen.bgcolor("gray")  # Cor de fundo
screen.title("Snake Game")  # Título da janela
screen.tracer(0)

snake = Snake()  # Instanciamento da classe Snake
food = Food()  # Instanciamento da classe Food
scoreboard = Scoreboard()  # Instanciamento da classe Scoreboard

screen.listen()  # Escuta os eventos do teclado
screen.onkey(snake.up, "Up")  # Tecla para cima
screen.onkey(snake.down, "Down")  # Tecla para baixo
screen.onkey(snake.left, "Left")  # Tecla para esquerda
screen.onkey(snake.right, "Right")  # Tecla para direita

game_is_on = True
while game_is_on:
    screen.update()  # Atualiza a tela (necessário para mostrar os quadrantes)
    time.sleep(0.20)  # Velocidade de deslocamento da cobra
    snake.move()  # Executa a movimentação dos quadrantes da classe Snake

    """ Detectar a colisão com a comida """
    if snake.head.distance(food) < 15:
        food.refresh()  # Move a comida para outra posição
        snake.extend()  # Adiciona um novo quadrante à cobra
        scoreboard.increase_score()  # Incrementa a pontuação

    """ Detectar a colisão com a parede """
    if (snake.head.xcor() > 595 or snake.head.xcor() < -595 or
            snake.head.ycor() > 395 or snake.head.ycor() < -395):
        game_is_on = False
        scoreboard.game_over()  # Mostra a mensagem de game over

    """ Detectar a colisão com o próprio corpo """
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()  # Mostra a mensagem de game over

screen.exitonclick()  # Mantém a janela aberta até que seja clicado
