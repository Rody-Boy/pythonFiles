import turtle 
win= turtle.Screen()
win.bgcolor("lightgreen")
turtle.speed(40) 
turtle.pensize(2)
for rasengan in range(50): 
    turtle.circle(10*rasengan) 
    turtle.circle(-10*rasengan) 
    turtle.left(rasengan)
    turtle.color("blue")
turtle.done()