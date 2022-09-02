import turtle
zoro=turtle.Turtle()
awit=turtle.Screen()
awit.bgcolor('lightgreen')
zoro.pensize(3)

def drawSquare(zoro, sword):
    for i in range(4):
        zoro.forward(sword)
        zoro.left(90)
zoro.hideturtle()

win= turtle.Screen()
roronoa=turtle.Turtle()
roronoa.color('pink')
roronoa.pensize(3)
roronoa.speed(10)

roronoa.hideturtle()

sword = 20
for i in range(5):
    drawSquare(roronoa, sword)
    sword = sword + 20
    roronoa.up()
    roronoa.backward(10)
    roronoa.right(90)
    roronoa.forward(10)
    roronoa.left(90)
    roronoa.down()
    
turtle.done()