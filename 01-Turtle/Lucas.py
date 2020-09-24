import turtle

myPen = turtle.Pen()
colors = ["red", "blue"]
turtle.bgcolor("black")
for x in range(50):
    myPen.right(45)
    myPen.pencolor(colors[x % 2])
    myPen.forward(x * 10)

turtle.done()
