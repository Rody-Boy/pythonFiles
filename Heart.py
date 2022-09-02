import turtle
import random
turtle.speed(5)
turtle.bgcolor("yellow")


def circle():
	turtle.speed(20)
	turtle.pensize(5)
	turtle.right(60)
	turtle.circle(110)

def bilog():
	turtle.speed(20)
	turtle.pensize(5)
	turtle.color('pink')
	turtle.right(60)
	turtle.begin_fill()
	turtle.circle(110)
	turtle.end_fill()	

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color("red", "pink")        
turtle.speed(10)

circle()

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

for i in range(100):
	x=random.randint(-550, 550)
	y=random.randint(-300, 300)
	
	turtle.up()
	turtle.goto(x, y)
	turtle.down()
	bilog()
	
turtle.write("Live, Love, Pray")
	
turtle.done()