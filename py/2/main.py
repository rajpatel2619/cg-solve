import turtle
import math

# setting screen
screen = turtle.Screen()
screen.mode('world')
screen.bgcolor("lightblue")

# setting the world coordinates
# case 1:  coordinate mentioned as in question
# turtle.setworldcoordinates(-1, -(math.pi)/2, 1, (math.pi))
# case 2:  coordinates for clear view
turtle.setworldcoordinates(-1.1, -(math.pi)*2, 1.1, (math.pi)*2)

myPen = turtle.Turtle()
myPen.speed(5)

# drawing x and y axis
def drawAxis():
    # X Axis
    myPen.penup()
    myPen.goto(-1,0)
    myPen.pendown()
    myPen.goto(1,0)
    
    # set position
    myPen.penup()
    myPen.setpos(-1, 0)
    myPen.pendown()

    # write -1
    myPen.write(-1, font=("Arial", 10))

    # set position
    myPen.penup()
    myPen.setpos(1, 0)
    myPen.pendown()
      
    # write 1
    myPen.write(1, font=("Arial", 10))

    # set position
    myPen.penup()
    myPen.setpos(0, 0)
    myPen.pendown()

    # write 0
    myPen.write(0, font=("Arial", 10))
    # Y Axis
    myPen.penup()
    myPen.goto(0, -(math.pi))
    myPen.pendown()
    myPen.goto(0, (math.pi))

    # set position
    myPen.penup()
    myPen.setpos(0, -math.pi/2)
    myPen.pendown()

    # write -π/2 
    myPen.write('-π/2', font=("Arial", 10))

    # set position
    myPen.penup()
    myPen.setpos(0, math.pi/2)
    myPen.pendown()

    # write π/2 
    myPen.write('π/2', font=("Arial", 10))
    # set position
    myPen.penup() 
    myPen.setpos(0, math.pi) 
    myPen.pendown() 
      
    # write π
    myPen.write('π', font=("Arial", 10))

#A procedure to trace a curve: y = asin(x)
def drawasingraph():
    # set position
    myPen.penup()
    myPen.setpos(-1, -0.8)
    myPen.pendown()

    # write AsinGraph
    myPen.write('Asin Graph', font=("Arial", 10))
    myPen.penup()
    # for loop from 1 to 10
    for k in range(0, 100):
        x=-1+k*0.02
        y=math.asin(x)
        myPen.goto(x,y)
        myPen.pendown()
    myPen.penup()
    myPen.goto(0, 0)
#A procedure to trace a curve: y = acos(x)
def drawacosgraph():
    # set position
    myPen.penup()
    myPen.setpos(-1, 1.8)
    myPen.pendown()
    # write Acos Graph
    myPen.write('Acos Graph', font=("Arial", 10))
    myPen.penup()
    for k in range(0, 100):
        x=-1+k*0.02
        y=math.acos(x)
        myPen.goto(x,y)
        myPen.pendown()

    myPen.penup()
    myPen.goto(0, 0)
# Main Program Starts Here
myPen.color("#000000")
drawAxis()
myPen.pensize(2)
myPen.color("#FF59F7")
drawasingraph()
drawacosgraph()
turtle.mainloop()