from turtle import Turtle, Screen
import random
import os

os.system("cls")

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Faça sua aposta",
    prompt="Qual tartaruga vai vencer a corrida? Digite a cor: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle in range(6):
    new_turtle = Turtle(shape="turtle")  # cria uma nova tartaruga e define sua forma
    new_turtle.color(colors[turtle])  # define a cor da tartaruga
    new_turtle.penup()  # remove a caneta do turtle
    new_turtle.goto(x=-240, y=-70 + turtle * 30)  # define o inicio de cada tartaruga
    all_turtles.append(new_turtle)  # adiciona uma nova tartaruga a lista de tartarugas

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Você venceu! A tartaruga {winning_color} venceu!")
            else:
                print(f"Você perdeu! A tartaruga {winning_color} venceu!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
