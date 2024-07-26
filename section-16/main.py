"""
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
"""

from prettytable import PrettyTable
from os import system

system("cls")

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Chespin", "Vivillon"])
table.add_column("Type", ["Electric", "Water", "Fire", "Grass", "Flying"])
table.align = "l"
table.header_style = "upper"
table.padding_width = 3
print(table)
