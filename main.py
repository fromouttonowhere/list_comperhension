from turtle import Turtle
from turtle import Screen

screen = Screen()
screen.title("Proba")
screen.setup(width=600, height=600)
screen.bgcolor("gray20")

timmy = Turtle()
timmy.color("red")
timmy.goto(50, 80)

screen.exitonclick()
