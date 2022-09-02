import turtle
nico=turtle.Turtle()


def Star(nico, star):
    for i in range(5):
        nico.forward(star)
        nico.right(720 / 5)
nico.hideturtle()

win = turtle.Screen()
win.bgcolor('lightgreen')
robin= turtle.Turtle()
robin.color('pink')
robin.speed(10)
robin.pensize(5)

robin.up()
robin.backward(200)
robin.down()

for i in range(5):
    Star(robin, 100)
    robin.up()
    robin.forward(350)
    robin.right(144)
    robin.down()
    
turtle.done()