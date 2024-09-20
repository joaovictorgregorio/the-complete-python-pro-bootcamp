from turtle import Screen, Turtle
from os import system
from time import sleep

system("cls")  # Limpa o terminal

screen = Screen()
screen.setup(width=600, height=600)  # Tamanho da tela
screen.bgcolor("black")  # Cor de fundo
screen.title("Snake Game")  # Título da janela
screen.tracer(0)

segments = []

for square in range(3):
    new_segment = Turtle(shape="square")  # Cria um novo quadrante
    new_segment.color("white")  # Cor do quadrante
    new_segment.penup()  # Remove o tracejado da linha quando se move
    new_segment.goto(x=-20 * square, y=0)  # Adiciona novos quadrantes a tela
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()  # Atualiza a tela (necessário para mostrar os quadrantes
    sleep(0.1)  # Define um tempo para deslocar, biblioteca time

    """Código que mantém a movimentaçõa da cobra agrupada,
    sem separar os quadrantes"""
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)





screen.exitonclick()  # Mantém a janela aberta até que seja clicado
