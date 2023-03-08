import turtle 
t = turtle.Turtle()
t.color("pink")
t.begin_fill()

t.penup()
t.forward(50)
t.pendown()

def draw_side():
  t.fd(100)
  t.rt(90)
  t.fd(100)
  t.rt(90)
  t.fd(100)
  t.lt(90)
  
  
for x in range(4):
  draw_side()
  
t.end_fill()
  

