# import colorgram as cg
#
# rgb_colors = []
# colors = cg.extract('hirst_painting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(42, 2, 176), (81, 252, 177), (235, 232, 253), (224, 151, 110), (154, 3, 85), (5, 210, 101), (4, 138, 60), (244, 42, 125), (109, 108, 245), (251, 252, 56), (184, 184, 250), (210, 106, 6), (175, 113, 246), (35, 35, 251), (139, 1, 0), (251, 37, 35), (51, 239, 57), (222, 115, 158), (16, 127, 143), (86, 249, 252), (185, 43, 107), (22, 5, 103), (10, 209, 214), (97, 7, 50), (228, 165, 206), (104, 7, 4), (206, 119, 31)]

tim.hideturtle()
tim.penup()
tim.speed(0)
tim.setposition(-225,-200)
number_of_dot = 100

for dot_count in range(1, number_of_dot + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
