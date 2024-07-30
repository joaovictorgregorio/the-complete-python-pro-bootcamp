from os import system
from time import sleep
from turtle import Turtle, Screen
import random

system("cls")

"""Criação do objeto"""
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("LightBlue4")


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)


for shape_side_number in range(3, 11):
    timmy_the_turtle.color(random.choice(colours))
    draw_shape(shape_side_number)





screen = Screen()
screen.exitonclick()
