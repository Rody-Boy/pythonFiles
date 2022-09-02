import turtle

win=turtle.Screen()
win.bgcolor('lightyellow')
bukid=turtle.Turtle()
bukid.pensize(5)
bukid.color('brown')
bukid.begin_fill()
bukid.penup()
bukid.goto(-550,-150)
bukid.pendown()

for i in range(3):
	bukid.forward(400)
	bukid.left(360/3)
	
bukid.end_fill()

bukidgamay=turtle.Turtle()
bukidgamay.color('brown')
bukidgamay.begin_fill()
bukidgamay.penup()
bukidgamay.goto(-300, -150)
bukidgamay.pendown()

for i in range(3):
	bukidgamay.forward(200)
	bukidgamay.left(360/3)
	
bukidgamay.end_fill()

bukidgamay.hideturtle()
bukid.hideturtle()


jewela=turtle.Turtle()
jewela.color('blue')
jewela.pensize(10)

rhod=turtle.Turtle()
rhod.pensize(10)
rhod.shape('arrow')
rhod.color('grey')

rhod.begin_fill()
for i in range(4):
		rhod.forward(150)
		rhod.right(360/4)
rhod.end_fill()

jewela.begin_fill()	
for i in range(3):
	jewela.forward(150)
	jewela.left(360/3)
jewela.end_fill()

rhod.hideturtle()
jewela.hideturtle()


awitise=turtle.Turtle()
awitise.pensize(5)
awitise.color('green')
awitise.penup()
awitise.goto(38, 3)
awitise.pendown()
awitise.begin_fill()
for i in range (4):
		awitise.forward(70)
		awitise.right(360/4)
		
awitise.end_fill()

		
awitise.hideturtle()


prometheus= turtle.Turtle() 
screen=turtle.Screen



def SunLight(ray, length, radius): 

    

    for i in range(4): 

        ray.penup() 
        ray.forward(radius) 
        ray.pendown() 
        ray.forward(length) 
        ray.penup() 
        ray.backward(length + radius) 
        ray.left(90) 
        
prometheus.penup() 

prometheus.goto(200, 250)

prometheus.pensize(10)
prometheus.fillcolor("yellow") 
prometheus.pendown() 
prometheus.begin_fill() 

prometheus.circle(45) 
prometheus.end_fill() 

  
prometheus.penup() 
prometheus.backward(10)
prometheus.goto(200, 300) 
prometheus.pendown() 

SunLight(prometheus, 85, 54) 

prometheus.right(45) 

SunLight(prometheus, 85, 54) 

prometheus.left(45) 

prometheus.hideturtle()



def SunLight(ray, length, radius): 

    

    for i in range(4): 

        ray.penup() 
        ray.forward(radius) 
        ray.pendown() 
        ray.forward(length) 
        ray.penup() 
        ray.backward(length + radius) 
        ray.left(90) 
        
prometheus.penup() 

prometheus.goto(200, 250)

prometheus.pensize(10)
prometheus.fillcolor("black") 
prometheus.pendown() 
prometheus.begin_fill() 

prometheus.circle(45) 
prometheus.end_fill() 

bulan=turtle.Turtle()
wan=turtle.Screen()
wan.bgcolor('black')
bulan.up()
bulan.goto(-290,250)
bulan.color('orange')
bulan.begin_fill()
bulan.circle(100)
bulan.end_fill()
bulan.speed(10)
bulan.up()
bulan.goto(-250,250)
bulan.color('black')
bulan.begin_fill()
bulan.circle(100)
bulan.end_fill()

turtle.done()



	



