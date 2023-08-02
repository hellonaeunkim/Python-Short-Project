from turtle import Turtle
import pandas

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

data = pandas.read_csv("50_states.csv")
state = data.state

class States(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        
    def write_state(self, answer):
        self.write(answer, align=ALIGNMENT, font=FONT)
        