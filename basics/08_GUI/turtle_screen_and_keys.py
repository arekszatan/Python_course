import turtle
import time

t = turtle.Turtle()
win = turtle.Screen()

win.title("Application")
win.bgcolor("yellow")
win.setup(width=550, height=550)

t.forward(100)
print("x: ", t.xcor())
print("y: ",t.ycor())

def key_pressed_w():
    print("w clicked")
    t.fd(20)

def key_pressed_s():
    print("s clicked")
    t.backward(20)

win.listen()
win.onkey(key_pressed_w, "w")
win.onkey(key_pressed_s, "s")

win.tracer(0)

while True:
    win.update()
    time.sleep(0.1)

turtle.mainloop()