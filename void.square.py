#1
import turtle

def Square(awit, sz):
   
    for i in range(4):
        awit.forward(sz)
        awit.left(90)

screen = turtle.Screen()       
screen.bgcolor("lightgreen")

pacman = turtle.Turtle()     
pacman.color('pink')
pacman.pensize(3)

for i in range(5):
    Square(pacman, 20)   
    pacman.penup()
    pacman.forward(40)       
    pacman.pendown()
    
pacman.hideturtle()

turtle.done()
