import turtle
from random import random, choice
from turtle import Turtle, Screen, colormode

"""extract colors of image"""
# from colorgram import colorgram
#
# paint_colors = colorgram.extract('hirst_painting.jpg', 50)
# list_colors = []
"""cool annexation (hehe) of the value's group as tuples in a list"""
# for i in range(len(paint_colors)):
#     list_colors.append(tuple(paint_colors[i].rgb))

list_colors = [(214, 157, 85), (33, 105, 151), (238, 215, 94), (153, 75, 52),
               (125, 168, 199), (209, 134, 163), (156, 60, 81), (22, 39, 54),
               (212, 85, 61), (176, 162, 47), (200, 85, 119), (135, 184, 150),
               (56, 119, 90), (240, 213, 4), (25, 46, 37), (228, 167, 186),
               (64, 46, 34), (87, 157, 100), (9, 99, 75), (34, 166, 189),
               (40, 60, 102), (228, 175, 166), (179, 189, 213), (95, 126, 173),
               (68, 34, 44), (105, 42, 60), (170, 205, 179), (113, 43, 37),
               (156, 206, 217), (78, 69, 35), (3, 90, 115)]

screen = Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
turtle.colormode(255)
timmy = Turtle("turtle")
timmy.color("green")
timmy.speed("fastest")


def paint_dots():
    for _ in range(16):
        timmy.dot(20, choice(list_colors))
        timmy.penup()
        timmy.forward(50)


def new_position():
    timmy.penup()
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(800)
    timmy.right(180)


for _ in range(13):
    paint_dots()
    new_position()



screen.exitonclick()
