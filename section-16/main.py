from turtle import Turtle, Screen
from os import system
from time import sleep

system("cls")
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("yellow", "green")
sleep(1)
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
