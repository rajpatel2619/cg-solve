from turtle import Turtle, Screen
from math import pi, asin as sine

screen = Screen()
screen.setworldcoordinates(-1, -pi/2, 1, pi)  

turtle = Turtle()

k = 0

while k < 100:
    angle = -1 + k*0.02
    print(angle)
    turtle.goto(angle, sine(angle))
    k += 1

screen.exitonclick()