import turtle
wd = turtle.Screen()
shape=str(input("Enter a desired shape to display: "))
times = int(input("How many times do you want it to display? "))

art = turtle.Turtle()
art.color("hotpink")
art.penup()
art.backward(100)
art.pensize(3)

# SQUARE
if shape == "Square":
    for i in range(times):
            for s in range(4):
                art.pendown()
                art.forward(20)
                art.left(90)
                art.penup()
            art.forward(30)
    art.penup()
    art.forward(20)

# CIRCLE
if shape == "Circle":
    for r in range(times):
        art.pendown()
        art.circle(20)
        art.penup()
        art.forward(50)
    art.penup()
    art.forward(50)

# TRIANGLE
if shape == "Triangle":
    for e in range(times):
        for o in range(3):
            art.pendown()
            art.forward(20)
            art.left(360/3)
            art.penup()
        art.forward(30)
    art.penup()
    art.forward(20)

wd.mainloop()