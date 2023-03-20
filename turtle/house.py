import turtle


wn = turtle.Screen()
wn.setup(700,500)
#wn.bgcolor('lightblue')

#code for the sun
t = turtle.Turtle()
# code for sun
t.penup()
t.goto(-300,80)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

#code for sun rays
for i in range(18):
   t.rt(90)
   t.fd(40)
   t.bk(40)
   t.lt(90)
   t.circle(50,20)
   
   #t.rt(90)
   #t.fd(40)
   #t.bk(40)
   #t.lt(90)
   #t.circle(50,20)

#starting the triangle/ roof
t.penup()
t.goto(0,0)
t.pendown()
t.color("grey")

# filling the roof with color
t.begin_fill()
for i in range(3):
  t.fd(200)
  t.lt(120)
t.end_fill()


t.fillcolor("pink")

#code for the box
t.rt(90)
t.begin_fill()
for i in range(3):
  t.fd(200)
  t.lt(90)
  t.end_fill()

t.color("black")
t.penup()
t.goto(80,-120)
t.pendown()

#code for door
t.lt(90)
t.fd(82)
t.lt(90)
t.fd(40)
t.lt(90)
t.fd(82)
t.lt(90)
t.fd(40)
t.end_fill()


#code for the left = window
t.penup()
t.rt(90)
t.fd(60)
t.pendown()

t.lt(90)
t.fd(60)
t.lt(90)
t.fd(40)
t.lt(90)
t.fd(60)
t.lt(90)
t.fd(40)
t.end_fill()

 


