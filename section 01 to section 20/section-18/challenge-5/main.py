from os import system
import turtle as t
import random

system("cls")

"""Criação do objeto"""
timmy_the_turtle = t.Turtle()
t.colormode(255)
timmy_the_turtle.shape("triangle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


timmy_the_turtle.speed("fastest")

for _ in range(144):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.left(2.5)

screen = t.Screen()
screen.exitonclick()