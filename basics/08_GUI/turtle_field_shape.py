import turtle

t1 = turtle.Turtle()
t1.pensize(10)
t1.color("blue")
t1.fillcolor("red")

t1.penup()
t1.goto(-200, 200)
t1.pendown()

t1.begin_fill()
for i in range(4):
    t1.forward(70)
    t1.right(90)
t1.end_fill()


t1.penup()
t1.goto(0, -200)
t1.pendown()

t1.begin_fill()
for i in range(3):
    t1.forward(70)
    t1.right(120)
t1.end_fill()

t2 = turtle.Turtle()
t2.pensize(10)
t2.color("blue")
t2.fillcolor("red")
t2.penup()
t2.goto(200, 200)
t2.pendown()
t2.begin_fill()
t2.circle(50)
t2.end_fill()

t3 = turtle.Turtle()
t3.pensize(3)
t3.color("green")
t2.penup()
t2.goto(0, 0)
t2.pendown()
t3.speed(50)
for i in range(360):
    t3.circle(100)
    t3.left(10)

turtle.mainloop()