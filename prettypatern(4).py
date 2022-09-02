import turtle
vinsmoke=turtle.Turtle()

def drawSquare(vinsmoke,side):
    for i in range(4):
        vinsmoke.forward(side)
        vinsmoke.left(90)


win = turtle.Screen()
win.bgcolor('lightgreen')
sanji = turtle.Turtle()
sanji.speed(19)
sanji.color('blue')


for i in range(20):
    drawSquare(sanji, 200)
    sanji.right(360 / 20)

turtle.done()
