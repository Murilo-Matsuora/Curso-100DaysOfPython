from turtle import Turtle, Screen
import turtle as t
import random

def generate_random_255rgb():
    t.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def generate_random_0to1rgb():
    t.colormode(1)
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

# def draw_shape(n):
#     angle = 360 / n
#     random_color = generate_random_rgb()
#     tim.pencolor(random_color)
#     for i in range(n):
#         tim.forward(100)
#         tim.right(angle)

tim = Turtle()
tim.shape("turtle")
tim.turtlesize(0.2, 0.2, 0.25)
tim.color("chartreuse4", "darkolivegreen2")
tim.pd()

# for i in range (50):
#     tim.forward(20)
#     tim.pu()
#     tim.forward(10)
#     tim.pd()

# for n in range(3, 11):
#     draw_shape(n)


# def grid_walk_turtle(turtles):
#     for turt in turtles:
#         turt.pensize(10)
#         turt.speed(0)
#
#     for i in range(50):
#         for turt in turtles:
#             turt.forward(30)
#
#             direction = random.randint(0, 3)
#             turt.right(direction * 90)
#
#             random_color = generate_random_0to1rgb()
#             turt.pencolor(random_color)
#
# tom = Turtle()
# tina = Turtle()
# tara = Turtle()
# grid_walk_turtle([tim, tom, tina, tara])

tim.speed(0)

n = 5
parent_radius = 25
children_radius = 100
for angle in range(1, 361):
    if angle % n == 0:
        print(angle)
        tim.right(n)
        tim.pu()
        tim.forward(parent_radius)
        tim.pd()
        tim.color(generate_random_0to1rgb())
        tim.circle(-children_radius)
        tim.pu()
        tim.backward(parent_radius)
        tim.pd()


screen = Screen()
screen.exitonclick()
