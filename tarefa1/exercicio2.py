import turtle

t = turtle.Turtle()

def draw_poly( n, sz):
  
  for i in range(n):
    t.forward(sz)
    t.left(360/n)

# draw_poly(8, 50)