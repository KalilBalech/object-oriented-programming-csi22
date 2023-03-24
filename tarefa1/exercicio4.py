import turtle

t = turtle.Turtle()

for j in range(80):
  t.forward(5 + j*3)
  t.right(90)

turtle.clearscreen()

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(100):
  t.forward(5 + 2*i)
  t.right(90-i/100)