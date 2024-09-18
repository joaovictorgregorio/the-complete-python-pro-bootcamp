import colorgram
import os

os.system("cls")

"""Extração das cores usando a biblioteca colorgram"""
colors = colorgram.extract('image-painting.jpg', 80)
rgb_colors = []


def extract_colors():
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        tuple_color = (r, g, b)
        rgb_colors.append(tuple_color)
    return rgb_colors


print(extract_colors())
