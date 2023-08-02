import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=700, height=650)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

final_line = Turtle(shape="arrow")
final_line.hideturtle()
final_line.penup()
final_line.setheading(270)
final_line.goto(x=320, y=310)
final_line.color("red")
final_line.pendown()
final_line.forward(615)

turtle_y = 250
for turtle_index in range(6):
    new_turtles = Turtle(shape="turtle")
    new_turtles.color(colors[turtle_index])
    new_turtles.turtlesize(stretch_wid=1.5, stretch_len=1.5)
    new_turtles.penup()
    new_turtles.goto(x=-300, y=turtle_y)
    turtle_y -= 100
    all_turtles.append(new_turtles)
    
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 300:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()
