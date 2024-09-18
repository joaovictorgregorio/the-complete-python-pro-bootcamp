import os
import turtle as t
import random as r


os.system("cls")

color_list = [
    (199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48),
    (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85),
    (167, 154, 49), (187, 143, 162), (134, 183, 147), (46, 55, 100),
    (181, 95, 107), (56, 39, 27), (96, 118, 167), (80, 150, 159),
    (89, 152, 92), (71, 118, 93), (220, 175, 187), (169, 207, 163),
    (161, 202, 215), (192, 95, 74), (178, 187, 213), (46, 73, 75),
    (76, 69, 44), (132, 41, 33), (36, 57, 57), (221, 177, 170), (46, 77, 66)
]

"""Criação do objeto Tartaruga e uso de vários métodos para personalização"""
spike = t.Turtle()
t.colormode(255)
spike.shape("triangle")
spike.speed("fast")


def random_colors():
    return r.choice(color_list)


spike.setheading(225)
spike.forward(300)
spike.setheading(0)

for _ in range(10):
    spike.dot(20, random_colors())
    spike.forward(50)


"""Criação do objeto Screen e uso do método exitonclick para fechar a tela
apenas com o click do usuário"""
screen = t.Screen()
screen.exitonclick()
