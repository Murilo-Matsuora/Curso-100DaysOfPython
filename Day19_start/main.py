from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_left():
    tim.setheading(tim.heading() - 10)

def rotate_right():
    tim.setheading(tim.heading() + 10)

def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_right)
screen.onkey(key="d", fun=rotate_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()

