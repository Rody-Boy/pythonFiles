import turtle
prometheus= turtle.Turtle() 
screen=turtle.Screen

def SunLight(t, length, radius): 

    

    for i in range(4): 

        t.penup() 
        t.forward(radius) 
        t.pendown() 
        t.forward(length) 
        t.penup() 
        t.backward(length + radius) 
        t.left(90) 
        
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
  
turtle.done()


