import turtle

t = turtle.Turtle()

for i in range (5):
    t.penup()
    t.goto(-10*i, 10*i)
    t.pendown()
    for j in range(4):
        t.forward(20*(i+1))
        t.right(90)

turtle.done()