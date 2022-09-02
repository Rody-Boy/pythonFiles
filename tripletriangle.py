import turtle

t=turtle.Pen()
for i in range(0,3):
	t.forward(100)
	t.left(120)
	
	t.back(100)
	for i in range(0,3):
		t.forward(100)
		t.left(120)
		
turtle.done()