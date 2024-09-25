from turtle import Screen
from snake import Snake
from os import system
from time import sleep

system("cls")  # Limpa o terminal

screen = Screen()
screen.setup(width=600, height=600)  # Tamanho da tela
screen.bgcolor("black")  # Cor de fundo
screen.title("Snake Game")  # Título da janela
screen.tracer(0)

snake = Snake()  # Instânciamento da classe Snake

screen.listen()  # Escuta os eventos do teclado
screen.onkey(snake.up, "Up")  # Tecla para cima
screen.onkey(snake.down, "Down")  # Tecla para baixo
screen.onkey(snake.left, "Left")  # Tecla para esquerda
screen.onkey(snake.right, "Right")  # Tecla para direita

game_is_on = True
while game_is_on:
    screen.update()  # Atualiza a tela (necessário para mostrar os quadrantes)
    sleep(0.1)  # Define um tempo para deslocar, biblioteca time
    snake.move()  # Executa a movimentação dos quadrantes da classe Snake


screen.exitonclick()  # Mantém a janela aberta até que seja clicado
